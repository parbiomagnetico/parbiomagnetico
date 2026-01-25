const fs = require('fs');
const path = require('path');
const xml2js = require('xml2js');
const axios = require('axios');
const sharp = require('sharp');
const slugify = require('slugify');

// Configuration
const INPUT_XML = process.argv[2] || './data/export.xml';
const OUTPUT_JSON = './src/data/posts.json';
const IMAGE_DIR = './public/images/posts';

// Category Mapping (Old -> New)
const CATEGORY_MAP = {
    'Terapia': 'CIENCIA BIOMAGNÉTICA',
    'Casos Clinicos': 'INVESTIGACIÓN',
    'Salud': 'BIENESTAR',
    'Uncategorized': 'GENERAL'
};

// Ensure directories exist
if (!fs.existsSync(IMAGE_DIR)) {
    fs.mkdirSync(IMAGE_DIR, { recursive: true });
}

// Helper: Download and Convert Image
async function processImage(url, filename) {
    if (!url) return null;

    try {
        const filepath = path.join(IMAGE_DIR, filename + '.webp');
        const publicPath = '/images/posts/' + filename + '.webp';

        if (fs.existsSync(filepath)) {
            console.log(`Skipping existing image: ${filename}`);
            return publicPath;
        }

        console.log(`Downloading: ${url}`);
        const response = await axios({ url, responseType: 'arraybuffer' });

        await sharp(response.data)
            .resize(1200, 800, { fit: 'cover', withoutEnlargement: true })
            .webp({ quality: 80 })
            .toFile(filepath);

        return publicPath;
    } catch (e) {
        console.error(`Failed to process image ${url}:`, e.message);
        return null;
    }
}

// Helper: Clean Divi Shortcodes
function cleanContent(html) {
    if (!html) return '';

    // 1. Remove [et_pb_*] tags but KEEP content
    // Regex for shortcodes: \[\/?et_pb_[^\]]*\]
    let cleaned = html.replace(/\[\/?et_pb_[^\]]*\]/g, '');

    // 2. Remove specific Divi garbage like empty p tags often left behind
    // cleaned = cleaned.replace(/<p>\s*<\/p>/g, '');

    // 3. Simple formatting cleanup
    cleaned = cleaned.replace(/\n\s*\n/g, '\n');

    return cleaned.trim();
}

async function runMigration() {
    console.log(`🚀 Starting Migration from ${INPUT_XML}...`);

    if (!fs.existsSync(INPUT_XML)) {
        console.error(`❌ Input file not found: ${INPUT_XML}`);
        console.log(`Usage: node scripts/migrate-divi.js <path-to-xml>`);
        return;
    }

    const xmlData = fs.readFileSync(INPUT_XML, 'utf-8');
    const parser = new xml2js.Parser();

    try {
        const result = await parser.parseStringPromise(xmlData);
        const channel = result.rss.channel[0];
        const rawItems = channel.item;

        console.log(`Found ${rawItems.length} total items. Filtering posts...`);

        // 1. Extract Attachments first (Media) to map IDs to URLs
        const attachments = {};
        rawItems.forEach(item => {
            const postType = item['wp:post_type'][0];
            if (postType === 'attachment') {
                const id = item['wp:post_id'][0];
                const url = item['wp:attachment_url'][0];
                attachments[id] = url;
            }
        });

        const posts = [];
        let count = 0;

        for (const item of rawItems) {
            const postType = item['wp:post_type'][0];
            const status = item['wp:status'][0];

            if (postType === 'post' && status === 'publish') {
                const title = item.title[0];
                const slug = item['wp:post_name'][0] || slugify(title, { lower: true });
                const date = new Date(item.pubDate[0]).toLocaleDateString('es-ES', {
                    year: 'numeric', month: 'long', day: 'numeric'
                });

                // Content Cleaning
                const rawContent = item['content:encoded'][0];
                const content = cleanContent(rawContent);
                const excerpt = content.substring(0, 150).replace(/<[^>]*>?/gm, '') + '...';

                // Categories
                const rawCats = item.category || [];
                // Find first mapped category or default
                let category = 'GENERAL';
                for (const catObj of rawCats) {
                    const catName = typeof catObj === 'string' ? catObj : catObj._;
                    if (CATEGORY_MAP[catName]) {
                        category = CATEGORY_MAP[catName];
                        break;
                    }
                }

                // Image Processing
                let thumbnail = null;
                const meta = item['wp:postmeta'];
                if (meta) {
                    const thumbMeta = meta.find(m => m['wp:meta_key'][0] === '_thumbnail_id');
                    if (thumbMeta) {
                        const thumbId = thumbMeta['wp:meta_value'][0];
                        const thumbUrl = attachments[thumbId];
                        if (thumbUrl) {
                            thumbnail = await processImage(thumbUrl, slug);
                        }
                    }
                }

                posts.push({
                    id: count + 1,
                    slug,
                    title,
                    content, // Full HTML for [slug] page
                    excerpt,
                    author: "Dr. A. Moreau", // Default for now
                    date,
                    category,
                    thumbnail: thumbnail || "https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=600" // Fallback
                });

                count++;
                console.log(`✅ Processed: ${title}`);
            }
        }

        fs.writeFileSync(OUTPUT_JSON, JSON.stringify(posts, null, 2));
        console.log(`🎉 Migration Complete! ${posts.length} posts saved to ${OUTPUT_JSON}`);

    } catch (err) {
        console.error('Migration Failed:', err);
    }
}

runMigration();

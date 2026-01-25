import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const xmlPath = path.join(__dirname, '../src/data/export.xml');
const outputPath = path.join(__dirname, '../src/data/reviews.json');

try {
    const xmlContent = fs.readFileSync(xmlPath, 'utf8');

    // Regex to capture comment blocks
    // <wp:comment> ... </wp:comment>
    const commentRegex = /<wp:comment>([\s\S]*?)<\/wp:comment>/g;
    let match;
    const reviews = [];

    while ((match = commentRegex.exec(xmlContent)) !== null) {
        const commentBlock = match[1];

        // Extract fields
        const authorMatch = /<wp:comment_author><!\[CDATA\[(.*?)\]\]><\/wp:comment_author>/.exec(commentBlock);
        const dateMatch = /<wp:comment_date>(.*?)<\/wp:comment_date>/.exec(commentBlock);
        const contentMatch = /<wp:comment_content><!\[CDATA\[([\s\S]*?)\]\]><\/wp:comment_content>/.exec(commentBlock);
        const approvedMatch = /<wp:comment_approved><!\[CDATA\[(.*?)\]\]><\/wp:comment_approved>/.exec(commentBlock);
        const typeMatch = /<wp:comment_type><!\[CDATA\[(.*?)\]\]><\/wp:comment_type>/.exec(commentBlock);

        // Filter: only approved comments, normal type (empty or 'comment')
        const isApproved = approvedMatch && approvedMatch[1] === '1';
        const isComment = !typeMatch || typeMatch[1] === '' || typeMatch[1] === 'comment';

        if (isApproved && isComment && contentMatch) {
            // Helper to strip CDATA and trim
            const clean = (str) => (str || '').replace('<![CDATA[', '').replace(']]>', '').trim();

            let content = clean(contentMatch[1]);
            const author = clean(authorMatch ? authorMatch[1] : 'Anónimo');
            const date = clean(dateMatch ? dateMatch[1] : new Date().toISOString());

            // Remove any HTML tags if present from content
            content = content.replace(/<[^>]*>?/gm, '');

            if (content.length > 5) { // Skip very short/empty comments
                reviews.push({
                    author,
                    date,
                    content,
                    rating: 5, // Defaulting to 5 as legacy reviews might not have stars
                    source: 'legacy'
                });
            }
        }
    }

    console.log(`Extracted ${reviews.length} reviews.`);

    // Sort by date descending
    reviews.sort((a, b) => new Date(b.date) - new Date(a.date));

    fs.writeFileSync(outputPath, JSON.stringify(reviews, null, 2));
    console.log(`Saved to ${outputPath}`);

} catch (err) {
    console.error('Error extracting reviews:', err);
}

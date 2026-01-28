import fs from 'fs';
import path from 'path';

const SITE_URL = 'https://parbiomagnetico.es';
const KEY = 'e61ed174b0984877a42d1f59fa62993e6';
const SITEMAP_PATH = path.join(process.cwd(), 'dist', 'sitemap-0.xml');

async function notifyIndexNow() {
    try {
        if (!fs.existsSync(SITEMAP_PATH)) {
            console.error('Sitemap not found at:', SITEMAP_PATH);
            return;
        }

        const sitemapContent = fs.readFileSync(SITEMAP_PATH, 'utf-8');
        const urls = [];
        const locRegex = /<loc>(.*?)<\/loc>/g;
        let match;

        while ((match = locRegex.exec(sitemapContent)) !== null) {
            urls.push(match[1]);
        }

        if (urls.length === 0) {
            console.log('No URLs found in sitemap.');
            return;
        }

        console.log(`Found ${urls.length} URLs in sitemap. Notifying IndexNow...`);

        const payload = {
            host: 'parbiomagnetico.es',
            key: KEY,
            keyLocation: `${SITE_URL}/${KEY}.txt`,
            urlList: urls
        };

        const response = await fetch('https://api.indexnow.org/indexnow', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8'
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            console.log('IndexNow notification sent successfully to api.indexnow.org');
        } else {
            const errorText = await response.text();
            console.error('IndexNow notification failed:', response.status, errorText);
        }

        // Individual search engines for fallback if needed, 
        // but IndexNow.org endpoint typically broadcasts to multiple engines (Bing, Yandex, etc.)

    } catch (error) {
        console.error('Error during IndexNow notification:', error);
    }
}

notifyIndexNow();

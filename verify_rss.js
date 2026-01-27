import fs from 'fs';
import http from 'http';

const url = 'http://localhost:4321/rss.xml';

http.get(url, (res) => {
    let data = '';
    res.on('data', (chunk) => {
        data += chunk;
    });
    res.on('end', () => {
        console.log('RSS Feed Length:', data.length);
        if (data.includes('xmlns:media="http://search.yahoo.com/mrss/"')) {
            console.log('PASS: Media namespace found.');
        } else {
            console.log('FAIL: Media namespace missing.');
        }

        // Check for media:content
        const mediaCount = (data.match(/<media:content/g) || []).length;
        console.log(`Found ${mediaCount} <media:content> tags.`);

        if (mediaCount > 0) {
            // Extract one example
            const example = data.match(/<media:content[^>]+>/)[0];
            console.log('Example tag:', example);
        }

        if (mediaCount > 0 && data.includes('<rss')) {
            console.log('VERIFICATION SUCCESSFUL');
        } else {
            console.log('VERIFICATION FAILED');
        }
    });
}).on('error', (err) => {
    console.log('Error: ' + err.message);
});

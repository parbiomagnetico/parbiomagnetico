
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const postsPath = path.join(__dirname, '../src/data/posts.json');
const contentDir = path.join(__dirname, '../src/content/blog');

// Ensure content directory exists
if (!fs.existsSync(contentDir)) {
    fs.mkdirSync(contentDir, { recursive: true });
}

// Simple HTML to Markdown converter
function htmlToMarkdown(html) {
    if (!html) return '';

    let text = html;

    // Remove comments
    text = text.replace(/<!--[\s\S]*?-->/g, '');

    // Headings
    text = text.replace(/<h2>(.*?)<\/h2>/g, '## $1\n');
    text = text.replace(/<h3>(.*?)<\/h3>/g, '### $1\n');

    // Bold/Italic
    text = text.replace(/<strong>(.*?)<\/strong>/g, '**$1**');
    text = text.replace(/<em>(.*?)<\/em>/g, '*$1*');

    // Links
    text = text.replace(/<a href="(.*?)">(.*?)<\/a>/g, '[$2]($1)');

    // Lists (Basic support)
    text = text.replace(/<ul>/g, '');
    text = text.replace(/<\/ul>/g, '');
    text = text.replace(/<ol>/g, '');
    text = text.replace(/<\/ol>/g, '');
    text = text.replace(/<li>(.*?)<\/li>/g, '- $1');

    // Paragraphs
    text = text.replace(/<p>/g, '');
    text = text.replace(/<\/p>/g, '\n\n');

    // Clean up excessive newlines
    text = text.replace(/\n\s*\n/g, '\n\n');

    // Decode HTML entities (basic)
    text = text.replace(/&nbsp;/g, ' ');
    text = text.replace(/&amp;/g, '&');
    text = text.replace(/&lt;/g, '<');
    text = text.replace(/&gt;/g, '>');
    text = text.replace(/&quot;/g, '"');

    return text.trim();
}

try {
    const rawData = fs.readFileSync(postsPath, 'utf8');
    const posts = JSON.parse(rawData);

    posts.forEach(post => {
        // Date formatting fixes if needed, assuming they are okay or just strings
        const frontmatter = `---
title: "${post.title.replace(/"/g, '\\"')}"
date: "${post.date}"
author: "${post.author}"
image: "${post.thumbnail}"
excerpt: "${post.excerpt.replace(/"/g, '\\"')}"
category: "${post.category}"
active: ${post.active}
---

`;
        const markdownBody = htmlToMarkdown(post.content);
        const fileContent = frontmatter + markdownBody;

        const fileName = `${post.slug}.md`;
        const filePath = path.join(contentDir, fileName);

        fs.writeFileSync(filePath, fileContent);
        console.log(`Created: ${fileName}`);
    });

    console.log('Migration completed successfully!');

} catch (err) {
    console.error('Error during migration:', err);
}

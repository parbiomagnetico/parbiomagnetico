import rss from '@astrojs/rss';
import posts from '../data/posts.json';

export async function GET(context) {
    // Use site from config or fallback
    const site = context.site?.toString() ?? 'https://parbiomagnetico.es';
    // Ensure site does not end with slash for cleaner concatenation with paths starting with slash
    const siteUrl = site.endsWith('/') ? site.slice(0, -1) : site;

    // Helper to parse Spanish dates like "26 de enero de 2026"
    const monthMap = {
        enero: 0, febrero: 1, marzo: 2, abril: 3, mayo: 4, junio: 5,
        julio: 6, agosto: 7, septiembre: 8, octubre: 9, noviembre: 10, diciembre: 11
    };

    const parseDate = (dateStr) => {
        try {
            if (!dateStr) return new Date();
            const parts = dateStr.split(' de ');
            if (parts.length !== 3) return new Date();
            const day = parseInt(parts[0], 10);
            const month = monthMap[parts[1].toLowerCase()] || 0;
            const year = parseInt(parts[2], 10);
            return new Date(year, month, day);
        } catch (e) {
            return new Date();
        }
    };

    const activePosts = posts.filter(post => post.active);

    return rss({
        title: 'Par Biomagnético - Blog',
        description: 'Artículos sobre biomagnetismo, salud y bienestar.',
        site: siteUrl,
        xmlns: {
            media: 'http://search.yahoo.com/mrss/',
        },
        items: activePosts.map((post) => ({
            title: post.title,
            pubDate: parseDate(post.date),
            description: post.excerpt || post.title, // Fallback to title if excerpt missing
            link: `/blog/${post.slug}/`,
            customData: `
        <media:content url="${siteUrl}${post.thumbnail}" medium="image" />
        <media:thumbnail url="${siteUrl}${post.thumbnail}" />
      `,
        })),
        customData: `<language>es-es</language>`,
    });
}

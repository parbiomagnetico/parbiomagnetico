import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://parbiomagnetico.es', // Esto ayuda al SEO y a generar el sitemap
  integrations: [
    tailwind(),
    sitemap({
      serialize(item) {
        if (item.url === 'https://parbiomagnetico.es/') {
          item.changefreq = 'daily';
          item.priority = 1.0;
        } else if (item.url.includes('/opiniones') || item.url.includes('/tratamientos')) {
          item.changefreq = 'weekly';
          item.priority = 0.9;
        } else if (item.url.includes('/blog/')) {
          item.changefreq = 'monthly';
          item.priority = 0.7;
        } else {
          item.changefreq = 'monthly';
          item.priority = 0.5;
        }
        return item;
      },
    }),
  ],
  prefetch: {
    defaultStrategy: 'hover',
  },
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp',
      config: {
        quality: 80,
      },
    },
  },
});
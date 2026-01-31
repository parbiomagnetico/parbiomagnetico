
import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
    schema: z.object({
        title: z.string(),
        date: z.string(),
        author: z.string(),
        image: z.string().optional(),
        excerpt: z.string(),
        category: z.string(),
        active: z.boolean().default(true),
    }),
});

export const collections = {
    'blog': blogCollection,
};

import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.string(),
    author: z.string().default('Author'),
    heroImage: z.string().optional().default(''),
    alt: z.string().optional().default(''),
  }),
});

export const collections = { blog };

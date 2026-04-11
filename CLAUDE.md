# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm install          # Install dependencies
npm run dev          # Start dev server at localhost:4321
npm run build        # Build to ./dist/
aws s3 sync dist s3://jounileino.com  # Deploy to AWS S3
```

## Architecture

This is a personal blog/portfolio site built with **Astro 5** using Content Collections.

**Page rendering flow:**
- `src/pages/index.astro` — home page; fetches all posts via `getCollection('blog')`, sorts by `publishDate`, renders them with `BlogPostPreview`
- `src/content/blog/*.md` — individual blog posts with frontmatter (`title`, `description`, `publishDate`, `author`, `heroImage`, `alt`); schema defined in `src/content/config.ts`
- `src/pages/blog/[...slug].astro` — dynamic route that renders each blog post using the `BlogPost` component
- `src/layouts/BlogPost.astro` — full-page layout wrapping `BaseHead`, `BlogHeader`, `BlogPost` component, and `Footer`

**Component hierarchy:**
- `BaseHead` — `<head>` meta tags, SEO, stylesheets
- `BlogHeader` — top navigation bar with logo
- `BlogPost` — article wrapper with hero image and metadata
- `BlogPostPreview` — card shown on the index page for each post
- `Intro` — hero section on homepage with author photo and social links
- `Footer` — page footer

**Static assets** live in `public/` and are mirrored to `dist/` on build. Blog post images go in `public/blog/<post-slug>/`.

**Deployment note:** The site uses CloudFront → S3 static website hosting. `build.format: 'directory'` generates `contact/index.html`, `blog/slug/index.html` etc., which S3's index document feature serves automatically. No post-processing needed before `aws s3 sync`.

**Adding a blog post:** Create a new `.md` file in `src/content/blog/` named `YYYY-MM-DD-slug.md` with the required frontmatter fields, and place any images under `public/blog/<slug>/`.

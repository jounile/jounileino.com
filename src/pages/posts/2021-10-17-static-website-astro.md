---
title: 'Static website hosting' 
description: 'Optimize for performance and ease of use' 
publishDate: '17. October 2021' 
author: 'Author' 
heroImage: '' 
alt: 'Astro' 
layout: '../../layouts/BlogPost.astro'
---

My blog was previously created with [Jekyll][jekyll-website] so it required using Ruby libs. I felt this was somehow a bit cumbersome so I kinda avoided updating the blog just for that reason. Jekyll outputs a static website which I hosted in AWS. 

I like the idea of a static website for many reasons. 

AWS provides a possibility to host a static website directly from a S3 bucket. This is convenient due to couple of reasons. 

1. Cost factor

    Hosting a website on a server instance may be rather expensive depending on the size of the traffic to your website.

    S3 storage on the other hand is ridiculously cheap. 

2. High availability

    Building a website with good uptime requires designing an architecture that is fail safe. 

    Such architecture requires duplicate resources so that in case a server goes down, another server instance can automatically step in and serve the website.

    AWS guarantees 99,99% availability of their S3 service. 

3. Scalability

    Server instance size must be selected upfront according to expected traffic size. When the traffic grows a bigger instance is required and that means more cost. 
    Adding autoscaling to upscale with more instances for peak usage requires more server instances and also results to higher cost.

    S3 scales automatically to meet your growing demand.


4. Maintenance

    Hosting a website on a server can be a laborous as it requires you to setup infrastructure. Setting up infrastructure in AWS requires knowing how to secure the environment properly. A server runs a process that may sometimes fail for various reasons which means that occationally a server requires maintenance. 

    S3 is fully managed by AWS and you do not need to care about any of the above.

5. Deployments

    Deploying your website to a server can be more laborous than deploying to a S3 bucket. 
    Deploying a website to S3 bucket can be done with a signle command from the local development environment.
    
    ```shell
    aws s3 sync . s3://<bucket-name>
    ```

Astro provides some great examples on their [Github][astro-github] which gives you a great starting point for exploring how to build things with it.
I used this example source code for my blog:
[astro-blog-example][astro-blog-example]

Some modifications were needed for the layout and I added a contact page.

The blog is structured so that each blog post can be created in [Markdown][markdown-website] syntax.
Creating a new post requires simply making a new file with .md extension.
The file should include some definitions in the header and content can be styled with Markdown.

For example this page has the following header definitions:


```markdown
---
title: 'Static website hosting'
description: 'Optimize for performance and easy of use'
publishDate: '17. October 2021'
author: 'Author'
heroImage: ''
alt: 'Astro'
layout: '../../layouts/BlogPost.astro'
---
```

I love this for it´s simplicity. 
Speaking of simplicity, my previous blog had one flaw that I wanted to correct with this rewrite. Pictures were hosted in a separate S3 bucket that made working on new content unneccessarily complicated. It is more convenient when pictures are handled in the same way as the blog posts directly in the development environment and deployed with the website code.

When building a static website, there is actually a lot more to it. So far we have focused on the hosting aspect but let´s clarify why I chose Astro. [Astro][astro-website]. 

First, have a look at the [introduction][astro-introduction].

"In Astro, you compose your website using UI components from your favorite JavaScript web framework. Astro renders your entire site to static HTML during the build. The result is a fully static website with all JavaScript removed from the final page. No monolithic JavaScript application required, just static HTML that loads as fast as possible in the browser regardless of how many UI components you used to generate it."

These features make Astro quite appealing to me.

- Bring Your Own Framework (BYOF): Build your site using React, Svelte, Vue, Preact, web components, or just plain ol’ HTML + JavaScript.
- 100% Static HTML, No JS: Astro renders your entire page to static HTML, removing all JavaScript from your final build by default.
- On-Demand Components: Need some JS? Astro can automatically hydrate interactive components when they become visible on the page. If the user never sees it, they never load it.
- Fully-Featured: Astro supports TypeScript, Scoped CSS, CSS Modules, Sass, Tailwind, Markdown, MDX, and any of your favorite npm packages.
- SEO Enabled: Automatic sitemaps, RSS feeds, pagination and collections take the pain out of SEO and syndication.

This is exactly what I want. Flexibility to use tools that I´m familiar with in order to maximize my productivity & distribution that is easy to deploy and gives best possible website performance.

I will soon make another post about the required AWS infrasturcture that is needed for hosting a static website in AWS. 

[jekyll-website]:   https://jekyllrb.com/
[astro-blog-example]:     https://github.com/vsnowpackjs/astro/tree/main/examples/blog
[astro-website]:     https://astro.build/
[astro-github]:     https://github.com/snowpackjs/astro/tree/main/examples
[astro-introduction]:     https://astro.build/blog/introducing-astro/
[markdown-website]:     https://www.markdownguide.org/
---
title: 'Static website hosting' 
description: 'Optimize for performance and easy of use' 
publishDate: '17. October 2021' 
author: 'Author' 
heroImage: '' 
alt: 'Astro' 
layout: '../../layouts/BlogPost.astro'
---

My blog was previously created with Jekyll and required using Ruby libs. This was cumbersome so I kinda avoided updating the blog just for that reason. Jekyll outputted a static website which I deployed to AWS S3. 

I like the idea of a static website for many reasons.

AWS provides a possibility to host a static website directly from a S3 bucket. This is convenient due to couple of reasons. 

1. Cost factor

    Hosting a website on a server instance may be rather expensive depending on traffic to the website.

    S3 storage on the other hand is ridiculously cheap. 

2. High availability

    Building a website with maximal uptime requires designing an architecture that is fail safe. 

    Such architecture requires duplicate resources so that in case a server goes down, another one can automatically step in to serve the website.

    Amazon guarantees 99,99% availability of S3 service.

3. Scalability

    Server instnce size must be selected according to expected traffic size. More traffic means more cost. Adding autoscaling to upscale for peak usage requires more server instances and results to higher cost.

    S3 scales automatically to meet your growing demand.


4. Maintenance

    Hosting a website from a server requires some work on the infrastructure setup and also occational maintenance.

    S3 is fully managed by AWS.

5. Deployments

    Deploying to a server can be more laborous than deploying to a S3 bucket which can be done with a signle command from the local development environment.


I used this example source code for my blog:
[astro-blog-example][astro-blog-example]

Some modifications were needed for the layout and I added a contact page.

The blog is structured so that each blog post can be created in Markdown syntax.
Creating a new post requires simply making a new file with .md extension /src/pages/posts.
The file should include some definitions in the header and content can be styled with Markdown.

I love this for it´s simplicity. 
Speaking of simplicity, my previous blog had one flaw that I wanted to correct with this rewrite. Pictures were hosted in a separate S3 bucket that made working on new content unneccessarily complicated. It is more convenient when pictures are handled in the same way as the blog posts directly in the development environment and deployed with the website structure.

When building a static website, there is actually a lot more to it. This post focused on the hosting aspect but we didn´t look into using the [Astro][astro-website] framework.
I will soon make another post about the required AWS infrasturcture that is needed for hosting a static website in AWS. 

[astro-blog-example]:     https://github.com/vsnowpackjs/astro/tree/main/examples/blog
[astro-website]:     https://astro.build/
title: 'Static website Astro' description: 'Optimize for performance and easy of use' publishDate: '16. October 2021' author: 'Author' heroImage: '' alt: 'Astro' layout: '../../layouts/BlogPost.astro'

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


I used this example source code for a blog:

https://github.com/vsnowpackjs/astro/tree/main/examples/blog
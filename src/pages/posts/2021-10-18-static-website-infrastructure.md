---
title: 'Static website infrastructure' 
description: 'Build a modern cost effective infrastructure on AWS' 
publishDate: '18. October 2021' 
author: 'Author' 
heroImage: '' 
alt: 'Astro' 
layout: '../../layouts/BlogPost.astro'
---

In this blog post I try to describe how you can put together a scalable and cost effective website infrastructure using AWS.

We will cover the following topics:
- Enabling static website hosting in S3
- Routing traffic using Route53
- Securing a website using SSL certificate
- Reducing latency using CloudFront edge locations

There are a number of tasks that we need to handle in various AWS services in order to achieve our goal. I categorized the tasks by service.


1. [Certificate Manager][certificate-manager]

- Creating SSL certificate

    Request certificate -> Request a public certificate -> Add domain name

    Insert yourdomain.com and additionally *.yourdomain.com

    After the certificate is successfully issued you will see something like.

    <img src="/blog/static-website-infrastructure/ssl-certificate.png" />
    


2. [CloudFront][cloudfront]

- Creating a CloudFront distribution

    Make sure that the SSL certificate you created in [Certificate Manager][certificate-manager] is defined to be used by the Cloudfront distribution.
    
    Also the default root object should be specified as index.html

    <img src="/blog/static-website-infrastructure/cloudfront-distribution.png" />

- Defining an origin

    Here the Origin domain field is suggesting entries but can also be manually edited. 
    
    <img src="/blog/static-website-infrastructure/cloudfront-origin.png" />

    I noticed that sub-pages on the website were not displayed for some reason and I would get Access Denied when entering for exampe /contact page. This <a href="https://gist.github.com/zulhfreelancer/24f73015c5437281f3b98c3cb34ea225" target="_blank">Gist</a> provided a solution tough.

    <b>Solution: <br>Insert into the Origin domain field the same value as in the Static Website Hosting in S3 bucket Properties.</b>
    
    <img src="/blog/static-website-infrastructure/static-website-hosting.png" />

- Defining a behavior

    <img src="/blog/static-website-infrastructure/cloudfront-behavior.png" />



3. [Route53][route53]

    I expect you have already purchased yourdomain.com so I will skip a few steps with Route53. When you have a Domain and a Hosted zone created in Route53, your NS records should be pointing to AWS nameservers. 
    
    Now let´s configure the website specific records.

- Creating A record

    Point your domain to cloud front distribution.

    <img src="/blog/static-website-infrastructure/a-record.png" />

- Creating CNAME

    Redirect requests from www.yourdomain.com to yourdomain.com

    <img src="/blog/static-website-infrastructure/cname.png" />



4. [S3][s3]

- Creating website

    For testing purposes you can just create index.html and error.html and upload those into your bucket.

- Creating a S3 Bucket policy

    Now let´s configure the bucket that will host our website.
    Insert the following into:
    Your bucket -> Permissions -> Bucket policy

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Allow-Public-Access-To-Bucket",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::yourdomain.com/*"
            }
        ]
    }
    ```

Now all the pieces should be in place. 
This setup is cheap and requires no maintenance. The website can be updated by just simply uploading a new version of the website into the S3 bucket.

My monthly bill includes the following:

| Service     | Cost          |
| ----------- | ------------- |
| S3          | $ 0.01        |
| Cloudfront  | $ 0.01        |
| Route53     | $ 1.00        |
| Route53 VAT | $ 0.19        |
| ----------- | ------------- |
| Total       | $ 1.21        |


[s3]:   https://aws.amazon.com/s3/
[cloudfront]:   https://aws.amazon.com/cloudfront/
[route53]:  https://aws.amazon.com/route53/
[certificate-manager]:  https://aws.amazon.com/certificate-manager/

---
title: 'AWS Gameday experience'
description: ''
publishDate: '17. October 2019'
author: 'Author'
heroImage: ''
alt: 'Astro'
layout: '../../layouts/BlogPost.astro'
---

AWS Gameday is a fun game like event where participants compete against each other in teams.
The goal is to create and run online services for a Fictional company named "Unicorn Rentals".

<img src="/blog/aws-live-virtual-gameday/scoreboard.png" width="720" alt="Scoreboard" />

The event was live streamed via [Twitch][twitch] with commentary and live scoreboard. Also some AWS employees participated in the event as a team and share their progress, insights and thoughts during the game.

In the beginning of the event each team gets access to a fully fledged AWS cloud environment via AWS Console and API. There is also a Team Dashboard where team´s running service endpoints must be entered when progressing in the game. The team scores points for each running service.

Each team gets a predefined service, a frontend API (called the "Service Router"). This runs on a EC2 instance and it´s purpose is to list team´s running services so other teams can use those.

Each team must run one of the many Service Routers and keep it alive. When the Service Router starts having issues teams must analyse the problem and bring it back up. 

Under the hood Service Router finds microservice endpoints from a DynamoDB table. Each team should edit this table by adding service endpoints of other teams. This is a way to score higher but when problems occur in the teams own services they begin to lose points, so every team is required to fix their issues and maintain good service availability.

Problems can be identified by monitoring logs and also watching teams score events for changes.

Tasks each team goes through:
- Deploy, Maintain and Optimize microservices for other teams to use.
- Publish teams services in "Services Marketplace" using a Dashboard. 
- Making teams Service Router highly available.
- Use the fastest microservices and score high 
- Keep everything going. 

Things teams should avoid:
- Consuming team´s own services

The ultimate goal is to use many services, preferably the fastest ones and thereby gain a high score. The Legacy Services provided at the start of the game are very slow so each team should swap their endpoints to more optimized ones. 

Services that each team needed to create and keep running.
1. swapcaser: SAM(Lambda and API Gateway)
2. reverser: Fargate
3. leeter: Elastic Beanstalk

Some unexpected events were designed to happen during the game. It was possible to for example suddenly lose a team member or to get hit by a security issue mid-flight.

The dashboard included a Chat link for teams to use in order to ask for help from AWS professional services team.

The game duration was 3 hours. Originally it was designed to be run in a 4h session so this was a rather tight schedule. Originally we had planned to have a small team with some of my colleagues from Siili Solutions but in the end I was going solo as everyone else cancelled due to the awkward timing (Game starting at 22:00 PM). To make things worse for myself I was not able to start when the live stream begun. I clocked in one hour late without any instructions as those were given in the beginning of the live stream. Luckily I found a [Readme][readme] document that steered me to the right path.

Here is a summary of what I accomplished during the two hours:

### Leeter
- Deployed a Beanstalk application
- Fixex Launch configuration to bring the application running again.

### Swapcaser
- Created an S3 bucket and uploaded a deployment package into it.
- Modified the Cloudformation template to point to S3 bucket URI
- Upload the application sources and modified the Cloudformation template 
- Deploy Cloudformation template to create Serverless infra
- Investigated Cloudwatch logs and X-ray traces to determine the root cause for a failing Lambda function.

### Reverser
- Created Security Group to allow HTTP port 80
- Created Fargate cluster from a predefined Task

### Service Router
- Re-created Service Router EC2 Instance with given Userdata


I noticed the Service Router failure too late to recover score wise and I was forced to quickly assess what next step would ensure me a better score in the end. I guessed starting the Servie Router had a high priority so decided to kick it up and right then returned to investigating the Lambda function error logs. It was dificult to keep track of my score as I was working with only one screen and constantly jumping between browser windows and tabs.  

The game was a lot of fun although quite stressful because there were multiple microservices to operate. Each task required knowledge of multiple AWS services and in the beginning the game seemed very overwhelming. It would have definately helped to have a team where tasks would have been distributed allowing a narrower focus area for each participant. Nevertheless, I really recommend AWS Gameday for everyone who likes solving technical problems in a well designed game setting. You may learn some new things along the way and get satisfaction from accomplishing real operational tasks in a first class cloud environment.


[readme]:      https://s3.amazonaws.com/ee-assets-prod-us-east-1/modules/gd2018-loadgen/v2/readme.md
[twitch]:   https://www.twitch.tv/aws/

---
title: 'Unreal Pixel Streaming' 
description: 'Deploying a UE4 CarConfigurator into Azure cloud' 
publishDate: '13. April 2022'
author: 'Author' 
heroImage: '' 
alt: 'Astro' 
layout: '../../layouts/BlogPost.astro'
---

Let´s have a look on how Unreal applications can be shared via browser using PixelStreaming.
Unreal PixelStreaming uses WebRTC which allows the user to interact with the Unreal project.
Epic Marketplace provides a CarConfigurator example project which we deploy to a PixelStreaming server.
The server can exist locally on a single computer or in the cloud either on one single VM. There is also a possibility to use auto-scaling in the cloud to allow more concurrent users. This however can quickly get very expensive to host as the VMs need to have multiple vCPUs (6,12 or 24) to compute the 3D application and stream it.
There is a convenient way to setup PixelStreaming server in Azure cloud. Epic has created a Marketplace offering together with Microsoft which automates the process of setting up the server.

https://docs.unrealengine.com/4.27/en-US/ProductionPipelines/CloudDeployments/AzurePixelStreaming/ 


You will need to have an Azure Cloud setting up the environment.

## How to guide ##

This guides you how to create a minimal setup.

 

### 1. Preparation ###

Make a Windows build of your application from Unreal Editor. 
File → Package → Windows

Create a ResourceGroup and a Container in Azure. Upload Windows build of your Unreal application in into the container.

<img src="/blog/unreal-pixel-streaming/create-container-and-upload-archive.png" />
 

### 2. Find Unreal Pixel Streaming offering in the Marketplace ###

You can find it by using search keyword “epic“.

<img src="/blog/unreal-pixel-streaming/marketplace.png" />

Press the Create -button

### 3. Create a ResourceGroup ###

This will hold all your resources in one bundle.

<img src="/blog/unreal-pixel-streaming/create-resourcegroup.png" />

### 4. Select Region ###

I selected the region West Europe, set GPU VM Instances Per Region to 1.

<img src="/blog/unreal-pixel-streaming/select-region.png" />

### 5. Select UE4 App GPU VM Size ###

Now select a VM size according to your requirements. 
If you use for example RayTracing in your application then more is better (and more expensive)

<img src="/blog/unreal-pixel-streaming/select-gpu-size.png" />

A dialog pops up and there you can choose another VM type.

<img src="/blog/unreal-pixel-streaming/select-vm-size.png" />

Good to know about quota limits

Azure has quota limits per region.  - Depending on how selected region, defined quota and you scaling options the deployment may fail due to insufficient vCPU quota.
You may get an error like this in the deployment log:

`
Code: QuotaExceeded
Message: Operation could not be completed as it results in exceeding approved Total Regional Cores quota. 
Location: eastus
Current Limit: 10, Current Usage: 0, Additional Required: 16, (Minimum) New Limit Required: 16. 
Submit a request for Quota increase.
`

In Azure you can request to get your quota increased. I sent the quota increase request and specified required 16. It was approved in about one minute.
Sometimes the quota increase cannot be automatically approved and in that case you must make a request to Microsoft Azure support team.
When the quota is not sufficient you can also try to downscale the VM size.

NV6 type requires only 6 x vCPUs and this was enough for me in the West Europe region. 

However NV6 series VMs are now actually legacy and should be migrated to more expensive VMs.
https://docs.microsoft.com/en-us/azure/virtual-machines/nv-series-migration-guide   

### 6. Select UE application to be deployed ###

The archive should be uploaded to a container in Azure in order to select it here.

<img src="/blog/unreal-pixel-streaming/select-archive.png" />

The archive can be created as Windows build from the Unreal Editor. Inside there should be the Engine build, CarConfigurator application directory and executable.

<img src="/blog/unreal-pixel-streaming/app-executable.png" />
 

### 7. Name your UE App ###

The name must match with the executable.

<img src="/blog/unreal-pixel-streaming/name-your-app.png" />

### 8. Enter credentials for accessing the VM ###

These can be used to connect to the VM via RDP for example.

<img src="/blog/unreal-pixel-streaming/credentials.png" />
 

### 9. Select Regions to deploy ###

To lower your cost you can set the GPU VM Instances Per Region to 1.

<img src="/blog/unreal-pixel-streaming/regions.png" />

### 10. Auto-Scaling ###

To minimize cost let´s disable auto-scaling.

<img src="/blog/unreal-pixel-streaming/auto-scaling.png" />

### 11. App resolution ###

Here you can customize the resolution to fit your needs.

<img src="/blog/unreal-pixel-streaming/app-resolution.png" />

### 12. Custom domain ###

We can also assign a custom domain name if the customer wants.

<img src="/blog/unreal-pixel-streaming/custom-domain.png" />

### 13. Admin dashboard ###

If you have the app´s Client ID you can Enable Admin Dashboard option.

<img src="/blog/unreal-pixel-streaming/admin-dashboard.png" />

### 14. Tags ###

Create at least the following tags to inform other Azure users what is this solution about and who to contact if they need to.

<img src="/blog/unreal-pixel-streaming/tags.png" />

Review and create the resources.

 

## Result ##

After successful deployment the Unreal based CarConfigurator application can be viewed with any device via the generated DNS name that can be found in the Traffic Manager profile.

<img src="/blog/unreal-pixel-streaming/trafficmanager.png" />

<img src="/blog/unreal-pixel-streaming/carconfigurator.png" />


### Considerations ###

Here are some considerations for going forward:

- Multiple streams are needed for example if the content is required to be viewed for example with different resolutions via different devices. e.g. PC, Tablet, Phone.

- If different users should have a different experience like admin to control the presentation and user to view the presentation, then Multiple Player Endpoints are needed. This can be done by implementing two entrypoint HTML pages on the Web Server.

- Instead of having all users connect to the same stream, you may want each person to end up in their own interactive experiences. In this case you will need multiple Signaling and Web servers.

- If you have fewer servers than users, people may need to wait until a connection is free. In this case you need to enable auto-scaling in Azure.

### Possibility to use Linux VMs instead? ###
Initially supported only on Windows hosts.

Pixel Streaming for Linux in GPU-accelerated Linux containers is limited to UE4.27. For previous UE versions it is deprecated.

Support on Linux seems to be available only inside Docker container. https://adamrehn.com/articles/pixel-streaming-in-linux-containers/ 

### Possibility to run in AWS Cloud? ###

The equivalent VM family in AWS is G4.


### Pricing ###

NV6 used here pricing in Azure. This does not include storage cost and other services.

<img src="/blog/unreal-pixel-streaming/pricing.png" />

Pricing in AWS cloud for this kind of minimal setup is comparable to Azure pricing.

1x EC2 G4 Windows Server VM (g4ad.xlarge)

373.67 USD / month

4,484.04 USD / year
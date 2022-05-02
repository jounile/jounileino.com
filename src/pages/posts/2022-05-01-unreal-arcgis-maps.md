---
title: 'ArcGis maps for Unreal' 
description: 'Getting started with ArcGis maps on Unreal Engine' 
publishDate: '1. May 2022'
author: 'Author' 
heroImage: '' 
alt: 'Astro' 
layout: '../../layouts/BlogPost.astro'
---

ArcGIS Maps SDK for Unreal Engine is a plugin developed by Esri that enables access to real world maps and 3D content from the ArcGIS Platform. You can join the beta program from the Esri Early Adopter site and download the ArcGIS Maps SDK for Unreal Engine beta plugin.

This guides you how to create the needed account, retrieve ApiKey, install the plugin and run the sample maps implementation.

 

### 1. Early access program ###

Navigate to https://earlyadopter.esri.com and create a new account.

Choose the Early Access Program - ArcGis Maps SDK for Game Engines.

<img src="/blog/unreal-arcgis-maps/arcgis-early-access.png" />

Once you are logged in, navigate to Software Downloads from the top menu. There you can select the plugin version of your choice. 

Current options are:
- ArcGIS Maps SDK for Unreal Engine 5 - Prerelease
- ArcGIS Maps SDK for Unity - Prerelease
- <b>ArcGIS Maps SDK for Unreal Engine 4 - Prerelease</b>
- ArcGIS Maps SDK for Unity - Beta 2
- ArcGIS Maps SDK for Unreal Engine 4 - Beta 2

As you can see the plugin is available also for Unity.


### 2. Installing ArcGis plugin ###

Create a new project in Unreal Engine.

Unarchive the plugin sources and copy it in your Unreal project under Plugins -directory.

<img src="/blog/unreal-arcgis-maps/arcgis-unreal-install-plugin.png" width="100" height="100" />

Once the plugin is located under the project structure you can start your project in the Unreal Editor.

There is a online guide in the arcgis developer portal https://developers.arcgis.com/dashboard and the plugin sources come with the same guide. You can view it by starting a local web-server and opening the guide from your disk.

<img src="/blog/unreal-arcgis-maps/arcgis-maps-sdk.png" />


Now check that the plugin is Enabled in Edit -> Plugins

<img src="/blog/unreal-arcgis-maps/arcgis-plugin.png" />


### 3. Configure map ###

Click on the ArcGis Maps button in the menu.

<img src="/blog/unreal-arcgis-maps/arcgis-create-component.png" />

That will create the required ArcGisMapController in the World Outliner.

<img src="/blog/unreal-arcgis-maps/arcgis-map-controller.png" />

There you can configure the origin location of the map as latitude and longitude.

<img src="/blog/unreal-arcgis-maps/arcgis-set-origin-location.png" />

### 4. Set API Key ###

In the developer dashboard copy the Default API Key to clipboard.

<img src="/blog/unreal-arcgis-maps/arcgis-developer-dashboard.png" />

Now navigate to the Map controller and paste the API Key into it´s reserved field. This will grant access to retrieve ArcGis data from their platform.

<img src="/blog/unreal-arcgis-maps/arcgis-paste-api-key.png" />



### 4. Run the map ###

There is a example map level that you can check to confirm that maps are getting rendered.

Open the ArcGisMapsSDK Content -> Samples -> DetailsPanelUIExample

<img src="/blog/unreal-arcgis-maps/arcgis-unreal-map.png" />

This is the starting point. 
Next you can configure your own map in Unreal, add layers and explore how to customize the map visualization.

This webinar https://youtu.be/H_VonQRokh0 demostrates some interesting map visualizations. Using layer attributes for altering the map seems to provide a lot of flexibility.



[introduction]:	https://youtu.be/H_VonQRokh0

[esri]: http://www.esri.com

[unreal-engine-sdk]: https://developers.arcgis.com/unreal-engine-sdk/

[arcgis developer dashboard]: https://developers.arcgis.com/dashboard/#

[esri-early-adopter]: https://earlyadopter.esri.com/

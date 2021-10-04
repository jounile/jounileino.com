---
title: 'Augmented reality app'
description: 'AR with AWS Sumerian'
publishDate: '6. May 2019'
author: 'Author'
heroImage: ''
alt: 'Astro'
layout: '../../layouts/BlogPost.astro'
---

AR with AWS Sumerian

This weekend I decided to test Amazon Sumerian more and see if I could make something interesting with it. I came across this <a href="https://www.youtube.com/watch?v=QKeCDZWkExQ">recording</a> and just followed the guide.


Apparently an easy way to get started with AR in Sumerian is to clone the <a href="https://github.com/aws-samples/amazon-sumerian-arkit-starter-app">Amazon Sumerian ARKit starter app</a>.

<img src="/blog/arkit-sumerian/laptop.jpg" width="720" alt="Laptop" />

In Amazon Sumerian you must click Publish and copy the generated URL that points to your public hosted scene.

In XCode ViewController.swift you need to change the sceneURL to the previously copied URL.
Also append in the end of the URL /?arMode=true

```bash
private let sceneURL = URL(string: "https://eu-central-1.sumerian.aws/30080fd84e4346b6a8179147c1b688b0.scene/?arMode=true")!
```

If the Xcode build fails with something saying "Trust" you should go to iPhone settings -> General -> Device Management -> Your developer account and click Trust (developer account).

<img src="/blog/arkit-sumerian/untrusted.png" width="30%" height="30%" />

It should look like this. Apps from your apple developer account are listed here.

<img src="/blog/arkit-sumerian/verified.png" width="30%" height="30%">

When the AR app tries to launch on the iPhone you need to allow accessing device Camera. 

<img src="/blog/arkit-sumerian/access-camera.png" width="30%" height="30%">

Now you should see your iPhone app installed.


<img src="/blog/arkit-sumerian/app-icon.png" width="30%" height="30%">

When the app starts it shows a progress bar and your AR app name.

<img src="/blog/arkit-sumerian/progressbar.png" width="50%" height="50%">

or possibly this error message if something goes wrong. Please check your sceneURL in XCode again.

<img src="/blog/arkit-sumerian/loading-error.png" width="50%" height="50%">

When the app is started it might take a second or two to load this box onto the scene.

<img src="/blog/arkit-sumerian/cube.jpg" width="50%" height="50%">

Look around through the iPhone camera and you should see other content you placed on the scene in Sumerian.

<img src="/blog/arkit-sumerian/character.jpg" width="50%" height="50%">

Creepy no?

Your scene items get augmented into the scene you are currently in. 
<img src="/blog/arkit-sumerian/cube-lamp.jpg" width="50%" height="50%">

For example here the lamps are placed in the ceiling.

<img src="/blog/arkit-sumerian/augmented-lamp.jpg" width="50%" height="50%">



Here is also a short tutorial on how to add a trusted app on iphone: <a href="https://www.youtube.com/watch?v=7ejkoLgoPGk">guide</a>

See the Amazon Sumerian [website][sumerian] for more info. 


[sumerian]:      https://docs.sumerian.amazonaws.com/tutorials/create/intermediate/augmented-reality-using-sumerian-arkit/

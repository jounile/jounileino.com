---
title: 'Hackathon Stuttgart'
description: ''
publishDate: '28. October 2019'
author: 'Author'
heroImage: ''
alt: 'Astro'
layout: '../../layouts/BlogPost.astro'
---


[Hackathon Stuttgart][hackathon-stuttgart] was organized in the Römerkastell 25th – 27th Oct. 2019.
The event started on Friday afternoon with an introduction and team building.
After sponsors had given an overview of the tools, equipment, software and hardware available each participant had a chance to pitch for their idea.
While participants went around discussing with each other about various ideas everyone had a possibility to join a team of their choice. 
Organizers helped teams to find fitting members and assisted on registering.

<img src="/blog/hackathon-stuttgart/pitch.png" width="720" alt="The pitch" />

I had a couple of ideas that I thought might be fun to implement. Previously I had noticed Bosch having some kind of mobility project called [COBI.Bike][cobi-bike]. I thought it might be fun to implement a cloud based platform for a bicycle challenge. I recall in Finland we have such a thing called "Kilometrikisa", a competition between companies about travelling collectively the greatest distance in a given time. I remember seeing some participants registering their kilometres on a whiteboard at the office. This could definitely be implemented as a digital platform with real-time scoreboard and automated recording of travels. COBI.Bike seems like a great asset for such. Unfortunately, I heard from some Bosch representative that the person who was supposed to be bringing COBI.Bike concept to the Hackathon became sick on the previous day and therefore this sponsor was not participating the event after all.

I had another idea while I was looking into what gadgets were available to us during the weekend. I have been interested in voice interfaces for a while now so it could have been a great opportunity to implement something like that now. I end up pitching my idea but struggled to find others interested in the same topic.

Soon I met some nice dudes during the team formation and it was fun to exchange ideas and to see everyone fuelling each other shaping the initial ideas to something more concrete. Eventually I got introduced to a couple of guys who wanted to work on the Porsche infotainment system and APIs provided by Stuttgart Airport. This sounded very challenging and a great learning opportunity & it linked well to my professional experience with cloud computing & automotive.

Friday night was well spent getting familiar with the Airport API and setting up initial project in technical terms. In the beginning, we had no clue about the software, hardware and interfaces. Consensus of the programming language to be used was formed with one simple question: "What languages have you used before?". We decided to write the backend with Python as it was well known within the team and we knew we could develop something relatively fast by using it. 

Our team was well rounded in terms of project roles: 
1. One designer without programming knowledge
2. Frontend developer
3. Two backend developers
4. One fullstack developer
5. One technical project lead

Two of the youngest guys were actually highly talented students with emerging potential.
I focused first on finding out how to use the Airport API so that we had proper live data to work with.

After sleeping the night at home, I returned on Saturday and started digging into the Porsche IVI systems deployment process. At first we deployed just a simple Hello World application proving that we are capable of publishing a custom application on the real hardware setup.

<img src="/blog/hackathon-stuttgart/testbench.jpeg" width="720" alt="Test bench" />

Next up was getting familiar with the Porsche APIs. Once we knew the options we were able to plan further what features we wanted our application to have.
The features were planned in two parts. Basic functionality we wanted to implement was flight lookup. Ability to quickly and easily search for a departure flight. The second part was planned around the data we already had at hand and the desire to use Porsche Navigation system.

1. Flight lookup
2. Navigate to parking space

The technical problem we faced was very surprising. The airport API did not have an endpoint where you could send a flight number and retrieve flight data. WTF? We imagined this would be the most obvious use case for such a application programming interface. The flight ID used by the API endpoints was actually a database primary key which (amsId). This was unusable to us as the person holding a flight ticket has no idea of such ID. In human terms flight ID is the sequence of characters starting with an airline identifier such as AF (Air France) or LH (Lufthansa) followed by some numbers. (For example, LH1234)
At the sponsor booth, we managed to find a person who was working at the airport IT team. He confirmed this was the case and suggested they implement such endpoint first thing on Monday. Unfortunately, that was too late for us so we decided to look for a workaround.
After a while I found out there was another endpoint that required passing in two dates (from & to) and returned a list of flights. Each flight in that list had the actual flight ID that we could use for our use case. We thought that the user of our application was a person already sitting in the car on his way to the airport and therefore we needed to query only flights that would departure in the next few hours. We trigger the query when the application launches and store the results in a JSON file. This file is the queried by the search input given by the user. 


<img src="/blog/hackathon-stuttgart/frontpage.jpeg" width="720" alt="Frontpage" />

<img src="/blog/hackathon-stuttgart/flightsearch.jpeg" width="720" alt="Flight search" />

Typing in AF we filter all Air France flights form the file that has time scoped results so the operation is fast and UI changes are instant creating a very responsive user experience. Next to the search field we show a list of the filtered results and clicking one of the flights takes user to a flight details view.


<img src="/blog/hackathon-stuttgart/flightdetails.jpeg" width="720" alt="Flight details" />

The two main features seemed otherwise quite straight forward but there was a missing piece that our guys implemented surprisingly well.
The Airport API provided flight data including departure terminal e.g. T1. The API did not provide information about the closest parking house e.g. P3.
We needed to somehow calculate for each terminal the closest park house with AVAILABLE parking spots. Unfortunately, the API does not provide information about availability of the parking spaces. The airport did however provide an Excel spreadsheet with historical data as a mock example of each parking house and it´s availability count. We linked this data to our solution so that unavailable parking houses did not get recommended but he system. We stored latitude and longitude of each parking house in the system and this allowed calculating distance from P3 to T1 and estimating walking time.

Having the terminal and parking problem solved we moved on to creating something useful for getting there. The driver would of course be interested to have navigation assistance to the correct parking house to avoid unnecessary time loss finding a parking space.
We already knew what interface to call and how. Now it was just a matter of passing the parking space coordinates to Porsche navigation to get the route displayed on a map.


<img src="/blog/hackathon-stuttgart/taycan.jpeg" width="720" alt="Porsche Taycan" />

The Airport API is public but using the Porsche API and tooling required our team to sign an NDA so disclosing details about the implementation is unfortunately not possible. 

The last challenge was to come up with a good storyline and a presentation that would explain what we achieved during the weekend. This was intimidating not only because of the audience. The judges might ask whatever questions so this tested also our social capability as a team.

It was truly a joy getting hands on experience with Porsche IVI and making some great connections. This is a perfect example of rapid development enabled by modern tooling and talented, highly motivated people.


<img src="/blog/hackathon-stuttgart/testing.jpeg" width="700" alt="Testing" />


[hackathon-stuttgart]:   https://www.hackathon-stuttgart.de/
[cobi-bike]:    https://cobi.bike    

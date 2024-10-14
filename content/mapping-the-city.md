Title: Mapping the City
Date: 2009-09-22 04:47
Author: lindsayrgwatt
Category: History, NYC, Technology
Tags: gis, google earth, maps, nypl, open street maps
Slug: mapping-the-city
Status: published

I went to the [Conflux Festival](http://confluxfestival.org/2009/) on Saturday morning and attended a talk by [Matt Knutzen](http://www.nypl.org/blogs/matt-knutzen) entitled [*Rebuilding the Historical City*](http://confluxfestival.org/2009/events/workshops/matt-knutzen/).  Matt's a cartographer working at the [NYPL](http://www.nypl.org) and he was explaining a new tool they've built - and the Very Big Idea behind the tool.

The NYPL has over 60,000 maps of NYC in their [Digital Gallery](http://digitalgallery.nypl.org/nypldigital/index.cfm), but they're simply digitized images.  They lack any actual mapping points: latlongs, etc. that can actually be use to project the map onto other maps.  As a result, they've decided to build a tool - the [Map Rectifier](http://dev.maps.nypl.org/warper) - that allows anyone to convert an image of a historical map into an actual working map and share the results with the world.

The process is simple: you find an old map you want to convert into a working map.  You put it side by side with an [OpenStreetMap](http://www.openstreetmap.org/) map of New York.  You then click on a point in the old map and click on a corresponding point in OpenStreetMap.  Once you've done at least four points, you click "rectify" and the system warps the image of the old map to fit it onto the real map.  At this point, the old map is converted into a set of latitude and longitudes and can be used elsewhere (the system is also smart enough to tell you if you did a bad job).  I'd show you screen shots, but I can't get a login to the system; it's still in invite only mode :(

There's some other cool functionality in the tool: it's got the ability to crop maps (so you can skip parts of the map) and you can also trace out buildings and add data about them (e.g., it's a public house, etc.).

This gets better and better because once you've converted the map into a set of KML coordinates and you can view it in Google Earth.  For example, here's a projection of a [1924 aerial set](http://dev.maps.nypl.org/warper/mapscans/9338) of photos vs. what's there today (a lot more farmland back then):

[<img src="{static}/images/2009/09/screen-shot-2009-09-22-at-73735-am-300x165.png" title="Long Island Aerial Images" class="alignleft size-medium " width="300" height="165" alt="Long Island Aerial Images" />]({static}/images/2009/09/screen-shot-2009-09-22-at-73735-am.png)

Here's another example, from the [20th Ward's fire insurance map](http://dev.maps.nypl.org/warper/mapscans/11733).  You can see what Madison Square looked like before the Garden and the Farley post office were built:

[<img src="{static}/images/2009/09/screen-shot-2009-09-22-at-74143-am-300x250.png" title="Madison Square with old fire insurance map projected on top" class="alignleft size-medium " width="300" height="250" alt="Madison Square with old fire insurance map projected on top" />]({static}/images/2009/09/screen-shot-2009-09-22-at-74143-am.png)

This technology is impressive as you can start to tell and visualize the history of the city.  Moreover, once the system launches, it's going to be open to the public and *anyone* can rectify a map (that's a sea change in how libraries work).  Also, kudos to the NYPL for making the entire system open source: you'll be able to install the software on your own server and start rectifying your own maps.

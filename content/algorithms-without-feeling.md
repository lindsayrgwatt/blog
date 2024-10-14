Title: Algorithms Without Feeling
Date: 2013-02-04 22:32
Author: lindsayrgwatt
Category: Technology
Tags: algorithms, google
Slug: algorithms-without-feeling
Status: published

I was playing around with the [Google Maps API's Autocomplete](https://developers.google.com/maps/documentation/javascript/reference#Autocomplete) today. This is the feature that lets you type something like "Vancouver" and turn it into the corresponding city. As you type each letter, it guesses what place you're looking for.

Google, being Google, has put a remarkable amount of intelligence into making this work.

For example, you can specify whether you want all types of places or just businesses or just city-like entities, etc.

The set of guesses is also dynamic. Google is famous for using data from one arm of the business to train other parts of the business. For instance, [while taking Street View photos they're also training driverless cars](http://www.holovaty.com/writing/streetview/). And it looks like they use the frequency with which people search for location names to best determine which places you might be looking for.

How do I know this? Well, here's the autocomplete result from this afternoon when I restricted it just businesses.

Type in the letter "s" and, awkwardly, the first result is Sandy Hook Elementary School - the site of last year's horrific school shooting.

[<img src="{static}/images/2013/02/Screen-Shot-2013-02-04-at-4.05.14-PM.png" class="aligncenter size-full " width="516" height="168" alt="Autocomplete Example" />]({static}/images/2013/02/Screen-Shot-2013-02-04-at-4.05.14-PM.png)

Google's unfeeling algorithm has no idea that Sandy Hook is infamous and almost certainly not the place people are looking for so it's going to keep serving it up.

Here's a [Google Trend report on the term "Sandy Hook Elementary School"](http://www.google.com/trends/explore#q=sandy%20hook%20elementary%20school&date=1%2F2012%2013m&cmpt=q). You can see the spike and decay in "interest". Apparently it hasn't decayed enough to have been removed from the autocomplete:

[<img src="{static}/images/2013/02/Screen-Shot-2013-02-04-at-9.23.36-PM-500x196.png" class="aligncenter size-medium " width="500" height="196" alt="Google Trends" />]({static}/images/2013/02/Screen-Shot-2013-02-04-at-9.23.36-PM.png)

 

There's nothing nefarious about Google's algorithm (and dealing with Black Swan events that skew your search data is tough) but they make us aware of the odd new world we live in.

Unemotional algorithms dictate what is topical; this shows up in unexpected locations and we can literally watch and measure the rate at which moments slip into our collective memory.

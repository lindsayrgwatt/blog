Title: Analyzing Violence in South Seattle
Date: 2017-07-16 21:50
Author: lindsayrgwatt
Category: Seattle
Tags: crime, gis, Open Data
Slug: analyzing-violence-in-south-seattle
Status: published

The corner of [37th & Oregon](https://www.google.com/maps/@47.5627698,-122.2861411,19z) is about a 15 minute walk from my house in Columbia City. Last week it was a candidate for the ignominious title of most dangerous place in America. On [July 9th](http://spdblotter.seattle.gov/2017/07/10/homicide-investigation-in-south-seattle-2/), a person was fatally shot there:

[<img src="{static}/images/2017/07/one_shrine-1024x648.jpg" class="aligncenter size-large " width="660" height="418" />]({static}/images/2017/07/one_shrine.jpg)5 days later on [July 14th](http://spdblotter.seattle.gov/2017/07/14/fatal-shooting-near-rainier-playfield-detectives-investigating/), a second person was fatally shot visiting the above shrine for the first victim. Now there are two shrines less than a block apart (and two police cars parked 24x7):

[<img src="{static}/images/2017/07/both_shrines-1024x768.jpg" class="aligncenter size-large " width="660" height="495" />]({static}/images/2017/07/both_shrines.jpg)

This is awful. No one wants people dying on any of Seattle's streets and, in our neighborhood, there's a perception that we're sliding backwards in terms of safety. I wanted to dig into the data and see if there is anything to back up the perception that the neighborhood feels substantially more dangerous than before.

The City of Seattle maintains an [Open Data portal](https://data.seattle.gov/) and I've used it to get both crime data (in the form of [police 911 calls](https://data.seattle.gov/Public-Safety/Seattle-Police-Department-911-Incident-Response/3k2p-39jp/data)) and [neighborhood boundaries](https://data.seattle.gov/dataset/Neighborhoods/2mbt-aqqx).

The data contains all reports of "shots fired" and I wanted to see if it's up for 2017 in my neighborhood, Columbia City. We're likely going to be ahead in July (data only for 1/2 the month) but YTD the numbers are not materially different:

[<img src="{static}/images/2017/07/shots_fired.png" class="aligncenter size-full " width="600" height="371" />]({static}/images/2017/07/shots_fired.png)

Homicides, however, are up. July's two murders are that spike below:

[<img src="{static}/images/2017/07/homicides.png" class="aligncenter size-full " width="688" height="425" />]({static}/images/2017/07/homicides.png)

We had no murders in 2016. Moreover, 2017's homicides are different than the one we had in 2015. That one was a [shooting within a family](http://spdblotter.seattle.gov/2015/12/06/man-sought-for-fatal-shooting-of-woman-in-columbia-city/). According to the police, the two this year are gang-related.

Moreover, drive-by shootings in Columbia City are way up - 11 YTD vs. 3 in 2016:[<img src="{static}/images/2017/07/drive_by_shootings.png" class="aligncenter size-full " width="600" height="371" />]({static}/images/2017/07/drive_by_shootings.png)

Equally concerning is that these shootings are more brazen in timing. These shootings are increasingly occurring during the day (and consequently increasing the likelihood of innocent bystanders getting hit).

[<img src="{static}/images/2017/07/time_of_day.png" class="aligncenter size-full " width="600" height="371" />]({static}/images/2017/07/time_of_day.png)

For folks in Columbia City, the location of these shootings is also increasingly concerning. The map below shows 2017 YTD drive-by shootings in South Seattle (drive-by shootings in Seattle are [exclusively a Central District/South Seattle phenomenon]({static}/images/2017/07/2017_july_ytd_drive_by_shooting_map.png)). The three dots below the words "Columbia City" represent three shootings on suburban streets near Columbia City's main pedestrian thoroughfare:

[<img src="{static}/images/2017/07/south_seattle_2017_drive_by_shootings-832x1024.png" class="aligncenter size-large " width="660" height="812" />]({static}/images/2017/07/south_seattle_2017_drive_by_shootings.png)

These are the first shootings in the Angeline to Dawson corridor. There were none there in 2016:

[<img src="{static}/images/2017/07/south_seattle_2016_drive_by_shootings-832x1024.png" class="aligncenter size-large " width="660" height="812" />]({static}/images/2017/07/south_seattle_2016_drive_by_shootings.png)

Or 2015:

[<img src="{static}/images/2017/07/south_seattle_2015_drive_by_shootings-822x1024.png" class="aligncenter size-large " width="660" height="822" />]({static}/images/2017/07/south_seattle_2015_drive_by_shootings.png)

The goal for South Seattle is zero gang-related shootings in any of our neighborhoods. The data above suggests that gangs are getting more brazen in both the frequency, location and hours of their attacks. I look forward to seeing what the SPD is going to do to combat it and need to figure out what I can do to help make all of South Seattle safe.

**Update: **created a [repo](https://github.com/lindsayrgwatt/analyzing_south_seattle_violence) with some of the raw data plus how to do your own analysis.

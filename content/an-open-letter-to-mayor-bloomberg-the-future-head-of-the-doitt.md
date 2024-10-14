Title: An Open Letter to Mayor Bloomberg & the Future Head of the DOITT
Date: 2010-01-04 21:47
Author: lindsayrgwatt
Category: NYC, Technology
Tags: Gov2.0, NYC Big Apps, NYC Data Mine, Open Data
Slug: an-open-letter-to-mayor-bloomberg-the-future-head-of-the-doitt
Status: published

I was part of a team that recently submitted an [app](http://www.uncoveryourcity.com/) for the [NYC BigApps](http://www.nycbigapps.com/) contest and therefore had the opportunity to play with a lot of the data sets in the [NYC Data Mine](http://www.nyc.gov/html/datamine/html/home/home.shtml).  In the spirit of continuous improvement, I wanted to suggest how the city can take a great resource and make it even better.

After combining nine data sets (and being unable to combine many others), we feel that we can talk to some of the challenges in working with the data and the overall opportunity to improve it.  Our main suggestion is that the City should think of itself as a platform that provides standardized data and end users like ourselves add value by bringing together the different data sets and 3rd party services.  We can't claim to have created the "[government as a platform](http://www.slideshare.net/timoreilly/government-as-platform)" idea, but we can tell you some of the issues New York City faces if this is the path you (hopefully) take.

With that, here are a few suggestions:

1.  Make all your data machine readable.  Some of your data is incredibly rich, but buried in formats that are hard to parse.  The best example is probably the [community district demographic info](http://www.nyc.gov/html/datamine/html/data/terms.html?dataSetJs=raw.js&theIndex=8): there are over 100 spreadsheet pages of rich data there, but it's incredibly difficult to use in CSV form.  Ideally, this would all simply be XML and it could be reused in seconds.
2.  Open source formats please.  Some of your data is locked in proprietary formats, accessible only to users with multi-thousand dollar software packages (a great example are the gdb files for ArcView shape data).  If you want random citizens like us to mash up your data, please provide the data in exclusively open source formats as our software budget is $0.  (It looks like this is changing - I noticed that some of the gdb files at the Data Mine now include shape files as well.  Kudos)
3.  Add lat/longs (the commercial standard for mapping services) to every address/point.  Some of your address data consists just of addresses without lat/longs.  Some of these (e.g., certain school locations) are improperly formatted, so we can't use commercial systems like the [Yahoo Geocoding API](http://developer.yahoo.com/maps/rest/V1/geocode.html) to calculate lat/longs and put them on a map or assign them to a district/neighborhood.  Other files contain lat/longs but they're in a different coordinate system: this means that developers need to convert them into lat/longs in order to map them - and this process introduces errors and takes unnecessary time.
4.  More documentation.  Some of your files contain lots of data but lack the documentation necessary to make them usable.  The best example are the health info shape files: they're full of statistical data for different areas, but there's no way to figure out exactly what each of the statistical values means.  Similarly, the shape files for each community district contains their area - but there's no unit of measurement (it's something called 'internal units squared').
5.  More data.  You gave us some great data to play with, but there's still a ton more.  What about Compstat for crime data?  School scores and their trends over time?  The location of different alarm boxes so we can see how response times vary by area?

These suggestions are meant entirely as an opportunity to build off of a great start.  We - the people of New York - want to work with the city to help make it a better place.  However, the value we add is in creating tools and finding hidden relationships in the data - not in standardizing it; that's where you can make the system work.

If you provide us with well-formed, machine-readable, standardized data, we'll help build the services that citizens need and free up the city's resources to focus where they're needed most.  We'll also find new relationships in the data that might help you rethink policy initiatives (see how your data suggests an [interesting link between 'education' and 'going green'](http://lindsayrgwatt.com/blog/2009/12/uncovering-uncoveryourcity-com/); I've no idea if you knew this).

2009 was a great start for a more open NYC.gov.  Can't wait to see what you do in 2010.

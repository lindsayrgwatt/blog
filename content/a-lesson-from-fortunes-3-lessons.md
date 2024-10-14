Title: A Lesson from Fortune's 3 Lessons
Date: 2015-08-30 21:25
Author: lindsayrgwatt
Category: Business
Slug: a-lesson-from-fortunes-3-lessons
Status: published

I follow [Tim O'Reilly on Twitter](https://twitter.com/timoreilly) and, both as an [Amazon employee](https://www.linkedin.com/in/lindsayrgwatt) \[1\] and someone who values his insight, I was intrigued when he tweeted this the other day:

https://twitter.com/timoreilly/status/637327865374085120

The link is to [an article](http://fortune.com/2015/08/18/amazon-new-york-times/) by [Jeffrey Pfeffer](http://jeffreypfeffer.com/), a Stanford GSB prof and Fortune columnist, about what we should learn from the recent [NY Times' article on Amazon](http://www.nytimes.com/2015/08/16/technology/inside-amazon-wrestling-big-ideas-in-a-bruising-workplace.html). I highly recommend you read it before continuing here.

Pfeffer offers us three lessons we can take from the experience:

1.  The leaders we admire aren't always that admirable
2.  Economic performance and costs trump employee well-being
3.  People participate in and rationalize their own subjugation

I'm not going to comment right now on whether the lessons are correct (I think that largely depends on whether your liked the NY Times article or thought it was a hatchet job), rather I want to explore the first lesson.

In his article, Pfeffer states the following:

> Simply put, dimensions of leader and company performance are poorly correlated. For instance, *Fortune*’s list of most admired companies, which reflects the size, financial performance, and stock appreciation of the enterprises, has only four entries in common with its [100 Best Companies to Work For](http://fortune.com/best-companies/) list. And only one of *Fortune’s *most admired companies also appears on the 2014 Hay Group’s [Best Companies for Leadership](http://www.haygroup.com/bestcompaniesforleadership/) list. (Hay also works with *Fortune* to create the Most Admired Companies list.)

If true, this is a huge story! The thought that you have the most admired companies in the world (presumably 100, right?) and the 100 best American-based companies to work for and only **4 (!) **overlap? 4 percent overlap would be terrible and this would be an incredible story: we've built a society where we say one thing and do another.

Unfortunately, Pfeffer doesn't state who these four unicorns happen to be. I desperately wanted to know, so I decided to find out myself. And this is where the story starts to unravel.

First, while Fortune lists the [100 best companies to work for](http://fortune.com/best-companies/), they only publicly share the [50 most admired](http://fortune.com/worlds-most-admired-companies/). I tried scraping their site to get the top 100, but for technical reasons \[2\], I had to abandon it.

What's interesting is that when you compare the 100 best companies to work for with the 50 most admired, the overlap is actually 7, not 4:

|  |  |  |
|----|----|----|
| Company Name | Rank in 50 Most Admired | Rank in 100 Best to Work for |
| Google | 2 | 1 |
| USAA | 28 | 33 |
| Goldman Sachs Group | 23 | 50 |
| American Express | 8 | 51 |
| Marriott International | 37 | 53 |
| Whole Foods Market | 18 | 55 |
| Nordstrom | 14 | 93 |
| Accenture | 49 | 98 |

Similarly, the Hay Group's Best Companies for Leadership overlap is also wrong. Their [website](http://www.haygroup.com/bestcompaniesforleadership/) only lists the Top 20 companies; I assume you have to pay for the rest:

<img src="http://www.haygroup.com/bcl/images/top-20-2014.gif" class="alignnone" width="590" height="458" />

Of these, Procter & Gamble is \#17 on the Most Admired List, General Electric is \#9, Coca-Cola is \#10, IBM is \#25, Unilever is \#36, Intel is \#40, McDonald's is \#46, 3M is \#21, Pepsico is \#41, Toyota is \#24, Accenture is \#49 and Johnson & Johnson is \#11,.

This dramatically changes the story. Pfeffer's sentences above could be rewritten as:

> Simply put, dimensions of leader and company performance are correlated. For instance, *Fortune*’s list of the 50 most admired companies, which reflects the size, financial performance, and stock appreciation of the enterprises, has seven entries in common with its [100 Best Companies to Work For](http://fortune.com/best-companies/) list. And 12 of *Fortune’s *most admired companies also appear on the 2014 Hay Group’s [Best Companies for Leadership](http://www.haygroup.com/bestcompaniesforleadership/) list. (Hay also works with *Fortune* to create the Most Admired Companies list.)

7 of 50 is 14% - which is much more ambiguous than the implied "only 4 percent overlap" in the original paragraph. Suddenly it looks like CEOs may be creating companies that are both worker-friendly and admirable. The story is much less clear. (And I bet the overlap is more than 14% if you compared the full 100 Most Admired with the full 100 Best to Work for; I doubt it's a linear relationship).

It's similar for the Hay numbers: a full 60% of the Top 20 Best Companies for Leadership are also in the Top 50 Most Admired.

These errors make it less clear that Lesson \#2 is correct. If economic performance and cost trumps employee well-being, then why are 14% of the most admired companies also wasting money to be known as one of the Top 100 places to work?

All in all, I'm disappointed by the fact-checking here. There is a very important conversation going on around what "work" and "employment" will mean in the 21st century. This article had an opportunity to contribute but the factual inaccuracies make it difficult to separate the real insights from speculative narrative.

Note: feel free to double-check my work. I created a [Github repo](https://github.com/lindsayrgwatt/fortune) with the data and Python script I used to Fortune's rankings.

\[1\] I didn't seek anyone at Amazon's opinion before publishing this and all the opinions on my blog are entirely my own. I am not authorized to speak on Amazon's behalf; you shouldn't interpret anything on this blog or my Twitter feed as being Amazon-approved. I also have no vested interest in whether you like or hate Amazon; it's a free country and you are entitled to your own opinion.

\[2\] There are 350 companies in the "Most Admired" companies section. Each has a URL and I tried scraping the URL for each to get each company's individual score. However, the pages render dynamically using JavaScript; I'm doing this in my spare time and ran out of time to figure out how to get the pages to properly render. This has no impact on the analysis discussed above.

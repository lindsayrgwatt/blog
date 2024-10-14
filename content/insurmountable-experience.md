Title: Insurmountable Experience
Date: 2009-02-18 14:57
Author: lindsayrgwatt
Category: Business
Tags: google, Kaizen, Toyota
Slug: insurmountable-experience
Status: published

I started my career as a management consultant and one of the concepts that was drilled into our heads was the "[experience curve](http://en.wikipedia.org/wiki/Experience_curve_effects)".  It's the notion that organizations learn over time and this enables them to produce goods at a lower cost per unit - and therefore makes it harder for competitors to underprice them to steal market share.

The other thing notion that was drilled into our heads was the notion of "[kaizen](http://en.wikipedia.org/wiki/Kaizen)" - best exemplified by how Toyota makes continuous small changes to its production lines and therefore is constantly lowering its costs (and subsequently becoming the best auto manufacturer in the world).

I couldn't help but think of these two concepts today when I read about [how Google performs searches](http://glinden.blogspot.com/2009/02/jeff-dean-keynote-at-wsdm-2009.html) on [Greg Linden's blog](http://glinden.blogspot.com).  The following is total geek-speak, but has stunning ramifications:

> The attention to detail at Google is remarkable. Jeff gleefully described the various index compression techniques they created and used over the years. He talked about how they finally settling on a format that grouped four delta of positions together in order to minimize the number of shift operations needed during decompression. Jeff said they paid attention to where their data was laid out on disk, keeping the data they needed to stream over quickly always on the faster outer edge of the disk, leaving the inside for cold data or short reads. They wrote their own recovery for errors with non-parity memory. They wrote their own disk scheduler. They repeatedly modified the Linux kernel to meet their needs. They designed their own servers with no cases, then switched to more standard off-the-rack servers, and now are back to custom servers with no cases again.  
> Google's agility is impressive. Jeff said they rolled out seven major rearchitecture efforts in ten years. These changes often would involve completely different index formats or totally new storage systems such as GFS and BigTable. In all of these rollouts, Google always could and sometimes did immediately rollback if something went wrong. In some of these rollouts, they went as far as to have a new datacenter running the new code, an old datacenter running the old, and switch traffic between datacenters. Day to day, searchers constantly were experiencing much smaller changes in experiments and testing of new code. Google does all of this quickly and quietly, without searchers noticing anything has changed. 

What this means is Google has and is doing everything they can to wrench the tiniest performance and accuracy gains out of their search.  Nothing is too small to change.  Toyota's famous for rejigging it's production lines to save 5 seconds on a procedure (do this a few hundred times and suddenly your productivity goes way up).  When Google engineers make sure that files are stored closer to one another on disk so that they can be accessed faster, they're doing the same thing, but with bits instead of rivets.

What's truly phenomenal is that they're able to maintain this culture despite having a 60+% in search.  Toyota is battling GM for the title of world's biggest automaker, but it's still a hugely fragmented industry and there's no global winner.  Search, on the other hand, is consolidated amongst Google/Yahoo/Microsoft in most countries.

Title: Plants. Without the Effort
Date: 2021-02-28 21:16
Author: lindsayrgwatt
Category: Technology
Tags: arduino, make, plants
Slug: plants-without-the-effort
Status: published



Ilove gardening but I hate having to constantly water plants. For years, I've longed for vegetables that would just water themselves.





As a technologist, I've often thought "this should be easy; just wire up a microcontroller, a pump and some sensors and make a self-watering plant system."





As a technologist, I also know that it is never as easy as I think it is.





On and off for the past few years I've played around at this. Years ago I bought an [Ecoduino kit](https://www.dfrobot.com/product-641.html) to see if it worked. It did but then one day it just crashed viciously and wouldn't restart. Plus, I wanted a bigger system (multiple plants vs. one) so I figured I'd roll my own.





I started making a [self-water plant system using Micropython](https://github.com/lindsayrgwatt/self_watering_plants) but I didn't get it finished - and then we had to move for a while as our house got renovated and the [Seeed Wio Terminal](https://www.seeedstudio.com/Wio-Terminal-p-4509.html) came out. I immediately coveted one (more on that later) and decided to redo the self-watering plant system using that.





I finally got it done. Some pictures and thoughts below; the [code](https://github.com/lindsayrgwatt/self-water-planter/) is open-source if you want more.





Before I go any further though, let me be clear about this. There are lots of commercial self-watering systems out there that work better than mine and are a lot cheaper (both in time and money). For me, this is a labor of love; I dig the tech and like to make things. The journey is the destination in building this.





<figure class=" size-large is-style-twentytwentyone-border">
<img src="{static}/images/2021/02/IMG_5169-1024x768.jpeg" class="" /><br />

<figcaption><em>Baby plants. Baby boy is not quite that baby anymore</em></figcaption>
</figure>





<figure class=" size-large is-style-twentytwentyone-border">
<img src="{static}/images/2021/02/IMG_5168-1024x768.jpeg" class="" /><br />

<figcaption><em>Beautiful it is not. But damn it, it works!</em></figcaption>
</figure>





<figure class=" size-large is-style-twentytwentyone-border">
<img src="{static}/images/2021/02/IMG_5170-1024x768.jpeg" class="" /><br />

<figcaption><em>Come over for dinner in about 80 days...</em></figcaption>
</figure>





**1. The Wio Terminal**





In the top photo above, you can see the Wio Terminal. This thing is an incredible dev board; it dramatically simplified everything vs. when I tried to create the same system on an original Micropython board.





The combination of built-in display, at least 8 inputs (3 buttons on top, 4-way joystick + button on joystick) and two ports that are compatible with the [Grove ecosystem](https://www.seeedstudio.com/category/Grove-c-1003.html) (Seeed's proprietary sensor hardware) dramatically speeds up your design time. I used only the built-in input and didn't have to worry about wiring up any buttons. I used the Grove port to connect to a [preconfigured relay](https://www.seeedstudio.com/Grove-Relay.html) that handled current, resistance, etc. for me. No worry about current, etc. It's literally plug & play.





Then add in the screen. No need to worry about writing up output; just follow the [YouTube tutorials](https://www.youtube.com/playlist?list=PLpH_4mf13-A0MzOdPNITVfoVBMvf7Rg9g) and you're off.





This is a really fun way to make; the feedback between making a change in your design and seeing the impact on the system is really quick because you don't need to wire up much in order to make it work. I see myself buying many more of these in the future.





**2. Making in 2021**





There's an old William Gibson quote:





> The future is already here - it's just not very evenly distributed.
>
> <cite>[Source](https://quoteinvestigator.com/2012/01/24/future-has-arrived/)</cite>

<!-- /wp:quote -->



Working on this project at times felt like that. The Wio Terminal feels a bit like an artifact from the future. It simplified making things so much vs. every other dev board I've used before (I'm a rank amateur; maybe it wouldn't be so impressive if I had more time for this stuff-but then again, I love that it lets me do this in my spare time and get to a working prototype instead of slogging through failed connections).





Add to this 3D printing: I needed brackets to mount the Wio Terminal and the water level sensor. I used [TinkerCad](https://www.tinkercad.com) on an iPad to design the brackets ([Terminal](https://www.tinkercad.com/things/l3VZhdOsj5c), [water level sensor](https://www.tinkercad.com/things/hj5l6Puo6tH)). I then AirDropped it to my laptop and minutes later they were being printed on a [Czech 3D printer](https://www.prusa3d.com). It feels insane that I can do CAD on an iPad and will into existence physical objects that have never existed before.





Now lets bring in that Shenzen ecosystem again. I realized partway through the project that a water level sensor would be a great simplifier (vs. using a water flow monitor); Seeed not only had one compatible with the Terminal, but it was at my house within 2-5 business days after flying across the world. I only have time to make things on weekends so Shenzhen is now the equivalent of driving to my local Fry's ([RIP](https://www.cnn.com/2021/02/24/business/frys-electronics-closure/index.html) - although it had been failing for years up here in Seattle).





Being at the intersection of these technologies, supply chains and ecosystems made me feel like I was on the vanguard of something new. You don't have to squint too hard to see a future where it will be a lot easier to prototype anything you want.





I was reminder of another quote:





> You can see the computer age everywhere but in the productivity statistics.
>
> <cite>[Robert Solow](https://en.wikipedia.org/wiki/Productivity_paradox) trolling before we knew what trolling was</cite>

<!-- /wp:quote -->



We're at the exact opposite now. The experience I had building this was literally watching time and space horizons shrink in front of me. I can now do in days what used to take months if it was even possible. I now truly get why so many people have been Messianic when describing the potential of the "Maker Movement."





*Update 4/4 - I added a new .stl file to the repo that replaces the block of wood holding the motor with a plastic bracket:*





<figure class=" size-large is-style-twentytwentyone-image-frame">
<img src="{static}/images/2021/04/IMG_5234-1024x768.jpeg" class="" /><br />

<figcaption>v2. Looks better visually. And check out that plant growth in the back!</figcaption>
</figure>



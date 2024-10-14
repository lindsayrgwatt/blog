Title: Art at Home
Date: 2021-07-24 22:57
Author: lindsayrgwatt
Category: Technology
Tags: Art, make, python
Slug: art-at-home
Status: published



For me, one of the paradoxes of the digital age has been that the more ubiquitous things are, the less I feel like I engage in them. If feels like there's just so much and I have so little time and attention.





One example of this are my photos. As I write this, I have 32,401 photos and 1,377 videos in my library. I am proud of these photos: I've ruthlessly pruned these to tell the story of my life since ~2000. Yet until recently these photos were languishing in my library. At least now my phone shows me "Featured Photos" and is trying to reconnect me with everything I've done and collected. It's not yet great, but it's a start and I appreciate the efforts (and expect we will only see more in the future).





Art feels the same way to me. You can take a tour of the best art every created by humanity via your web browser. I mean, the [Met](https://www.metmuseum.org/art/collection), the [Louvre](https://collections.louvre.fr/en/) - pretty much any gallery you can imagine - are now putting their entire catalogue online.





The greatest artistic achievements of history are available a click away...and yet, it is unsatisfying.





Why?





Well, here are a few reasons:





1.  The art is online, but not in a format that in any way competes with a gallery. Rather than immersing yourself in front of the artwork, you're staring at a thumbnail.
2.  You need to know what you're looking for. Art galleries have limited space but are optimized for discovery; the joy of the experience is wandering from room to room waiting to see what you'll find. The Internet is the opposite: infinite shelf space but you've got to know exactly where to look (which implies you need to know in advance what you want - the exact opposite of "art").





Is there a better way?





With the pandemic, I've found myself unable to visit art galleries, spending a lot more time at home and missing art. Around the same time as this, I got my hands on an [Adafruit PyPortal](https://www.adafruit.com/product/4116).





The PyPortal is a small display with big pixels (it's resolution is 240x320 px - about 1/35th my phone - with a comparable screen size) connected to a microcontroller and an SD card. I started wondering if I could use this to get "art" back into my life.





Here's the system that I wanted:





1.  I want "art" to appear next to where I'm working
2.  I don't want this art to command my attention. I want it to passively appear, persist and then fade away. I will give it my attention if I want to but I don't want it to steal my attention
3.  I want things that might be interesting to me to randomly appear
4.  I want to embrace the low fidelity of the PyPortal. I'll show high contrast, simple images; for complex images I'll zoom in to the details





After mucking around for a while (PyPortal doesn't have a lot of memory so I had to learn how to load images without crashing it), I came up with a system I call [MiniPics](https://github.com/lindsayrgwatt/mini_pics).





I downloaded images from around the web - [medieval Belgian woodblock prints](https://collectie.antwerpen.be/impressedbyplantin/all-woodcuts), [Japanese woodblock prints](https://ukiyo-e.org/), [Gustav Dore's drawings of 19th century London](https://www.bl.uk/collection-items/london-illustrations-by-gustave-dor#), [Hogarth's Beer Street/Gin Lane](https://www.tate.org.uk/art/artworks/hogarth-gin-lane-t01799), and more - and cropped them down to a tiny size. After 3D printing a case, they now appear on a device that sits next to my computer:





<figure class=" size-large">
<img src="{static}/images/2021/07/IMG_5707-768x1024.jpeg" class="" /><br />

<figcaption>A close-up from one of Gustav Dore's drawings of 19th century London</figcaption>
</figure>





There are hundreds of images on the device and each is selected randomly. They fade in over the course of a minute, stay up for three and then fade out.





If I'm not busy, I glance over and take a peak, otherwise I stay focused on whatever else I'm doing and don't worry. I know that the images will be back; I'm not missing anything if I don't pay attention right now.





<figure class=" size-large">
<img src="{static}/images/2021/07/IMG_5711-768x1024.jpeg" class="" /><br />

<figcaption>A Japanese woodblock print</figcaption>
</figure>





I have fallen in love with the low fidelity of the device. I think it makes me appreciate the art but also know that I cannot invest a lot of attention in the artwork. If I peer closer, there is nothing more to see; I won't see the brushstrokes or any subtle gradation of color; there are 76,800 pixels here (in only 256 colors!) and nothing else.





For a Japanese woodblock print, appreciate the colors and the choice of imagery. For Dore or Hogarth, zoom in on a scene and marvel at what they imagined. But know that there's no further depth and move on.





<figure class=" has-nested-images columns-default is-cropped">

</p>
<figure class=" size-large">
<img src="{static}/images/2021/07/IMG_5710-768x1024.jpeg" class="" />
</figure>
<p>
<br />

<figcaption>Durer's Hands</figcaption>
</figure>





We'll see how this goes. I've had it up and running for a few weeks and enjoy it as a simple escape from work when I have a free moment. I hope a year from now I'm still loving it as much as today.





\-





Here's a photo of a work in progress version. The first version had the images upside down and also had completely incorrect dimensions on the plastic case. Thank god that CAD software makes it (relatively) easy to change these things and 3D printing is cheap:





<figure class=" has-nested-images columns-default is-cropped">

</p>
<figure class=" size-large">
<img src="{static}/images/2021/07/IMG_5697-768x1024.jpeg" class="" />
</figure>
<p></p>
</figure>





*Update 1/15/23 - New version at Github. You can now touch the screen to toggle it on/off*



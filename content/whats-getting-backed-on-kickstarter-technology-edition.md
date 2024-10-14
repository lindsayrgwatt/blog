Title: What's Getting Backed on Kickstarter: Technology Edition
Date: 2015-03-24 15:54
Author: lindsayrgwatt
Category: Technology
Tags: Analysis, kickstarter, statistics
Slug: whats-getting-backed-on-kickstarter-technology-edition
Status: published

I'm a huge [Kickstarter](https://www.kickstarter.com) fanboy. The creativity that they've unleashed is mind-boggling and embodies exactly what the Internet is capable of.

The [projects I've backed](https://www.kickstarter.com/profile/lindsayrgwatt) tend to skew tech-heavy and I recently wondered if there were any identifiable trends as to what sort of tech projects get backed. I hear all the time about companies that started with a Kickstarter campaign; are there any patterns?

Kickstarter is really open about [what projects get backed](https://www.kickstarter.com/discover/advanced?state=successful&category_id=16&sort=most_funded) (note that it's not clear how accurate the project counts are; they seem to appear/disappear/dramatically change based on when you access the site), so I went out and scraped some data (code [here](https://github.com/lindsayrgwatt/kickstarter)).

I managed to get data on 1700 successful tech projects, which raised a cumulative total of $212,472,913. That's an average of $124,984 per project-but this is no even distribution. The winners (like the [Pono](https://www.kickstarter.com/projects/1003614822/ponomusic-where-your-soul-rediscovers-music?ref=discovery) music player, [Reading Rainbow](https://www.kickstarter.com/projects/readingrainbow/bring-reading-rainbow-back-for-every-child-everywh?ref=discovery) or [Zano](https://www.kickstarter.com/projects/torquing/zano-autonomous-intelligent-swarming-nano-drone?ref=discovery) drone) raise millions while [Kymira](https://www.kickstarter.com/projects/88282627/kymira-sport-reactive-apparel?ref=discovery) smart sports apparel is limping in at $8,000 or so (but still successful; kudos). The median raised is $45,992.

I wrote some code to try and cluster these projects and found a few categories that people like to back:

**Physical Computing: **Arduino clones and shields; Raspberry Pi accessories galore. Examples include [Microview](https://www.kickstarter.com/projects/1516846343/microview-chip-sized-arduino-with-built-in-oled-di), [RFDuino](https://www.kickstarter.com/projects/1608192864/rfduino-iphone-bluetooth-40-arduino-compatible-boa) and the [Touch Board](https://www.kickstarter.com/projects/863853574/touch-board-interactivity-everywhere).

**3D Printers: **Every type you can imagine, including the [Micro](https://www.kickstarter.com/projects/m3d/the-micro-the-first-truly-consumer-3d-printer?ref=discovery), the [Form1](https://www.kickstarter.com/projects/formlabs/form-1-an-affordable-professional-3d-printer?ref=discovery) and the [3Doodler](https://www.kickstarter.com/projects/1351910088/3doodler-the-worlds-first-3d-printing-pen?ref=discovery).

**Home Automation: **Smart plugs, dimmers, remotes - Kickstarters want a connected home. Sample projects are [Ube Wifi dimmer](https://www.kickstarter.com/projects/702772580/ube-wifi-connected-smart-light-dimmer), the [NEEO remote](https://www.kickstarter.com/projects/1227115988/neeo-the-thinking-remote) and  the [Ninja Sphere controller](https://www.kickstarter.com/projects/ninja/ninja-sphere-next-generation-control-of-your-envir).

**Lighting: **Make it glow-whether lights attached to your stereo, fancy bike lights or an enhancement to your GoPro. Examples are the [Notti Smart Light](https://www.kickstarter.com/projects/26398080/notti-a-more-beautiful-smart-light), [Lume Cube](https://www.kickstarter.com/projects/1193685734/lume-cube-flash-and-video-light-for-gopro-iphone-a) flashbulbs or [Playbulb candles](https://www.kickstarter.com/projects/mipowusa/playbulb-candle-color-led-flameless-candle-with-mo).

**Phone Accessories: A**nything that can pimp your phone. Check out the [Jorno foldable keyboard](https://www.kickstarter.com/projects/jorno/jorno-the-pocketable-folding-bluetooth-keyboard), [Thermodo thermometer](https://www.kickstarter.com/projects/robocat/thermodo-the-tiny-thermometer-for-mobile-devices) or [Chipolo item finder](https://www.kickstarter.com/projects/1015015457/chipolo-bluetooth-item-finder-for-iphone-and-andro).

**Solar Powered Gizmos**: Kickstarter backers seem to really want to take their electronics outside. Witness the [WakaWaka Base](https://www.kickstarter.com/projects/wakawaka/wakawaka-base-a-power-and-light-first-aid-kit), [SPOR](https://www.kickstarter.com/projects/spor/spor-solar-battery-chargers-usb-cables-and-accesso) and [Solarpod Pyxis](https://www.kickstarter.com/projects/solarpod/solarpod-pyxis-the-best-portable-usb-charger) chargers/lights.

Here's how many projects fall into each category:

\[wp_charts title="projects_per_category" type="bar" align="aligncenter" width="100%" margin="5px 20px" datasets="329,181,433,246,271,240" labels="Physical Computing,3D Printers,Home Automation,Lighting,Phone Accessories,Solar Powered Gizmos" scaleoverride="true" scalesteps="16" scalestepwidth="25" scalestartvalue="100"\]

That's a high of 433 for Home Automation versus 181 3D printers.

(Hate that there are no numbers in these graphs? I do, but can't figure out how to add labels. All the raw data is [here](https://github.com/lindsayrgwatt/kickstarter/blob/master/kickstarter_technology_projects_v2.ipynb#L701).)

The total funds raised varies dramatically across the categories ($M):

\[wp_charts title="total_funding_per_category" type="bar" align="aligncenter" width="100%" margin="5px 20px" datasets="46.4,41.4,40.4,30.8,31.8,21.5" labels="Physical Computing,3D Printers,Home Automation,Lighting,Phone Accessories,Solar Powered Gizmos" scaleoverride="true" scalesteps="10" scalestepwidth="5" scalestartvalue="0"\]

Surprisingly, Physical Computing has clocked almost $50M ($46.4M), closely followed by 3D Printers at $41.4M. Solar Power is half this at $21.5M.

There's a similar difference in the the amount raised per category-both the average and median ($K):

\[wp_charts title="funding_breakdown_per_category" type="bar" align="aligncenter" width="100%" margin="5px 20px" datasets="141.2,229.0,93.4,125.2,117.6,89.4 next 43.3,79.9,36.9,49.2,55.3,42.3" labels="Physical Computing,3D Printers,Home Automation,Lighting,Phone Accessories,Solar Powered Gizmos" scaleoverride="true" scalesteps="10" scalestepwidth="25" scalestartvalue="0"\]

On a per-project basis, 3D Printers have captured peoples wallets (most likely have a much higher per unit cost than other projects) and clock in with a $229.0K/$79.9K average/median raise. This median is almost as high as the average for solar power projects: $89.4K/$42.3K average/median.

A couple of closing thoughts:

- I was amazed at how much money has gone towards backing Physical Computing. I imagine that most of these devices were bought by geeks to make geeky devices, so I'm guessing that we're only at the starting of a big revolution in Internet-connected devices
- There was no major cluster for robotics or drones. This surprised me as I would have guessed more based on the buzz in the press. Big difference between what is bought vs. what is talked about
- Some of the major success stories (like Pono or Reading Rainbow) don't fall into an of these categories. I don't yet know how to interpret these "one hit wonders" but its interesting to think about why they succeeded as a product but didn't launch a category

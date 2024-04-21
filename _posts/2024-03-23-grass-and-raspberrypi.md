---
layout: post
title: "Grass and RaspberryPi"
date: 2024-03-23 00:00:00 +0000
---
AI summary
> "Grass" is a service that allows users to profit from AI by selling their unused internet through a web extension. The author has been earning Grass rewards by keeping their browser window open, and initially used multiple devices to increase their earnings. However, Grass changed the rules to reward per network, not per device. Attempts to use Cloud VPS for extra points were unsuccessful, as Grass only farms unused residential IPs. The author found a solution by using a Raspberry Pi to ensure Grass is always connected, even when their laptop is off.

"Grass" lets users profit from AI by selling their unused internet through a web extension. This service helps AI firms with tasks like web scraping and training models, while prioritizing user privacy and security. It also features a referral program to boost earnings.

You can learn more about Grass here: https://www.getgrass.io/

## Earning points

I’ve been earning Grass rewards for a while now, since December I believe. The way I collect points:

1. I install the Grass chrome extension
2. I have my browser window open
3. I get rewards

At first, I was able to run a lot of devices for the same Grass account (I used AdsPower to emulate multiple devices) and multiply the points I’d get for my home network. Then they changed the rules in such way that the reward unit is the network. So, multiple devices on the same network doesn’t give you leverage, as for each device you’ll only get rewards R/n per device where n is the number of devices on the network. 

## Earning extra points using Cloud VPS

Firing up a bunch of cloud virtual machines dedicated public IPs should be doable and a pretty easy way to multiply the rewards, right? I tried this approach, setting up the [Grass VPS App](https://github.com/alafon/grass-vps) on a Cloud VPS, but it doesn’t count toward points, because Grass is only interested in farming unused internet of residential IPs. They do a pretty good job at detecting this.

## Problem with using my laptop for earning points

If I turn off my laptop, close the lid, or put it in sleep mode, I don’t earn any Grass points.

## Solution: RaspberryPi

I have a couple of Raspberry Pi 3 laying around doing nothing, so I booted one and installed the [Grass VPS App](https://github.com/alafon/grass-vps) on there. Since doing that on March 17th, my earnings are stable. Even when I’m away from home, travelling, touching grass, the Raspberry Pi makes sure to always have Grass connected.

![Grass Reward Dashboard](/assets/images/grass-reward-dashboard.png)
*Image: Grass Reward Dashboard showing the author's earnings*

## Update 2024-04-14

Using the Grass VPS in Raspberry Pi stopped working after an update issued by Grass. Their support team told me that using the VPS package is not supported anymore. So, I've fallbacked to using Raspberry Pi in desktop mode, with the Grass chrome extension running on Chromium there. I set it up using a VNC connection. This works well, and is stable.

## Update 2024-04-21

My raspberry pi rebooted for some reason and didn't resume with an open Chromium window farming Grass points. So, I added really a simple health check, as suggested by ChatGPT:
1. Sign up for healthchecks.io
2. On raspberry pi
    1. `sudo apt-get install wmctrl`
    2. `nano /home/tumi/check_chromium_and_ping.sh` and add script below
    3. `crontab -e`
    4. `0 * * * * /home/tumi/check_chromium_and_ping.sh`
    5. `crontab -l` to check for crontab config

    ```jsx
    #!/bin/bash

    # Set DISPLAY variable
    export DISPLAY=:0

    # Check for Chromium windows
    if wmctrl -l | grep -i chromium; then
        # Chromium is running, perform the ping
        curl -fsS --retry 3 https://hc-ping.com/<my healthchecks.io key> >/dev/null 2>&1
    else
        echo "No Chromium window is open."
    fi
    ```

3. On healthchecks.io, create a telegram integration
4. Done
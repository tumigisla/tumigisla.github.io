---
layout: post
title: "tgislason.xyz uptime checker"
date: 2024-04-21 00:00:00 +0000
---

## Motive
This is another meta post on the building blocks of this website. It's a simple, statically rendered webpage, hosted on GitHub servers, with only one developer making changes every once in a while. The page shouldn't really go down. But still, I want to know if it happens.

## Stack
For this I'm using a really simple stack: Zapier + healthchecks.io. Both free tools and easy to setup. This whole thing takes literally 5 minutes to make.

## Implementation
1. In healthchecks.io create a new check
    1. Schedule: Period 1 hour, grace time 1 hour
    2. Notification methods: Telegram (or email or whatever you prefer)
3. In Zapier create a two step Zap.
    1. Every Hour in Schedule by Zapier
    2. Run Python Code by Zapier
        ```
          import requests

          def check_website_status(url):
              try:
                  response = requests.get(url)
                  return response.status_code == 200
              except requests.exceptions.RequestException:
                  return False

          my_website = 'https://tgislason.xyz'
          health_check = 'https://hc-ping.com/<your healthchecks.io key>'

          is_up = check_website_status(my_website)
          if is_up:
              check_website_status(health_check)
      ```
4. Done, that's it!

![Zapier automation](/assets/images/zapier-uptime-checker.png)
*Image: Zapier automation*

![healthchecks.io events](/assets/images/healthchecksio-events.png)
*Image: healthchecks.io events*
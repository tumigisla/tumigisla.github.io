---
layout: post
title: "Website builder"
date: 2024-03-17 00:00:00 +0000
---

For this website I considered a couple of options. Let’s go through some of them and list some of the pros and cons and do a comparison and eventually talk about how I came to a conclusion.

TL;DR

> The document provides an analysis of various website building platforms including Notion, Wordpress, Wix, Squarespace, Substack, and GitHub Pages. Each platform is evaluated based on its features, ease of use, and suitability for different purposes. The author ultimately chose GitHub Pages for its simplicity and compatibility with their existing workflow.

## Notion

Notion allows you to publish a page as a website. It’s super easy to do, in only 1 minute you can publish your Notion page with it’s subpages, databases etc. as a website. What I don’t like is you’re unable to use your custom domain. They allow you to choose <*your-own-sub-domain>.notion.site,* but I wanted to use the domain I purchased, *tgislason.xyz.*

It’s possible to jump through some hoops to use a custom domain though, either by paying $10 a month for a SaaS product that does this for you, or by reverse-proxying with something like Cloudflare Workers. IMO that defeats the purpose of the simplicity offered by Notion.

## Wordpress, Wix, Squarespace

No-code bloatware platforms that let you choose from a variety of themes. You can spin up a beautiful webpage in just 5 minutes. I’m not a fan though, because as soon as you want to customize something it’s huge hazzle. Maybe I’m too lazy to learn how to use these platforms properly, but I only briefly considered these options. Also, most of these platforms seem to be targeted toward online shops, which is not what I’m aiming for.

## Substack

This is great for creating newsletters, building a community and monetizing your blog. You reach out to all of your subscribers via email where they can read your newsletter. This would be great for me actually if I had already decided on a topic for my webpage. For now, I mainly want to write to get my thoughts out there, and get into a habit of writing and publishing regularly. It will be on a wide variety of topic, so if it were a newsletter it would be very unstructured and not interesting for people to read. Mabye sometime in the future when I’ve distilled what I want to write about then I can create a newsletter.

## GitHub Pages

Really simple to setup for me since I already live and breathe git. GitHub Pages let’s you with a few clicks in the settings of a repo change your repo into a static webpage. Then you simply create a CNAME record with your domain registrar, pointing toward <*your-github-username>.github.io*.

This is the option I ended up using because it’s the environment I’m most used to. Everything is so simple to set up, although I ended up spending a bit of time styling my page with Jekyll (that’s mainly because I hate CSS, but ChatGPT actually helped a lot there), and this is something I will also refine with time. 

The workflow of updating the page or adding a new blog post is really straight forward and something I am heavily used to: create a pull request and merge it, that’s it. An out of the box GitHub Action takes care of publishing the new content to your webpage in under a minute.

Here is the GitHub repo: [https://github.com/tumigisla/tumigisla.github.io](https://github.com/tumigisla/tumigisla.github.io)

## Conclusion

In conclusion, the choice of GitHub Pages for building my website was primarily guided by familiarity, ease of use, and its seamless integration with my existing workflow.
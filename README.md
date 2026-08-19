# OSINT correlation tool

Before I explain how this works, I just wanna point out a few things.

I did **NOT** try to make "here we go, another OSINT tool"

What I wanted to make was a **correlation system**, where if a username is found on selected sites, in this case Mastodon and Bluesky, we can compare information from those accounts.

It checks the recent posts of the user (if found) on these sites and compares things like the post date, post text, and image (yeah, I know, sites can resize or compress images, thats why it checks the perceptual hash here).

The checks are basically done in this order:

```markdown
1. Date check
2. Text check (if the date similarity is > 0.7)
3. Image check (if the text similarity is > 0.7)
```

The idea is to see whether information from these different platforms has enough similarity to say the accounts could be related.

I dont use these sites that often. Heck, I only found out these sites existed when I was looking for a completely free **public API** for this project.

It only supports around like 4 sites because I didnt intend this to be an OSINT tool that anyone could use for their daily work. I mainly wanted to experiment with the **correlation system**, which I've never seen before in any OSINT tool, and I thought these sites were enough for that.

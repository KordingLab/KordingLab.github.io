# Kording lab (Bayesian Behavior Lab) page


To run locally, follow instruction [here](https://jekyllrb.com/) to install Jekyll then run `jekyll serve` to see in `localhost:4000`.

We are welcome for other people to contribute to our site not just lab member. Feel free to fork and pull-request!


### How to add posts

It's very easy to add post. All the posts are located in `_posts` folder. It arrangement is based on
date. For posts that we port from Kording lab original website, we put random date right now.
Each post can be written in markdown format. On top of each post, you just have to state 3 main things, `title`, `description` and `categories`. `description` will be shown when you share on social media like Facebook or twitter. See the following

```
---
title: Summer School in Computational Sensory-Motor Neuroscience (CoSMo)
description: all links to CoSMo summer school in computational neuroscience materials
categories: scientists
---
```

we have only 4 categories: `scientists`, `students`, `discussion`, `blog` you can choose.


### Way to add posts

**Directly add on Github**, you can simply go to `_posts` and click `New file` then put some markdown file e.g. `2016-02-03-post-name.md` and start writing blog post. Github also allows you to preview it so it's nice for people who don't want to clone the repo. **note** that you should commit or add description when you add more post!

**Clone the repo**, kind of the same as directly add post on Github. You just have to clone the repository. Then add more file, commit and push to the repo.

It will take half a minute and you can see the new posts or changes on [kordinglab.github.io](http://kordinglab.github.io/)!


### How to add yourself to lab page

You can also add yourself to the page in `_people` folder just create file name `<firstname>_<lastname>.md` in the folder. We require few line of header before you start writing your page. See the following

```
---
name: Eva Dyer
position: postdoc
avatar: eva.jpg
twitter:
joined: 2014
---
```

If you don't have information, just leave it blank. The avatar will bring photo from `images/people` folder and display it on people page. You can also add photo in your own personal page the same way your add photo in blog post.

For position, you can choose position from 4 choices including `postdoc`, `gradstudent`, `visiting`, `others` (Honorary members). It will put you in section that you choose.

### How to add new publications

All publications from the lab are located in `publications.md`. Please upload new publication on your own!

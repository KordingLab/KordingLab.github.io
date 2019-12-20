---
title: How to add blog post on Jekyll
description: simple way to add post on Jekyll for Kording lab's blog
categories: blog
header-img: images/post/dino3.jpg
---

We use Jekyll to creat Kording lab blog. Not only us that use Jekyll as an organization blog, [Stack Overflow Blog](http://blog.stackoverflow.com/) also use Jekyll. They host all the blog on Github  [StackExchange/stack-blog](https://github.com/StackExchange/stack-blog) which has really nice instruction to add new posts.

Using Jekyll, it's very easy to add post on `kordinglab.github.io`. All the posts are located in `_posts` folder located in [`KordingLab.github.io`](https://github.com/KordingLab/KordingLab.github.io). Post arrangement is based on date. Each posts can be written in markdown format (also in `html` too, like `<br>` means new line). File name of each post is in `year-month-date-post-name.md` format such as `2016-02-05-how-to-add-blog.md` or `2016-01-22-bayesian-theory.md`. On top of each post, you just have to state 3 main things in markdown before writing a post: `title`, `description` and `categories` as follows

```
---
title: Summer School in Computational Sensory-Motor Neuroscience (CoSMo)
description: all links to CoSMo summer school in computational neuroscience materials
categories: scientists
---
```

where `categories` can be only 4 choices: `scientists`, `students`, `discussion`, `blog`. It will automatically put that blog post on the page depending on categories you put. `description` will be shown when you share on social media like Facebook or Twitter.

There are multiple ways for someone to add posts:

- First way is going directly to [KordingLab.github.io](https://github.com/KordingLab/KordingLab.github.io) then go to `_post` folder and directly add markdown file. Github allows you to see preview of the markdown too so you can check before you submit any file.
- Second way is to clone the repository and add post in your local computer then push to the repository. This way you can install `Jekyll` and test to see your post on local computer by running `jekyll serve` on terminal (after you follow [instruction](http://jekyllrb.com/)) and go to `localhost:4000`. For example, this post has `blog` categories, I can see preview of my blog on `localhost:4000/blog` before I push to [KordingLab.github.io](https://github.com/KordingLab/KordingLab.github.io).


<hr>

#### Add math equation

No problem, Jekyll allows you to add math equation!

To add inline math, we don't use `$` like in LaTeX since it can be conflicted with a lot of actual dollar sign so we have to use `\\(` and `\\)` as opening and closing bracket instead i.e. <br> `\\(\mathbf{y} = A \mathbf{x}\\)` will render as \\(\mathbf{y} = A \mathbf{x}\\)

For one-line equation, we can use the same as LaTeX that is <br>`$$\cfrac{d}{dt}\cfrac{\partial L}{\partial \dot{q}} = \cfrac{\partial L}{\partial q}$$`. It will render as

$$\cfrac{d}{dt}\cfrac{\partial L}{\partial \dot{q}} = \cfrac{\partial L}{\partial q}$$


#### Add code snippet

For inline code, it's the same format as simple markdown format. Use back tick (symbol below tilde) to highlight inline code. If you want to add multiple line of codes, see [jekyllrb.com/docs/templates/](http://jekyllrb.com/docs/templates/) for more information. Basically we will use liquid tag `highlight <programming language>` and `endhighlight` as beginning and end tag for code snippet. Or you can simple use triple back tick same as when you write `README.md` on Github repository.


#### Add images link or Youtube video

For images link, we can add `html` as follows

```html
<figure><center>
  <img width="300" src="http://explainxkcd.com/wiki/images/4/4d/git.png"/>
</center></figure>
```

<figure><center>
  <img width="300" src="http://explainxkcd.com/wiki/images/4/4d/git.png"/>
</center></figure>


For Youtube, you can just copy embed link from Youtube (`share` > `embed`). For example,

```html
<center>
<iframe width="420" height="315" src="https://www.youtube.com/embed/pF5xBtaL3YI" frameborder="0" allowfullscreen></iframe>
</center>
```

<center>
<iframe width="420" height="315" src="https://www.youtube.com/embed/pF5xBtaL3YI" frameborder="0" allowfullscreen></iframe>
</center>

<hr>

#### Again, why Jekyll?

First, Jekyll allows very easy way to transform and render plain markdown file (lingua franca of open-source community) to html which is our blog. It's free hosting on with Github pages which just updating to Jekyll 3.0 which is much faster. See more at [GitHub Pages now faster and simpler with Jekyll 3.0](https://github.com/blog/2100-github-pages-now-faster-and-simpler-with-jekyll-3-0) blog. It uses `kramdown` markdown which is very intuitive way to write.

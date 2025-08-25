# Kording lab page

This is repository for [Kording lab page](http://kordinglab.com/). We use Jekyll to run our Github page. We are welcome for other people to contribute to our site not just lab members. Feel free to fork and pull-request!

## Run the page locally using Jekyll

To run locally, follow instruction [here](https://jekyllrb.com/) to install Jekyll then run `jekyll serve` to see in `localhost:4000`. Here is a brief install guidelines.

```bash
sudo gem install jekyll
sudo gem install rouge
jekyll serve
```

## Editing the lab website

Below, we explain how to edit the lab webpage

### Add posts

It's very easy to add post. All the posts are located in `_posts` folder. It arrangement is based on
date. Each post can be written in markdown format. You just have to state headers before writing: `title`, `description` and `categories`. `description` will be shown when you share on social media like Facebook or twitter. See the following headers:

``` markdown
---
title: Summer School in Computational Sensory-Motor Neuroscience (CoSMo)
description: all links to CoSMo summer school in computational neuroscience materials
categories: scientists
---
```

We have 4 categories: `scientists`, `students`, `discussion`, `blog` you can choose and this will be rendered to different location.

### How to add posts

- **Directly edit on Github**, you can simply go to `_posts` and click `New file` then put some markdown file e.g. `2016-02-03-post-name.md` and start writing blog post. Github also allows you to preview it so it's nice for people who don't want to clone the repo. 

- **Clone the repository**, kind of the same as directly add post on Github. You just have to clone the repository. Then add new post file, commit and push to the repo.

The changes will take approximately half a minute to render. You can see the new posts or changes on [kordinglab.com](http://kordinglab.github.io/)!

### Add yourself

You can add yourself to the page in `_people` folder just create file name `<firstname>_<lastname>.md` in the folder. We require few line of header before you start writing your own page. See the following for the header

``` markdown
---
name: Eva Dyer
position: postdoc
avatar: eva.jpg
twitter:
joined: 2014
---
```

If you don't have information, just leave it blank. The avatar will bring photo from `images/people` folder and display it on people page. 
For lab position, you can choose position from 4 classes including `postdoc`, `gradstudent`, `visiting`, `others` (so called Honorary members). Position will put you into section that you choose.

### Add new publications

All publications from the lab are located in `publications.md`. Please upload new publication on your own!

### Add news

All news presented in the front page by editing `_data/news.yml`. There are some symbol that cannot be used directly e.g. `:`, be careful

## Internal

### When to Add/Remove Yourself from the Webpage

**When to ADD yourself:**
- When you officially join the Kording Lab as a graduate student, postdoc, research staff, or visiting scholar
- Ideally within your first week of joining the lab
- After confirming with Konrad or the lab manager that you are officially part of the lab

**When to REMOVE yourself:**
- When you graduate or complete your position in the lab
- When transitioning to alumni status (you don't delete your profile, just change your position to 'alumni')
- If you're a visiting scholar, when your visit period ends

### How to Add Yourself to the People Page

1. **Create your profile file:**
   - Navigate to the `_people` folder
   - Create a new file named `<firstname>_<lastname>.md` (all lowercase, e.g., `john_smith.md`)
   
2. **Add the required header:**
   ```markdown
   ---
   name: Your Full Name
   position: [choose one: gradstudent/postdoc/researchstaff/visiting/alumni]
   avatar: yourphoto.jpg
   twitter: yourtwitterhandle
   joined: 2024
   ---
   ```
   
3. **Add your photo:**
   - Add a professional photo to the `images/people/` folder
   - Name it to match the avatar field in your header (e.g., `yourphoto.jpg`)
   - Recommended: square aspect ratio, at least 400x400 pixels
   
4. **Write your bio:**
   - After the header, write a brief bio (2-3 paragraphs)
   - Include your research interests, background, and current projects
   - You can use markdown formatting for links, bold text, etc.

5. **Submit your changes:**
   - If comfortable with git: commit and push your changes, then create a pull request
   - If not: email your files to the lab manager or ask for help

### How to Update Your Profile

1. **Edit your existing file** in `_people/<firstname>_<lastname>.md`
2. **Update any information** that has changed
3. **Update your photo** if needed (replace the file in `images/people/`)
4. **Commit and push** your changes or ask for help

### How to Transition to Alumni Status

When leaving the lab:

1. **Edit your profile file** in `_people/<firstname>_<lastname>.md`
2. **Change the position field** from your current position to `alumni`:
   ```markdown
   position: alumni
   ```
3. **Add a line about where you're going** in your bio (e.g., "Now at [Company/University]")
4. **Keep your profile** - don't delete it! Alumni remain part of the lab community
5. **Commit and push** the changes

### Getting Help

- If you're not familiar with Git/GitHub, ask any lab member for help
- You can also edit directly on GitHub.com through the web interface
- For technical issues, contact the lab member maintaining the website
- Always test locally with `jekyll serve` before pushing if you're making significant changes

## Community for Rigor (C4R)

The [Community for Rigor (C4R)](https://c4r.io) is an initiative founded by Konrad Kording that operates closely with the lab. C4R is dedicated to improving scientific rigor through education and community engagement.

### What is C4R?

C4R is a user-friendly, open-source educational platform that addresses critical issues in research methodology:
- **Biases in research** - Understanding and mitigating various forms of bias
- **Logical fallacies around causality** - Improving causal reasoning
- **Hypothesis development** - Crafting better research questions
- **Literature search design** - Systematic approaches to reviewing existing work
- **Identifying experimental variables** - Proper variable selection and control
- **Reducing confounding variables** - Improving experimental design

### Lab Involvement with C4R

- Many lab members contribute to C4R content and development
- C4R principles are integrated into lab research practices
- Lab meetings often discuss C4R topics and materials
- Students are encouraged to complete C4R modules as part of their training

### How to Get Involved

- Visit [c4r.io](https://c4r.io) to explore the educational modules
- Consider contributing content if you have expertise in research methods
- Participate in C4R community discussions and events
- Apply C4R principles in your own research projects
- Share C4R resources with colleagues who might benefit

### Resources

- Main website: [c4r.io](https://c4r.io)
- GitHub repository: Check the C4R organization on GitHub for open-source materials
- Contact: Reach out to Konrad or lab members involved in C4R for more information

C4R represents the lab's commitment to not just doing good science, but actively working to improve how science is done across the research community.

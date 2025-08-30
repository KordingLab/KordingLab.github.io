---
title: Internal
permalink: /internal/
---

## Internal Lab Resources

This page contains important information for current lab members about managing their presence on the lab website and other internal processes.

### When to Add/Remove Yourself from the Webpage

**When to ADD yourself:**
- When you officially join the Kording Lab as a graduate student, postdoc, research staff, or visiting scholar
- Ideally within your first week of joining the lab
- After confirming with Konrad or the lab manager that you are officially part of the lab

**When to REMOVE/UPDATE yourself:**
- When you graduate or complete your position in the lab
- When transitioning to alumni status (you don't delete your profile, just change your position to 'alumni')
- If you're a visiting scholar, when your visit period ends

### How to Add Yourself to the People Page

#### Step 1: Create Your Profile File
- Navigate to the `_people` folder in the repository
- Create a new file named `<firstname>_<lastname>.md` (all lowercase, e.g., `john_smith.md`)

#### Step 2: Add the Required Header
```markdown
---
name: Your Full Name
position: [choose one: gradstudent/postdoc/researchstaff/visiting/alumni]
avatar: yourphoto.jpg
twitter: yourtwitterhandle
joined: 2024
---
```

#### Step 3: Add Your Photo
- Add a professional photo to the `images/people/` folder
- Name it to match the avatar field in your header (e.g., `yourphoto.jpg`)
- Recommended: square aspect ratio, at least 400x400 pixels
- Make sure the photo is professional and represents you well

#### Step 4: Write Your Bio
- After the header, write a brief bio (2-3 paragraphs)
- Include your research interests, background, and current projects
- You can use markdown formatting for links, bold text, etc.
- Keep it professional but feel free to add personality

#### Step 5: Submit Your Changes
- **If comfortable with Git**: 
  - Commit and push your changes
  - Create a pull request
- **If not familiar with Git**:
  - Email your files to the lab manager
  - Or ask any lab member for help with the Git process

### How to Update Your Profile

1. **Find your file** in `_people/<firstname>_<lastname>.md`
2. **Edit the content** - update your bio, position, or other information
3. **Update your photo** if needed (replace the file in `images/people/`)
4. **Commit and push** your changes or ask for help

### How to Transition to Alumni Status

When leaving the lab:

1. **Edit your profile file** in `_people/<firstname>_<lastname>.md`
2. **Change the position field** to `alumni`:
   ```markdown
   position: alumni
   ```
3. **Add your next position** to your bio (e.g., "Now at [Company/University]")
4. **Keep your profile** - don't delete it! Alumni remain part of the lab community
5. **Commit and push** the changes

### Conference Presentation Policy

**Important Lab Policy:** Any significant piece of work from the lab should be presented at exactly one conference before submitting to a journal.

This policy ensures:
- Work receives feedback from the community before publication
- Ideas are tested and refined through presentation
- Lab members gain presentation experience
- The lab maintains visibility in the research community

Guidelines:
- Choose the most appropriate conference for your work
- Coordinate with Konrad about conference selection
- Budget for conference attendance should be discussed in advance
- After presentation, incorporate feedback before journal submission

### Adding Publications

When you publish a paper:

1. **Edit** `publications.md`
2. **Find the correct year** section
3. **Add your publication** in this format:
   ```markdown
   _Paper Title_<br>
   Author1, Author2, KP Kording, etc<br>
   Journal Name, Year ([Article](link-if-available))
   ```
4. **Maintain chronological order** within the year
5. **Include all lab members** who are authors

### Adding News Items

For lab news and announcements:

1. **Edit** `_data/news.yml`
2. **Add a new entry** at the top:
   ```yaml
   - date: YYYY-MM-DD
     details: "Your news item here. Can include <a href='link'>links</a>"
   ```
3. **Note**: Some characters like `:` need special handling - use quotes around your text

### Technical Help

#### Using Git/GitHub

**Basic Git workflow:**
```bash
git pull                     # Get latest changes
git add .                    # Stage your changes
git commit -m "message"      # Commit with descriptive message
git push                     # Push to GitHub
```

**Editing directly on GitHub:**
1. Navigate to the file on GitHub.com
2. Click the pencil icon to edit
3. Make your changes
4. Commit directly or create a pull request

#### Testing Changes Locally

Before pushing changes:
```bash
jekyll serve
```
Then visit `localhost:4000` to preview

### Getting Help

- **Administrative questions**: Email Thomas McDonald <taomcd@seas.upenn.edu>
- **Git/GitHub issues**: Ask any lab member familiar with Git
- **Website technical issues**: Contact the designated website maintainer
- **Content questions**: Check with Konrad or senior lab members
- **Emergency updates**: Contact multiple lab members to ensure quick response

### Best Practices

- **Keep profiles updated** - Outdated information reflects poorly on everyone
- **Use professional photos** - This is a public-facing website
- **Write clear commit messages** - Help others understand what you changed
- **Test before pushing** - Use `jekyll serve` for significant changes
- **Ask for help** - Better to ask than to break something
- **Regular updates** - Check your profile every semester

### Important Links

- **Lab GitHub**: [github.com/KordingLab](https://github.com/KordingLab)
- **Website Repository**: [github.com/KordingLab/KordingLab.github.io](https://github.com/KordingLab/KordingLab.github.io)
- **Live Website**: [kordinglab.com](http://kordinglab.com)
- **C4R Platform**: [c4r.io](https://c4r.io)

---

*This page is for internal use by Kording Lab members. If you're not a lab member but interested in joining, please see the [About](/about) page for more information.*
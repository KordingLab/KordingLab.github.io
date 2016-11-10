---
title: Installing Python with Anaconda
categories: students
---

As the lab, we're now moving more to use Python. There is an easy way to install
Python using [Anaconda](https://www.continuum.io/downloads). Here, we'll go through
step-by-step to set up Anaconda.

Anaconda is a distribution of Python. It means that when you install Anaconda,
you will have Python will pre-installed packages (`numpy`, `pandas`, `nltk`, `pip`, ...).
This becomes handy compared to install Python from scratch using package management system
like Macports or Homebrew on macOS.

To install Anaconda, first you have to go to download pages [(https://www.continuum.io/downloads)]((https://www.continuum.io/downloads)).
Then, what I prefer is installing using command line. Click on command-line installer
in order to download `Anaconda3-4.2.0-MacOSX-x86_64.sh`. Then, you can go to terminal and run

```bash
bash Anaconda3-4.2.0-MacOSX-x86_64.sh
```

Anaconda also comes with package management for python namely `pip`. Here, we can
update installed libraries or install new packages using just command-line, e.g.

```bash
pip install nltk --upgrade
```

I add `--upgrade` here since we already installed `nltk`. Now, to run Jupyter Notebook
(or used to be IPython notebook), we can move to directory that has notebook file and
run

```bash
jupyter notebook
```

This will bring up web browser (default is `localhost:8888`) for us to edit the notebook.

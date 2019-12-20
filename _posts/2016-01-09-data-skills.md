---
title: Data Skills
categories: scientists
header-img: images/post/dino2.jpg
---

**Data skills – results of discussion between Josh Vogelstein and Konrad Kording**

Foundational (courtesy Josh):

  - use median instead of mean if you want an estimate of position (for univariate data; multivariate is more complicated)
  - use MAD or some other robust statistic if you want an estimate of scale (for univariate data; multivariate is more complicated)
  - when doing regression, consider using something robust to outliers, svm is a popular example, but other options are simpler/more intuitive, eg, change from L2 loss to huber loss, L1 loss, etc.
  - never conduct a statistical test without first looking at the data that goes into the function and deciding whether the assumptions of the test are approximately satisfied by the data. if the assumptions are woefully not satisfied, the p-values are worse than meaningless, they are deceiving.
  - always plot your data **before** doing any analyses, preferably in a whole bunch of ways, to get ideas of what might be going on.
  - if you n vectors, each d-dimensional, and n is not bigger than say 5d or 10d, you **must** regularize. lasso is the most popular choice these days, though it is highly problematic if data are correlated at all. elastic net is a hacky and effective solution that i would try first.
  - if you would like to reduce the dimensionality of your data, always try pca **first**. always remember that pca is terribly sensitive to outliers (simulate data with 1 strong outlier and you will see). always remember that eigenvectors are **not unique**, ie, sign flips and rotations are equally good. therefore, the eigenfunctions are **not intreptable**, without considerable additional work.
  - **never** steal code from matlab exchange to implement an algorithm if the code is not written by the dude who published the paper, or verified by that dude. lots of code is **wrong** or otherwise bad.
  - always try your code on simulated data **prior** to running it on real data. confirm that the code works when it should work and fails when it should fail. if your code does fail when it should, then it failed. don't forget to try things like data corrupted with a NaN, or a few actual zeros, both of which can be highly problematic.
  - never write if `x == y`. numerical precision dictates that this will not be true many times. write if `(x-y)^2 < eps`, for some small choice of epsilon, eg, 10 standard deviations.
  - always consider the bias/variance tradeoff. where did you make unstated assumptions/simplifications? did you spike sort? did you filter? did you digitally sample? why did you make these assumptions? computational reasons? is it the standard in the field?
  - always remember the information processing lemma: you cannot add information via processing your data, only keep it or lose it!

1-5 derive from the fact that big data is almost always dirty. 6-7 derives from big data leads to large problems. 8-10 are important to avoid bugs.

Specialized techniques (mostly Konrad) Konrad just put together a list of techniques he would like his students to know

  - Elastic net glm
  - MCMC
  - Gaussian process regression, Hierarchical Regression
  - Variational bayes
  - Graphical models, e.g. hmm, kalman, learning
  - Extended Kalman Filters, dynamical systems, stability
  - Particle filters
  - Linear/convex programming
  - Sequence alignment algorithms / time warping
  - Regression trees
  - SVMs , kernel approaches
  - Search trees (e.g efficient nn)
  - Deep learning (contentious if this should be on the list)
  - Neural networks with regularizing (history matters)
  - Model comparison AIC, BIC, cross-validation, corrections
  - Bootstrap
  - Network metrics/ inference/ generative grammars
  - Nonparametric /infinite bayes
  - Standard feature sets (sift, time series, wavelets, etc)
  - Standard frequentist tests


<i class="fa fa-twitter"></i> [`@Jovo`](https://twitter.com/jovo), [`@Kordinglab`](https://twitter.com/KordingLab)

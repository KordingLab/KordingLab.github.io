---
title: Leave Neuroscience to become a data scientist?
description: how to leave neuroscience to become scientist guideline
categories: scientists
header-img: images/post/dino2.jpg
---

A bunch of helpful links

- [http://kaggle.com](http://kaggle.com)
- [http://insightdatascience.com/](http://insightdatascience.com/)

### **Some very helpful thoughts by Jeong-Yoon Lee who very successfully made the transition**

First, I'd like to say that data science is a relatively new field (like computational neuroscience), and you don't need to feel bad to make the transition after your Ph.D.

When I was out to the job market in May 2011, I didn't have any analytic background at all either. I started my industrial career at one of analytic consulting companies, Opera Solutions in San Diego, where one of Nicolas' friends, Jacob, runs the R&D team of the company. Jacob did his Ph.D under the supervision of Prof. Michael Arbib at USC in computational neuroscience as well. During the interview, I was tested to prove my thought process, basic knowledges in statistics and machine learning, and programming, which I'd practiced though out my whole Ph.D.

So, if he/she has good machine learning background with programming skills (I'm sure he/she does based on the fact he/she's your student), he/she can be competent to pursue his/her career in data science.


### **Useful tools in data science**

Back in the graduate school, I used MATLAB a lot and some SPSS and very rarely C. In the data science field, Python and R are most popular languages, and SQL is a kind of necessary evil.

R is similar to MATLAB except that it's free. It is not a hardcore programming language and doesn't take much time to learn. It comes with the latest statistical libraries and provides powerful plotting functions.

There are many IDEs which make easy to use R, but my favorite is [R Studio](http://www.rstudio.com/). If you run R on the server with R Studio Server, you can access it from anywhere via your web browser, which is really cool.

Although native R plotting functions are excellent by themselves, the ggplot2 library provides more eye-catching visualization.

In Python, Numpy + Scipy packages provides similar vector-matrix computation functionalities as MATLAB. For machine learning algorithms, you need Scikit-Learn, and for data handling, Pandas will make your life easy. For debugging and prototyping, iPython Notebook is really handy and useful.

SQL is an old technology but still widely used. Most of data are stored in the data warehouse, which can be accessed only via SQL or SQL equivalents (Oracle, Teradata, Netezza, etc.). Postgres and MySQL are

### **Some hints for ML competitions**

Fortunately, I had a chance to work with many of top competitors such as the 1st and 2nd place teams at Netflix competitions, and learn how they do at competitions. Here are some tips I found helpful.

- **Don't jump into the algorithms too fast.** Spend enough time to understand data. Algorithms are important, but no matter how good algorithm you use, if you put garbage in it, you will get garbage out of it. Many regression algorithms assume the Gaussian distributed variables, and fail to make good predictions if you provide non-Gaussian distributed variables. So, standardization, normalization, non-linear transformation, discretization, binning are very important.

- **Use different algorithms and blend.** There is no universal optimal algorithm. Most of times (if not all), the winning algorithms are ensembles of many individual models with tens of different algorithms. Combining different kinds of models can improve prediction performance a lot. For individual models, I find random forest, gradient boosting machine, factorization machine, neural network, support vector machine, logistic/linear regression, naive bayes, and collaborative filtering are mostly useful, and gradient boosting machine and factorization machine are often the best individual models.

- **Optimize at last. Each competition has a different evaluation metric**, and optimizing algorithms to do the best for that metric can improve your chance to win. Two most popular metrics are RMSE and AUC (area under the ROC curve), and algorithms optimizing one metric is not the optimal for the other metric. If you use the standard library as it is, it often provides only RMSE optimization, so for AUC (or other metric) optimization, you need to implement it by yourself.


see more at <i class="fa fa-linkedin-square"></i>
[`jeongyoonlee`](https://www.linkedin.com/in/jeongyoonlee)

---
title: Fortran-glmnet-in-python
categories: students
header-img: images/post/dino4.jpeg
---

Purpose: To compile the original Fortran code of GLMNET to use it in Python which contains the Poisson link function that many people and me use in the lab.

Requirements:

- `git`
- `f2py` (translator from fortran to python)
- `gfortran` (fortrain compiler)
- `scikit-learn` (for the example)

**clone repository from github**

```bash
$ git clone https://github.com/dwf/glmnet-python
```

**change directory and compile**

```bash
$ cd glmnet-python
$ python setup.py build
```

**compile fortran code**

```bash
$ cd glmnet/
$ f2py -c --fcompiler=gnu95 --f77flags='-fdefault-real-8' --f90flags='-fdefault-real-8' glmnet.pyf glmnet.f
```

**test code by going to root of project**

```bash
cd ..
```

**and in IPython run this example to see if it works**

```python
from glmnet import ElasticNet
from cv import CVGlmNet
from sklearn.datasets.samples_generator import make_regression

enet = ElasticNet(alpha=.1)
enet_cv = CVGlmNet(enet, n_folds=10, n_jobs=10)
X, y = make_regression(n_samples=100, n_features=10, n_informative=10, random_state=0, noise=35)
enet_cv.fit(X, y)
plot
enet_cv.plot_oof_devs()
```

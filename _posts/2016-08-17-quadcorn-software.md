---
title: Software in Quadcorn
description: List of main software installed and how to install it
categories: blog
---


## General instructions

To install for **all users**

```
$ sudo -i
```
then install package. `git clone` in `~\repos` if need.


To install only for user then add `--user` at the end. E.g.:

```
$ python setup.py install --user
```

## Installing NVidia Drivers 

NVidia graphics card drivers should be downloaded from [here](http://www.geforce.com/drivers/results/105343) and installed.

## Installing CUDA

1. Install AMD ATI drivers:
```
sudo apt-get install fglrx-updates
```

2. Stop the SSH X11 forwarding by modifying /etc/ssh/sshd_config:
```
sudo nano /etc/ssh/ssh_config
```
Find the following line:
X11Forwarding yes
and change it to:
X11Forwarding no

3. Stop the default X server by running:
```
sudo service mdm stop
```
4. The latest supported version of CUDA is 7.5 which can be downloaded from [here](https://developer.nvidia.com/cuda-downloads). Select Linux > X86_64 > Ubuntu > 14.04 > runfile (local). Follow the instructions on that page.

## Software list

We generally followed the instructions in [Setting up a Deep Learning Machine from Scratch](https://github.com/saiprashanths/dl-setup).

Here are some specifics and extra software:



##### [Tensorflow](https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html#using-pip)

```
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0rc0-cp27-none-linux_x86_64.whl
$ pip install --ignore-installed --upgrade $TF_BINARY_URL
```

##### [XGBoost](https://xgboost.readthedocs.io/en/latest/build.html#building-on-ubuntu-debian)

```
$ git clone --recursive https://github.com/dmlc/xgboost
$ cd xgboost; make -j4
$ cd python-package
$ python setup.py install
```


##### Opencv 

```
$ conda install opencv
```



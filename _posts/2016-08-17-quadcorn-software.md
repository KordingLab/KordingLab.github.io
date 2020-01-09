---
title: Software in Quadcorn
description: List of main software installed and how to install it
categories: blog
header-img: images/post/dino2.jpg
---


We generally followed the instructions in [Setting up a Deep Learning Machine from Scratch](https://github.com/saiprashanths/dl-setup).


### Installing NVidia Drivers 

Before installing the drivers, make sure there are no nvidia drivers already installed by doing the following:

```
$ sudo apt-get --purge remove nvidia-*
```

And reboot. Then download NVidia drivers from [here](http://www.geforce.com/drivers/results/105343) and install them according to instructions.

### Installing CUDA

First, install some AMD drivers that will be used by CUDA.

```
$ sudo apt-get install fglrx-updates
```

After installation, reboot the computer.

Next, stop the SSH X11 forwarding by modifying /etc/ssh/sshd_config:

```
$ sudo nano /etc/ssh/sshd_config
```
Find the following line:

```
X11Forwarding yes
```

and change it to:

```
X11Forwarding no
```
After saving the changes, restart the ssh service by typing:

```
$ sudo service ssh restart
```

Now, stop the default X server by typing:

```
$ sudo service mdm stop
```

Now we can install CUDA. The latest supported version is 7.5 which can be downloaded from [here](https://developer.nvidia.com/cuda-downloads). Select Linux > X86_64 > Ubuntu > 14.04 > runfile (local). Follow the instructions on the page to complete the installation.

After finishing the installation of CUDA, undo the change that you made to /etc/ssh/sshd_config, and restart the ssh server using `sudo service ssh restart`. Also, start the X server again: `sudo service mdm start`

### Installing cuDNN

Download cuDNN from [here](https://developer.nvidia.com/cudnn). Select a version which is compatible with CUDA. After downloading, do the following:

```
$ tar xvf <DOWNLOADED FILE NAME>
$ cd cuda
$ sudo cp */*.h /usr/local/cuda/include/
$ sudo cp */libcudnn* /usr/local/cuda/lib64/
$ sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
```

## Software

To install for all users

```
$ sudo -i
```
then install package. `git clone` in `~\repos` if need.


To install only for user then add `--user` at the end. E.g.:

```
$ python setup.py install --user
```

Here are some specific instructions:



##### Theano

```
$ pip install theano
```

Edit/create `~/.theanorc`:

```
[global]
floatX = float32
device = gpuX
```

choose as `gpuX` your assigned gpu, there will be random inspections. Grad students all share `gpu1`. `klab` uses `gpu0`

##### [Tensorflow](https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html#using-pip)

```
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0rc0-cp27-none-linux_x86_64.whl
$ pip install --ignore-installed --upgrade $TF_BINARY_URL
```

Note: right now `tensorflow` is not working because we are using `cuDNN v5`. Either wait for it to be compatible or downgrade `cuDNN` to `v4` when we really need to use tensorflow (don't do it). Or try to compile/install `tensorflow` [from source](https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html#installing-from-sources) (good luck with that).

##### Keras

```
$ pip install keras
```

See [here](https://keras.io/backend/) to choose `tensorflow` and `theano` in `Keras`


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

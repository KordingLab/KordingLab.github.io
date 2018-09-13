---
title: Useful commands for Quadcorn and Bleen
categories: students
---

We have been using workstation from [Lambda lab](https://lambdalabs.com/products/quad) for a while which runs on Ubuntu 16.04. 
And there are a lot of common commands that we always have to google it for. 
We decide to put most of the command that we typically use on the workstation here. 
This hopefully will be useful for the lab to check workstation status before running an experiment or task. 

In this blog post, we will divide these commandlines into 3 sections (1) CPU usage (2) Memory usage (3) GPU


### CPU usage

Eventhough we have multiple CPU cores to run something. It is better to share the cores for others people. 
We can check what is going on by running:

```sh
htop
```

This will show us most of the things happening e.g. memory usage, CPU usage, and more.
There is a column name `PID` when running `htop` and we can kill the specific by 
using `kill -9 {PID}` (if it's using a lot of CPUs, for example).


### Memory

When we talk about memory, it's about RAM and there is an active memory usage and swap memory. Same as before, 
we can check the memory by running `htop` to check the overall memory.

Now, if we want to know who is taking most SWAP and active memory. We can run the following command
as a `root` or `ubuntu`

```sh
sudo smem -ur
```


### GPU

To check GPU and memory on GPU usage, 

```sh
nvidia-smi
```

Alternatively, we installed [gpustat](https://github.com/wookayin/gpustat) where you can call to see who is 
using how much memory on each GPU.

```sh
gpustat # or gpustat -cp 
```

This will return something like:

```
[0] GeForce GTX 1080 Ti | 60'C,   0 % |  7610 / 11169 MB | root(30M)
[1] GeForce GTX 1080 Ti | 62'C,   0 % |  1155 / 11172 MB |
[2] GeForce GTX 1080 Ti | 41'C,   0 % |  6134 / 11172 MB | username1(6123M)
[3] GeForce GTX 1080 Ti | 31'C,   0 % |  9012 / 11172 MB | username2(9001M)
```

which we can notice that GPU 3 is running out of memory and we should use the others. 
Here, we can change the default GPU by running 

```sh
export CUDA_VISIBLE_DEVICES=0
```
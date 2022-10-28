---
title: 'Lab Teaching: Docker 101 for reproducible science'
description: Using Docker for a reproducible and reusable data science workflow
categories: newblog
---

# Docker 101 for Reproducible Science
*By [Jordan Matelsky](https://twitter.com/j6m8)*

> See the video version of this Lab Teaching [on YouTube](https://www.youtube.com/watch?v=fs1ko2UNVOo).

> A brief note — I will use the term "Docker" to refer to a container management system, even though Docker is not the only one. I will use the term "container" to refer to a running instance of a Docker image.

## What's the difference between a container and a virtual machine?

A container runs a single process, taking no more memory than any other executable, while virtual machines (VMs) run a full-blown “guest” operating system with virtual access to host resources through a hypervisor. In general, containers are considered much more lightweight. Containers are becoming popular for reliably deploying applications because they are:

-   Portable across clouds and OS platforms
-   Scalable up and down as needed
-   Isolated from one another and the host environment

## What's the difference between a container and an environment like Anaconda?

Anaconda is a distribution of Python and R and many of their most popular packages for scientific computing. It is a great tool for data scientists and analysts who want to have a consistent environment for their work. However, it is not a container. Containers are a way to package an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the containerization software, you can rest assured that the application will run quickly and reliably from one computing environment to another.

## Why is Docker useful for scientific computing?

Docker is useful for scientific computing because it allows you to package your entire scientific computing environment into a single "image" that you can easily share with others. This image can be run on any computer that has Docker installed, regardless of the operating system or other applications that are already installed.

This means:

-   You can easily share your work with collaborators, who can run it on their own computers without having to install any dependencies.
-   You don't have to worry about breaking your system by installing a bunch of dependencies for a project that you're only going to work on for a few days.
-   You can easily deploy your work on a cloud computing service, such as Amazon Web Services (AWS) or Microsoft Azure to scale it up.

## Getting Started

Our first venture into Docker will be to create an Image (blueprint) and then use that image to create and run a simple container.

```dockerfile
FROM ubuntu:20.04
LABEL maintainer="Jordan Matelsky <tutorial@example.com>"

CMD echo "Hello World"
```

This is a simple Dockerfile that will create an image that is based on the latest version of Ubuntu (20.04). It will also add a label to the image that includes the name and email address of the person who created it. Finally, it will run the command `echo "Hello World"` when the container is started.

To build this image, we will use the `docker build` command. This command will look for a file called `Dockerfile` in the current directory and use the instructions in that file to build the image.

```bash
docker build -t hello-world .
```

The `-t` flag lets us specify a name and tag for the image that will be created. In this case, we are using the name `hello-world` and the tag `latest`. The `.` at the end of the command tells Docker to look for the `Dockerfile` in the current directory.

You can see a list of all of the images that you have built on your computer by running:

```bash
docker image ls
```

You should see output that looks something like this:

```bash
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              4ab4c602aa5e        3 minutes ago       72.9MB
ubuntu              20.04               4ab4c602aa5e        3 minutes ago       72.9MB
```

The first time we build an image, Docker will download the base image (in this case, Ubuntu 20.04) from Docker Hub, a registry of Docker images. This image will be stored on your computer so that you don't have to download it again the next time you want to build an image. 

Docker tends to be pretty smart and will only re-run the steps that are necessary to update an image. For example, if we change the `CMD` in our Dockerfile and then run `docker build` again, Docker will only have to re-run that last step, since the rest of the image is the same.

```dockerfile
FROM ubuntu:20.04
LABEL maintainer="Jordan Matelsky <tutorial@example.com>"

CMD echo "Greetings, World!"
```

Note that just changing the Dockerfile is NOT enough to change the image on disk. If we run a container built from the current image, it will still say "Hello World". We need to rebuild the image for the changes to take effect.

```bash
docker build -t hello-world .
```

Now, if we run a container from the new image, we will see the updated message.

```bash
docker run hello-world
```

```bash
Greetings, World!
```

## I told you Docker containers live in their own world

...and I was serious. What do you think happens here?

```dockerfile
FROM ubuntu:20.04

CMD ls 
```

```bash
docker build -t tutorial-isolation .
```

```bash
docker run tutorial-isolation
```

Did you expect to see the `Dockerfile`? in the `ls` output? Remember, as far as the container is concerned, it is the only thing that exists on the computer. It doesn't know that there is a `Dockerfile` in the current directory; in fact, (modulo some special cases) it doesn't even know that it's a container.

What if we _want_ it to see files from our host computer?

There are two ways of doing this; we can either mount a directory from our host computer into the container, or we can copy files from our host computer into the container when we build the image.

### Mounting a directory


Let's think about the first option for a second. If we mount a directory from our host computer into the container, then the container will be able to see the files in that directory. But what happens if we change the files in that directory? Will the container see those changes? What if we delete the files in that directory? Will the container still be able to see them? What if we delete the directory? Will the container still be able to see it?

Now that you've thought about it for a second, let's try it out.

```dockerfile
FROM ubuntu:20.04

CMD ls /mnt
```

```bash
docker build -t tutorial-mount .
```

```bash
docker run -v $(pwd):/mnt tutorial-mount
```

Did you see what you expected?

### Copying files into the image

In the last section, we let the _container_ see files from our host machine. But what if we want the _image_ to see files from our host machine? (Think for a moment about what the difference is!)

We can do this by copying files from our host machine into the image when we build it.

```dockerfile
FROM ubuntu:20.04

COPY Dockerfile /mnt
CMD ls /mnt
```

```bash
docker build -t tutorial-copy .
```

```bash
docker run tutorial-copy
```

Did you see what you expected?

Because we COPIED the file into the image when we built it, the container will still be able to see the file even if we delete it from our host machine, and if we delete the file inside the container, it won't impact the file on our host machine.

## I want to go to there

It's good to treat a container as a relatively immutable object: If you put all of your analysis code in the image, then anyone who runs a container from your image will get a reproducible output. 

But it is also possible to "ssh" into a container (really, you're just running a shell inside the container) and make changes to the container. This is useful for working in a more powerful virtual environment, debugging, or just poking around.

```bash
docker run -it hello-world /bin/bash
```

We pass the `-it` flag to `docker run` to tell Docker that we want to run the container in interactive (and TTY) mode. This will give us a shell inside the container.

We then pass a program that we want to run (in this case, bash). This is the command that will be run when the container starts.

```bash
root@e0b0b0b0b0b0: echo "I'm in a container!"
```

You can exit the container by quitting the shell (Ctrl-D) or by running `exit`.

## Using a container as an environment

So far, we've learned about three capabilities that will be very useful to us:

* We can isolate executables and make reproducible environments by running them in containers.
* We can mount a piece of our filesystem into a container, so that the container can see files from our host machine and change them in realtime.
* We can run containers interactively.

Let's apply these three capabilities to a real-world problem.

### Setup

Let's do a simple experiment --- we'll use a Python script to generate some random numbers and save them to a file.

First, we'll write a `requirements.txt` file. Unlike our usual workflow, we WON'T install the packages in this file into our host environment. Instead, we'll install them into a container.

```requirements.txt
# requirements.txt

numpy
```

WAIT! We should version-pin our dependencies! We can do it manually, like this:

```requirements.txt
# requirements.txt

numpy==1.23.4
```

Or we can use the power of Docker!

```dockerfile
FROM python:3.9

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
```

```bash
docker build -t tutorial-env .
```

Now we can version-pin using Docker by having Docker output the version of the packages that it installed.

```bash
docker run --rm tutorial-env pip freeze -r /tmp/requirements.txt
```

Docker containers are cheap and fast! 



## Getting started with machine learning exploratory data analysis in Docker

Each lab member can now begin using Docker to run their own experiments. It's common to start off with some exploratory data analysis in a Jupyter notebook. Here's a command that starts a notebook server in a Docker container with GPU access, and mounts the current directory as a volume inside the container:

```shell
docker run --rm -it --gpus all -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/datascience-notebook
```

This command will start a Jupyter notebook server in a Docker container, and mount the current directory as a volume inside the container. The `--rm` flag tells Docker to remove the container when it exits, and the `-it` flag tells Docker to run the container in interactive mode. The `--gpus all` flag tells Docker to give the container access to all GPUs on the host machine. The `-p 8888:8888` flag tells Docker to forward port 8888 on the host machine to port 8888 on the container. (You may want to use another port if other users are also running notebooks; for example, `-p 8889:8888` will let you point to `http://myfancyserver:8889` in a browser.)

The `-v $(pwd):/home/jovyan/work` flag tells Docker to mount the current directory as a volume inside the container, at the path `/home/jovyan/work`. Finally, the `jupyter/datascience-notebook` argument tells Docker to use the [`jupyter/datascience-notebook`](https://hub.docker.com/r/jupyter/datascience-notebook) image as the base image for the container.

## Connecting to a Docker Container in Visual Studio Code

It is possible to connect to a Docker container in Visual Studio Code. This is useful if you want to use Visual Studio Code to edit files in the container, or if you want to use Visual Studio Code's debugger to debug code running in the container. To connect to a Docker container in Visual Studio Code, you need to install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension. Once you've installed the extension, you can connect to a Docker container by clicking on the green "Remote-Containers: Open Folder in Container..." button in the bottom left corner of the Visual Studio Code window. You can then select the folder you want to open in the container, and Visual Studio Code will automatically build a Docker image for the container and start the container.

## Running a machine learning hyperparameter search using Docker

Because Docker completely isolates an environment, it is also a perfect tool for running a hyperparameter search. In this example, we'll write a simple sklearn demo, and then try a few different hyperparameter sets, writing out evaluation results to a text file.

### Creating the base experiment

First, create a file called `main.py` with the following contents:

```python
# For parsing command line arguments:
import argparse
# For writing out evaluation results:
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def main():
    # Parse command line arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_depth", type=int, default=2)
    parser.add_argument("--n_estimators", type=int, default=100)
    args = parser.parse_args()
    # Load the iris dataset:
    iris = load_iris()
    X = iris.data
    y = iris.target
    # Split the dataset into training and test sets:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # Train a random forest classifier:
    clf = RandomForestClassifier(max_depth=args.max_depth, n_estimators=args.n_estimators)
    clf.fit(X_train, y_train)
    # Evaluate the classifier:
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    # Write out evaluation results:
    with open(
        f"results/results-depth_{args.max_depth}-ests_{args.n_estimators}.txt", "w"
    ) as f:
        json.dump({
            "accuracy": accuracy,
            "max_depth": args.max_depth,
            "n_estimators": args.n_estimators
        }, f)
if __name__ == "__main__":
    main()
```

### Creating a Dockerfile and Image

Realistically, we could reuse the `jupyter/datascience-notebook` image from earlier. But to show how to install custom dependencies, let's look at an engineered example:

Create a file called `Dockerfile` with the following contents:

```dockerfile
FROM python:3.10
# Install dependencies:
RUN pip install scikit-learn
# Copy the experiment code into the container:
COPY main.py /main.py
# Run the experiment:
CMD ["python", "/main.py"]
```

By default, Docker will run the `CMD` command when the container starts. In this case, we want to run the `main.py` script, so we set the `CMD` to `["python", "/main.py"]`. (Because we set defaults for argparse, we don't need to pass any arguments to `main.py` in the default case.)

Let's make sure it works. First, build the Docker image:

```bash
docker build -t hyperparam .
```

Then, run the Docker container:

```bash
docker run -it -v $(pwd):/results hyperparam
```
```
You should see a new `results-depth_2-ests_100.txt` file in your current directory. If you open it, you should see something like this:
```json
{"accuracy": 0.95, "max_depth": 2, "n_estimators": 100}
```

### Running the hyperparameter search

Let's run a hyperparameter search. We'll try a few different values for `max_depth` and `n_estimators`, and write out the results to a text file.

Create a file called `search.sh` with the following contents:

```bash
#!/bin/bash
for max_depth in 2 4 6 8 10
do
    for n_estimators in 10 20 30 40 50
    do
        docker run -v $(pwd):/results hyperparam \
            --max_depth $max_depth \
            --n_estimators $n_estimators
    done
done
```

This script will run the `main.py` script with different values for `max_depth` and `n_estimators`. It will write out the results to a file called `results/results-depth_<max_depth>-ests_<n_estimators>.txt`.

Let's run the script:

```bash
./search.sh
```

When it's done, you should see a bunch of new files in the `results` directory.

Note that this runs ALL of the experiments simultaneously; for a less ridiculous workload, consider using `parallel` or `xargs` to run the experiments in parallel:

```bash
for max_depth in 2 4 6 8 10
do
    for n_estimators in 10 20 30 40 50
    do
        echo "docker run -v $(pwd):/results hyperparam --max_depth $max_depth --n_estimators $n_estimators"
    done
done | parallel -j 4 # Run 4 experiments in parallel
```

For more complex job dependency graphs, consider using a [DAG job scheduler](https://en.wikipedia.org/wiki/Directed_acyclic_graph) like [frof](https://github.com/j6k4m8/frof/).

## Seeing the status of the server

Because everything is running in containers, it's easy to see what's running on the server. Just run `docker ps`:

```bash
docker ps
```

## Conclusion

In this post, we looked at how to use Docker to run a machine learning experiment. We used Docker to create a reproducible environment, and to run the experiment on a remote server. We also used Docker to run a hyperparameter search, and to see the status of the server. This is just a small sample of what you can do with Docker. And while it may feel like there is some extra overhead to using Docker, you may discover that many of the features of containerized, isolated environments are well worth learning a powerful new tool!

---
title: Screen and Tunneling
description: How to tunnel and how to use screen
categories: blog
header-img: images/post/dino3.jpg
---

## Screen

Screen is a useful Linux tool to create multiple shell windows within a single SSH connection, and to leave them running after logging out of the SSH.

#### Some Important Screen Commands

To create a new screen:

```bash
$ screen
```

To terminate a screen:

```bash
$ exit
```

To leave a screen without terminating it:

```
`CTRL+a+d`
```

To see a list of current running screens:

```bash
$ screen -ls
```

To reconnect (re-attach) to an existing screen:

```bash
$ screen -r <SCREEN ID>
```

## Tunneling

Tunneling allows you to map a local port on the host machine (Quadcorn) to a port on your own machine (laptop). Using tunneling, we are able to run iPython Notebook on Quadcorn and access it from our laptop.

Before moving forward, choose a specific iPython Notebook port for yourself so that there is no interference with other users. 

Strong suggestion: choose the port number using the following command in `python` and using your own full name:

```python
>> sum([ord(c) for c in 'Konrad Paul Kording'])
>> 1791
```

ssh to Quadcorn with tunneling using the following command:

```bash
$ ssh <USERNAME>@<QUADCORN> -p 5000 -L 8888:localhost:<iPython Notebook PORT>
```

where `<QUADCORN>` is Quadcorn's IP address. 
  
Recommended: On Quadcorn, create a screen using the `screen` command.
  
Initiate iPython Notebook:

```bash
$ ipython notebook --no-browser --port=<iPython Notebook PORT>
```

`<iPython Notebook PORT>` is the unique port number that you created for yourself. 

Your iPython Notebook is now ready to use. Just type

```
localhost:8888
```

in your browser.

Note: If you created a screen, you can leave the screen (detach) by pressing `CTRL+a+d`.
If you logout of the machine, the tunnel will be disconneted but iPython notebook will remain running. Next time you only need to repeat the tunnel command, you don't need to initiate iPython notebook again.

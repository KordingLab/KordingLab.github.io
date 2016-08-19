---
title: Screen and Tunneling
description: How to tunnel and how to use screen
categories: blog
---

## Screen

Screen is a useful Linux tool to create multiple shell windows within a single SSH connection, and to leave them running after logging out of the SSH.

#### Some Important Screen Commands

To create a new screen:

```
$ screen
```

To terminate a screen:

```
$ exit
```

To leave a screen without terminating it:

```
`CTRL+a+d`
```

To see a list of current running screens:

```
$ screen -ls
```

To reconnect (re-attach) to an existing screen:

```
$ screen -r <SCREEN ID>
```

## Tunneling

Tunneling allows you to map a local port on the host machine (Quadcorn) to a port on your own machine (laptop). Using tunneling, we are able to run iPython Notebook on Quadcorn and access it from our laptop.

Before moving forward, choose a specific iPython Notebook port for yourself so that there is no interference with other users. 

0. Strong suggestion: choose the port number using the following command and using your own full name:

  ```
  In [1]: sum([ord(c) for c in 'Konrad Paul Kording'])
  Out[1]: 1791
  ```
  
1. ssh to Quadcorn with tunneling using the following command:

  ```
  $ ssh <USERNAME>@<QUADCORN> -p 5000 -L 8888:localhost:<iPython Notebook PORT>
  ```

  where `<QUADCORN>` is Quadcorn's IP address. 

  Recommended: On Quadcorn, create a screen using the `screen` command.

2. Initiate iPython Notebook:

  ```
  $ ipython notebook --no-browser --port=<iPython Notebook PORT>
  ```
  
  `<iPython Notebook PORT>` is the unique port number that you created for yourself. 
  
3. Your iPython Notebook is now ready to use. Just type

  ```
  localhost:8888
  ```

  in your browser.

Note: If you created a screen, you can leave the screen (detach) by pressing `CTRL+a+d`.
If you logout of the machine, the tunnel will be disconneted but iPython notebook will remain running. Next time you only need to repeat the tunnel command (Step 2), you don't need to initiate iPython notebook again.

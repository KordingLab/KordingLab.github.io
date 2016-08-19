---
title: Screen and Tunneling
description: 
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

Before moving forward, choose a specific iPython Notebook port for yourself so that there is no interference with other users. Choose the port number using the following command and using your own full name:

```
In [1]: sum([ord(c) for c in 'Konrad Paul Kording'])
Out[1]: 1791
```

Next, ssh to Quadcorn normally:

```
$ ssh <USERNAME>@<QUADCORN> -p 5000
```

where `<QUADCORN>` is Quadcorn's IP address. Now on Quadcorn, create a screen using the `screen` command, and type the following:

```
$ ipython notebook --no-browser --port=<PORT>
```

`<PORT>` is the unique port number that you created for yourself. After iPython Notebook started running, leave the screen (detach) by pressing `CTRL+a+d`, and log out of the machine.

Now ssh again into Quadcorn, but this time with tunneling using the following command:

```
$ ssh <USERNAME>@<QUADCORN> -p 5000 -L <PORT>:localhost:8888 -N
```

where you replace `<PORT>` with your specific port number.

Your iPython Notebook is now ready to use. Just type `localhost:8888` in your browser.

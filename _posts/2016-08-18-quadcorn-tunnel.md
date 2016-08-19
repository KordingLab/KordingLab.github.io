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
exit
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

### Tunneling

0. Choose your port:

```
In [1]: sum([ord(c) for c in 'Konrad Paul Kording'])
Out[1]: 1791
```

HOST = 165.124.149.97
PORT = 5000
1. ssh USERNAME@HOST -p PORT

2. 
```
$ screen
```
ipython notebook --no-browser --port=1791

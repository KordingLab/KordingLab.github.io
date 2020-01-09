---
title: Introduction to Lab Resources
categories: students
header-img: images/post/dino.jpg

---

# Introduction to Lab Resources

## Local Computational Resources

We currently have three local machines named Bleen, Dolores, and Quadcorn.

| Machine  | OS     | CPU                            | GPU                            | RAM   |
|----------|--------|--------------------------------|--------------------------------|-------|
| Dolores  | Ubuntu | i9-7920X @ 2.90 GHz - 12 cores | 3x GTX 1080 Ti, 1x RTX 2080 Ti | 94 Gb |
| Bleen    | Ubuntu | i7-6850k @ 3.60GHz - 6 cores   | 4x GTX 1080 Ti                 | 64 GB |
| Quadcorn | Mint   | i7-5960X @ 3.00GHz - 8 Cores   | 3x GTX 1080 Ti, 1x RTX 2080 Ti | 64 Gb |

### Getting Started

**Getting an account**

You can either email a senior lab member for help, or, if you know some bash, create an account yourself.
First, ask around to get the password to the admin account. Type `useradd my_username` to create
and account, then `passwd my_username` to make a password. Make sure it's a good one so we don't get hacked.
(These servers are on the web and vulnerable to password-guessing hacks.)
Finally, make sure to copy a `.profile` and `.bash_profile` file from an existing user to steal their setup (with Anaconda, etc.)

**Setting Up Anaconda**

Anaconda is a python environment manager. This allows separate users to easily have different versions of python as well as different versions of packages.
Individual users can also create separate environments if different projects have conflicting version needs.

All the servers already have a system-wide Anaconda installed. Test to make sure you are seeing it
by typing `which conda`. See which environments exist by typing `conda-env list`.

These environments are good if you need standard things (Pytorch, etc.).
If you need to install your own software, you should create an environment of your own.

[installation instructions](https://docs.anaconda.com/anaconda/install/linux/)

[creating and managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

**Useful Commands**

[See here](http://kordinglab.com/2018/09/20/bleen-quadcorn-commands.html)


### Common Issues

**Dolores**

Spontaneous restarting: A bug in intel's CPU sometimes causes Dolores to restart spontaneously when if Turbo Mode is enabled. To prevent this, run the following command everytime the machine is booted up:

    echo "1" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo

To permanently disable do the following:

Disable Turbo for i9 CPU

    Boot up machine


    Press DEL or F2 (repeatedly)  to enter the BIOS


    Enter Advanced Mode (F7)


    Navigate to Advanced  in the horizontal options bar


    Press enter on CPU Configuration


    Scroll down to the bottom and enter into CPU Power Management Configuration


    Navigate to Turbo Mode and press enter and change to Disabled


### Workflow

**Screen**

The screen function is used to manage virtual terminals that can run in the background. These virtual terminals continue to persist after you disconnect from the ssh terminal. That allows you to run long programs without needing to stay connected, as well as run jupyter notebook sessiosn that won't crash if you disconnect. [Here is a page with extensive documentation](https://www.gnu.org/software/screen/manual/screen.html).

In the screen documentation, "C-" refers to clicking "Ctrl+c". For example, the command "C-a" means "Click 'Ctrl+c' then click 'a'".

Basics of Screen:

    screen -S <name of screen>

The -S option allows you to create a new screen, and give it a name. This makes it easy to reconnect afterwards.

    C-a

C-a is the command to detatch from the screen and return to your base terminal.

    screen -r <name of screen>

The -r command allows you to reconnect to a screen with the name you have given it. To get a list of currently open and running screens, type "screen -r" without a name.

Occasionally a screen will be listed as "attached" while you are actually not connected to it. In that case use the -d command to attach to screens that for some reason remain listed as attached.

**Jupyter Notebook/Lab**

I recommend running notebook sessions within a virtual terminal from the screen function. That way if you momentarily lose connection, your session won't be closed.

To start a jupyter notebook or lab session type:

    jupyter notebook --no-browser --port=<XXXX>
or

    jupyter lab --no-browser --port=<XXXX>

where XXXX is an unused port number.  
Next on your local machine's terminal type:

    ssh -N -f -L localhost:YYYY:localhost:XXXX ribeiro@dolores.seas.upenn.edu

Use the same XXXX and above. YYYY is any port number available on your local machine.

Finally, open your browser and connect to 'localhost:YYYY'. You may be prompted to input a password, which is found on the screen in which you launched the jupyter session.

**Matlab**

### Best Practices

Please be mindful of the storage you are using, especially in the home folder. Most machines have seperate hardrives, generally under a folder named /data<X>, where you can store large datasets. Additionally, if you are finished with a project on home, it is best to move it to one of these other drives. Use the command

    df -h
to get a list of all drives and their available space.


### Miscellaneous Tips and Tricks

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

#### Getting an account

You can either email a senior lab member for help, or, if you know some bash, create an account yourself.
First, ask around to get the password to the admin account. Type `useradd my_username` to create
and account, then `passwd my_username` to make a password. Make sure it's a good one so we don't get hacked.
(These servers are on the web and vulnerable to password-guessing hacks.)
Finally, make sure to copy a `.profile` and `.bash_profile` file from an existing user to steal their setup (with Anaconda, etc.)

#### Setting Up Anaconda

Anaconda is a python environment manager. This allows separate users to easily have different versions of python as well as different versions of packages.
Individual users can also create separate environments if different projects have conflicting version needs.

All the servers already have a system-wide Anaconda installed. Test to make sure you are seeing it
by typing `which conda`. See which environments exist by typing `conda-env list`.

These environments are good if you need standard things (Pytorch, etc.).
If you need to install your own software, you should create an environment of your own.

[installation instructions](https://docs.anaconda.com/anaconda/install/linux/)

[creating and managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

### Useful commands and best-practices

#### General tips and best practices

Save results to files early and often. Write code that can "pick up where it left off."

This includes notebooks! Don't leave lots of notebooks hanging around eating up memory. Check if you have notebooks running and close them when you're done. If you need the same state later, save/load files from inside your notebook.

#### Storage

Please be mindful of the storage you are using, especially in the home folder. All servers have separate storage hardware, one small-but-fast in `/`, which includes your `/home/USERNAME` directory, and others that are big-but-slow. The big-slow storage is in `/data/` or /data2/. Use the command

    df -h

to get a list of all drives and their available space.

To see how much space you are personally using, go to your home directory and run

    cd; du -hs # the simple command
    cd; du -hs .[^.]* | sort -hr # the fancier command which includes hidden things (names prefixed with "." like "~/.conda") and sorts the results
    
This will list all of the files and subdirectories of your home directory in order of their size (`cd;` gets you to home, `du` is the "disk usage" command, `.[^.]*` is a file pattern telling it to include hidden directories, and `sort` puts things in order of size).

**Best practice** is to limit yourself to 100G of `/home`, and you should try to limit this to only one of the servers. One trick you can do is move a directory from `/home/` to `/data/` then "symlink" or "soft link" to its original location. For example, say `/home/myusername/old-project` is a big directory containing data from a project I don't need immediately. I can run

    mkdir /data/myusername/ # make sure I have my own private place to store things inside /data
    mv /home/myusername/old-project /data/ # move the entire directory (this can take a while)
    ln -s /data/myusername/old-project ~/old-project # create symbolic link
    ls -lh ~ # listing files, I should now see that "~/old-project" takes up zero space, and points to a different location in /data

**Conda clean-up**

An easy way to free up some space in your home directory is to clean up unused conda tarballs and cached files. Run the following command:

    conda clean -a
    
This can free upwards of 1-10 GB, depending on how many conda environments you have!

#### CPU/GPU usage

Before running a big job, take a look at current resource-usage using the `htop` command. This will display a live window of running processes, who owns them, memory use, CPU use, etc... Similarly, use the `nvidia-smi` command to see current load on the GPUs. If it looks like someone is hogging all of the resources, your options are

1. ask that person to scale back (after all, they ideally should have written code that can be safely stopped and restarted)
2. move your data and code to a server with more available resources
3. consult the compute czars

### Other Common Issues

**CUDA**

In Fall 2020, we upgraded to CUDA 10.2 on all machines, which solved some of the past compatibility issues. Still, these things have been known to break in strange ways. When this happens, reboot. If it still fails, reinstall CUDA and reboot.

How to reinstall CUDA, you ask? There are many ways, but here's the recommended one that has worked for us consistently: someone with admin privileges [downloads the runfile from NVIDIA](https://developer.nvidia.com/cuda-downloads). It's not a bad idea to check for `gcc` updates at this point, too. Then follow instructions on the nvidia site (usually this is just a single command like `sudo sh cuda_10.2.89_440.33.01_linux.run` with whatever `.run` file was downloaded). One recommended non-standard option in the installer is `Options > Driver > Update the system X config file`, and everything else is fine as defaults. The machine will need a reboot after this upgrade.

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

**Remote interpreter via PyCharm**

PyCharm can be configured to automagically sync files and run code on the lab machines over SSH. It provides all the features you'd expect like a GUI for interactive debugging, plotting, and a console, all while running remotely.

Recommended setup:

1. Connect to the VPN
2. Make a virtual environment on the lab server of your choice. Make a note of its path.
3. In PyCharm preferences, go to "Project > Python Interpreter" and find the button to add an interpreter. Add an SSH interpreter and follow the instructions, setting the python interpreter path to `<path/to/your/new/environment>/bin/python`)
4. Select the box that says automatically sync files. This means whenever you modify and save a file in the editor, it is immediately uploaded to the server.
5. You can configure the remote directory structure by going to "Build, Execution, Deployment > Deployment" then selecting the "Mappings" tab.

It is not completely bug-free. PyCharm gets especially confused when you open a project but the VPN is off and it can't figure out how to connect. Occasionally this leaves things in a broken state. To un-break them, you need to

1. Connect to the VPN
2. SSH to the server and remove the `~/.pycharm_helpers/` directory manually
3. Follow the instructions to rebuild things [here](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000738804-How-to-update-skeletons-remote-interpreter?page=1#community_comment_115000623624)

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

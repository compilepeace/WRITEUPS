## VORTEX2

Login to the vortex2 challenge via ssh :

```
critical@d3ad:~$ ssh vortex2@vortex.labs.overthewire.org -p 2228

                 _            
__   _____  _ __| |_ _____  __
\ \ / / _ \| '__| __/ _ \ \/ /
 \ V / (_) | |  | ||  __/>  < 
  \_/ \___/|_|   \__\___/_/\_\
                              
a http://www.overthewire.org wargame.

vortex2@vortex.labs.overthewire.org's password: 23anbT\rE
```

Source code provided :
```
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>


int main(int argc, char **argv)
{
        char *args[] = { "/bin/tar", "cf", "/tmp/ownership.$$.tar", argv[1], argv[2], argv[3] };
        execv(args[0], args);
}

```

**A TIP :** In order to break into something, we need to focus on `where` and `how` the **attacker-controlled data** `goes` and `affects` a piece of software. Also, with **attacker-controlled data** we need to touch the code places that are sensitive to software and can lead to software crash/break.

### Analysis Of Source Code

* `execv()` is invoked which replaces the parent process address space with the new process it spawns. 
* The new process it creates depends on the *args* provided to it as parameter.
*  Here, it will spawn `/bin/tar` program with `cf` flag and three parameters provided by user as command line arguments.
* The `-c` flag creates an new archive (can be file or a directory).
* The `-f` flag specifies to perform action on a *file* or *device*.
* The character `'$$'` is a *special parameter* to the shell which expands into the Process ID (PID) of the shell.

Let's focus on the attacker-controlled data - `argv[1]`, `argv[2]` and `argv[3]`.
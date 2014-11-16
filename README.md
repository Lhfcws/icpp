# Easy C/C++ Interpreter (icpp)

> author: Lhfcws Wu (宸风)  
> version: 0.0.2  
> create-time: 2013-07-15  


#### v0.0.2 Change log:
+ Divided into C++ language mode(default) and C language mode.
+ Main Wrapper mode added.  
    > #main  
    > cout << "These codes are directly runnable." << endl;  
    > #r  


###

First day of my formal internship is so free and boring, and I have to learn C-language deeply. So I wrote this simple interpreter in the afternoon.  
This is not a compiler, it is just a interpreter shell of gcc/g++.  

## Installation
I haven't add python setup utils into the project, so just `python icpp.py` in the scripts.  
Or if you want a better experience, add the following alias in `~/.profile`:  

    alias icpp='python /path/to/icpp.py'
    source ~/.profile

Then you can use `icpp` in anywhere in your shell.

**Read `help.md` to learn how to use `icpp`.**

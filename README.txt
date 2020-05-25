Unixify is a command line utility to rename all files and directories in a
directory tree in compliance with Unix/Linux naming conventions. 

Unixify will rename files and directories to comply with the following rules:
    1) No special characters will be allowed other than period, hyphen,
        and underscore.
    2) Spaces in filenames will be converted to underscores.
    3) Filenames will not be permitted to start with a hyphen.

The script requires a directory name as an argument. 
Invoke the script as follows:

$ python3 unixify.py [dir_name]

where dir_name is the name of the directory you want to process.

This utility should be concidered beta: use at your own risk. I have tested 
it on some fairly simple directory trees and it works as advertised.
However, please note the following:

    0) I'm not a professional and this is a learning project for me.

    1) At this time there is no error checking of any kind (It's comming.)

    2) At this time the script does not check to ensure it is not creating 
        duplicate file names. If your directory contains similar files like:
        'foo_bar' and 'foo bar', or 'spam-and-eggs' and 'spam%and@eggs'
        you're probably going to have a bad time. 
        (Checking for this behavior is comming.)



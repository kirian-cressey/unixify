import sys, os


def space_to_underscore(string):
    """Takes a string and returns a new string with all whitespace converted
        to underscores."""
    # Return this string
    new_string = ''

    for i in string:
        if i.isspace():
            new_string += '_'
        else:
            new_string += i

    return new_string


def special_to_dash(string):
    """Takes a string and returns a new string with non-period special
        charecters converted to hyphens."""
    # note: this is seperated from space_to_dash() because I would like to
    # add optional command line arguments in the future to choose not to 
    # convert special charecters. There may be situations where this could be
    # useful. Not sure. Will look into this and refactor if I see no use.

    new_string = ''

    for i in string:
        # We will permit only numbers, letters, and these characters:
        # (Note: spaces permitted because that's for space_to_underscore()) 
        permited_chars = ['.', '-', '_', ' ']

        if not i.isalnum() and not i in permited_chars:
            new_string += '-'
        else:
            new_string += i

    # File names should not start with a hyphen
    if new_string[0] == '-':
        new_string = '_' + new_string[1:]

    return new_string


def rename(targ_dir):
    """Changes the name of all files and directories in targ_dir to comply
    with Unix/Linux naming best practices by calling space_to_underscore()
    and special_to_dash() on all items in targ_dir."""

    for fname in os.listdir(targ_dir):
        new_name = special_to_dash(fname)
        new_name = space_to_underscore(new_name)

        old_path = os.path.join(targ_dir, fname)
        new_path = os.path.join(targ_dir, new_name)

        os.rename(old_path, new_path)


def walk(targ_dir):
    # Change all file and directory names to conform with Unix best practices
    rename(targ_dir)

    # Now get ready to take a walk
    directories= []

    # Make a list of all directories and a list of all files in target dir
    for item in os.listdir(targ_dir):
        path = os.path.join(targ_dir, item)

        if os.path.isdir(path):
            directories.append(path)

    print("directories: {}".format(directories))

    for directory in directories:
        walk(directory)


if __name__ == '__main__':

    directory = sys.argv[1]
    warning = """You are about to rename all files and directories in {}
and rename all files and directories contained therein.
This operation cannot be undone.
Please enter 'yes' if you have checked the directory path
and are absolutely sure.""".format(directory)

    print(warning)
    response = input("\nContinue?\n>>> ").lower()

    if response == 'y' or response == 'yes':
        walk(directory)
    else:
        sys.exit()

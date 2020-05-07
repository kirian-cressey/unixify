def space_to_dash(string):
    """Takes a string and returns a new string with all whitespace converted
        to hyphens."""
    # Return this string
    new_string = ''

    for i in string:
        if i.isspace():
            new_string += '-'
        else:
            new_string += i

    return new_string

def special_to_dash(string):
    """Takes a string and returns a new string with non-period special
        charecters converted to hyphens."""
    # note: this is seperated from space_to_dash() because I would like to
    # add optional command line arguments in the future to choose not to 
    # convert special charecters. There are situations where this could be
    # useful.

    new_string = ''

    for i in string:
        # If i is not a number, letter, or period, convert i to hyphen
        if not i.isalnum() and i != '.':
            new_string += '-'
        else:
            new_string += i

    return new_string

# These strings are being used for testing/debugging during development
symbols = "~`!@#$%^&*()_-+={[}]|:;'<,>.?/"
test = "I am a h!ppomoutham*u$."
unenthused_world = "Hello, World."

def space_to_dash(string):
    
    # Return this string
    new_string = ''

    for i in string:
        if i.isspace(): 
            new_string += '-'
        else:
            new_string += i
    
    return new_string

test = "I am a hippomouthamous."

print(space_to_dash(test))

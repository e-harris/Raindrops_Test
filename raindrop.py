

# creating the function

def raindrop(number):

    # checking to see if the number is divisible by 7
    if number % 7 == 0:
        # if the number is divisible by 7, 'plong' will be returned
        return ('plong')

    # checking to see if the number is divisible by 5
    elif number % 5 == 0:
        # if the number is divisible by 5, 'plang' will be returned
        return ('plang')

    # checking to see if the number is divisible by 3
    elif number % 3 == 0:
        # if the number is divisible by 3, 'pling' will be returned
        return ('pling')
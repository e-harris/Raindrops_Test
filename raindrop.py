

# creating the function

def raindrop(number):

    # checking to see if the number is divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        # if the number is divisible by 3 and 5, 'PlingPlang' will be returned
        return ('PlingPlang')

    # checking to see if the number is divisible by 7
    elif number % 7 == 0:
        # if the number is divisible by 7, 'Plong' will be returned
        return ('Plong')

    # checking to see if the number is divisible by 5
    elif number % 5 == 0:
        # if the number is divisible by 5, 'Plang' will be returned
        return ('Plang')

    # checking to see if the number is divisible by 3
    elif number % 3 == 0:
        # if the number is divisible by 3, 'Pling' will be returned
        return ('Pling')

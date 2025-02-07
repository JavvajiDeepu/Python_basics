def interact():
    while true:
        try:
            user_input = int(input('Please input an integer: '))
        except ValueError:
            print('Pleas einput intagers only: ')
        else:
            print('{} is {}.' .format(user_input, 'even' if user_input % 2==0 else 'add') )
        finally:
            user_input = input('Do you want to play again ? (Y/N):')
            if user_input != 'Y':
                print('Good Bye.')
                break

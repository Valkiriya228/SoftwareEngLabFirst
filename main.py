def main():
    print('Welcome! Here you can translate numbers from different systems (temperature, length)\n'
          'If you want to quit the program, enter Q\n')
    while True:
        choose_conv = (input('Please, select by what criterion the conversion will be carried out '
                             '- Temperature (1) or Length (2) or Exit(Q) -------> '))
        # Convert temperature
        if choose_conv == '1':
            while True:
                choose_temp = input('Choose: 1.Celsius -> Fahrenheit 2.Celsius -> Kelvin ------> ')
                if choose_temp == '1':
                    value_temperature = float(input('Choose: 1.Celsius -> Fahrenheit 2.Celsius -> Kelvin ------> '))
                    print(f'{value_temperature} degrees Celsius = {round(((9 / 5) * value_temperature + 32), 2)} '
                          f'degrees Fahrenheit')
                elif choose_temp == '2':
                    value_temperature = float(input('How many degrees Celsius?: '))
                    print(f'{value_temperature} degrees Celsius = {round((value_temperature + 273.15), 2)} '
                          f'degrees Kelvin')
                else:
                    print('Incorrect entry. Please try again.')
                    continue
                break

        # Convert length
        elif choose_conv == '2':
            while True:
                choose_type_len = input('Choose: 1.Kilometers -> Miles 2.Meters -> Yards 3.Meters -> Feet 4.'
                                        'Centimeters -> Inches -------> ')
                if choose_type_len == '1':
                    value_of_len = float(input('How many kilometers?: '))
                    print(f'{value_of_len} kilometers = {round((value_of_len * 1.60934), 2)} miles')
                elif choose_type_len == '2':
                    value_of_len = float(input('How many meters?: '))
                    print(f'{value_of_len} meters = {round((value_of_len * 1.09361), 2)} yards')
                elif choose_type_len == '3':
                    value_of_len = float(input('How many meters?: '))
                    print(f'{value_of_len} meters = {round((value_of_len / 0.3048), 2)} feet')
                elif choose_type_len == '4':
                    value_of_len = float(input('How many centimeters?: '))
                    print(f'{value_of_len} centimeters = {round((value_of_len * 2.5400013716), 2)} inches')
                else:
                    print('Incorrect entry. Please try again.')
                    continue
                break
        elif choose_conv == 'Q':
            print('All the best! :)')
            quit(0)
        else:
            print('Incorrect entry. Please try again.')
            continue


if __name__ == '__main__':
    main()

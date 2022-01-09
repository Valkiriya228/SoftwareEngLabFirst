import main


def run_test(input_data):
    output = []

    def _input(item):
        output.append(item)
        return input_data.pop(0)

    main.input = _input
    main.print = lambda item: output.append(item)
    main.main()
    return output


def test_1():

    output = run_test(['1', '', '1', '0', 'Q'])
    print(output)
    assert output[1] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[2] == 'Choose: 1.Celsius -> Fahrenheit 2.Celsius -> Kelvin ------> '
    assert output[3] == 'Incorrect entry. Please try again.'
    assert output[4] == 'Choose: 1.Celsius -> Fahrenheit 2.Celsius -> Kelvin ------> '
    assert output[5] == 'Choose: 1.Celsius -> Fahrenheit 2.Celsius -> Kelvin ------> '
    assert output[6] == '0.0 degrees Celsius = 32.0 degrees Fahrenheit'
    assert output[7] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[8] == 'All the best! :)'


def test_2():

    output = run_test(['', 'Q'])

    assert output[1] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[2] == 'Incorrect entry. Please try again.'
    assert output[3] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[4] == 'All the best! :)'


def test_3():

    output = run_test(['2', '1', '10', 'Q'])

    assert output[1] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[2] == 'Choose: 1.Kilometers -> Miles 2.Meters -> Yards 3.Meters -> Feet 4.Centimeters -> Inches ' \
                        '-------> '
    assert output[3] == 'How many kilometers?: '
    assert output[4] == '10.0 kilometers = 16.09 miles'
    assert output[5] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or Length (2) or Exit(Q) -------> '
    assert output[6] == 'All the best! :)'


def test_4():
    output = run_test(['ab', 'Q'])

    assert output[1] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[2] == 'Incorrect entry. Please try again.'
    assert output[3] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[4] == 'All the best! :)'


def test_5():
    output = run_test(['2', '2', '100', 'Q'])

    assert output[1] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[2] == 'Choose: 1.Kilometers -> Miles 2.Meters -> Yards 3.Meters -> Feet 4.Centimeters -> Inches ' \
                        '-------> '
    assert output[3] == 'How many meters?: '
    assert output[4] == '100.0 meters = 109.36 yards'
    assert output[5] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[6] == 'All the best! :)'


def test_6():
    output = run_test(['Q'])

    assert output[1] == 'Please, select by what criterion the conversion will be carried out - Temperature (1) or ' \
                        'Length (2) or Exit(Q) -------> '
    assert output[2] == 'All the best! :)'

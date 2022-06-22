market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)

# When either of the dictionaries are used as arguments, neither of the values will change
# to red, which can cause the imaginary cars to crash. The assertion added to the function
# returns an error if none of the values in the dictionary change to red. This is useful in
# the case of having a long program that uses this function. This way, the error returned by
# the assertion can inform on precisely what the problem is.

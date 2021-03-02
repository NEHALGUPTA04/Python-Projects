
def convert(CELCIUS) :
    CELCIUS = float(CELCIUS)
    FERHENHEIT  = (CELCIUS * 9/5) + 32
    KELVIN = (273.15 + CELCIUS)
    return FERHENHEIT,KELVIN

print(convert(2))

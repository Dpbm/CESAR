from distutils.log import error


def checkInteger(value):
    if(not value.isnumeric()):
        return 0

    try:
        integer_value = int(value)

        if(integer_value < 0):
            raise 'less than 0 value'

        return integer_value

    except Exception:
        return 0

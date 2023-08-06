"""
2022, March 12
"""

import importlib_resources as ir
import json


# Load JSON files in dictionaries for fast access
# see https://importlib-resources.readthedocs.io/en/latest/using.html
def getdict(filename):
    source = ir.files('stringunitconverter').joinpath(filename)
    with ir.as_file(source) as filepath:
        with open(filepath, 'r') as f:
            a = json.load(f)
    return a


prefixes = getdict('prefixes.json')
units = getdict('units.json')
#print('units:', units)
#pau = {**prefixes, **units}

operators_and_brackets = frozenset(('*', '/', '^', '-', '+', '(', ')', ' ',
                                    '.'))
digits = frozenset(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
nonunits = operators_and_brackets.union(digits)


def multiplier(a, b):
    """
    :param a: input unit (string)
    :param b: output unit (string)
    :return: multiplier (float)
    """
    return get_factor(a) / get_factor(b)


def get_factor(a):
    #print('get_factor')
    """
    :param a: input unit (string)
    :return: multiplier (float)
    """
    # Replace each hat with two asterisks
    for i in range(len(a)-1, -1, -1):
        if a[i] == '^':
            a = a[:i] + '**' + a[i+1:]

    # Replace every unit-with-prefix with its appropriate multiplier
    #print('a:', a)
    k = len(a) - 1
    while i > -1:
        while k > -1 and a[k] in nonunits:
            k -= 1
        i = k
        while i > -1 and a[i] not in nonunits:
            #print('  i:', i, ', a[i]:', a[i])
            i -= 1
        #print(' i:', i)
        if k > i:
            detected_unit = a[i+1:k+1]
            #print(' det unit:', detected_unit)
            a = a[:i+1] + unit_to_factor_string(detected_unit) + a[k+1:]
            #print('  a:', a)
            k = i
            # Replace ' ' with '*' if space between two units
            #print('i:', i)
            #print('a:', a)
            if i > 0 and a[i] == ' ' and a[i-1] not in operators_and_brackets:
                a = a[:i] + '*' + a[i+1:]
    #print(' a:', a)
    # Evaluate string
    a = eval(a)
    return a


def unit_to_factor_string(a):
    #print('unit_to_factor_string')
    #print(' a:', a)
    # get unit w/o prefix
    for i in range(1, len(a)+1):
        c = a[-i:]
        #print(' c:', c)
        #print(' i:', i)
        if c in units:
            # get prefix
            for k in range(1, len(a)+2-i):
                #print(' k:', k)
                d = a[-i-k:-i]
                #print(' d:', d)
                if d in prefixes:
                    #print(' d:', d)
                    factor_string = '(' + prefixes[d] + "*" + units[c] + ')'
                    string_remaining = a[:-i-k]
                    if string_remaining:
                        #print('string remaining (1):', string_remaining)
                        return '(' + unit_to_factor_string(string_remaining) + '*' + factor_string + ')'
                else:
                    factor_string = '(' + '1' + "*" + units[c] + ')'
                    string_remaining = a[:-i]
                if string_remaining:
                    #print('string remaining (2):', string_remaining)
                    return '(' + unit_to_factor_string(string_remaining) + '*' + factor_string + ')'
                else:
                    return factor_string
    print('Failed to decode string: <' + a + '>')


if __name__ == '__main__':
    import testing as t
    #print('Main')

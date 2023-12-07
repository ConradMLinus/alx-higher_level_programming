#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return (0)
    else:
        units = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['M', 'MM', 'MMM']
        roman = units.copy()
        for x in tens:
            roman.append(x)
            for i in units:
                roman.append(x + i)

        roman2 = roman.copy()
        for c in hundreds:
            roman2.append(c)
            for x in roman:
                roman2.append(c + x)

        roman3 = roman2.copy()
        for m in thousands:
            roman3.append(m)
            for c in roman2:
                roman3.append(m + c)

        dict_list = []
        for i, j in zip(roman3, list(range(1, len(roman3) + 1))):
            dict_list.append((i, j))
        num_dict = dict(dict_list)

        return(int(num_dict[roman_string]))

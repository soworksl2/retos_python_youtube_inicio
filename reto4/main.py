# 65,780
# ciento sesenta y cinco mil seteciento ochenta

my_input = [
    5992,
    4211,
    4400,
    683,
    2435,
    3801,
    9233,
    1105,
    3851,
    165,
    8868
]

HUNDRED_TABLE = [
    (' ', ' '),
    ('cien ', 'ciento '),
    ('dosciento ', 'dosciento '),
    ('tresciento ', 'tresciento '),
    ('cuatrociento ', 'cuatrociento '),
    ('quiniento ', ' quiniento '),
    ('seisiento ', 'seisiento '),
    ('seteciento ', 'seteciento '),
    ('ochosiento ', 'ochosiento '),
    ('noveciento ', 'noveciento '),
]

TEN_TABLE = [
    (' ', ' '),
    ('Diez ', 'dieci'),
    ('veinte ', 'veinti '),
    ('treinta ', 'treinta y '),
    ('cuarenta ', 'cuarenta y '),
    ('cincuenta ', 'cincuenta y '),
    ('sesenta ', 'sesenta y '),
    ('setenta ', 'setenta y '),
    ('ochenta ', 'ochenta y '),
    ('noventa ', 'noventa y '),
]

UNIT_TABLE = [
    'cero',
    'uno',
    'dos',
    'tres',
    'cuatro',
    'cinco',
    'seis',
    'siete',
    'ocho',
    'nueve'
]


def split_number_by_millars(digit_str: str) -> list[str]:
    output = []
    digit_str_len = len(digit_str)
    while digit_str_len > 0:
        if digit_str_len > 3:
            start = digit_str_len - 3
            pack = digit_str[start:]
            digit_str = digit_str[:start]
            digit_str_len = len(digit_str)
            output.append(pack)
        else:
            output.append(digit_str)
            output.reverse()
            return output

def check_is_base(number: str, i) -> bool:
    l: int = len(number)
    if i >= l:
        return True

    while i < l:
        if number[i] != '0':
            return False
        i+=1
    return True

def hundred2text(d: str, is_base: bool) -> str:
    d_i: int = int(d)
    is_base_index = 0 if is_base else 1
    return HUNDRED_TABLE[d_i][is_base_index]

def ten2text(d: str, is_base: bool, unit: str) -> str:
    d_i: int = int(d)
    unit: int = int(unit)
    
    if d_i == 1:
        if unit == 1:
            return 'once'
        elif unit == 2:
            return 'doce'
        elif unit == 3:
            return 'trece'
        elif unit == 4:
            return 'catorce'
        elif unit == 5:
            return 'quince'

    is_base_index = 0 if is_base else 1
    return TEN_TABLE[d_i][is_base_index]

def unit2text(d: str, ten: str) -> str:
    d_i: int = int(d)

    if ten == '1':
        if d_i == 1:
            return ''
        elif d_i == 2:
            return ''
        elif d_i == 3:
            return ''
        elif d_i == 4:
            return ''
        elif d_i == 5:
            return ''

    return UNIT_TABLE[d_i]

# 0 = unidad
# 1 = decena
# 2 = centena
def number_group_to_text(number: str, group_level: int) -> str:
    output: str = ''
    number_len: int = len(number)

    for i, d in enumerate(number):
        ntype: int = number_len - 1 - i
        is_base: bool = check_is_base(number, i)

        if ntype == 0:
            ten: str = number[i-1] if number_len >= 2 else None
            output += unit2text(d, ten)
        elif ntype == 1:
            output += ten2text(d, is_base, number[i + 1])
        elif ntype == 2:
            output += hundred2text(d, is_base)

        if is_base:
            break

    if group_level == 1:
        output += ' mil '

    return output

def number2text(digit: int) -> str:
    output = ''
    digit_str: str = str(digit) 
    number_millars_group = split_number_by_millars(digit_str)
    nmg_len: int = len(number_millars_group)

    for i, g in enumerate(number_millars_group):
        group_level = nmg_len - 1 - i
        output += number_group_to_text(g, group_level)
    return output

for i in my_input:
    print(number2text(i))

file = open('text.txt', 'r')
content = file.read()
file.close()

vowel_a = ['a', 'A', 'á', 'Á']
vowel_e = ['e', 'é', 'E', 'É']
vowel_i = ['i', 'í', 'I', 'Í']
vowel_o = ['o', 'ó', 'O', 'Ó']
vowel_u = ['u', 'ú', 'U', 'Ú']

counter_a = 0
counter_e = 0
counter_i = 0
counter_o = 0
counter_u = 0

for c in content:
    if c in vowel_a:
        counter_a += 1
        continue
    elif c in vowel_e:
        counter_e += 1
    elif c in vowel_i:
        counter_i += 1
    elif c in vowel_o:
        counter_o += 1
    elif c in vowel_u:
        counter_u += 1

print(f'el texto contiene {counter_a} a')
print(f'el texto contiene {counter_e} e')
print(f'el texto contiene {counter_i} i')
print(f'el texto contiene {counter_o} o')
print(f'el texto contiene {counter_u} u')

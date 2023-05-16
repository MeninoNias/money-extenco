from num2words import num2words


def number_to_long_number(number_p):
    number_p = '{:.2f}'.format(number_p)
    if number_p.find('.') != -1:
        number_p = number_p.split('.')
        number_p2 = int(number_p[1])
        number_p = int(number_p[0])
    else:
        number_p2 = 0

    if number_p == 1:
        aux1 = ' real'
    else:
        aux1 = ' reais'

    if number_p2 == 1:
        aux2 = ' centavo'
    else:
        aux2 = ' centavos'

    text1 = ''

    if number_p > 0:
        text1 = num2words(number_p, lang='pt_BR') + str(aux1)
    else:
        text1 = ''

    if number_p2 > 0:
        text2 = num2words(number_p2, lang='pt_BR') + str(aux2)
    else:
        text2 = ''

    result = text1 + ' e ' + text2

    return result

name_in = input("Nome do arquivo de texto (entrada): ")
name_out = input("Nome do arquivo de texto (saida): ")

with open(name_in, encoding='utf8') as f:
    data = []
    while True:
        line = f.readline()
        if not line:
            break
        
        line = line[2:].strip()
        line = line.replace('.', '')
        line = line.replace(',', '.')
        line = number_to_long_number(float(line))
        data.append(line)

with open(name_out, 'w') as f:
    for d in data:
        f.write(d)
        f.write('\n')

print('finalizado')
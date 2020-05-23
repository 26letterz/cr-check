#poly = input()
transmit = '10100101110110000110100111'
corrected = transmit + '00000'
print('Стартовый полином: ', corrected)
g = '111011'
table = {}
reverse_table = {}
def div(poly):
    chast = ""
    curr = 5
    i = 0
    while poly[i] != '1':
        i += 1
    poly = poly[i:]  # поправка на нули в начале
    temp = poly[:6]  # первая шестерка
    print('Первая шестерка:', temp)
    while True:
        for k in range(6):
            if temp[k] == g[k]:
                chast += '0'
            else:
                chast += '1'
        #print('Начальный остаток: ', chast)
        m = 0
        for f in range(len(chast)):  #поправка на нули вначале
            if chast[f] == '0':
                m+=1
            else:
                break
        #print(m)
        chast = chast[m:]
        if (len(poly)-1 - curr < m):
            #print('Corrected chast: ', chast)
            if curr == len(poly) - 1:
                extra = ""
                for t in range(5-len(chast)):
                    extra += '0'
                chast = extra + chast
                #print('front')
            else:
                #print('back')
                chast += poly[curr+1:]
                if len(chast) < 5:
                    extra = ""
                    for i in range(5 - len(chast)):
                        extra += "0"
                    chast = extra + chast
                elif len(chast) > 5:
                    rem = len(chast) - 5
                    chast = chast[rem:]
            print('Финальный остаток: ', chast)
            break
        else:
            #print('Corrected chast: ', chast)
            for t in range(m):
                chast += poly[curr+1+t]
            curr += m
            #print('Остаток + сносим: ', chast)
            temp = chast
            chast = ""

    print('Кодировка: ', chast)
    return chast

leftover = div(corrected)
newmsg = transmit + leftover
print('\nЗакодированное:',newmsg,'\n\n')

for i in range(31):
    if newmsg[i] == '0':
        spoil = '1'
    else:
        spoil = '0'
    spoiled = newmsg[:i] + spoil + newmsg[i+1:]
    print("C испорченным разрядом:", spoiled)
    print("FOR ", 30-i, " POSITION ERROR IS ", div(spoiled))
    table[30-i] = div(spoiled)

print('\n\n', table, '\n')
for key in table.keys():
    reverse_table[table[key]] = key

print(reverse_table, '\n\n')
print('CORRECT MESSAGE: ', newmsg)

i = 13
if newmsg[i] == '0':
    spoil = '1'
else:
    spoil = '0'
spoiled = newmsg[:i] + spoil + newmsg[i+1:]
print(reverse_table[div(spoiled)])
print("Ошибка в позиции (справа налево): ", reverse_table[div(spoiled)], ", ошибка в позиции (слева направo): ", 30 - reverse_table[div(spoiled)])
ind = 30 - reverse_table[div(spoiled)]
if spoiled[ind] == '0':
    cor = '1'
else:
    cor = '0'
spoiled = spoiled[:ind] + cor + newmsg[ind+1:]

print('\nСРАВНЕНИЕ ИСПРАВЛЕННОГО И ОРИГИНАЛЬНОГО:')
print(newmsg)
print(spoiled)

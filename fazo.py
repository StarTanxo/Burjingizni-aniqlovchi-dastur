if moon[1].lower() == 'yanvar' and 21 <= int(moon[0]) < 32 or moon[1].lower() == 'fevral' and 21 > int(moon[0]) > 0:
    print('Qovga')
elif moon[1].lower() == 'fevral' and 21 <= int(moon[0]) < 29 or moon[1].lower() == 'mart' and 0 < int(moon[0]) <= 21:
    print('Baliq')
elif moon[1].lower() == 'mart' and 21 <= int(moon[0]) < 32 or moon[1].lower() == 'aprel' and 0 < int(moon[0]) <= 21:
    print('Qoy')
elif moon[1].lower() == 'aprel' and 21 <= int(moon[0]) < 32 or moon[1].lower() == 'may' and 0 < int(moon[0]) <= 21:
    print('Buzoq')
elif moon[1].lower() == 'may' and 21 <= int(moon[0]) < 32 or moon[1].lower() == 'iyun' and 0 < int(moon[0]) <= 21:
    print('Egizaklar')
elif moon[1].lower() == 'iyun' and 22 <= int(moon[0]) < 32 or moon[1].lower() == 'iyul' and 0 < int(moon[0]) <= 22:
    print('Qisqichbaqa')
elif moon[1].lower() == 'iyul' and 23 <= int(moon[0]) < 32 or moon[1].lower() == 'avgust' and 0 < int(moon[0]) <= 23:
    print('arslon')
elif moon[1].lower() == 'avgust' and 24 <= int(moon[0]) < 32 or moon[1].lower() == 'sentyabir' and 0 < int(moon[0]) <= 23:
    print('Sunbula')
elif moon[1].lower() == 'sentyabir' and 24 <= int(moon[0]) < 32 or moon[1].lower() == 'oktyabir' and 0 < int(moon[0]) <= 23:
    print('Tarozi')
elif moon[1].lower() == 'oktyabir' and 24 <= int(moon[0]) < 32 or moon[1].lower() == 'noyabir' and 0 < int(moon[0]) <= 22:
    print('Chayon')
elif moon[1].lower() == 'noyabir' and 23 <= int(moon[0]) < 32 or moon[1].lower() == 'dekabir' and 0 < int(moon[0]) <= 21:
    print('Qavs')
elif moon[1].lower() == 'oktyabir' and 22 <= int(moon[0]) < 32 or moon[1].lower() == 'yanvar' and 0 < int(moon[0]) <= 20:
    print('togechkisi')
else:
    print('Xatolik\nBoshqatdan kiritib kuring!')

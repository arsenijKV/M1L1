while True:
    print('Здраствуйте✋, это програма поможет разобрать сленг')
    meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ": "Что-то очень смешное",
                'РАК': 'Тот кто плохо играет',
                'РОФЛ': 'шутка',
                'КД': 'как дела',
                'АГРИТЬСЯ': ' злиться',
                'ЗАТАЩИЛ': 'выйграл',
                'ОНЛИ': 'только'
                }
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        yess = input('Хотите закончить?: ')
        if yess == 'да' or yess == 'Да':
            break
        else:
            print('продолжаем')
        
    else:
        print('такого слова нет, будет в следущем обновление')
        yess = input('Хотите закончить?: ')
        if yess == 'да' or yess == 'Да':
            break
        else:
            print('продолжаем')

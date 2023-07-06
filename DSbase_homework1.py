import pandas as pd
Kola = ['Да','Нет','Нет','Нет','Да']
Dasha = ['Нет','Нет','Да','Нет','Да']
Petya = ['Нет','Нет','Нет','Да','Нет']
Masha = ['Нет','Да','Нет','Нет','Нет']
Denis = ['Нет','Нет','Нет','Нет','Нет']
Sport = ['Футбол','Волейбол','Легкая атлетика','Киберспорт','Фитнес']
Names = ['Коля','Даша','Петя','Маша','Денис']
df = pd.DataFrame(
    [Kola,Dasha,Petya, Masha,Denis],
    columns=['A','B','C','D','E'],
    index=Names
)
for i in df.keys():
    df[i] = df[i].map({'Да':1,"Нет":0})
print(df)
print()
Height = {'A':176,'B':188,'C':173,'D':171,'E':169}

def set_height(row):
    answer = 0
    count_sport = 0
    for i in row.keys():
        if row[i] == 1:
            answer += Height[i]
            count_sport += 1
    return 170 if answer == 0 else answer//count_sport

df['Рост'] = df.apply(set_height,axis=1)
print(df)

for i in df.index:
    if df['Рост'][i] > 180:
        print(i + ' выше 180 см, его (её) рост: ' + str(df['Рост'][i]))
    else:
        print(i + ' не выше 180 см, его (её) рост: ' + str(df['Рост'][i]))

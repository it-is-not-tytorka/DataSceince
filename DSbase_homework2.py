import pandas as pd
df = pd.read_csv('kindergarten_dataset__w0di.csv',index_col=0)
print(df.info())

# Задание 1 completed
df = df.drop(df[df['Возраст'].isna()].index)
print(df.info())

# Задание 2 completed
df = df.drop(df[df['Возраст_папы'] == 0].index)
df = df.drop(df[df['Возраст_мамы'] == 0].index)
print(df.describe())

# Задание 3 completed
df = df.drop(df[df['Возраст_папы'] <= df['Возраст']].index)
df = df.drop(df[df['Возраст_мамы'] <= df['Возраст']].index)
print(df.describe())

# Задание 4 completed
df = df.drop(df[df['Возраст_папы'] > 200].index)
df = df.drop(df[df['Возраст_мамы'] > 200].index)
print(df.describe())

# Задание 5 completed
print(df['Ходит_в_детский_сад'].unique()) # читаем, какие варианты ответов могут быть
df['Ходит_в_детский_сад'] = df['Ходит_в_детский_сад'].map({'да' : 1, 'нет' : 0})
print(df['Ходит_в_детский_сад'].unique()) # убедились, что все заменено на 1 или 0
df.to_csv('kindergiden_dataset_clean.csv')
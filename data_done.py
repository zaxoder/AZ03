import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('divan.csv')

def convert_rub_to_number(value):
    if isinstance(value, str):
        value = value.replace(' руб.', '').replace('руб.', '').replace(' ', '')
        return float(value)
    return value


for column in df.columns:
    df[column] = df[column].apply(convert_rub_to_number)


df.to_csv('divan_processed.csv', index=False)

average_price = df['Цена'].mean()
print(f"Средняя цена: {average_price}")

prices = df['Цена']

plt.hist(prices, bins=10, edgecolor='black')

plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')

plt.show()
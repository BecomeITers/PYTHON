import pandas as pd
df = pd.read_csv("D:\\Pandas\\Bài 3\\u.user", delimiter="|")
tb = df.groupby('occupation')['age'].mean()
print(tb)
print("-------------------------------------------------")
sort_age = df.sort_values('age', ascending=False)
print(sort_age)
print("-------------------------------------------------")
max_age = df.loc[df['age'].max()]
min_age = df.loc[df['age'].min()]
print(max_age)
print(min_age)
print("-------------------------------------------------")
average_age = df.groupby(['occupation', 'gender'])['age'].mean()
print(average_age)
print("-------------------------------------------------")
percentage = df['gender'].value_counts(normalize=True) * 100
# Hàm ở trên sẽ tính %
print(percentage)
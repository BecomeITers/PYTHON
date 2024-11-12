import pandas as pd
df = pd.read_csv("D:\\Pandas\\Bài 5\\wind.data.txt", delimiter=" ")
df['Yr_Mo_Dy'] = df['Yr'].astype(str) + '-' + df['Mo'].astype(str).str.zfill(2) + '-' + df['Dy'].astype(str).str.zfill(2)
print(df[['Yr_Mo_Dy']])
print("---------------------------------------------------------")
tm = df.set_index('Yr_Mo_Dy', inplace=True)
print(tm)
print("---------------------------------------------------------")
missing_values = df.loc[:, 'RPT':'MAL'].isnull().sum()
available_values = df.loc[:, 'RPT':'MAL'].count()
print("Missing values per column:")
print(missing_values)
print("\nAvailable values per column:")
print(available_values)
print("---------------------------------------------------------")
average_wind_speed = df.loc[:, 'RPT':'MAL'].mean().mean()
print("Average wind speed for all data:", average_wind_speed)
print("---------------------------------------------------------")
loc_stats = pd.DataFrame({
    'min': df.loc[:, 'RPT':'MAL'].min(),
    'max': df.loc[:, 'RPT':'MAL'].max(),
    'mean': df.loc[:, 'RPT':'MAL'].mean(),
    'std': df.loc[:, 'RPT':'MAL'].std()
})
print("Location statistics (min, max, mean, std):")
print(loc_stats)
print("---------------------------------------------------------")
df['month'] = pd.to_datetime(df['Yr_Mo_Dy']).dt.month
print("---------------------------------------------------------")
january_avg = df[df['month'] == 1].loc[:, 'RPT':'MAL'].mean()
print("Average wind speed in January at each location:")
print(january_avg)
# Thêm các cột `year`, `month`, `week`
df['year'] = pd.to_datetime(df['Yr_Mo_Dy']).dt.year
df['month'] = pd.to_datetime(df['Yr_Mo_Dy']).dt.month
df['week'] = pd.to_datetime(df['Yr_Mo_Dy']).dt.isocalendar().week

# Thống kê theo năm
yearly_stats = df.groupby('year').mean().loc[:, 'RPT':'MAL']
print("Yearly statistics:")
print(yearly_stats)

# Thống kê theo tháng-năm
monthly_stats = df.groupby(['year', 'month']).mean().loc[:, 'RPT':'MAL']
print("\nMonthly-Yearly statistics:")
print(monthly_stats)

# Thống kê theo tuần-tháng-năm
weekly_stats = df.groupby(['year', 'month', 'week']).mean().loc[:, 'RPT':'MAL']
print("\nWeekly-Monthly-Yearly statistics:")
print(weekly_stats)

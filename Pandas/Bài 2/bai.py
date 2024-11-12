import pandas as pd
df = pd.read_csv("D:\\Pandas\\Bài 2\\chipotle.tsv.txt", delimiter="\t")
df['item_price'] = df['item_price'].replace('[\$,]', '', regex=True).astype(float)
# Hàm replace đó là để loại bỏ ký hiệu $
fill = df[df['item_price'] > 10]
print(fill)
print("-------------------------------------------------")
sort = df.sort_values('item_name', ascending=True)
print(sort)
print("-------------------------------------------------") 
max_price = df.loc[df['item_price'].idxmax()]
# Hàm loc là lấy toàn bộ chỉ số của item_price và idmax là lấy chỉ số lớn nhất
print(max_price)
print("-------------------------------------------------") 
veggie_orders = df[df['item_name'] == "Veggie Salad Bowl"]
count = veggie_orders['order_id'].nunique()
# Hàm nunique là dùng để đếm số hàng duy nhất của veggie_order
quantities = veggie_orders['quantity'].sum()
print(count, quantities)
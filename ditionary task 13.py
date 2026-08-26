
def Highestprice_items(data):
    max_price=max(data.values())
    for item,price in data.items():
        if price==max_price:
          print(item)

items={
   "moong dal":150,
   "Urad dal":200,
   "Almond":1000
   }
Highestprice_items(items)

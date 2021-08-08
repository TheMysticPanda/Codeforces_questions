waysToBuy, waysToSell, UnitsofMoney= input().split()
UnitsofMoney=int(UnitsofMoney)
buyPrices= input().split()
sellPrices=input().split()


for i in range(len(buyPrices)):
  buyPrices[i]=int(buyPrices[i])


for i in range(len(sellPrices)):
  sellPrices[i]=int(sellPrices[i])

min_buy_price=min(buyPrices)
max_sell_price=max(sellPrices)

if min_buy_price<max_sell_price:
  number_of_shares=UnitsofMoney//min_buy_price
  UnitsofMoney=UnitsofMoney%min_buy_price
  UnitsofMoney+=(number_of_shares*max_sell_price)
  print(UnitsofMoney)
else:
  print(UnitsofMoney)
  





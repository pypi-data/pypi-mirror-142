# wxve

A stock analysis package in Python that equips objects with the information required to streamline operations.

## Install
```shell
pip install wxve
```

## Subscribe to API
Stock data is provided by the YH Finance API.
Create an account on RapidAPI and subscribe to the right plan for you. The **free** plan provides 500 requests per month with a rate limit of 5 requests per second. <br>
https://rapidapi.com/apidojo/api/yh-finance/

## Tutorial
```python
import wxve as x

IBM = x.Stock('IBM', 'YOUR_API_KEY')

IBM.candlestick.show()

print(IBM.div_df)
print(IBM.hist_df)
```
```python
import wxve as x

stock_list = ['IBM', 'INTC', 'NVDA']
ai_chip_makers = x.StockSet(stock_list, 'YOUR_API_KEY') 

ai_chip_makers.stocks['IBM'].candlestick.show()

print(ai_chip_makers.stocks['IBM'].div_df)
print(ai_chip_makers.stocks['IBM'].hist_df)
```
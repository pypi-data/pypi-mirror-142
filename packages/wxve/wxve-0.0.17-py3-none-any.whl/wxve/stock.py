import pandas as pd
import plotly.graph_objects as go
import yh_finance as yhf


class Stock:
    """Represents a stock."""

    def __init__(self, symbol, api_key, time_range='10y', interval='1d', region='US'):
        """
        Initialize attributes.
        """
        self.symbol = symbol.upper()
        self._json_resp_chart = yhf.get_chart(interval=interval,
                                              symbol=self.symbol,
                                              time_range=time_range,
                                              region=region,
                                              include_pre_post='false',
                                              use_yahoo_id='true',
                                              include_adj_close='true',
                                              events='div,split',
                                              api_key=api_key)

        # Dividend dataframe
        if 'events' in self._json_resp_chart['chart']['result'][0] and 'dividends' in self._json_resp_chart['chart']['result'][0]['events']:
            self._div_data = list(self._json_resp_chart['chart']['result'][0]['events']['dividends'].values())
            self.div_df = pd.DataFrame.from_records(self._div_data).rename(columns={'amount': 'div_amount'})
            self.div_df['date'] = pd.to_datetime(self.div_df['date'], unit='s').dt.date

            self.div_df['div_growth'] = self.div_df['div_amount'].diff()

            self.div_df = self.div_df[['date', 'div_amount', 'div_growth']]
            self.div_df = self.div_df.fillna(0)

        # Historical dataframe
        self._hist_data = self._json_resp_chart['chart']['result'][0]['indicators']['quote'][0]
        self.hist_df = pd.DataFrame.from_dict(self._hist_data)
        self.hist_df['date'] = self._json_resp_chart['chart']['result'][0]['timestamp']
        self.hist_df['date'] = pd.to_datetime(self.hist_df['date'], unit='s').dt.date

        self.hist_df = self.hist_df[['date', 'volume', 'open', 'low', 'high', 'close']]

        # Candlestick
        self.candlestick = go.Figure(data=[go.Candlestick(x=self.hist_df['date'],
                                                          open=self.hist_df['open'],
                                                          low=self.hist_df['low'],
                                                          high=self.hist_df['high'],
                                                          close=self.hist_df['close'])])
        self.candlestick.update_layout(title=self.symbol, yaxis_title='Stock Price')


if __name__ == '__main__':
    EVA = Stock(symbol='IBM',
                api_key='d73bb60f82mshbe3e55c57b941abp1abe67jsn7d7492f26dee')
    print(EVA.div_df)

from .stock import Stock


class StockSet:
    """Represents a series of stocks."""

    def __init__(self, symbol_list, api_key, date_range='max', interval='1d', region='US'):
        """Initialize attributes."""
        self.stocks = dict()
        for symbol in symbol_list:
            self.stocks[symbol] = Stock(symbol=symbol,
                                        api_key=api_key,
                                        date_range=date_range,
                                        interval=interval,
                                        region=region)

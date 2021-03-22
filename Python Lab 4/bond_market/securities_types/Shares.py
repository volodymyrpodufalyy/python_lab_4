from bond_market.Securities import Securities


class Shares(Securities):
    def __init__(self,type, brand,price,buying_date,risk_level,trading_trend,shares_category):
        Securities.__init__(self,type, brand,price,buying_date,risk_level,trading_trend)
        self.shares_category = shares_category

    def __del__(self):
        del self

    def __str__(self):
        return Securities.__str__(self) + f"Shares category:{self.shares_category}\n"


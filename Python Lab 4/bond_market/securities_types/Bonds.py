from bond_market.Securities import Securities


class Bonds(Securities):
    def __init__(self,type,brand,price,buying_date,risk_level,trading_trend,maturity,bond_percent):
        Securities.__init__(self,type,brand,price,buying_date,risk_level,trading_trend)
        self.maturity = maturity
        self.bond_percent = bond_percent

    def __del__(self):
        del self

    def __str__(self):
        return Securities.__str__(self) + f"Maturity:{self.maturity}\nBond percent:{self.bond_percent}\n"


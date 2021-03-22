from ..Securities import RiskLevel
from ..Securities import TradingTrend
from bond_market.brocker_manager.sortOrder import SortOrder


class BrokerManager:
    securities = []

    def add_securities(self, securities: list):
        self.securities += securities

    def search_by_price(self, price):
        return [item for item in self.securities
                if item.price == price]

    def search_by_risk_level(self, risk_level: RiskLevel):
        return [item for item in self.securities
                if item.risk_level == risk_level]

    def search_by_trend(self, trading_trend: TradingTrend):
        return [item for item in self.securities if item.trading_trend == trading_trend]

    def print_securities(self):
        for item in self.securities:
            print(item)

    def sort_by_price(self, securities: list, order: SortOrder):
        return sorted(securities, key=lambda e: e.price, reverse=order.value)

    def sort_by_date(self, securities: list, order: SortOrder):
         return sorted(securities, key=lambda e: e.buying_date, reverse=order.value)






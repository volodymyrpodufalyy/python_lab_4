from bond_market.Securities import RiskLevel as r
from bond_market.Securities import TradingTrend as t
from bond_market.brocker_manager.BrokerManager import BrokerManager
from bond_market.securities_types.Bonds import *
from bond_market.securities_types.Shares import *
from bond_market.brocker_manager.sortOrder import *
import unittest
import pep8
import os

gm_shares = Shares("Shares of", "General Motors", 65, "20 February", r.HIGH.name, t.DESCENDING.name, "Usual")
clubhouse_shares = Shares("Shares of", "Clubhouse", 2000, "21 February", r.EXTRAHIGH.name, t.GROWING.name, "Usual")
apple_bonds = Bonds("Bonds of", "Apple", 100, "1 February", r.LOW.name, t.GROWING.name, "short term", 1.25)
google_bonds = Bonds("Bonds of", "Google", 1000, "28 February", r.LOW.name, t.GROWING.name, "long term", 2.35)
microsoft_bonds = Bonds("Bonds of", "Microsoft", 950, "13 February", r.MEDIUM.name, t.GROWING.name, "medium term", 3.25)
telegram_shares = Shares("Shares of ", "Telegram", 500, "24 February", r.MEDIUM.name, t.DESCENDING.name, "Privilege")


class TestPep8(unittest.TestCase):
    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 120
        filenames = []
        for root, _, files in os.walk(''):
            if "venv" not in root:
                python_files = [f for f in files if f.endswith('.py')]
                for file in python_files:
                    filename = '{0}/{1}'.format(root, file)
                    filenames.append(filename)
        check = style.check_files(filenames)
        print(f'PEP8 style errors: {check.total_errors}')


class TestManager(unittest.TestCase):
    securities = [gm_shares, clubhouse_shares, apple_bonds, google_bonds, microsoft_bonds, telegram_shares]
    broker = BrokerManager()
    broker.add_securities(securities)

    def test_add_securities(self):
        self.assertEqual(self.broker.securities, self.securities)

    def test_search_by_price(self):
        self.assertEqual(self.broker.search_by_price(100), [apple_bonds])

    def test_search_by_risk_level(self):
        self.assertEqual(self.broker.search_by_risk_level("MEDIUM"), [microsoft_bonds, telegram_shares])

    def test_search_by_trend(self):
        self.assertEqual(self.broker.search_by_trend("GROWING"),
                         [clubhouse_shares, apple_bonds, google_bonds, microsoft_bonds])

    def test_sort_by_price_asc(self):
        sorted_securities = self.broker.sort_by_price(self.securities, SortOrder.ASC)
        self.assertEqual(sorted_securities,
                         [gm_shares, apple_bonds, telegram_shares, microsoft_bonds, google_bonds, clubhouse_shares])

    def test_sort_by_price_desc(self):
        sorted_securities = self.broker.sort_by_price(self.securities, SortOrder.DESC)
        self.assertEqual(sorted_securities,
                         [clubhouse_shares, google_bonds, microsoft_bonds, telegram_shares, apple_bonds, gm_shares])

    def test_sort_by_date_asc(self):
        sorted_securities = self.broker.sort_by_date(self.securities, SortOrder.ASC)
        self.assertEqual(sorted_securities,
                         [apple_bonds, microsoft_bonds, gm_shares, clubhouse_shares, telegram_shares, google_bonds])

    def test_sort_by_date_desc(self):
        sorted_securities = self.broker.sort_by_date(self.securities, SortOrder.DESC)
        self.assertEqual(sorted_securities,
                         [google_bonds, telegram_shares, clubhouse_shares, gm_shares, microsoft_bonds, apple_bonds])


if __name__ == '__main__':
    unittest.main()

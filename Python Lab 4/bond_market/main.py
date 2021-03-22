from Securities import RiskLevel as r
from Securities import TradingTrend as t
from securities_types.Shares import Shares
from securities_types.Bonds import Bonds
from bond_market.brocker_manager.BrokerManager import BrokerManager as BM
from bond_market.brocker_manager.sortOrder import SortOrder

if __name__ == '__main__':

    BM().add_securities([Shares("Shares of", "General Motors", 65, "20 February", r.HIGH.name, t.DESCENDING.name, "Usual")])
    BM().add_securities([Shares("Shares of","Clubhouse", 2000, "21 February", r.EXTRAHIGH.name, t.GROWING.name, "Usual")])
    BM().add_securities([Bonds("Bonds of", "Apple", 100, "1 February", r.LOW.name, t.GROWING.name, "short term", 1.25)])
    BM().add_securities([Bonds("Bonds of", "Google", 1000, "28 February", r.LOW.name, t.GROWING.name, "long term", 2.35)])
    BM().add_securities([Bonds("Bonds of", "Microsoft", 950, "13 February",  r.MEDIUM.name, t.GROWING.name, "medium term", 3.25)])
    BM().add_securities([Shares("Shares of ", "Telegram", 500, "24 February", r.MEDIUM.name, t.DESCENDING.name,"Privilege")])

    # BM().print_securities()

    """Search by price"""
    price_list = BM().search_by_price(100)
    for i in price_list:
        print(i)

    """Search by risk"""
    # risk_list = BM().search_by_risk_level("MEDIUM")
    # for i in risk_list:
    #     print(i)

    # """Search by trend"""
    # trend_list = BM().search_by_trend("GROWING")
    # for i in trend_list:
    #     print(i)

    """Sort by price"""
    # using_list = BM().securities
    # print("\n\nSecurities sorted by price from smallest to biggest:\n")
    # sorted_secs_price = BM().sort_by_price(using_list, SortOrder.ASC)
    # print(*sorted_secs_price)
    # print("\n\nSecurities sorted by price from biggest to smallest:\n")
    # sorted_secs_price = BM().sort_by_price(using_list, SortOrder.DESC)
    # print(*sorted_secs_price)
    #

    """Sort by date"""
    # print("\n\nFrom oldest to newest:\n")
    # sorted_secs_date = BM().sort_by_date(using_list, SortOrder.ASC)
    # print(*sorted_secs_date)
    # print("\n\nFrom newest to oldest:\n")
    # sorted_secs_date = BM().sort_by_date(using_list, SortOrder.DESC)
    # print(*sorted_secs_date)




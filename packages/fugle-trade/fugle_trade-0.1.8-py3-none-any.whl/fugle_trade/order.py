"""
Define Order Objects
"""
import typing
from fugle_trade.constant import (
    Action,
    APCode,
    Trade,
    PriceFlag,
    BSFlag
)

class OrderObject():
    apCode: APCode
    priceFlag: PriceFlag
    bsFlag: BSFlag
    trade: Trade
    buySell: Action
    price: float
    stockNo: str
    quantity: int

    def __init__(
            self,
            buySell: Action,
            price: float,
            stockNo: str,
            quantity: int,
            apCode: APCode = APCode.Common,
            bsFlag: BSFlag = BSFlag.ROD,
            priceFlag: PriceFlag = PriceFlag.Limit,
            trade: Trade = Trade.Cash,
        ):

        if type(buySell) is not Action:
            raise TypeError("Please use fugleTrade.constant Action")

        # fugle_trade_core will check price format, no need to check price here

        if type(stockNo) is not str:
            raise TypeError("Please use type str in stockNo")

        if type(quantity) is not int:
            raise TypeError("Please use type int in quantity")
        elif apCode == APCode.Common or apCode == APCode.AfterMarket:
            if quantity < 1 or quantity > 500:
                raise TypeError("quantity must within range 1 ~ 499")

        elif apCode == APCode.Odd or apCode == APCode.IntradayOdd:
            if quantity < 1 or quantity > 1000:
                raise TypeError("quantity must within range 1 ~ 999")
        elif apCode == APCode.Emg:
            if quantity < 1 or quantity > 499000 or (quantity > 1000 and quantity % 1000 != 0):
                raise TypeError("quantity must within range 1 ~ 499000, or multiply of 1000")

        if type(apCode) is not APCode:
            raise TypeError("Please use fugleTrade.constant APCode")

        if type(bsFlag) is not BSFlag:
            raise TypeError("Please use fugleTrade.constant BSFlag")

        if type(priceFlag) is not PriceFlag:
            raise TypeError("Please use fugleTrade.constant PriceFlag")

        if type(trade) is not Trade:
            raise TypeError("Please use fugleTrade.constant Trade")

        self.apCode = apCode
        self.priceFlag = priceFlag
        self.bsFlag = bsFlag
        self.trade = trade
        self.buySell = buySell
        self.price = price
        self.stockNo = stockNo
        self.quantity = quantity

    def __str__(self):
        return "apCode: %s, priceFlag: %s, bsFlag: %s, trade: %s, buySell: %s, price: %s, stockNo: %s, quantity: %s" % (self.apCode, self.priceFlag, self.bsFlag, self.trade, self.buySell, self.price, self.stockNo, self.quantity)

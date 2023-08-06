"""
 - position sizing, ...


Current Price | Price Movement Estimation | Capital Needed | Capital At Risk | Leverage | Volume
--------------|---------------------------|----------------|-----------------|----------|-------
$1            | 10*e-4                    | $10*e+4        | $100            | 100      | 10*e+6
$1            | 10*e-4                    | $10*e+4        | $100            | 10       | 10*e+5
$1            | 10*e-4                    | $10*e+3        | $10             | 10       | 10*e+4

Formulas:
 - Volume * Price Movement Estimation = Capital At Risk
 - Volume = Capital Needed * Leverage
 - Volume = dividable by Micro/Micro/complete lot

"""
import backtrader as bt

LOT_SIZE = 100000
MINI_LOT_SIZE = 10000
MICRO_LOT_SIZE = 1000

PIP_CONST = 0.0001
PIP_IN_DOLLAR = LOT_SIZE * PIP_CONST
# todo: just for now lower to small pips
# RISK_IN_PIP = (CASH_TOTAL * RISK_PORTFOLIO) / PIP_IN_DOLLAR

# RISK_PORTFOLIO = 0.01  # what % of your portfolio wanna risk
PIP_VALUE = 10


class PositionTypeConstants:
    POSITION_LONG = "LONG"
    POSITION_NONE = "NONE"
    POSITION_SHORT = "SHORT"


from moosir_common.live_traders.core import PredictionTypeConstants


class OrderPosition:
    def __init__(self, position_size_lot, trail_amount, price):
        # self.position_size = position_size
        self.position_size_lot = position_size_lot
        self.trail_amount = trail_amount
        self.price = price


# todo: why it needs to know abt trader stuff!!
class RiskManager:
    def __init__(self,
                 leverage: int = 10,
                 initial_cash: float =10000.0,
                 risk_p_trade_perc: float=0.01):

        assert 0 < risk_p_trade_perc < 1, "risk per trader percentage must be between 0 and 1"
        assert initial_cash > 1, "initial cash must be greater than 1"
        assert leverage >= 1, "leverage must be greater than 1"

        self.initial_cash = initial_cash
        self.risk_p_trade_perc = risk_p_trade_perc
        self.leverage = leverage

    def calculate_order(self, current_price, stop_loss_price_move_pips, current_cash) -> OrderPosition:
        """

        :param current_price: current price
        :param stop_loss_price_move_pips:
            - (absolute) pips that triggers stop-loss (no matter buy or sell)
            - your estimation about price movement in opposite direction
        :return:
        """
        assert stop_loss_price_move_pips > 0, "price movement needs to be in absolute format (i.e. positive)"
        assert current_price > 0, "current price must be greater than 0"

        cash = self.initial_cash
        risk_per_trade_cash = self.risk_p_trade_perc * cash

        # todo: problematic, needs to be transalated to lots!!!
        price_move_cash = PIP_CONST * stop_loss_price_move_pips
        position_size = int(risk_per_trade_cash/price_move_cash)
        # todo: what if not devidable to mini/... lot, does broker accept micro lot?!!!
        position_size_lot = round(position_size / LOT_SIZE, 2) # to be max on micro measure, cant do less than micro

        leverage_needed = position_size / current_cash
        # todo: should leverage needed be round up?!!!
        # todo: how about current cache? might be lower than
        if leverage_needed > self.leverage:
            raise Exception(f"leverage needed ({leverage_needed}) is higher than current leverage {self.leverage}")

        # position_size_lot = round(risk_per_trade_cash / (stop_loss_price_move_pips * PIP_VALUE), 2)
        # position_size = position_size_lot * LOT_SIZE

        trail_amount = 1 * stop_loss_price_move_pips * PIP_CONST
        result = OrderPosition(position_size_lot=position_size_lot,
                               trail_amount=trail_amount,
                               price=current_price)
        return result

    def make_orders_long(self, strategy, position_size, price, trail_amount, is_bracket_order=True):
        if is_bracket_order:
            take_profit_price = price + 2 * trail_amount
            stop_loss_price = price - trail_amount

            strategy.buy_bracket(limitprice=take_profit_price,
                                 stopprice=stop_loss_price,
                                 size=position_size,
                                 exectype=bt.Order.Market)
        else:
            # todo: might cause prob when next bar is too big up or down!!!
            strategy.buy(size=position_size, exectype=bt.Order.Limit, price=price)
            #
            # # trailing
            strategy.sell(
                size=position_size
                , exectype=bt.Order.StopTrailLimit
                , trailamount=trail_amount
                , trailpercent=0.0
            )

    def make_orders_short(self, strategy, position_size, price, trail_amount, is_bracket_order=True):

        if is_bracket_order:
            take_profit_price = price - 2 * trail_amount
            stop_loss_price = price + trail_amount

            strategy.sell_bracket(limitprice=take_profit_price,
                                  stopprice=stop_loss_price,
                                  size=position_size,
                                  exectype=bt.Order.Market)
        else:
            # todo: might cause prob when next bar is too big up or down!!!
            strategy.sell(size=position_size, exectype=bt.Order.Limit, price=price)
            #
            # # trailing
            strategy.buy(
                size=position_size
                , exectype=bt.Order.StopTrailLimit
                , trailamount=trail_amount
                , trailpercent=0.0
            )

    def calculate_trade_type(self, existing_position, signal: PredictionTypeConstants) -> PositionTypeConstants:
        if existing_position:
            return PositionTypeConstants.POSITION_NONE

        if signal == PredictionTypeConstants.FLAT:
            return PositionTypeConstants.POSITION_NONE

        if signal == PredictionTypeConstants.HIGH or signal == PredictionTypeConstants.VERY_HIGH:
            return PositionTypeConstants.POSITION_LONG

        if signal == PredictionTypeConstants.LOW or signal == PredictionTypeConstants.VERY_LOW:
            return PositionTypeConstants.POSITION_SHORT

    # todo: from arima time
    # LEVERAGE_N = 100
    # RISK_IN_PIP = 5
    # ORDER_SIZE = 1
    # def calculate_order(self, price):
    #     take_profit = 1 + 2 * RISK_IN_PIP * PIP_CONST
    #     take_profit_price = price * take_profit
    #
    #     stop_loss = 1 + RISK_IN_PIP * PIP_CONST
    #     stop_loss_price = price / stop_loss
    #
    #     # https://www.quantconnect.com/forum/discussion/7442/calculating-lot-size-for-a-forex-order-based-on-portfolio-value-and-leverage/p1
    #     # todo: needs more investigation
    #     # link: https://docs.google.com/spreadsheets/d/1qL-sACNxGF1gF25x_Wwr8d0ibkt1InFHkza7GDMWz_o/edit?usp=sharing
    #     # leverage = self.Securities[self.pair].Leverage
    #
    #     borrowing_power = CASH_TOTAL * LEVERAGE_N
    #     money_needed_for_order = price * ORDER_SIZE * LOT_SIZE
    #
    #     order_size = 1
    #
    #     if borrowing_power < money_needed_for_order:
    #         raise Exception(
    #             f"cannt affor to run order: borrowing power: {borrowing_power}, money needed: {money_needed_for_order} , price: {price}")
    #
    #     return order_size, take_profit_price, stop_loss_price

    # todo: from arima time
    # def make_orders(self, order_size, take_profit_price, stop_loss_price ):
    #     orders = self.buy_bracket(limitprice=take_profit_price,
    #                            stopprice=stop_loss_price,
    #                            size=order_size,
    #                            exectype=bt.Order.Market)
    #
    #     return orders

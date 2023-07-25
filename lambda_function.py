import sys
from algotrade_engine import main as app


def handler(event, context):
    app.algo_trade_engine(sys.argv)

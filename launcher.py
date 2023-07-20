import sys
from algotrade_engine import main as app


print("[INFO] Launcher - Argument List: ", str(sys.argv))
print("[INFO] Launcher v0.1 - HRC ENGINE starting")
app.algo_trade_engine(sys.argv)

import math
import numpy as np

avg_daily_rets = 0.001
daily_rf = 0.0002
std_daily_rets = 0.001


sharpe = math.sqrt(252) * np.mean(avg_daily_rets - daily_rf) / std_daily_rets

print sharpe

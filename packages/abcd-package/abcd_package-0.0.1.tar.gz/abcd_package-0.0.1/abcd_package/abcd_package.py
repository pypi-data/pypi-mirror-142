from scipy import stats
from scipy.optimize import root
import math

def CalSampleSize(mde=0.025, ci=0.05, power=0.8, p=0.5, N=2, side='two-sided', message=True):
    cohen = mde / math.sqrt(p*(1-p)/2 + (p+mde)*(1-p-mde)/2)
    lift = mde / p
    cr = N - 1
    # For each given n, we can obtain a power. We only need to find the minimum n such that power is large enough.
    if side == 'two-sided':
        def help_fun(n):
            p1 = stats.t.cdf(x = stats.t.ppf(q=1-ci/2/cr, df=n*2-2) - cohen / math.sqrt(2/n), df= n*2-2)
            p2 = stats.t.cdf(x = stats.t.ppf(q=ci/2/cr, df=n*2-2) - cohen / math.sqrt(2/n), df= n*2-2)
            return 1 - (p1 - p2) - power
    elif side == 'one-sided':
        def help_fun(n):
            p1 = stats.t.cdf(x = stats.t.ppf(q=1-ci/cr, df=n*2-2) - cohen / math.sqrt(2/n), df= n*2-2)
            return 1 - p1 - power
    else:
        raise ValueError('side should be one-sided or two-sided')
    res = int(root(fun=help_fun, x0=10).x[0])
    if message:
        print(f"Cohen's D is {cohen}.")
        print(f"Lift is {lift}.")
        print(f"Minimum sample size per group is {res}")
    return cohen, lift, res

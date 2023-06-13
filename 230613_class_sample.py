lst = [1, 5, 2, 4, 8, 2, 10] 

print(sum(lst))
print(sorted(lst))
print(type(lst))
print()

import pandas as pd
series = pd.Series(lst)
print(series.sum())
print(series.sort_values())
print(type(series))
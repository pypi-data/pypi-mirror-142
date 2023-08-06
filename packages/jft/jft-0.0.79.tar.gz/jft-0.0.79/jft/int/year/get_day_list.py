from datetime import date as d
from datetime import timedelta as td

f = lambda x:[
  _ for _ in [d(x, 1, 1) + td(days=δ) for δ in range(367)] if _ <= d(x, 12, 31)
]

t = lambda: f(2022) == sorted([
  *[d(2022, m, _) for _ in range(1, 32) for m in [1, 3, 5, 7, 8, 10, 12]],
  *[d(2022, m, _) for _ in range(1, 31) for m in [4, 6, 9, 11]],
  *[d(2022, 2, _) for _ in range(1, 29)],
])
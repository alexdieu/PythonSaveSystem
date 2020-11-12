from reader import taker
from creator import save

a = 24

save(a, "dat", 0)
print(taker("dat"))
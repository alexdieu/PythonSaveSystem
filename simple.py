from reader import taker
from creator import save

a = 45

b = "WHAT"

c = ["carrots", "rabbits"]

save(a, "dat", 0)
save(b, "dat", 1)
save(c, "dat", 1)

print(taker("dat"))
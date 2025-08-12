def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
dong1 = input().lower().split()
dong2 = input().lower().split()

tap1 = set(dong1)
tap2 = set(dong2)

hop = tap1 | tap2
giao = tap1 & tap2
print(" ".join(sorted(hop)))
print(" ".join(sorted(giao)))
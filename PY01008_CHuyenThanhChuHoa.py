str = input()
for s in str:
    if s.isalpha():
        s = s.upper()
    print(s, sep = "", end = "")

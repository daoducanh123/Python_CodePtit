
f = open("CONTACT.in", "r")

a = set()

for line in f:
    email = line.strip().lower()
    if email:
        a.add(email)
        
f.close()

for email in sorted(a):
    print (email)
    
binary = input().strip()

while len (binary) % 3 != 0:
    binary = "0" + binary
result = ""
for i in range(0,len(binary),3):
    
    group = binary[i:i+3]
    value = int(group,2)
    result = result + str(value)
    
print(result)
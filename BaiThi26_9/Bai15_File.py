

file1 = open ("DATA1.in", "r")
file2 = open ("DATA2.in", "r")

# read() Đọc toàn bộ nội dung file → trả về chuỗi (str).
a = set (file1.read().lower().split()) # split -> list ['hello', 'world', 'python', 'is', 'easy']
b = set (file2.read().lower().split())

#auto
x = a-b
y = b-a
# A có, B không có manual
for aa in a:
    if aa not in b:
        x.add(aa)


x = sorted(x)
y = sorted(y)

for xx in x:
    print(xx, end = " ")
print()
for yy in y:
    print(yy, end = " ")
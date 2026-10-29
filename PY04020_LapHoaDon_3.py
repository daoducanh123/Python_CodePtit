# Mã mặt hàng (xâu ký tự độ dài không quá 10, không có khoảng trống)
# Tên mặt hàng (xâu ký tự độ dài không quá 100, có thể có khoảng trống)
# Số lượng mua (không quá 50)
# Đơn giá (số nguyên dương có thể đến 10 chữ số)
# Tiền chiết khấu của hóa đơn (có thể đến 9 chữ số).

class SanPham:
    def __init__(self, ma,name,number,price,discount,total):
        self.ma= ma
        self.name = name
        self.number = number
        self.price = price
        self.discount = discount
        self.total = total
        
n = int(input())
listSanPham = list()
for _ in range(n):
    ma = input()
    name = input()
    number = int(input())
    price = int(input())
    discount = int(input())
    total = price*number-discount
    sanPham = SanPham (ma,name,number,price,discount, total)
    listSanPham.append(sanPham)
listSanPham = sorted(listSanPham, key = lambda x: x.total, reverse=True)
for sanpham in listSanPham:
    print(f"{sanpham.ma} {sanpham.name} {sanpham.number} {sanpham.price} {sanpham.discount} {sanpham.total}")
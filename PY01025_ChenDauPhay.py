# 153,920,529
s = input()
res = ""    

while(len(s) > 3):
    res = "," + s[-3:] + res  # lấy 3 thằng cuối
    s = s[:-3]  #sub string lấy trừ 3 thằng cuối gán vào biến s (string gốc ko bị thay đổi nhé)
    
res = s+ res
print(res)
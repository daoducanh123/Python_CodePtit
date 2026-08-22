Str = input().lower()
pos = Str.find(".py")

# if pos != -1:
#     print("yes")
# else:
#     print("no")

if ".py" in Str:
    print("yes")
else:
    print("no")
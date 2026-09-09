def ThapHaNoi(n, start, via ,end):
    if n == 1:
        print(start + " -> " + end)
        return
    
    ThapHaNoi(n-1, start, end, via)
    ThapHaNoi(1, start, via,end)
    ThapHaNoi(n-1, via, start, end)
    
        
n = int(input())
ThapHaNoi(n, "A", "B", "C")
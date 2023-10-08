c0 = int(input("Enter number: "))
step = 0

while c0 != 1:

    if c0 & 1:
        c0 = 3 *c0 +1
    else:
        c0 = c0//2
    print(c0)
    step += 1
    
print("Steps needed:", step)











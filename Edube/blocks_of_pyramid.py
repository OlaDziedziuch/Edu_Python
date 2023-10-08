sum_blocks = int(input("Enter the number of blocks: "))
height = 0

while sum_blocks > height:
    height += 1
    sum_blocks -= height

print("The height of pyramid is: ", height)

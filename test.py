
while True:
    n = int(input())
    print(f"the multipiclation table for {n} is : ")

    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    print("Enter 1 to run again : ",end="")
    l = int(input())
    if l != 1:
        break

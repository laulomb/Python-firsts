largest= None
smallest= None

while True:
    numb = input("Enter a number: ")
    if numb == "done" :
        break
    try:
        num=int(numb)
    except:
         print('Invalid input')
         continue

    if largest is None:
        smallest=num
        largest=num
    elif num<smallest:
        smallest=num
    elif num>largest:
        largest=num


print("Maximum is", largest)
print('Minimum is', smallest)

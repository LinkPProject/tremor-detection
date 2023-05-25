
DictionaryOfProducts={"Pizza":150,"Burgur":80,"Noodles":100,"French_Fires":100,"Dessert":50}
print(DictionaryOfProducts)
print()
print("What would you Like to order?")


def addToCart(initialInputList):
    total=0
    cart={};
    for i in initialInputList:
        cart[i]=DictionaryOfProducts[i]
        total=total+DictionaryOfProducts[i]
    print("Please Review Your Order \n")
    return [cart,total]

    

initialInputList=list(input().split())
print()
itemsAdded=addToCart(initialInputList)

print("Your Order Currently")
print("foodItems:",itemsAdded[0])
print("Total:",itemsAdded[1])

Print("Press 1 to add mo")
    
    
    

    


import generateBillModules as pm

DISCOUNT = 2

collectionName = pm.connection()

name = input('Please enter your name:\n')

check = pm.checkUser(collectionName, name)
if check:
    DISCOUNT = 3

pm.displayItems()

amount = 0
items = {1:'Dosa',2:'Idly',3:'Pongal',4:'Vada',5:'Rice Bath'} # itemCode mapped to itemName
prices = {1:45.00,2:30.00,3:35.00,4:38.20,5:40.52} # itemCode mapped to price
random = {}
while True:
    itemCode = int(input('Enter the item: '))
    if itemCode > 5:
        break
    else:
        quantity = int(input('Enter the quantity: '))
        random[itemCode] = quantity # itemCode mapped to quantity
        amount += (quantity * prices.get(itemCode))

discount, vat, service, netAmount = pm.calAttr(amount, DISCOUNT)
paymentMode = input('Cash or Card ?? ')

if check:
    pm.updateTheRecord(collectionName, name, netAmount, paymentMode)
else:
    push = input('You want to insert or not ??')
    if push == 'Yes':
        pm.pushTheRecord(collectionName, name, netAmount, paymentMode)

result = bool(input('You want a bill copy or not: '))
if result:
    pm.displayBill(random, items, prices, amount, discount, vat, service, netAmount, name)
else:
    print('Visit again !!')


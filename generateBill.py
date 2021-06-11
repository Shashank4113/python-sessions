import pythonMongo as pm

DISCOUNT = 2

collectionName = pm.connection()

name = input('Please enter your name:\n')

check = pm.checkUser(collectionName, name)
if check:
    DISCOUNT = 3
    print('We Found the user !')

print('List of available items'.center(50))
print('-'*60)
print('Code\t\tItem Name\t\t\tPrice')
print('-'*60)
print('1\t\tDosa\t\t\t\t45.00')
print('2\t\tIdly\t\t\t\t30.00')
print('3\t\tPongal\t\t\t\t35.00')
print('4\t\tVada\t\t\t\t38.20')
print('5\t\tRice Bath\t\t\t40.52')
print('-'*60)

amount = 0
items = {1:'Dosa',2:'Idly',3:'Pongal',4:'Vada',5:'Rice Bath'}
prices = {1:45.00,2:30.00,3:35.00,4:38.20,5:40.52}
random = {}
while True:
    itemCode = int(input('Enter the item: '))
    if itemCode > 5:
        break
    else:
        quantity = int(input('Enter the quantity: '))
        random[itemCode] = quantity
        amount += (quantity * prices.get(itemCode))

discount = (amount * DISCOUNT)/100
vat = (amount * 5.5)/100
service = (amount * 3)/100
netAmount = amount - discount + vat + service
paymentMode = input('Cash or Card ?? ')

if check:
    pm.updateTheRecord(collectionName, name, netAmount, paymentMode)
else:
    push = input('You want to insert or not ??')
    if push == 'Yes':
        pm.pushTheRecord(collectionName, name, netAmount, paymentMode)
        print('Inserted Successfully !')

result = bool(input('You want a bill copy or not: '))
if result:
    pm.displayBill()



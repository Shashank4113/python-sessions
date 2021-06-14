import pymongo
import smtplib

def connection():
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["test_python"] # DB name
  mycol = mydb["customersTwo"] # Collection name

  return mycol

def pushTheRecord(collection, name, amount, modeOfP):
  collection.insert_one({"name": name, "amount": [amount], "PaymentMode": [modeOfP], "visited": 1})

  print('Inserted Succesfully !')

def checkUser(collection, name):
  record = collection.find({"name": name})
  for x in record:
    if x['name'] == name:
      print('User Found !')
      return True
    else:
      return False

def updateTheRecord(collection, name, amount, modeOfP):
  data = collection.find({"name": name}, {'_id': 0 ,"name": 0})
  amounts = [amount]
  paymentModes = [modeOfP]
  for x in data:
    amounts.append(x['amount'])
    paymentModes.append(x['PaymentMode'])
    vis = x['visited']
  collection.update_one({"name": name}, {"$set": {"amount": amounts, "PaymentMode": paymentModes, "visited": vis + 1}})

  print('Updated Succesfully !')

def sendMail():
  server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
  server.login("testPythoncjr@gmail.com", "tpCJR123")
  message = """ Test mail """
  server.sendmail("testPythoncjr@gmail.com", "seethudhoni@gmail.com",  message)

  server.quit()

def displayBill(random, items, prices, amount, discount, vat, service, netAmount, name):
  file = open('generateBill.txt', 'a')
  file.write('Meghana Foods'.center(85))
  print('Meghana Foods'.center(85))
  print('No. 124 1st Cross Road, near Jyothi'.center(85))
  print('Nivas College, KHB Colony, 5th Block,'.center(85))
  print('Koramangala, Bengaluru, Karnataka, 560095'.center(85))
  print('PH: 080 41440087'.center(85))
  print('Cash/Bill'.center(85))
  print('-'*90)
  print('Item\t\t\tPrice\t\tQuantity\t\tTotal Rs.')
  print('-'*90)
  for item in random.keys():
      print('{}\t\t\t{}\t\t{}\t\t\t{}'.format(items[item], prices[item], random[item], prices[item] * random[item]))
  print('-'*90)
  print('Total Quantity\t\t\t\t{}'.format(sum(random.values())))
  print('Gross Total\t\t\t\t\t\t\t{}'.format(amount))
  print('Discount\t\t\t\t\t\t\t-{}'.format(discount))
  print('VAT 5.5 %\t\t\t\t\t\t\t+{}'.format(vat))
  print('Service Tax\t\t\t\t\t\t\t+{}'.format(round(service, 2)))
  print('Net Amount\t\t\t\t\t\t\t{}'.format(round(netAmount, 2)))
  print('Get Back {}!'.format(name).center(85))
  print('-'*90)

def displayItems():
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

def calAttr(amt, DISCOUNT):
  discount = (amt * DISCOUNT)/100
  vat = (amt * 5.5)/100
  service = (amt * 3)/100
  netAmount = amt - discount + vat + service

  return discount, vat, service, netAmount
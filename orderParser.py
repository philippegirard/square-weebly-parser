import pandas
import csv
from dataclasses import LineOrder

df = pandas.read_csv('splitting-11-13.csv')

print(list(df.columns))

lineOrderList = []

for index, row in df.iterrows():
    # print(row[0], row[1])
    orderNum = row['OrderNum']
    date = row['Date']
    firstName = row['Shipping First Name']
    lastName = row['Shipping Last Name']
    email = row['Shipping Email']
    productId = row['Product Id']
    productOptions = row['Product Options']
    productQty = row['Product Quantity']
    productPrice = row['Product Price']
    productOptionPrice = row['Product Options Total Price']
    productPaidPrice = row['Product Total Price']
    coupon = row['Coupon']

    # get line order if exists in list
    lineOrder = None
    for lo in lineOrderList:
        if lo.orderNum == orderNum:
            lineOrder = lo

    # add line order if not exist in list
    if lineOrder is None:
        lineOrder = LineOrder(orderNum, date, firstName, lastName, email, coupon)
        lineOrderList.append(lineOrder)

    lineOrder.addProduct(productId, productOptions, productQty, productPrice, productOptionPrice, productPaidPrice)

    # print(orderNum, date, firstName, lastName, email, productId, productOptions, productQty, coupon)


# for lo in lineOrderList:
#     print(lo.orderNum, lo.albumPrice, lo.albumNum, lo.activitePrice, lo.activite)

def correct(a):
    if a is None:
        return None
    return a.replace('&eacute;', 'é').replace('&Eacute;', 'É').replace('&euml;', 'ë').replace('&egrave;', 'è')


def cc(a):
    if a is None:
        return
    if len(a) > 0:
        return correct(a[0])


with open('OUTPUT.csv', mode='w', newline='') as csv_file:
    fieldnames = ['orderNum', 'date', 'firstName', 'lastName', 'email', 'coupon', 'totalPrice', 'totalDiscount',
                  'totalPaid', 'joncSize', 'joncInvite', 'joncParrain', 'joncParrainName',
                  'casinoTicketNumber', 'b1Occupation', 'b1C1', 'b1C2', 'b1C3',
                  'b2Occupation', 'b2C1', 'b2C2', 'b2C3', 'b2AccompOccup', 'b2AccompName', 'b2Vege', 'b2VegeAccomp',
                  'allergie', 'activite', 'albumNum', 'cotonVertOption', 'cotonNoirOption', 'bockOption', 'joncQty',
                  'joncTicketQty', 'casinoTicketQty', 'B1Qty', 'b2Qty',
                  'activiteQty', 'albumQty', 'cotonVertQty', 'cotonNoirQty', 'bockQty', 'joncPrice', 'joncTicketPrice',
                  'casinoPrice',
                  'b1price', 'b2price', 'activitePrice', 'albumPrice', 'cotonVertPrice', 'cotonNoirPrice', 'bockPrice']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for lo in lineOrderList:
        writer.writerow({'orderNum': lo.orderNum, 'date': lo.date, 'firstName': lo.firstName, 'lastName': lo.lastName,
                         'email': lo.email, 'coupon': lo.coupon, 'totalPrice': lo.loTotalProductPrice,
                         'totalDiscount': lo.loTotalProductDiscount, 'totalPaid': lo.loTotalProductPaidPrice,
                         'joncSize': cc(lo.joncSize), 'joncInvite': cc(lo.joncInvite),
                         'joncParrain': cc(lo.joncParrain), 'joncParrainName': cc(lo.joncParrainName),
                         'casinoTicketNumber': lo.casinoTicketNumber,
                         'b1Occupation': cc(lo.b1Occupation), 'b1C1': cc(lo.b1C1), 'b1C2': cc(lo.b1C2),
                         'b1C3': cc(lo.b1C3), 'b2Occupation': cc(lo.b2Occupation), 'b2C1': cc(lo.b2C1),
                         'b2C2': cc(lo.b2C2), 'b2C3': cc(lo.b2C3), 'b2AccompOccup': cc(lo.b2AccompOccup),
                         'b2AccompName': cc(lo.b2AccompName), 'b2Vege': cc(lo.b2Vege),
                         'b2VegeAccomp': cc(lo.b2VegeAccomp), 'allergie': cc(lo.allergie), 'albumNum': lo.albumNum,
                         'cotonVertOption': correct(lo.cotonVertOption), 'cotonNoirOption': correct(lo.cotonNoirOption),
                         'bockOption': correct(lo.bockOption),
                         'joncQty': lo.joncqty, 'joncTicketQty': lo.joncTicketQty,
                         'casinoTicketQty': lo.casinoTicketNumber, 'B1Qty': lo.b1qty, 'b2Qty': lo.b2qty,
                         'activiteQty': lo.activiteQty,
                         'albumQty': lo.albumNum,
                         'cotonVertQty': lo.cotonVertQty, 'cotonNoirQty': lo.cotonNoirQty, 'bockQty': lo.bockQty,
                         'activite': correct(lo.activite),
                         'joncPrice': lo.joncPrice, 'joncTicketPrice': lo.joncTicketPrice,
                         'casinoPrice': lo.casinoPrice,
                         'b1price': lo.b1price, 'b2price': lo.b2price, 'activitePrice': lo.activitePrice,
                         'albumPrice': lo.albumPrice,
                         'cotonVertPrice': lo.cotonVertPrice, 'cotonNoirPrice': lo.cotonNoirPrice,
                         'bockPrice': lo.bockPrice})

print(len(lineOrderList))

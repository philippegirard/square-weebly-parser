import re


class LineOrder:
    def __init__(self, orderNum, date, firstName, lastName, email, coupon):
        self.orderNum = orderNum
        self.date = date
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.coupon = coupon

        self.loTotalProductPrice = 0
        self.loTotalProductDiscount = 0
        self.loTotalProductPaidPrice = 0

        self.joncSize = None
        self.joncInvite = None
        self.joncParrain = None
        self.joncParrainName = None
        self.joncqty = 0
        self.joncPrice = 0
        self.joncTicketQty = 0
        self.joncTicketPrice = 0

        self.casinoTicketNumber = 0
        self.casinoPrice = 0

        self.b1Occupation = None
        self.b1C1 = None
        self.b1C2 = None
        self.b1C3 = None
        self.b1price = 0
        self.b1qty = 0

        self.b2Occupation = None
        self.b2C1 = None
        self.b2C2 = None
        self.b2C3 = None
        self.b2AccompOccup = None
        self.b2AccompName = None
        self.b2Vege = None
        self.b2VegeAccomp = None
        self.allergie = None
        self.b2price = 0
        self.b2qty = 0

        self.albumNum = 0
        self.albumPrice = 0

        self.activite = None
        self.activitePrice = 0
        self.activiteQty = 0

        self.cotonVertQty = 0
        self.cotonVertPrice = 0
        self.cotonVertOption = None

        self.cotonNoirQty = 0
        self.cotonNoirPrice = 0
        self.cotonNoirOption = None

        self.bockQty = 0
        self.bockPrice = 0
        self.bockOption = None

    def addProduct(self, productId, productOptions, productQty, productPrice, productOptionPrice, productPaidPrice):
        totalProductPrice = productQty * productPrice + productOptionPrice
        totalDiscount = totalProductPrice - productPaidPrice
        self.loTotalProductPrice += totalProductPrice
        self.loTotalProductDiscount += totalDiscount
        self.loTotalProductPaidPrice += productPaidPrice

        if productId == 12:
            self.joncSize = re.findall(
                'Confirmez une derni&egrave;re fois votre grandeur de jonc. R&eacute;sultat des sondages : https://www.promo61.com/jonc-casino : ([0-9][0-9]?-?),',
                productOptions)
            self.joncInvite = re.findall(
                ', Invit&eacute;s remise des joncs \(le parrain est un invit&eacute;\) : ([0-9][0-9]?) invit&eacute',
                productOptions)
            self.joncParrain = re.findall(' J\'ai un parrain : ([^,]*),', productOptions)
            if not self.joncParrain:
                self.joncParrain = re.findall(' J\'ai un parrain : ([^$]*)$', productOptions)
            self.joncParrainName = re.findall(
                'Nom de votre/vos parrain\(s\) \(Indiquer &quot;N/A&quot; si non applicable\) : (.*)$', productOptions)
            if not self.joncParrainName:
                self.joncParrainName = re.findall('Nom de votre/vos parrain\(s\) : (.*)$', productOptions)

            self.joncPrice += 25 * productQty
            self.joncTicketPrice += productOptionPrice + (1.50 * productQty)

            self.joncqty += productQty
            joncInviteTicketNum = 0
            if self.joncInvite:
                joncInviteTicketNum = int(self.joncInvite[0])
            self.joncTicketQty += productQty * (1 + joncInviteTicketNum)

        elif productId == 16:
            self.joncTicketQty += productQty
            self.joncTicketPrice += totalProductPrice

        elif productId == 14:
            self.casinoTicketNumber += productQty
            self.casinoPrice += totalProductPrice

        elif productId == 7:
            self.b1Occupation = re.findall('Variante : ([^,]*),', productOptions)
            if not self.b1Occupation:
                self.b1Occupation = re.findall('Variante : ([^$]*)$', productOptions)
            if not self.b1Occupation:
                self.b1Occupation = re.findall('Variation : ([^,]*),', productOptions)
            if not self.b1Occupation:
                self.b1Occupation = re.findall('Variation : ([^$]*)$', productOptions)

            self.b1C1 = re.findall('Nom Co-Chambreur 1 \(si applicable\) : ([^,]*),', productOptions)
            if not self.b1C1:
                self.b1C1 = re.findall('Nom Co-Chambreur 1 \(si applicable\) : ([^$]*)$', productOptions)

            self.b1C2 = re.findall('Nom Co-Chambreur 2 \(si applicable\) : ([^,]*),', productOptions)
            if not self.b1C2:
                self.b1C2 = re.findall('Nom Co-Chambreur 2 \(si applicable\) : ([^$]*)$', productOptions)

            self.b1C3 = re.findall('Nom Co-Chambreur 3 \(si applicable\) : ([^,]*),', productOptions)
            if not self.b1C3:
                self.b1C3 = re.findall('Nom Co-Chambreur 3 \(si applicable\) : ([^$]*)$', productOptions)

            self.b1price += totalProductPrice
            self.b1qty += productQty

        elif productId == 8:
            self.b2Occupation = re.findall('Variante : ([^,]*),', productOptions)
            if not self.b2Occupation:
                self.b2Occupation = re.findall('Variante : ([^$]*)$', productOptions)
            if not self.b2Occupation:
                self.b2Occupation = re.findall('Variation : ([^,]*),', productOptions)
            if not self.b2Occupation:
                self.b2Occupation = re.findall('Variation : ([^$]*)$', productOptions)

            self.b2C1 = re.findall('Nom Co-Chambreur 1 \(si applicable\) : ([^,]*),', productOptions)
            if not self.b2C1:
                self.b2C1 = re.findall('Nom Co-Chambreur 1 \(si applicable\) : ([^$]*)$', productOptions)

            self.b2C2 = re.findall('Nom Co-Chambreur 2 \(si applicable\) : ([^,]*),', productOptions)
            if not self.b2C2:
                self.b2C2 = re.findall('Nom Co-Chambreur 2 \(si applicable\) : ([^$]*)$', productOptions)

            self.b2C3 = re.findall('Nom Co-Chambreur 3 \(si applicable\) : ([^,]*),', productOptions)
            if not self.b2C3:
                self.b2C3 = re.findall('Nom Co-Chambreur 3 \(si applicable\) : ([^$]*)$', productOptions)

            self.b2AccompOccup = re.findall(', Accompagnateur : ([^,]*),', productOptions)
            if not self.b2AccompOccup:
                self.b2AccompOccup = re.findall(', Accompagnateur : ([^$]*)$', productOptions)

            self.b2AccompName = re.findall(', Nom accompagnateur \(si applicable\) : ([^,]*),', productOptions)
            if not self.b2AccompName:
                self.b2AccompName = re.findall(', Nom accompagnateur \(si applicable\) : ([^$]*)$', productOptions)

            self.b2Vege = re.findall('V&eacute;g&eacute;tarien : ([^,]*),', productOptions)
            if not self.b2Vege:
                self.b2Vege = re.findall('V&eacute;g&eacute;tarien : ([^$]*)$', productOptions)

            self.b2VegeAccomp = re.findall('V&eacute;g&eacute;tarien - Accompagnateur : ([^,]*),', productOptions)
            if not self.b2VegeAccomp:
                self.b2VegeAccomp = re.findall('V&eacute;g&eacute;tarien - Accompagnateur : ([^$]*)$', productOptions)

            self.allergie = re.findall('(Allergie.*)$', productOptions)
            if len(self.allergie) > 0:
                self.allergie[0] = self.allergie[0].replace(',', ' *ET*')

            self.b2price += totalProductPrice
            self.b2qty += productQty

        elif productId == 9:
            self.albumNum += productQty
            self.albumPrice += totalProductPrice

        elif productId == 11:
            self.activite = productOptions
            self.activitePrice += totalProductPrice
            self.activiteQty += productQty

        elif productId == 17:
            # coton ouaté - vert écriture jaune
            self.cotonVertQty += productQty
            self.cotonVertPrice += totalProductPrice
            self.cotonVertOption = productOptions

        elif productId == 18:
            # coton ouaté - noir écriture blanche
            self.cotonNoirQty += productQty
            self.cotonNoirPrice += totalProductPrice
            self.cotonNoirOption = productOptions

        elif productId == 19:
            # bock
            self.bockQty += productQty
            self.bockPrice += totalProductPrice
            self.bockOption = productOptions

        else:
            print("PLEASE PARSE : ", productId)

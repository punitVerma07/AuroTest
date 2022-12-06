from xml.dom import minidom

from queue import PriorityQueue

class Book:
    def __init__(self,name) -> None:
        self.buy = PriorityQueue()
        self.sell = PriorityQueue()
        self.name = name

    def buy(self,price,vol):
        self.buy.put((-1*price,vol))
        self.updateOrder()

    def sell(self,price,vol):
        self.sell.put((price,vol))
        self.updateOrder()

    def updateOrder(self):
        try:
            while(self.buy[0][0] >= -1*self.sell[0][0] ):
                if(self.buy[0][1] > self.sell[0][1]):
                    tempSell = self.sell.get()
                    tempBuy = self.buy.get()

                    self.buy.put((tempBuy[0],tempBuy[1]-tempSell[1]))
                elif(self.buy[0][1] == self.sell[0][1]):
                    tempSell = self.sell.get()
                    tempBuy = self.buy.get()
                else:
                    tempSell = self.sell.get()
                    tempBuy = self.buy.get()

                    self.buy.put((tempSell[0],tempSell[1]-tempBuy[1]))

            return True


        except:
            return False





class OrderBook:
    def __init__(self,xml_path) -> None:
        self.xml_path = xml_path

    def parse(self):
        file = minidom.parse(self.xml_path)
        models = file.getElementsByTagName('Addorder')


    def addOrder(self):
        pass

    def deleteOrder(self):
        pass

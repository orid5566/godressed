import datetime

class Item:
    def __init__(self,user,type,color,price,size,itemID,upload_date):
        self.user=user
        self.type=type
        self.color=color
        self.price=price
        self.size=size
        self.itemID=itemID
        self.upload_date=upload_date
from products import PRODUCTS

class Purchase:
    def __init__(self):
        self.cart={}

    def add_item(self, item, quantity):
        item=item.upper()
        if item not in PRODUCTS:
            return "ERROR_INVALID_ITEM"
        MQ=PRODUCTS[item]["MQ"]
        CQ=self.cart.get(item, 0)
        if CQ+quantity>MQ:
            return "ERROR_QUANTITY_EXCEEDED"
        self.cart[item]=CQ+quantity
        return "ITEM_ADDED"

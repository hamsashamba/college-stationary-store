from products import PRODUCTS

class Billing:
    def __init__(self, cart):
        self.cart=cart

    def calculate_bill(self):
        total_before_discount=0
        item_discount_total=0

        for key, value in self.cart.items():
            price=PRODUCTS[key]["Price"]
            discount_rate=PRODUCTS[key]["Discount"]
            total_before_discount+=price*value

        if total_before_discount>=1000:
            for key, value in self.cart.items():
                price=PRODUCTS[key]["Price"]
                discount_rate=PRODUCTS[key]["Discount"]
                item_discount_total+=price*value*discount_rate
        subtotal=total_before_discount-item_discount_total

        extra_discount=0
        if subtotal>=3000:
            extra_discount=subtotal*0.05
            subtotal-=extra_discount

        total_discount=item_discount_total+extra_discount

        tax=subtotal*0.10
        total_amount=subtotal+tax

        return round(total_discount, 2), round(total_amount, 2)

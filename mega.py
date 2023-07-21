class Product:
    def __init__(self,product,price):
        self.product=product
        self.price=price
        
class MegaSupermarket:
    def __init__(self):
        self.max_price=2000
        self.max_products=4
        self.cart=[]

    def get_product(self):
        return self.product
    
    def get_price(self):
        return self.price
    
    def verify_products(self,product):
        self.product=product
        if len(self.product) < self.max_products and self.price<=self.max_price:
            self.cart.append(product)
            return True
        return False
    
    def calculate_total_price(self):
        total_price=sum(product.get_price() for product in self.cart)
        return total_price
    
    def apply_discount(self,total_price):
        if total_price >=6000:
            discount_percent=(5/100)
        elif total_price >=3000:
            discount_percent=(3/100)
        else:
            discount_percent=0
        return discount_percent
    
    def calculate_final_amount(self):
        total_price=self.calculate_total_price()
        discount_percent=self.apply_discount(total_price)
        discount_amount=total_price*discount_percent
        final_amount=total_price-discount_amount
        return final_amount
    

def main():
    supermarket_mega=MegaSupermarket()
    for items in range(supermarket_mega.max_products):
        product_name=input("Enter the product name: ")
        product_price=float(input("Enter the product price in shillings: "))
        product=Product(product_name,product_price)

    final_amount=supermarket_mega.calculate_final_amount()
    print(f"Total Amount: {supermarket_mega.calculate_final_amount():.2f} shillings")
    print(f"Discount: {supermarket_mega.apply_discount(supermarket_mega.calculate_final_amount()):.0f}%")
    print(f"Final Amount to Pay: {final_amount:.2f} shillings")



if __name__ == "__main__":
    main()
    


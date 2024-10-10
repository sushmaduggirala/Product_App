class Product:
    all_products={}
    def __init__(self, id, category, name, price):
        self.id = id
        self.category = category
        self.name = name
        self.price = price
        self.all_products[self.id] = {"category":self.category, "name":self.name, "price":self.price}
        print("Product added successfully!!")
    
    @classmethod
    def UpdateProduct(self, id, price):
        if id in self.all_products:
            self.all_products[id]['price'] = price
            print("Product price updated successfully!!!")   
        else:
            print(f"No product available with {id}")
    
    @classmethod
    def DeleteProduct(self, id):
        if id in self.all_products:
            self.all_products.pop(id)
            print("Product deleted successfully..!!!")
        else:
            print(f"No product available with {id}")
        
    @classmethod
    def GetProductById(self, id):
        if id in self.all_products:
            print(self.all_products[id])
        else:
            print(f"No product available with id {id}")
    
    @classmethod
    def GetAllProducts(self):
        print(self.all_products)
    
    @classmethod
    def GetProductsByCategory(self, category):
        l = list(self.all_products.values())
        print(f"Products of {category} are: ")
        for i in l:
            if i['category']== category:
                print(i)
        else:
            print(f"No products with this category {category}")
    
    @classmethod
    def GetProductsBetweenPrices(self, a,b):
        l = list(self.all_products.values())
        for i in l:
            if i['price']>= a and i['price']<=b:
                print(i)
        else:
            print("No products in given range")
        


while(1):
    print('''
            1. Add Product
            2. Update Product
            3. Delete Product
            4. Get Product by PId
            5. Get All Products
            6. Get Products By Category
            7. Get Products between prices
            8. Exit''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Enter product details to add")
        id = int(input("Enter product id: "))
        category = input("Enter Category of the product: ")
        name = input("Enter name of the product: ")
        price = float(input("Enter price of the product: "))
        pro = Product(id, category, name, price)
    
    elif choice == 2:
        id = int(input("Enter id of product to be updated: "))
        price = float(input("Enter updated price: "))
        Product.UpdateProduct(id,price)
    
    elif choice == 3:
        id = int(input("Enter id of product to be deleted: "))
        Product.DeleteProduct(id)
        
    elif choice == 4:
        id = int(input("Enter id of product you want: "))
        Product.GetProductById(id)
        
    elif choice == 5:
        Product.GetAllProducts()
    
    elif choice == 6:
        category = input("Enter category to search: ")
        Product.GetProductsByCategory(category)
    
    elif choice == 7:
        a,b = map(int,input("enter range of prices separated with space").split())
        Product.GetProductsBetweenPrices(a,b)
    
    else:
        print("You chose to exit or invalid choice")
        break

class Category:
  def __init__(self, name, no_of_product, code):
    self.name = name
    self.no_of_product = no_of_product
    self.code = code

  def myfunc(self):
    print( self.name, self.code, self.no_of_product)

cat = Category("computer", 36, 6577)
cat.myfunc()

category1 = Category("Electronics", "E", 100)
category1.myfunc()
category2 = Category("Clothing", "C", 200)
category2.myfunc()
category3 = Category("Books", "B", 50)
category3.myfunc()

class Category:
    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products
    def show(self):
        return self.name, self.no_of_products


electronics_category = Category("Electronics", "ELEC", 100)


print("Category: " , electronics_category.name,"has" ,electronics_category.no_of_products,"Product")



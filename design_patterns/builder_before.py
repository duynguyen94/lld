class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product1 parts: {', '.join(self.parts)}", end="")


class Product2:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product2 parts: {', '.join(self.parts)}", end="")


# Client code
def build_products():
    product1 = Product1()
    product1.add("PartA1")
    product1.add("PartB1")
    product1.add("PartC1")

    product2 = Product2()
    product2.add("PartA2")
    product2.add("PartB2")
    product2.add("PartC2")

    return product1, product2


if __name__ == '__main__':
    # Usage
    product1, product2 = build_products()
    product1.list_parts()
    print()
    product2.list_parts()

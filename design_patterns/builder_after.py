from abc import ABC, abstractmethod


# Abstract Builder
class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


# Concrete Builder for Product1
class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")


# Concrete Builder for Product2
class ConcreteBuilder2(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product2()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA2")

    def produce_part_b(self):
        self._product.add("PartB2")

    def produce_part_c(self):
        self._product.add("PartC2")


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


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


# Usage
if __name__ == "__main__":
    director = Director()

    builder1 = ConcreteBuilder1()
    director.builder = builder1

    print("Standard basic product1: ")
    director.build_minimal_viable_product()
    builder1.product.list_parts()

    print("\n")

    print("Standard full featured product1: ")
    director.build_full_featured_product()
    builder1.product.list_parts()

    print("\n")

    builder2 = ConcreteBuilder2()
    director.builder = builder2

    print("Standard basic product2: ")
    director.build_minimal_viable_product()
    builder2.product.list_parts()

    print("\n")

    print("Standard full featured product2: ")
    director.build_full_featured_product()
    builder2.product.list_parts()

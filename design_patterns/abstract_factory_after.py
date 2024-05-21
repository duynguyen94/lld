from abc import ABC, abstractmethod


# Abstract Products
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


# Concrete Products
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"


class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern chair"


class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa"


class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a Modern sofa"


# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


# Concrete Factories
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


# Client code
def create_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.sit_on())
    print(sofa.lie_on())


if __name__ == '__main__':
    # Usage
    victorian_factory = VictorianFurnitureFactory()
    modern_factory = ModernFurnitureFactory()

    create_furniture(victorian_factory)
    create_furniture(modern_factory)

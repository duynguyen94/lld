# Refactor this using Abstract factory
class Chair:
    def sit_on(self):
        pass


class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"


class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern chair"


class Sofa:
    def lie_on(self):
        pass


class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa"


class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a Modern sofa"


# Client code
def create_furniture(style):
    if style == 'Victorian':
        chair = VictorianChair()
        sofa = VictorianSofa()
    elif style == 'Modern':
        chair = ModernChair()
        sofa = ModernSofa()
    else:
        raise ValueError('Unknown style')

    print(chair.sit_on())
    print(sofa.lie_on())


if __name__ == '__main__':
    # Usage
    create_furniture('Victorian')
    create_furniture('Modern')

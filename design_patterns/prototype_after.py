"""
After Refactoring with the Prototype Design Pattern
By applying the Prototype pattern, we introduce cloning methods to handle object duplication efficiently.
"""
import copy


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects

    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    # Client code
    component1 = SomeComponent(23, [1, 2, 3])
    component2 = component1.clone()
    component3 = component1.deep_clone()

"""
Before Using the Prototype Design Pattern
Suppose we have an application that needs to create many objects of similar types, and manually cloning these objects is
cumbersome. Without the Prototype pattern, we might have something like this
"""


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects


if __name__ == '__main__':
    # Client code
    component1 = SomeComponent(23, [1, 2, 3])
    component2 = SomeComponent(component1.some_int, component1.some_list_of_objects.copy())

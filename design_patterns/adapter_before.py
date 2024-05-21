"""
Scenario: Integrating a legacy system with a new interface
Imagine you have a legacy system that provides specific functionality through a class, but its interface is incompatible
with the new system you are developing. You want to integrate this legacy class without modifying its source code.
"""


class LegacyPrinter:
    def print_legacy(self):
        return "Printing from the legacy printer."


# Client code
def print_document():
    legacy_printer = LegacyPrinter()
    print(legacy_printer.print_legacy())


if __name__ == '__main__':
    # Usage
    print_document()

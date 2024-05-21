"""
After Using Adapter Pattern (Inheritance-based Adapter)
Key Differences and Benefits
- Decoupling: The adapter pattern decouples the client code from the legacy class, allowing you to change the legacy class
 or use a different one without modifying the client code.
- Single Responsibility Principle: The adapter class is responsible for adapting the interface, while the legacy class
 remains unchanged.
- Reusability: You can reuse the adapter class with different legacy classes that have similar functionality but
 incompatible interfaces.

The choice between inheritance and composition depends on your specific needs. Inheritance is straightforward but less
flexible, while composition offers greater flexibility and adheres more closely to the principle of composition over inheritance.
"""


class Target:
    def print(self):
        pass


class LegacyPrinter:
    def print_legacy(self):
        return "Printing from the legacy printer."


class PrinterAdapter(Target, LegacyPrinter):
    def print(self):
        return self.print_legacy()


# Client code
def print_document(printer: Target):
    print(printer.print())


if __name__ == '__main__':
    # Usage
    legacy_printer_adapter = PrinterAdapter()
    print_document(legacy_printer_adapter)

class Target:
    def print(self):
        pass


class LegacyPrinter:
    def print_legacy(self):
        return "Printing from the legacy printer."


class PrinterAdapter(Target):
    def __init__(self, legacy_printer: LegacyPrinter):
        self.legacy_printer = legacy_printer

    def print(self):
        return self.legacy_printer.print_legacy()


# Client code
def print_document(printer: Target):
    print(printer.print())


if __name__ == '__main__':
    # Usage
    legacy_printer = LegacyPrinter()
    legacy_printer_adapter = PrinterAdapter(legacy_printer)
    print_document(legacy_printer_adapter)

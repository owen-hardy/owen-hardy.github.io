class SymbolTable:
    def __init__(self):
        """Initialize symbol table with all predefined symbols."""
        self.symbols = {
            "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
            "SCREEN": 16384, "KBD": 24576
        }
        
        # Add registers R0 to R15
        for i in range(16):
            self.symbols[f"R{i}"] = i

        self.next_available_address = 16   # Variables start at RAM address 16

    def add_entry(self, symbol: str, address: int) -> None:
        """Add a new symbol (label or variable) and its address to the table."""
        self.symbols[symbol] = address

    def contains(self, symbol: str) -> bool:
        """Return True if the symbol exists in the table."""
        return symbol in self.symbols

    def get_address(self, symbol: str) -> int:
        """Return the address associated with the symbol.
        Raises ValueError if the symbol is not found."""
        if symbol not in self.symbols:
            raise ValueError(f"Symbol '{symbol}' not found in symbol table")
        return self.symbols[symbol]

    def add_variable(self, symbol: str) -> int:
        """Add a variable if it doesn't exist and return its RAM address.
        Variables are assigned sequentially starting at address 16."""
        if not self.contains(symbol):
            self.add_entry(symbol, self.next_available_address)
            self.next_available_address += 1
        return self.get_address(symbol)

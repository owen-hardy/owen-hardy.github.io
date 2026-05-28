from parser import Parser
from code import Code
from symbol_table import SymbolTable

class Assembler:
    """
    Translates a Hack assembly (.asm) file into a .hack binary file.
    """
    
    def __init__(self, input_file: str):
        self.input_file = input_file
        # Output file will have same name but .hack extension
        self.output_file = input_file.replace('.asm', '.hack')
        
    def assemble(self):
        """Main method: Perform two-pass assembly."""
        print(f"Assembling {self.input_file}...")

        # === PASS 1: Build Symbol Table (Labels only) ===
        parser = Parser(self.input_file)
        symbol_table = SymbolTable()
        instruction_address = 0

        while parser.has_more_lines():
            parser.advance()
            if parser.instruction_type() == 'L':
                label = parser.symbol()
                symbol_table.add_entry(label, instruction_address)
            else:
                instruction_address += 1

        # === PASS 2: Translate to Binary ===
        parser = Parser(self.input_file)  # Reset parser
        code = Code()
        binary_lines = []

        while parser.has_more_lines():
            parser.advance()
            itype = parser.instruction_type()

            if itype == 'A':
                symbol = parser.symbol()
                if symbol.isdigit():
                    address = int(symbol)
                else:
                    # This is the key fix: use add_variable for new symbols
                    address = symbol_table.add_variable(symbol)
                
                binary = f"0{address:015b}"

            elif itype == 'L':
                continue  # Labels are skipped in Pass 2

            else:  # C-instruction
                dest = code.dest(parser.dest())
                comp = code.comp(parser.comp())
                jump = code.jump(parser.jump())
                binary = f"111{comp}{dest}{jump}"

            binary_lines.append(binary)

        # Write output
        with open(self.output_file, 'w') as f:
            for line in binary_lines:
                f.write(line + '\n')

        print(f"Successfully assembled! Output: {self.output_file}")

# Main entry point
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python assembler.py <filename.asm>")
    else:
        assembler = Assembler(sys.argv[1])
        assembler.assemble()

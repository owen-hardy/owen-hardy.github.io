class Parser:
    """
    Parses a Hack assembly (.asm) file and provides access to its components.
    Removes whitespace and comments, then allows sequential access to instructions.
    """
    
    def __init__(self, filename: str):
        """
        Opens the .asm file, cleans it (removes whitespace and comments),
        and prepares the list of instructions.
        """
        self.filename = filename
        self.lines = []           # List of cleaned assembly lines
        self.current_line = -1    # Index of the current instruction (-1 = before first)
        self.current_instruction = ""  # The current instruction being processed
        
        self._load_and_clean_file()

    def _load_and_clean_file(self):
        """Private method: Read file and remove comments + whitespace."""
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                # Remove inline comments and whitespace
                line = line.strip()
                if line and not line.startswith('//'):
                    # Remove any comments that appear after code
                    if '//' in line:
                        line = line[:line.find('//')].strip()
                    if line:  # Only add non-empty lines
                        self.lines.append(line)

    def has_more_lines(self) -> bool:
        """Return True if there are more lines to process."""
        return self.current_line + 1 < len(self.lines)

    def advance(self) -> None:
        """Move to the next instruction in the file."""

        if self.has_more_lines():
            self.current_line += 1
            self.current_instruction = self.lines[self.current_line]

    def instruction_type(self) -> str:
        """ Returns the type of the current instruction:
        - 'A' for A-instruction (@Xxx)
        - 'C' for C-instruction (dest=comp;jump)
        - 'L' for Label ((Xxx))
        """
        instr = self.current_instruction.strip()
    
        if instr.startswith('@'):
            return 'A'
        elif instr.startswith('(') and instr.endswith(')'):
            return 'L'
        else:
            return 'C'

    def symbol(self) -> str:
        """Returns the symbol or decimal for current A-instruction or Label."""
        if self.instruction_type() not in ('A', 'L'):
            raise ValueError(f"symbol() called on invalid instruction type: {self.instruction_type()}")
    
        instr = self.current_instruction.strip()
    
        if self.instruction_type() == 'A':
            return instr[1:]           # Remove @
        else:  # Label
            return instr[1:-1]         # Remove ( and )

    def dest(self) -> str:
        """Returns the destination part of a C-instruction (e.g. 'D', 'M', 'MD').
        Returns empty string if no destination (e.g. '0;JMP')."""
        instr = self.current_instruction.strip()
    
        if self.instruction_type() != 'C':
            return ""
    
        if '=' in instr:
            return instr.split('=')[0].strip()
        else:
            return ""   # No destination


    def comp(self) -> str:
        """Returns the computation part of a C-instruction."""
        instr = self.current_instruction.strip()
    
        if self.instruction_type() != 'C':
            return ""
    
        # Case 1: dest=comp (e.g. D=M+1)
        if '=' in instr:
            return instr.split('=')[1].split(';')[0].strip()
    
        # Case 2: comp;jump (e.g. D;JGT)
        elif ';' in instr:
            return instr.split(';')[0].strip()
    
        # Case 3: Just comp (rare, but possible)
        else:
            return instr.strip()


    def jump(self) -> str:
        """Returns the jump part of a C-instruction.
        Returns empty string if no jump."""
        instr = self.current_instruction.strip()
    
        if self.instruction_type() != 'C':
            return ""
    
        if ';' in instr:
            return instr.split(';')[1].strip()
        else:
            return ""   # No jump

class Code:
    """
    Translates Hack assembly symbolic instructions into binary codes.
    The format of the binary code is:
    - A-instruction: 0vvvvvvvvvvvvvvv (where v is the value)
    - C-instruction: 111accccccdddjjj (where a, c, d, j are bits determined by the comp, dest, and jump mnemonics)
    """

    def __init__(self):
        # dest mnemonic -> 3-bit binary
        self.dest_table = {
            "":    "000",   # null
            "M":   "001",
            "D":   "010",
            "MD":  "011",
            "A":   "100",
            "AM":  "101",
            "AD":  "110",
            "AMD": "111"
        }

        # jump mnemonic -> 3-bit binary
        self.jump_table = {
            "":    "000",   # null
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }

        # comp mnemonic -> 7-bit binary (a c1..c6)
        self.comp_table = {
            "0":   "0101010",
            "1":   "0111111",
            "-1":  "0111010",
            "D":   "0001100",
            "A":   "0110000",
            "!D":  "0001101",
            "!A":  "0110001",
            "-D":  "0001111",
            "-A":  "0110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "D+A": "0000010",
            "D-A": "0010011",
            "A-D": "0000111",
            "D&A": "0000000",
            "D|A": "0010101",
            # When a=1 (use M instead of A)
            "M":   "1110000",
            "!M":  "1110001",
            "-M":  "1110011",
            "M+1": "1110111",
            "M-1": "1110010",
            "D+M": "1000010",
            "D-M": "1010011",
            "M-D": "1000111",
            "D&M": "1000000",
            "D|M": "1010101"
        }

    def dest(self, mnemonic: str) -> str:
        """Return 3-bit dest code."""
        return self.dest_table.get(mnemonic, "000")

    def comp(self, mnemonic: str) -> str:
        """Return 7-bit comp code."""
        return self.comp_table.get(mnemonic, "0000000")

    def jump(self, mnemonic: str) -> str:
        """Return 3-bit jump code."""
        return self.jump_table.get(mnemonic, "000")

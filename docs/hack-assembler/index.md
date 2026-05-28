# Hack Assembler

A complete two-pass Hack Assembler written in Python as part of the Nand to Tetris course.

## Files

- **[parser.py](parser.py)** - Parses Hack assembly instructions
- **[symbol_table.py](symbol_table.py)** - Handles symbols, labels, and variables
- **[code.py](code.py)** - Translates mnemonics to binary
- **[assembler.py](assembler.py)** - Main driver that coordinates the two-pass assembly process

## How to Run

```bash
python assembler.py <input.asm>

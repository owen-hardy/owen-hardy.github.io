# Building A Computer From Scratch: My Journey Learning Computer Architecture

**Author:** Owen Hardy  
**Date:** May 2026

## Introduction

As a recent Philosophy graduate from the University of California, Davis, I found myself with time between graduation and graduate school to deepen my technical knowledge. While I greatly enjoyed studying philosophy, I eventually realized that the field lacked the technical rigor and hands-on problem-solving I was craving.

The rapid advancement of Artificial Intelligence since the early 2020s particularly captivated me. I didn’t just want to use these powerful new tools — I wanted to understand how they actually worked at a fundamental level.

This realization prompted me to pivot from academic philosophy back to computer science, a path I had stepped away from during my sophomore year. I knew that to become a capable AI Engineer, I needed a strong foundation in both mathematics and low-level systems. Since late 2025, I’ve been rebuilding my programming skills in Python, C++, and SQL, while strengthening my knowledge of object-oriented programming, data structures, algorithms, and databases.

Yet as I developed my software engineering skills, I became increasingly curious about the lower levels of computing. How does code actually translate into electrical signals? How does a CPU work, and how does it interact with memory? To answer these questions from first principles, I enrolled in the renowned Nand to Tetris course by Noam Nisan and Shimon Schocken.

Nand to Tetris guides students through building a complete 16-bit computer — known as the “Hack” computer — starting from nothing but NAND gates. I chose this course because I wanted a true bottom-up understanding of computer architecture, from the lowest hardware level all the way up through higher abstractions. This project has become a cornerstone of my transition into Artificial Intelligence.

## The Nand To Tetris Hardware Journey

### 2.1 From NAND Gates to Basic Logic

The entire hardware journey in Nand to Tetris begins with one remarkably simple but powerful component: the NAND gate (short for “NOT AND”).

A NAND gate takes two binary inputs (0 or 1) and produces an output that is the opposite of an AND gate. In other words, it outputs 0 only when both inputs are 1. In every other case, it outputs 1.

What makes the NAND gate truly special is that it is a *universal gate* — every other logic gate can be built using nothing but NAND gates. From NAND, I first constructed the three fundamental gates:

- **NOT gate** (inverter): Connect both inputs of a NAND gate together. The output is the logical inverse of the input.
- **AND gate**: Take the output of a NAND gate and feed it into a NOT gate (`AND = NOT(NAND)`).
- **OR gate**: Use De Morgan’s law to combine inverted inputs (`OR = NOT(NAND(NOT(A), NOT(B)))`).

Once these basic gates were in place, I could build more complex components:

- **XOR gate**: Outputs true only when its two inputs differ.
- **Multiplexer (MUX)**: Selects one of two inputs based on a selector bit. It is essentially a controlled switch.
- **Demultiplexer (DMUX)**: The inverse of a MUX — routes a single input to one of two outputs based on a selector bit.

This early work revealed something profound: complex digital systems don’t require complex primitives. They only require the right combinations of very simple ones. Starting from just NAND gates gave me a genuine first-principles understanding of how all digital logic is ultimately constructed.

### 2.2 Boolean Arithmetic and the ALU

Once the basic logic gates were complete, the next challenge was moving from pure logic to actual arithmetic.

I began by building a Half Adder, which adds two single bits and produces a sum bit and a carry bit. Extending this design led to a Full Adder, which adds three bits (two inputs plus a carry-in from the previous stage). By chaining 16 Full Adders together, I created a complete 16-bit Adder capable of adding two 16-bit numbers.

The centerpiece of this stage was the **Arithmetic Logic Unit (ALU)** — the computational heart of the Hack CPU. The ALU takes two 16-bit inputs (`x` and `y`) and uses six control bits (`zx`, `nx`, `zy`, `ny`, `f`, `no`) to perform any one of 18 different operations. These control bits work as follows:

- `zx` and `nx`: Zero or negate the `x` input
- `zy` and `ny`: Zero or negate the `y` input
- `f`: Determines whether to compute `x + y` (arithmetic) or `x & y` (bitwise AND)
- `no`: Negates the final output

By cleverly manipulating these six bits, a relatively compact circuit gains enormous flexibility. The ALU can perform addition, subtraction, bitwise operations, and more — all controlled by simple binary signals.

This stage elegantly illustrated how hardware achieves generality through abstraction and control logic.

### 2.3 Sequential Logic: Registers and Memory

Up until this point, every circuit I built had been combinational — its output depended only on the current inputs. To create a real computer capable of storing state and executing instructions over time, I needed to introduce the concept of memory and the flow of time.

The fundamental building block of sequential logic is the **Data Flip-Flop (DFF)**. A DFF stores a single bit of information from one clock cycle to the next. On each rising edge of the clock signal, it captures the value at its input and holds it until the next cycle.

Using 16 DFFs in parallel, I built a **16-bit Register** — a basic memory unit capable of storing a full 16-bit value. These registers became the foundation for larger memory structures.

From there, I constructed **Random Access Memory (RAM)** — specifically a 16K × 16-bit memory module. This allowed the computer to store and retrieve data at any address using a 15-bit address bus. I also implemented the **Program Counter (PC)**, a special register that keeps track of the current instruction address. The PC can increment, reset, or load a new value depending on control signals.

This transition from combinational to sequential logic was a major turning point. It transformed the computer from a pure calculator into a machine that could remember past results and execute sequences of instructions over time — the true beginning of programmable computation.

## Deep Dive: Assembling the Hack Computer

The Hack computer is built on the **Von Neumann architecture**, the foundational model that underpins nearly every modern computer. Proposed by John von Neumann in 1945, this architecture is based on a simple but profound idea: both program instructions and data are stored in the same shared memory space.

This design choice carries deep philosophical and practical implications. By treating code and data as the same fundamental “substance,” the Von Neumann architecture enables incredible flexibility — the computer can load new programs dynamically, modify its own instructions if needed, and treat computation as a fluid, unified process. It trades some potential performance (the famous “Von Neumann bottleneck” where the CPU must constantly fetch instructions and data over the same bus) for simplicity, elegance, and generality. This unified memory model is why the architecture became the dominant standard: it makes computers easier to design, program, and reprogram.

### Memory System

I first constructed the complete memory system by combining the following components:

- **Instruction Memory (ROM)**: 32K × 16-bit read-only memory that stores the program
- **Data Memory (RAM)**: 16K × 16-bit read/write memory
- **Screen**: 8K × 16-bit memory-mapped display (256 × 512 pixels)
- **Keyboard**: A single 16-bit memory-mapped register for keyboard input

These components together form the complete memory architecture of the Hack computer.

### The Central Processing Unit (CPU)

The CPU was assembled using the previously built ALU, two 16-bit registers (A and D), several multiplexers, and control logic.

- The **A Register** can hold data, addresses, or constants.
- The **D Register** holds intermediate computation results.
- The **ALU** performs arithmetic and logical operations on the values in A and D.
- Multiplexers route data between the registers, ALU, memory, and instruction bus.

The Program Counter (PC) keeps track of the current instruction address and can increment, reset, or jump based on program flow.

Connecting the CPU to the memory system completed the Hack computer. At this point, the machine could run actual programs, marking the transition from individual hardware modules to a fully functional stored-program computer.

## Reflection & Takeaways

Completing Nand to Tetris and assembling the Hack computer from scratch was one of the most rewarding intellectual experiences I’ve had. As someone who built his first desktop computer at fourteen, I had always understood computers at a surface level. This course finally gave me the deep, low-level understanding I had been missing for years.

### Key Technical Insights

The most striking realization was how something as systematically complex as a computer can be built from a component as rudimentary as a NAND gate. From basic logic gates, we climbed a ladder of abstraction: building the ALU, registers, RAM, and finally integrating the CPU and memory into a complete stored-program machine.

I also gained a much deeper appreciation for the elegance of the Von Neumann architecture and why its unified memory model became the dominant standard in computing.

Two of the most valuable lessons I learned were the power of modularity and the discipline of persistence through complex debugging. By designing each major component — from basic logic gates to the ALU, registers, and memory system — as independent modules with clean, well-defined interfaces, even the construction of an entire computer became comprehensible. At the same time, the project repeatedly tested my patience. There were numerous moments when the hardware simulator produced mysterious errors, forcing me to trace signals and isolate problems one gate at a time. These experiences taught me that successful system design depends as much on thoughtful architecture as it does on the willingness to push through repeated failures.

### Connection to My Future in AI

While I have a personal preference for working at higher levels of abstraction, a solid understanding of low-level systems is what separates a good AI engineer from a great one. This knowledge is crucial for optimization, model efficiency, debugging AI hallucinations, and ensuring systems meet security and alignment standards.

Nand to Tetris was a beautifully insightful and satisfyingly challenging course. For the first time, I can look at a computer and truly understand how and why it works. Instead of seeing a CPU or RAM stick as mysterious black boxes, I can explain their fundamental operation from first principles.

This project has inspired me to continue deepening my knowledge of computer architecture. The fourteen-year-old version of myself would be proud of how far this journey has come.
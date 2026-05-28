# Amortized Analysis Explained: How Dynamic Arrays Achieve Constant-Time Appends

**Author:** Owen Hardy  
**Date:** May 2026

## Introduction

For anyone familiar with data structures and algorithms, time complexity is a fundamental metric for designing and analyzing algorithms. Worst-case and best-case analyses tell us the most and least expensive individual operations, but they don’t always reflect real-world performance. This is where **amortized analysis** becomes valuable: it reveals the *average cost per operation* over a long sequence of actions.

While working through UC San Diego’s Data Structures and Algorithms Specialization, amortized analysis quickly became the topic that confused and intrigued me the most. It elegantly explains why real-world dynamic arrays — such as Python’s `list` or Java’s `ArrayList` — can deliver constant-time append operations in practice, even though individual operations can occasionally be expensive.

In this document, I break down the core concepts behind amortized analysis using dynamic arrays as the primary example. I cover the three main methods (Aggregate, Accounting, and Potential), compare different growth strategies, and reflect on why amortized analysis is such a powerful tool for building efficient systems, including those used in AI and large-scale data processing.

## The Problem with Naive Dynamic Arrays

One of the most commonly used data structures in programming is the dynamic array. Unlike a fixed-size array, it automatically grows as new elements are added. In languages like Python and Java, dynamic arrays appear to support constant-time append operations.

However, this apparent efficiency hides an important catch. When a dynamic array runs out of space, it must allocate a larger block of memory and copy all existing elements into the new array. This resize operation is expensive — its cost is proportional to the current size of the array.

If we analyze this behavior using traditional worst-case analysis, every append operation could potentially cost **O(n)** time, because a resize might occur on any given insertion. This makes dynamic arrays seem inefficient on paper, even though in practice they perform very well for most use cases.

This mismatch between theoretical worst-case analysis and real-world performance is exactly why amortized analysis is such a valuable tool. It allows us to understand the *true average cost* of operations over a long sequence of appends, rather than focusing only on the occasional expensive resize.

## What Is Amortized Analysis?

Amortized analysis is a technique used to determine the *average cost per operation* over a long sequence of operations, rather than focusing solely on the worst-case cost of any single operation.

While traditional worst-case analysis is useful for guaranteeing performance bounds, it can be overly pessimistic for data structures whose expensive operations are rare. Amortized analysis gives us a more realistic picture of efficiency in practice by spreading the cost of occasional expensive operations across many cheap ones.

There are three primary methods for performing amortized analysis:

- The **Aggregate Method** calculates the total cost of a sequence of *n* operations and divides by *n*.
- The **Accounting Method** (also called the Banker’s Method) assigns “credits” to cheap operations to pay for future expensive ones.
- The **Potential Method** uses a potential function to measure “stored energy” in the data structure.

Each method has its strengths depending on the problem, but they all aim to answer the same question: what is the true average cost of each operation when viewed over the long run?

In the case of dynamic arrays, amortized analysis reveals why appending elements is effectively **O(1)** time in practice, even though occasional resizes cost **O(n)**.

## The Three Main Methods of Amortized Analysis

There are three primary techniques used to perform amortized analysis. Each method approaches the same problem from a different angle, but they all aim to calculate the average cost per operation over a long sequence.

### The Aggregate Method

The simplest approach is the **Aggregate Method**. We calculate the total cost of a sequence of *n* operations and then divide by *n* to find the amortized cost per operation.

**Example with dynamic arrays (doubling strategy):**  
When an array doubles in size, the expensive resize operation costs *O(n)*. However, after a resize, the next *n* appends are cheap (*O(1)* each). Over a long sequence, the expensive resizes become infrequent enough that the average cost per append drops to **O(1)**.

$$\text{Amortized Cost} = \frac{1}{n} \sum_{i=1}^{n} c_i$$

*Figure 1: Aggregate Method — total cost divided by number of operations*

### The Accounting Method (Banker’s Method)

The **Accounting Method** is more intuitive for many people. We assign “credits” to cheap operations to save up for future expensive ones.

In the dynamic array example:
- Each append is charged **2 credits**.
- 1 credit pays for the actual append operation.
- The second credit is saved in the “bank” to pay for future resizes.

When a resize occurs, the saved credits cover the entire cost of copying elements. This way, every operation appears to cost a constant amount, even though some operations are more expensive behind the scenes.

$$\text{Charge per append} = 2 \quad \Big(1 \text{ for the actual append} + 1 \text{ saved for future resize}\Big)$$

*Figure 2: Accounting (Banker’s) Method — credit system for dynamic arrays*

### The Potential Method

The **Potential Method** is the most mathematically elegant. It uses a **potential function** Φ that measures the “stored energy” or “unpaid work” in the data structure.

The amortized cost of an operation is defined as:

$$\text{Amortized Cost} = c_i + \Delta \Phi$$

*Figure 3: Potential Method — amortized cost equals actual cost plus change in potential*

For dynamic arrays with doubling, a common potential function is:

$$\Phi = 2 \times \text{current size} - \text{current capacity}$$

*Figure 4: Potential function for dynamic arrays with 2× growth*

This method is especially powerful when the potential function is chosen carefully, as it can give very tight bounds.

## Deep Dive: Dynamic Arrays with Geometric Growth

The classic example used to teach amortized analysis is the dynamic array that grows by doubling its capacity each time it becomes full.

Imagine we start with an array of size 1. As we append elements, the array eventually fills up and must resize:

- When it reaches size 1 → resize to 2 (copy 1 element)
- When it reaches size 2 → resize to 4 (copy 2 elements)
- When it reaches size 4 → resize to 8 (copy 4 elements)
- And so on...

Here is the cost breakdown for the first 16 append operations:

| n (Appends) | Resize Cost | Total Cost | Amortized Cost |
|-------------|-------------|------------|----------------|
| 1           | 1           | 1          | 1.0            |
| 2           | 2           | 3          | 1.5            |
| 4           | 4           | 7          | 1.75           |
| 8           | 8           | 15         | 1.875          |
| 16          | 16          | 31         | 1.9375         |

As you can see, even though some operations are expensive, the average cost per append approaches **O(1)** as *n* grows.

### How the Three Methods Explain This Behavior

**1. Aggregate Method**  
We simply sum the total cost of *n* operations and divide by *n*:

$$\text{Amortized Cost} = \frac{1}{n} \sum_{i=1}^{n} c_i$$

For doubling arrays, the total cost of *n* appends is less than *2n*, so the amortized cost is **O(1)**.

**2. Accounting Method (Banker’s Method)**  
We assign **2 credits** to each append:
- 1 credit pays for the current append.
- 1 credit is saved for future resize operations.

When a resize occurs, the saved credits pay for the entire copy operation. This keeps the amortized cost constant at 2 per operation.

**3. Potential Method**  
We define a potential function Φ that tracks “stored energy”:

$$\Phi = 2 \times (\text{current size}) - (\text{current capacity})$$

The amortized cost of each operation becomes:

$$\text{Amortized Cost} = \text{Actual Cost} + \Delta \Phi$$

This potential function elegantly balances the expensive resizes with the cheap appends that follow them.

## Growth Factor Comparison (2× vs 4× vs Real-World)

So far we have focused on the classic **2× doubling** strategy taught in most textbooks. But what happens if we choose a different growth factor?

The choice of growth factor creates an interesting engineering trade-off between time efficiency and memory usage. Here is how the three most relevant strategies compare:

| Growth Factor | Amortized Append Cost | Resize Frequency | Memory Waste | Real-World Usage              |
|---------------|-----------------------|------------------|--------------|-------------------------------|
| **2×**        | O(1)                  | Moderate         | Moderate     | Most textbook examples        |
| **4×**        | O(1)                  | Lower            | Higher       | Occasionally used             |
| **~1.125×**   | O(1)                  | Higher           | Lower        | Python’s `list` (CPython)     |

Interestingly, CPython does **not** use pure 2× doubling for large lists. Instead, it uses an overallocation strategy with an effective growth factor of approximately **1.125×** (or 9/8).

This smaller growth factor reduces memory waste while still maintaining **O(1)** amortized append time. It is a practical engineering decision that balances time efficiency and memory usage — showing that real-world implementations often favor more conservative growth to save memory at the cost of slightly more frequent (but still cheap) resizes.

In practice, as long as the growth factor is a constant greater than 1, the amortized cost remains **O(1)**. The main difference lies in the memory–time trade-off each strategy makes.

## Reflection & Takeaways

Amortized analysis was one of the most useful and satisfying topics I’ve encountered while working through UC San Diego’s Data Structures and Algorithms Specialization. Most discussions around algorithms focus heavily on worst-case or best-case time complexity, but amortized analysis finally answered the question I had been wondering about: what is the *real-world average* cost of an operation over time?

I found the **Accounting Method** (Banker’s Method) particularly intuitive. Using the idea of “credits” to pay for future expensive resizes felt like a practical, functional way to think about dynamic allocation. It made the math click for me in a way the other methods didn’t at first.

What truly fascinates me is how data structures like dynamic arrays can achieve such elegant efficiency. By using geometric growth, we can build structures that are fast in both time and memory usage on average, even though individual operations can occasionally be expensive. As someone who uses Python heavily, I now have a much better mental model for what’s happening behind the scenes when I append to a list or grow an array in my own projects.

### Key Takeaways

- Amortized analysis bridges the gap between theoretical complexity and practical performance.
- Simple design choices, like geometric resizing, can lead to surprisingly powerful efficiency guarantees.
- Understanding these concepts deeply helps me write better technical explanations and make more informed engineering decisions.

This topic has reinforced my belief that low-level systems knowledge is incredibly valuable, even (and especially) when working at higher levels of abstraction in AI and software engineering. It’s another reminder that the best tools are often built on clever, well-understood fundamentals.

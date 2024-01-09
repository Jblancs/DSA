# Two Pointer

## Pattern
Pattern uses 2 pointers to iterate over an array or list until conditions of the problem are satisfied.

- Allows you to keep track of values of 2 idexes in a **single iteration**
- Pointers can be used to iterate data structures in one or both directions

### Does my problem match this pattern?
**Yes if:**
- input data can be traversed in a linear fashion (array, linked list, string)
- We limit focus to specific range of elements within input data, as dictated by two pointers

Additionally problems usually involve comparing or swapping values pointed by 2 indexes

**No if:**
- input cannot be traversed in linear fashion
- problem requires exhaustive search of solution space (eliminating 1 solution does not eliminate others)

## Real-world problems
- **Memory Management:** Two pointers are vital for memory allocation and deallocation. Start pointer moves forward, designating a new memory block. Start pointer is shifted backward, marking deallocated memory as available for future allocations.

- **Product suggestions:** When shopping cart doesn't qualify for free shipping, suggest items that would bring to the require amount.

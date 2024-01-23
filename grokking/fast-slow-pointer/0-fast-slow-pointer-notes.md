# Fast and Slow Pointer

## Pattern
Pattern uses two pointers to traverse an iterable data structure at different speeds.
- Used to identify distinguishable features of directional data structures such as **LINKED LISTS** or **ARRAYS**
- Used to determine data structure traits using indices in arrays or node pointers in linked list
- Commonly used to **detect cycles in given datta structure**
- Pointers start at same location

**Slow Pointer**
- Generally moves forward by a factor of 1

**Fast Pointer**
- Moves by a factor of two in each step

## Does my problem match this pattern?

**Yes if:**
- problem requires first x% of elements in linked list
- problem requires element at k-way point in list (middle element of start of 2nd quartile)
- problem requires kth last element in linked list
- detect cycle in linked list or sequence of symbols

**No if:**
- data cannot be traversed in linear fashion
- problem can be solved with 2 pointers traversing array at same pace

## Real-World Problems

**Symlink verification:** A symbolic link is a shortcut to another file. This can detect loops in symlinks by moving along connected files or directories at diff speeds

**Compiling an object-oriented program:** There might be cyclic dependencies that can lead to error from compililation of different files

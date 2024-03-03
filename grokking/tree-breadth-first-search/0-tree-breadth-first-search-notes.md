# Tree Breadth-first Search

Important for finding node in tree that satisfies the given constraints.
- Starts by search root node **moves down level by level** exploring adjacent nodes at level k + 1.
- Helps in efficiently finding neighbor nodes (ex. peer-to-peer networking)

## Does my problem match this pattern?

Yes if:
- We have reason to believe that a solution is near the root of the tree
- The solution dictates traversing the tree one level at a time

No if:
- tree being searched is very wide
- we have reason to believe the solution is near the leaves of the tree

## Real World Problems

Traversing DOM Tree I
- Need to figure out a way to traverse the DOM structure that we obtain from single web page

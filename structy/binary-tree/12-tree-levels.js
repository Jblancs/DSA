// Write a function, treeLevels, that takes in the root of a binary tree. The function should return a 2-Dimensional array where each subarray represents a level of the tree.

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const treeLevels = (root) => {
    if(root === null)return []

    let result = []

    let stack = [[root,0]]
    while(stack.length > 0){
        [node, level] = stack.pop()

        if(!result[level]){
            result[level] = []
        }

        result[level].push(node.val)

        if(node.right){
            stack.push([node.right,level+1])
        }
        if(node.left){
            stack.push([node.left,level+1])
        }
    }

    return result
  };

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

console.log(treeLevels(a)); // ->
// [
//   ['a'],
//   ['b', 'c'],
//   ['d', 'e', 'f']
// ]

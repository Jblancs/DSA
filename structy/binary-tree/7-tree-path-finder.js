// Write a function, pathFinder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return null.

// You may assume that the tree contains unique values.

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const pathFinder = (root, target) => {
    let result = pathFinderHelper(root, target)

    if(result === null){
        return false
    }else{
        return result.reverse()
    }
  };

const pathFinderHelper = (root, target) => {
    if(root === null) return null
    if(root.val === target) return [root.val]

    let left = pathFinderHelper(root.left, target)
    if(left !== null){
        left.push(root.val)
        return left
    }

    let right = pathFinderHelper(root.right, target)
    if(right !== null){
        right.push(root.val)
        return right
    }

    return null
}


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

  console.log(pathFinder(a, 'e')); // -> [ 'a', 'b', 'e' ]

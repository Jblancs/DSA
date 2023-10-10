// Write a function, linkedListValues, that takes in the head of a linked list as an argument. The function should return an array containing all values of the nodes in the linked list.

// Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive! -AZ

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const linkedListValues = (head) => {
    let result = []

    let current = head
    while(current){
        result.push(current.val)
        current = current.next
    }

    return result

  };

  const a = new Node("a");
  const b = new Node("b");
  const c = new Node("c");
  const d = new Node("d");

  a.next = b;
  b.next = c;
  c.next = d;

  // a -> b -> c -> d

  console.log(linkedListValues(a)); // -> [ 'a', 'b', 'c', 'd' ]

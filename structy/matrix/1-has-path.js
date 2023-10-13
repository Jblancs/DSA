// Write a function, hasPath, that takes in an object representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

// Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

const hasPath = (graph, src, dst) => {
    let stack = [src]

    while(stack.length > 0){
        let current = stack.pop()

        for(let neighbor of graph[current]){
            if(neighbor === dst){
                return true
            }else{
                stack.push(neighbor)
            }
        }
    }

    return false
  };

  const graph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
  };

  console.log(hasPath(graph, 'f', 'k')); // true

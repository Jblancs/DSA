// Write a function, undirectedPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB). The function should return a boolean indicating whether or not there exists a path between nodeA and nodeB.

const undirectedPath = (edges, nodeA, nodeB) => {
    let graph = {}

    // populates graph using edges array
    for(let edge of edges){
        [a, b] = edge
        if(!(a in graph)){
            graph[a] = []
        }
        if (!(b in graph)){
            graph[b] = []
        }

        graph[a].push(b)
        graph[b].push(a)
    }

    // traverse using depth first algo
    let visited = new Set()
    visited.add(nodeA)
    let stack = [nodeA]

    while(stack.length > 0){
        let current = stack.pop()

        for(let neighbor of graph[current]){
            if(neighbor === nodeB){
                return true
            }else if(!visited.has(neighbor)){
                visited.add(neighbor)
                stack.push(neighbor)
            }
        }
    }

    return false
};

const edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
  ];

  console.log(undirectedPath(edges, 'j', 'm')); // -> true

  const edges1 = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
  ];

   console.log(undirectedPath(edges1, 'm', 'j')); // -> true

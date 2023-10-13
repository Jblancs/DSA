// Write a function, longestPath, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.

const longestPath = (graph) => {
    let distance = {}

    for(let node in graph){
        if(graph[node].length === 0){
            distance[node] = 0
        }
    }

    for(let node in graph){
        explorePath(node, graph, distance)
    }

    return Math.max(...Object.values(distance))
  };

  const explorePath = (node, graph, distance) => {
    let pathLength = 0
    let stack = [node]

    while(stack.length > 0){
        let current = stack.pop()

        if(!(current in distance)) distance[current] = pathLength
        else pathLength = distance[current]

        for(let neighbor of graph[current]){
            stack.push([neighbor])
            distance[neighbor] = pathLength+1
        }
    }

  }

  const graph = {
    a: ['c', 'b'],
    b: ['c'],
    c: []
  };

  console.log(longestPath(graph)); // -> 2

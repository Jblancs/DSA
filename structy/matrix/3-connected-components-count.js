// Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

const connectedComponentsCount = (graph) => {
    let visited = new Set()
    let count = 0

    for(let key in graph){
        if(!visited.has(key)){
            visited.add(key)
            count += 1
            explore(key, graph, visited)
        }
    }

    return count
  };

const explore = (node, graph, visited) => {
    let queue = [node]

    while(queue.length > 0){
        let current = queue.shift()

        for(let neighbor of graph[current]){
            let stringNeighbor = String(neighbor)
            if(!visited.has(stringNeighbor)){
                visited.add(stringNeighbor)
                queue.push(stringNeighbor)
            }
        }
    }
}

  console.log(connectedComponentsCount({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
  })); // -> 2

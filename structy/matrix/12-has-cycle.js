// Write a function, hasCycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle.

const hasCycle = (graph) => {
    let visiting = new Set()
    let visited = new Set()

    for (let node in graph) {
        if (!visited.has(node)) {
            let cycle = cycleFound(node, graph, visiting, visited)
            if (cycle) {
                return true
            }
        }
    }

    return false
};

const cycleFound = (node, graph, visiting, visited) => {
    let stack = [node]

    while (stack.length > 0) {
        let current = stack.pop()

        if(graph[current].length > 0){
            for (let neighbor of graph[current]) {
                if(visiting.has(neighbor)) return true
                stack.push(neighbor)
                visiting.add(neighbor)
            }
            
        }else{
            for (let value of visiting) {
                visited.add(value)
            }
            visiting.clear()
        }
    }


    return false
}

console.log(hasCycle({
    a: ["b"],
    b: ["c"],
    c: ["a"],
})); // -> true

console.log(hasCycle({
    a: ["b", "c"],
    b: ["c"],
    c: ["d"],
    d: [],
  })); // -> false

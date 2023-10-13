// Write a function, bestBridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.

const bestBridge = (grid) => {
    let visited = new Set()
    let islandFound = false

    for(let row=0; row < grid.length; row++){
        for(let col=0;col < grid[0].length; col++){
            if(grid[row][col] === "L"){
                explore(row,col,grid,visited)
                islandFound = true
                break
            }
        }
        if(islandFound) break
    }

    // find best bridge
    let queue = []
    for(let val of visited){
        [r,c] = val.split(",")
        queue.push([Number(r),Number(c),0])
    }

    while(queue.length > 0){
        [r,c,dist] = queue.shift()

        let deltas = [[-1,0],[0,1],[1,0],[0,-1]]
        for(let delta of deltas){
            [rowDelta,colDelta] = delta
            let neighborRow = r+rowDelta
            let neighborCol = c+colDelta

            if(inbounds(neighborRow,neighborCol,grid) && !visited.has(`${neighborRow},${neighborCol}`)){
                if(grid[neighborRow][neighborCol] === "L"){
                    return dist
                }
                visited.add(`${neighborRow},${neighborCol}`)
                queue.push([neighborRow,neighborCol,dist+1])
            }
        }

    }

  };

  const explore = (row,col,grid,visited) => {
    let stack = [[row,col]]
    visited.add(`${row},${col}`)

    while(stack.length > 0){
        [r,c] = stack.pop()

        let deltas = [[-1,0],[0,1],[1,0],[0,-1]]
        for(let delta of deltas){
            [rowDelta,colDelta] = delta
            let neighborRow = r+rowDelta
            let neighborCol = c+colDelta

            if(inbounds(neighborRow,neighborCol,grid) && !visited.has(`${neighborRow},${neighborCol}`) && grid[neighborRow][neighborCol] === "L"){
                visited.add(`${neighborRow},${neighborCol}`)
                stack.push([neighborRow,neighborCol])
            }
        }
    }
  }

  const inbounds = (row,col,grid) => {
    let rowIn = 0 <= row && row < grid.length
    let colIn = 0 <= col && col < grid[0].length
    return rowIn && colIn
  }

  const grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
  ];
  console.log(bestBridge(grid)); // -> 1

  const grid2 = [
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["L", "L", "W", "W", "L"],
    ["W", "L", "W", "W", "L"],
    ["W", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W"],
  ];
  console.log(bestBridge(grid2)); // -> 2

  const grid3 = [
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["L", "W", "W", "W", "W"],
  ];
  console.log(bestBridge(grid3)); // -> 3

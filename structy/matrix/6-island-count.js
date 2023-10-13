// Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

const islandCount = (grid) => {
    let visited = new Set()
    count = 0

    for(let row = 0; row < grid.length; row++){
        for(let col = 0; col < grid[0].length; col++){
            if(grid[row][col] === "L" && !visited.has(`${row},${col}`)){
                visited.add(`${row},${col}`)
                exploreIsland(row,col,grid,visited)
                count += 1
            }
        }
    }

    return count
  };

  const exploreIsland = (row,col,grid,visited) => {
    let stack = [[row,col]]

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
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
  ];

  console.log(islandCount(grid)); // -> 3

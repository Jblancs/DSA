// Write a function, closestCarrot, that takes in a grid, a starting row, and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.

const closestCarrot = (grid, startRow, startCol) => {
    let visited = new Set()
    let queue = [[startRow, startCol,0]]
    visited.add(`${startRow},${startCol}`)

    while(queue.length > 0){
        [r,c,distance] = queue.shift()

        let deltas = [[-1,0],[0,1],[1,0],[0,-1]]
        for(let delta of deltas){
            [rowDelta,colDelta] = delta
            let neighborRow = r+rowDelta
            let neighborCol = c+colDelta

            if(inbounds(neighborRow,neighborCol,grid) && !visited.has(`${neighborRow},${neighborCol}`) && grid[neighborRow][neighborCol] !== "X"){

                if(grid[neighborRow][neighborCol] === "C"){
                    return distance + 1
                }

                visited.add(`${neighborRow},${neighborCol}`)
                queue.push([neighborRow,neighborCol,distance+1])
            }
        }
    }

    return -1

  };

  const inbounds = (row,col,grid) => {
    let rowIn = 0 <= row && row < grid.length
    let colIn = 0 <= col && col < grid[0].length
    return rowIn && colIn
  }

  const grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
  ];

  console.log(closestCarrot(grid, 1, 2)); // -> 4

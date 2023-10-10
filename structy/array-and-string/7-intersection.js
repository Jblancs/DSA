// Write a function, intersection, that takes in two arrays, a,b, as arguments. The function should return a new array containing elements that are in both of the two arrays.

// You may assume that each input array does not contain duplicate elements.

const intersection = (a, b) => {
    let result = []
    let setA = new Set(a)

    for(let val of b){
        if(setA.has(val)){
            result.push(val)
        }
    }

    return result
  };

console.log(intersection([4,2,1,6], [3,6,9,2,10])) // -> [2,6]

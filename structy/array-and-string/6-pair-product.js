// Write a function, pairProduct, that takes in an array and a target product as arguments. The function should return an array containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

// Be sure to return the indices, not the elements themselves.

// There is guaranteed to be one such pair whose product is the target.

const pairProduct = (numbers, targetProduct) => {
    let prevNums = {}

    for(let i = 0; i < numbers.length; i++){
        let num = numbers[i]
        let comp = targetProduct/num

        if(comp in prevNums) return [prevNums[comp], i]

        prevNums[num] = i
    }
  };

  console.log(pairProduct([3, 2, 5, 4, 1], 8)); // -> [1, 3]

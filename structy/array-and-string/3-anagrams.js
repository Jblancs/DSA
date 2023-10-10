// JavaScript Solution
// separate for loop create hash map for first string
// separate for loop to iterate through s2
// key into hash map and decrement value -1
// if key undefined return false
// separate for loop to iterate through hash map
// if any value != 0 return false
// return true

const anagrams = (s1, s2) => {
    let hash1 = {}
    for (let char of s1){
        if (!(char in hash1)){
            hash1[char] = 0
        }
        hash1[char] += 1
    }

    for (let char of s2){
        if (hash1[char] === undefined){
            return false
        }else{
            hash1[char] -= 1
        }
    }

    for (let char in hash1){
        if (hash1[char] !== 0){
            return false
        }
    }

    return true
  };

console.log(anagrams('restful', 'fluster')); // -> true

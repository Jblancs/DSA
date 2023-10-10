
const mostFrequentChar = (s) => {
    let hashmap = {}
    for(let char of s){
        if(!(char in hashmap)){
            hashmap[char] = 0
        }
        hashmap[char] += 1
    }

    most_freq = null
    for(let char in hashmap){
        if(most_freq === null){
            most_freq = char
        }
        if(hashmap[most_freq] < hashmap[char]){
            most_freq = char
        }
    }

    return most_freq
  };


  console.log(mostFrequentChar('bookeeper')); // -> 'e'
  console.log(mostFrequentChar('david')); // -> 'd'
  console.log(mostFrequentChar('mississippi')); // -> 'i'

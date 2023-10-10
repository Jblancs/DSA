// JavaScript Solution
// create result string and initialize to ''
// create i and j variable and initialize to 0
// i and j are in place holders
// while loop to iterate while j <= s.length
// if s[i] == s[j] increment j
// else create num = j - i (difference is how many of that char there is)
// in else if num == 1 result += s[i]
// else result += num + s[i]
// set i = j
// return result

const compress = (s) => {
    let result = []
    let i = 0
    let j = 0

    while (j <= s.length) {
        if (s[i] === s[j]) {
            j += 1

        } else {
            const num = j - i
            if (num === 1) {
                result.push(s[i])
            } else {
                result.push(String(num), s[i])
            }
            i = j
        }

    }
    return result.join('')
}

console.log(compress('ccaaatsss')); // -> '2c3at3s'

arr = ['jason', 'justin', 'dan'];
function changeArray(a) {
  // Write a function that updates elements of an array in 2 ways. 1) Return all characters UPPERCAASE and Sort them
  // Example: changeArray(['jason', 'justin', 'dan']) returns 'DAN', JASON', 'JUSTIN'
    let result = []

    for(let name of a){
        result.push(name.toUpperCase())
    }

    result.sort()

  return result;
}
console.log(changeArray( arr ));

dt = '2022-05-24';
function dayOfYear(dt) {
  // Write a function that takes a date string (ISO Format YYYY-MM-DD) as argument. (example: '2019-01-31')
  // return the nth day of the year
  // Example 1: dayOfYear( '2019-09-01' ) returns 244
  // Example 2: dayOfYear( '2022-01-31' ) returns 31
  // Example 3: dayOfYear( '2022-12-31' ) returns 365

  return dt;
}
dayOfYear(dt);

start = '2021-08-10T15:14:00';
finish = '2021-08-10T15:16:00';
function timeDiff(a,b) {
  // Write a function that takes two Date/TIME strings in ISO Format as argument
  // It should return the hours:minutes:seconds between the two
  // Expect that either the start or end time can come first.
  // Example: timeDiff( '2023-08-10T15:14:00', '2023-08-10T15:16:00' ) returns 00:02:00
  a = '2021-08-10T15:14:00'; b = '2021-08-10T15:16:00';
    let msA = Date.parse(a)
    let msB = Date.parse(b)
    let diff;
    if(msA > msB) diff = msA - msB
    if(msA < msB) diff = msB - msA

    const secs = diff/1000
    
  return 'calculation';
}
timeDiff(start,finish);

a = [1,2,5,10];
b = 9;
function sumSomeArrayElements(a,b) {
  // Write a function that takes an array (a) and a number (b) as arguments
  // Sum up all array elements with a value less than b + 1
  // Example: sumSomeArrayElements( {1,2,5,10}, 9) returns 8

  let sum = 0
  for(let num of a){
    if(num < b+1){
        sum += num
    }
  }

  return sum;
}
console.log(sumSomeArrayElements(a, b));

a = ['Saleo','demo','two'];
function returnLongestString(a) {
  // Write a function that takes an array of strings as argument
  // Return the longest string
  // If multiple matches, return them all
  // Example: returnLongestString({'Saleo', 'demo', 'two'}) returns 'Saleo'
  let longest = 0
  for(let string of a){
    if( string.length > longest ){
        longest = string.length
    }
  }

  let result = a.filter(el => el.length === longest)
  if (result.length === 1) return result[0]
  return result


}
returnLongestString(a)

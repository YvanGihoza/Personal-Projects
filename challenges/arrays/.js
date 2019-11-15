function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    for (i = 1; i < 1000000; i++) {
    //since we have a boundary, in this case we can easily use the method
    //includes(), which determines whether an array includes a certain value
    if(!A.includes(i)) return i;
  }
}

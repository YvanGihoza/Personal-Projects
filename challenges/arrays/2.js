function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let newArr = [];
    for (let i = 0; i < A.length; i++)
    {
        //if the value is positive store it in the new array
        if (A[i] > 0)
            newArr[A[i]] = true;
    }
    //now go through the new array and find a number which is not defined
    //and print it
    for(let i = 1; i <= newArr.length; i++)
    {
        if (undefined === newArr[i])
            return i;
    }
    //if the array is populated by negative numbers
    return 1;
}

// loop can execute a block of code
// a number of times until a certain condition is met

// for loop
// while loop
// do while loop
// for in loop
// for of loop

//for loop
for (let i = 0; i < 5; i++) {
    console.log("The value of i is: " + i);
}

//while loop
let j = 0;
while (j <5) {
    console.log("The value of j is: " + j);
    j++;
}

//do while loop
let k = 0;
do {
    console.log("The value of k is " + k);
    k++;
} while (k < 5);

//for in loop
const person = {fname: "Muzammil", lname: "Waris", age: 25};

for (let x in person) {
    console.log(x + ": " + person[x]);
}

//for of loop
const cars = ["BMW", "Volvo", "Mini"];
for (let car of cars) {
    console.log(car);
}

let len = cars.length;
let reply = "";
for (let i = 0; i < len;  i++){
    reply += cars[i] + " ";
}
console.log(reply);

let message = "";
let r = 0;
while (r < len) {
    message += cars[r] +  " "; 
    r++;
}
console.log(message);

// do while, runs at leaset once even if 
let t = 0;
do {
    console.log("The value of t is " + t);
    t++;
} while (t > 5);

// break and continue
// continue skips and jumpts to next iteration

//infinite loop
/* let m = 0
while (m < 5){
    console.log("The value of m is " " + m")
    }
*/

for (let n = 0; n < 10, n++ ; ) {
    if (n == 4){ continue; }// skips 4
    if (n == 7){ break;} //stops at 7
    console.log("The value of n is:" + n);

}

/*
for (let i = 0; i < 5; i++) {
    console.log("The value of i is: " + i);
}
*/


//1. Print numbers 1 to 10.
for (let o=1; o < 11; o++ ) {
    console.log(o);
}

//2. Print even numbers 1-20.
for (let z=1; z < 21; z++) {
    if (z % 2 == 0){
        console.log(z)
    }
}

//3. Print odd numbers 1-20.
for (let x=1; x < 21; x++){
    if (x % 2 == 1) {
        console.log(x)
    }
}

//4. Print multiplcation table of 7.
for (let x=7; x < 71; x++ ) {
    if (x % 7 == 0) {
        console.log(x)
    }
}

//5. Print numbers 10-->1 (reverse).
for (let x=10; x > 0; x--){
    console.log(x)
}

//6. Print numbers 1-5
for (let x =1; x < 6; x++){
    console.log(x)
}

//7. Print sum of numbers 1-10.
sum = 0
for (let x = 1; x < 11; x++){
    sum += x;
    console.log(sum)
}

//8. Print multiples of 3 up to 30.
for (let x=3; x < 31; x++){
    if (x % 3 == 0){
        console.log(x)
    }
}

/*
let j = 0;
while (j <5) {
    console.log("The value of j is: " + j);
    j++;
}
*/

//9. Keep dividing a number by 2 until it becomes less than 1.


//10. Print factorial of a number using while.
let num = 5;
factorial = 1
while (num !=0){
    factorial *= num
    num--;    
}
console.log(factorial)

//13. Start from 1 and keep doubling until > 100
let x = 1; 
while (x < 100) {
    x = x * 2;
    if (x < 100){
        console.log(x);
    }
}

//14. Keep subtracting 5 from a number until it reaches 0.
let number = 57;
while (number >= 0){
    console.log(number)
    number -= 5;
    
}

//15. Print first 10 Fibonacci numbers.
/*
let f = 1;
let myarray = [0,1];
while (f <= 34){
    for (let i = 2, i)
    myarray.push(f);    
    f = myarray[i - 1] + myarray[i-2];
}
    */

/*
for (let n = 0; n < 10, n++ ; ) {
    if (n == 4){ continue; }// skips 4
    if (n == 7){ break;} //stops at 7
    console.log("The value of n is:" + n);

}
*/


//16. Print numbers 1-10 but stop at 7 (break)
let s = 1;
while (s < 11){
    if (s==7){
    break;
    }
    console.log(s);
    s++
}

//17. Print numbers 1-10 but skip 5 (continue)

for (x=1; x < 11; x++){
    if (x==7){continue;}
    console.log(x)
}

//18. Keep asking for a number until you get a 0. (Break)
/*
let input = prompt("Please enter a number: ")
while (input != 0){
    input;
}*/

//19. Print numbers 1-20 but only show odd numbers (use continue to skip even numbers)
for (h=1; h<21; h++){
    if (h % 2 == 0){continue;}
    console.log(h);
}

//20. Print numbers 1-50 but stop when you reach first number divisible by 13.
for (x=1; x<51; x ++) {
    if (x % 13 == 0){break;}
    console.log(x);
}
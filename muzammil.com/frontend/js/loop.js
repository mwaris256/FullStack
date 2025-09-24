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
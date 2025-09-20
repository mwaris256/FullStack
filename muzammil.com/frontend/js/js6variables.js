// let is for variable declaration and initialization
// const is for constant variable declaration and initialization
// var is old way of variable declaration and initialization, avoid using var

// Block scope new let const
// Global scope var let const
// function scope


let a = 10; // global scope
console.log(a);
{
let a = 10; // block scope
const b = 20; 
// const b = 25; // block scope
var c = 30; // global scope
console.log(a);
console.log(b);
let x = 15;
//let x = 20; cannot be re-declared
//console.log(c);

const d = [1,2,3,4,5];
d.push(6);
console.log(d);
}

{let k = 100;
    {
      let k = 200;
      console.log(k);//prints 200   
    }
    console.log(k);//prints 100  
}


const m = 32;
m = 33;
console.log(m);

//console.log(a);
//console.log(c);
//a is not accessible
//b is not accessible
//c is accessible

// variable let cannot be re-declared
// var can be re-declared

let x = 10;
// let x = 20; // cannot be re-declared
x = 20; // reinitialization
console.log(x);

var y =10;
var y = 20; // can be re-declared

//hoisting
name = 'John'; // initialization
var name; // declaration

subject = "javascript"; // initialize
let subject; // declaration
console.log(name);
console.log(subject);

const pi = 3.14; // constant variable
//pi = 3.15; // cannot be re-initialized
//const pi = 3.15; // cannot be re-declared
console.log(pi);


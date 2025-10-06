// number can be negative or positive
// number can be whole or decimal
// maximum number length can be 64 digits
// number can be infinity or -infinity
// number can be NaN (not a number)

let num1 = 123; //012
let num2 = 12.56 // decimal/float
let num3 = -456 // negative number
let num4 = 1.2e3 // 1.2 * 10^3 = 1200
let num5 = 0xFF; // hexadecimal (255 in decimal)
let num6 = 0b1010; // binary (10 in decimal)
let num7 = 0o12// octal (10 in decimal)
let nu8 = Infinity; // infinity
let num9 = -Infinity; // -infinity
let num10 = NaN; // not a number

num1= num1.toString();
console.log(typeof num1);
console.log(typeof 768);

console.log(Number.isInteger(num2));

console.log(num2.toExponential(2));

console.log(num2.toFixed(2));
console.log(num2.toPrecision());
console.log(num3.valueOf());

console.log(typeof Number(num1)); //"18"
console.log(new Date("1970-01-01"));

console.log(parseInt("10 years"));

console.log(parseFloat("10 years"));

let x = Number.EPSILON;
console.log(x);

// Big integer
let z = 12345678901234567890123456789012345678901234567890;
let y = 12345678901234567890123456789012345678901234567890n;

z = BigInt(z);
console.log(z);
console.log(typeof y);
console.log(typeof z);

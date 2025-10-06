/*
Functions are fundamental building blocks in Javascript
A function is a set of statements that performs a task or calculates a value
To use a function, you must define it somewhere in the scope from which you wish to call it.
A function definition (also called a function declaration, or function statement) consists of the function keyword, followed by:
1. The name of the function.
2. A list of parameters to the function, enclosed in parentheses and separated by commas.
3. The JavaScript statements that define the function, enclosed in curly brackets, { }.
*/

// Function Declaration
function welcome(name, age) {
    console.log("Hello " + name + "!" + age);
}

welcome("Muzammil",20);
welcome("Ali", );
welcome("Ahmed", 25);

// Function Expression
let welcomeMessage = function(name, age){
    console.log("Hello " + name + "!" + age);

}

welcomeMessage("Waris", 22);
welcomeMessage("Ahsan", 21);    
welcomeMessage("Asad", 23);

// Arrow Function
let sum = (a, b) => {
    return a + b;
}   
console.log(sum(5, 10));

let sum1 = (a, b) => a + b;         
console.log(sum1(15, 10));
let square = x => x * x;
console.log(square(5));


// parameters: we declared
// arguments: we passed

// 1. Greet function

function greet(){
    console.log("Hello, welcome to Javascript!");

}

greet();

// 2. Add function

function add(a,b){
    return a + b;
    
}

console.log(add(5,10));

//3. Muiltiply 

function multiply(a,b) {
    return a * b;
}

console.log(multiply(6,4));

//4. Square
function squared(n){
    return n * n;
}

console.log(squared(6));

//5. isEven
function isEven(n){
    return n % 2 == 0;
}

console.log(isEven(10));
console.log(isEven(4));
console.log(isEven(7));

//6. ToUpperCaeName
function toUpperCaseName(name){
    return name.toUpperCase();
}

console.log(toUpperCaseName("muzammil waris"));

//7. findLength

function findLength(str){
    return str.length;

}

console.log(findLength("Muzammil"));

//8.areaofCircile
function areaOfCircle(r){
    return Math.PI * r * r;
}

console.log(areaOfCircle(5));

//9 converttoCelcius
function converttoCelcius(fahrenheit){
    return (fahrenheit - 32) * 5/9;
}

console.log(converttoCelcius(100));

//10. converttoFahrenheit
function converttoFahrenheit(celcius){
    return (celcius * 9/5) + 32;
}

console.log(converttoFahrenheit(37));

//11. addBigInts
function addBigInts(a, b){
    return a + b;
}   
console.log(addBigInts(12345678901234567890n, 98765432109876543210n));

//12. subtractBigInts
function subtractBigInts(a, b){
    return a - b;
}
console.log(subtractBigInts(98765432109876543210n, 12345678901234567890n));

//13. Compare
function compare(a, b){
    if(a > b){
        return a + " is greater than " + b;
    }   else if(a < b){
        return a + " is less than " + b;
    } else{
        return a + " is equal to " + b;
    }
}
console.log(compare(10, 20));
console.log(compare(30, 20));
console.log(compare(10, 10));

//14. factorial
function factorial(n){
    for (let i = n - 1; i >= 1; i--){
        n = n * i;
    }
    return n;
}

console.log(factorial(5));
console.log(factorial(6));
console.log(factorial(7));

//15. isPrime
function isPrime(n){
    if (n <= 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++){
        if (n % i == 0) return false;
    }       
    return true;
}
console.log(isPrime(11));
console.log(isPrime(15));
console.log(isPrime(17));
console.log(isPrime(18));
console.log(isPrime(19));
console.log(isPrime(20));

//16. Fullname

function fullName(firstName, lastName){
    return firstName + " " + lastName;
}   
console.log(fullName("Muzammil", "Waris"));

//17. average

function average(a,b,c){
    return (a + b + c) / 3;

}
console.log(average(10,20,30));
console.log(average(5,15,25));
console.log(average(7,14,21));

//18. maxofThree
function maxOfThree(a,b,c){
    return Math.max(a,b,c);
}   
console.log(maxOfThree(10,20,30));
console.log(maxOfThree(5,15,25));
console.log(maxOfThree(7,14,21));   

//19. reverseString
function reverseString(str){
    return str.split("").reverse().join("");
}

console.log(reverseString("Muzammil"));
console.log(reverseString("Waris"));
console.log(reverseString("JavaScript"));

//20. countVowels
function countVowels(str){
    let count = 0;
    let vowels = "aeiouAEIOU";
    for (let char of str){
        if (vowels.includes(char)){
            count++;
        }
    }
    return count;
}

console.log(countVowels("Muzammil"));
console.log(countVowels("Waris"));
console.log(countVowels("JavaScript"));

//21. isPositive
function isPositive(n){
    if (n == 0){
        return "Zero"
    }
    else if (n > 0){
        return "Positive"
    }
    else {
        return "Negative"
    }
}
console.log(isPositive(10));
console.log(isPositive(-5));
console.log(isPositive(0));

//22. getGrade
function getGrade(marks){
    if (marks >= 90){
        return "A"
    } else if (marks >= 80){
        return "B"
    }
    else if (marks >= 70){
        return "C"
    }   
    else if (marks < 70){
        return "Fail"
    }

}
console.log(getGrade(95));
console.log(getGrade(85));
console.log(getGrade(75));
console.log(getGrade(55));  

//23. power
function power(base, exponent){
    return Math.pow(base, exponent);
}
console.log(power(2,3));
console.log(power(3,4));
console.log(power(5,2));

//24. simpleInterest
function simpleInterest(principal, rate, time){
    return (principal * rate * time) / 100;
}
console.log(simpleInterest(1000,5,2));
console.log(simpleInterest(2000,7,3));

//25. isPalindrome
function isPalindrome(str){
    let reversed = str.split("").reverse().join("");
    return str === reversed;
}
console.log(isPalindrome("madam"));
console.log(isPalindrome("hello"));
console.log(isPalindrome("racecar"));
console.log(isPalindrome("javascript"));
a = 10;
b = 20;

if (a > b) {
    console.log("a is les than b");
    if (a + b == 50) {
        console.log("a + b is equal to 50");
    }
} else if (a ==b) {
    console.log("a is equal to b");
} else {
    console.log("a is greater than b");
}

/*
switch(express) {
    case 1: 
        console.log("this is case 1");
        break;
    case 2:
        console.log("this is case 2");
        break;
    case 3:
        console.log("this is case 3");
        break;
    default:
        console.log("this is default case");
    }*/

// ternary operator
condition = (a > b) ? "a is less than b" : "a is greater than or equal to b";
console.log(condition);

let hour = 7;
if (hour < 8){
    greeting = "Good morning";
    console.log(greeting);
}


/*
let age = 18;
let answer = "you can not drive";

if (age >= 18) {
    answer = "you can drive";
} else {
    answer = "you can not drive";
}
console.log(answer);
*/


//ontario, quebec, manitoba, saskatchewan, alberta, british columbia
let stuage = 15;
let province = "ontario";
let ticket = "ticket not issued";

if (province == "ontario") {
    if (stuage >= 16){
        ticket = "ticket not issued";
    } else {
        ticket = "ticket issued";
    }
} else if (province == "quebec") {
    if (stuage <= 16) {
        ticket = "ticket not issued";
    } else {
        ticket = "ticket issued";
    }
}
console.log(ticket);

marks = 64;
let grades = (marks >= 80) ? "A+" : (marks < 80 && marks >= 70) ? "A" : (marks < 70 && marks >= 60) ? "B" : (marks < 60 && marks >= 50) ? "C" : "D";

console.log(grades);

// switch case, control flow , if else alternative

switch (new Date().getDay()){
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
        break;
    default:
        day ="Today";
}
console.log(`Today is ${day}`);


switch (new Date().getDay()){
    case 0:
    case 6:
        text = "Today is the Weekend";
        break;
    case 1:
    case 2:
        text = "Weekend is far away";
        break;
    case 3:
    case 4:
        text = "Weekend is coming up";
        break;
    case 5:
        text = "Today is Friday";
    default:
        text ="Today";
}
console.log(text);


/*
let stuage = 15;
let province = "ontario";
let ticket = "ticket not issued";

if (province == "ontario") {
    if (stuage >= 16){
        ticket = "ticket not issued";
    } else {
        ticket = "ticket issued";
    }
} else if (province == "quebec") {
    if (stuage <= 16) {
        ticket = "ticket not issued";
    } else {
        ticket = "ticket issued";
    }
}
console.log(ticket);
*/


// 1. Check if a number is positive or negative
/*let n = 0;
let number = ""

if (n > 0) {
    (number = "positive");
} else if (n < 0) {
    (number = "negative");
} else {
    (number = "zero");
}
console.log(number);

*/

// 2. Check if a number is even or odd
/*

let n = 11
let number = ""

if (n % 2 == 0) {
    number = "even";
} else if (n % 2 == 1) {
    number = "odd";
}
console.log(number)
*/

// 3. Compare two numbers and print the larger one.

/*let num1 = 32;
let num2 = 18;

if (num1 > num2) {
    console.log(num1);
} else {
    console.log(num2)
}

*/

// 4. Check if a number is divisible by 5

n = 10
result = ""

if (n % 5 == 0) {
    result = "is divisible by 5"
} else {
    result = "is not divisible by 5"
} 
console.log(result);

// 5. Check if age >= 18 --> "Adult" else "Minor"

let age = 11;
text = "";

if (age >= 18) {
    text = "Adult"
} else {
    text = "Minor"
}
console.log(text);

// 6. Print Grade for Marks

let mark = 65;
grade = ""

if (mark >= 90){
    grade = "A";
} else if (mark >= 80 && mark <= 89) {
    grade = "B"
} else if (mark >= 70 && mark <= 79) {
    grade = "C"
} else {
    grade = "Fail"
}
console.log(grade);

// 7. Check if a year is a leap year
year = 2025


if (year % 400 == 0) {
    text = "leap year";
} else if (year % 400 != 0) {
    if (year % 100 == 0) {
        text = "not a leap year";
    } else if (year % 4 == 0) {
        text = "leap year";
    } else {
        text = "not a leap year"
    }
} 
console.log(text)

// 8. Check if a character is a vowel or consonant
char = "m"
const vowels = ["a","e","i","o","u"]

if (vowels.includes(char)) {
    text = "It's a vowel"
} else {
    text = "It's a consonant"
}
console.log(text)

//9. Compare three numbers and print the largest.

let num1 = 222;
let num2 = 35;
let num3 = 112;

if (num1 > num2 && num3){
    console.log(num1)
} else if (num2 > num3){
    console.log(num2)
} else {
    console.log(num3)
}

//10. Print morning, afternoon, evening, or night based on hours.
switch (new Date().getHours()){
    case (hour >= 0 && hour <=6):
    case (hour >= 20 && hour <=23):
        time = "Night";
        break;
    case (hour >= 7 && hour <=12):
        time = "Morning";
        break;
    case (hour >= 13 && hour <=17):
        time = "Afternoon";
        break;
    case (hour >= 18 && hour < 20):
        time = "Evening";
        break;
    default:
        time ="Time";
}
console.log(time);

//11. Print day of week

switch (new Date().getDay()){
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
        break;
    case 7:
        day = "Sunday";
        break;
    default:
        day ="Today";
}
console.log(day)

//12. Print month name

switch (new Date().getMonth()){
    case 1:
        month = "January";
        break;
    case 2:
        month = "February";
        break;
    case 3:
        month = "March";
        break;
    case 4:
        month = "April";
        break;
    case 5:
        month = "May";
        break;
    case 6:
       month = "June";
        break;
    case 7:
        month = "July";
        break;
    case 8:
        month = "August";
        break;
    case 9:
        month = "September";
        break;
    case 10:
        month = "October";
        break;
    case 11:
        month = "November";
        break;
    case 12:
        month = "December";
        break;
    default:
        month ="Today";
}
console.log(month)

//13.Print traffic signal meaning 

traffic = "green";
let signal = (traffic == "red") ? "Stop" : (traffic == "yellow") ? "Wait" : (traffic == "green") ? "Go": "";

console.log(signal);

//14. Print fruit price based on fruit name.

fruit = "banana";
let price = (fruit=="apple") ? "$4" : (fruit=="orange") ? "$3" : (fruit=="banana") ? "$2.50" : "";

console.log(price)

//15. Print season based on month number.

switch (new Date().getMonth()){
    case 1:
    case 2:
    case 12:
        season = "Winter";
        break;
    case 3:
    case 4:
    case 5:
        season = "Spring";
        break;
    case 6:
    case 7:
    case 8:
    season = "Summer";
        break;
    case 9:
    case 10:
    case 11:
    season = "Fall";
        break;
    default:
        season ="Today";
}
console.log(season)

//16. Check if number > 100 --> "Big" else "Small"

num = 43;
let checknum = (num > 100) ? "Big" : (num <= 100) ? "Small" : "";

console.log(checknum);

//17. Check if string is empty or not 

let mystring = ""

if (mystring.length != 0) {
    text = "String is not empty"
} else {
    text = "String is empty"
}
console.log(text);

//18. Check if age >= 60 --> Senior Citizen else not Senior

age = 58;
if (age >= 60) {
    text = "Senior Citizen"
} else {
    text = "Not Senior"
}
console.log(text);

//19. Check if the number is divisible by 2 and 3 --> "Yes" else "No"

num = 9;
if (num % 2 == 0 && num % 3 == 0){
    text = "Yes"
} else {
    text = "No"
}
console.log(text);

//20. Check if the temperature > 30 --> "Hot" else "Cold"

temperature = 31;
if (temperature > 30) {
    text = "Hot"
} else {
    text = "Cold"
}
console.log(text);
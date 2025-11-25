//let text = "Unknown";

text = ""

/*
if (age >= 18) {
    text = "Adult";
} else {
    text = "Minor";
}*/


// Repeat flow until a condition (i < 5) is false
for (let i= 0; i < 5; i++) {
    text += "The number is " + i + " ";
}
console.log(text)


// Terminate (break) the loop when the counter is 3
for (let i = 0; i < 10; i++) {
    if (i === 3) { break; }
    text += "The number is " + i + " ";
}

// Function to compute the product of two numbers

function myFunction(p1,p2) {
    return p1 * p2
}

console.log(myFunction(4,7));

//<button onclick="displayDate()">The time is?</button>

function myDisplayer(some) {
    document.getElementById("demo").innerHTML = some;
}

function myCalculator(num1,num2,myCallback){
    let sum = num1 + num2;
    myCallback(sum);
}

myCalculator(5,5,myDisplayer);
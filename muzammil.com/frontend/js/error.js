// 4 types of Errors
// 1. Syntax Error
// 2. Runtime Error (also known as Reference Error)
// 3. Logical Error
// 4. Compilation Error

// Syntax Error 
console.log('Hello World');

// Runtime Error
/*
console.log(undeclaredVariable);
*/

//Logical Error
let a = 10;
let b = 20;
let sum = a - b; // should be a+b
console.log("Sum is " + sum);

try {
    if (b===0) {
        throw new Error("Division by zero is not allowed");
    }
} catch(error) {
    console.log("An error occurred: " + error.message);
}

//Compilation Error
//Only occurs in languages like C, C++, Java
//Javascript is an integretated langauge, so it does not have compilation 
//errors in the traditional sense

let num = 18;
console.log(num);

//try catch
try {
    console.log(undeclaredVar);
} catch(error){
    console.log("An error occured: " + error.message);
} finally {
    console.log("This will always execute");
}

try {
    console.log("Trying to execute code");
} catch(error) {
    console.log("Caught an error: " + error.message);
}

//1. 

try {
    console.log("Before Error");
    throw "something went wrong!";
} catch (error) {
    console.log("Caught error:", error);
}

//2. 

try {
    console.log(x);
} catch (erorr) {
    console.log("Error handled safely");
}


//3. 

num = 11; 

try {
    num.toUpperCase();
} catch (error) {
    console.log("Error has occurred: " + error.message);
}

//4.

try {
    eval("alert(hello)");
} catch (error) {
    console.log("invalid code detected");
}

//5. 

function checkName(name) {
    try {
        if (name === "") {
            throw new Error ("name cannot be empty");
        }
        console.log("Name is valid: ", name);
    } catch (error) {
        console.log(error.message);
    }
}

checkName("");
checkName("Muzammil");

//6.

function checkAge(age) {
    try {
        if (age < 18) {
            throw new Error("Underage not allowed");
        }
        console.log("Access granted");
    } catch (error) {
        console.log(error.message);
    }
}

checkAge(12);
checkAge(25);

//7. 

function validateEmail(email) {
    try {
        if (!email.includes("@")) {
            throw new Error("Invalid Email");
        }
        console.log("Valid Email");
    } catch (error) {
        console.log(error.message);
    }
}

validateEmail("mwaris256.com");
validateEmail("mwaris256@gmail.com");

//8. 

try{
    console.log("This is a valid statement");
    console.log(undefinedVariable);
    console.log((42).toLowerCase());
} catch (error) {
    console.log("error found, continuing safely in javascript");

}

//9. 

try {
    console.log(undeclaredVar);
} catch (error) {
    console.log("An error occurred " + error.message);
} finally {
    console.log("This will always execute");
}

//10.

function nestedTryCatch() {
    try {
        console.log("Outer try block");
    try {
        console.log("Inner try block");
        throw new Error ("Error thrown in inner try block");
    } catch (innerError) {
        console.log(" Inner catch block caught:", innerError.message);
    } finally {
        console.log("Inner finally block executed");

    }

    console.log("Outer try block continues after inner try");
    } catch (OuterError) {
        console.log("Outer catch block caught:", OuterError.message);
    } finally {
        console.log("Outer finally block executed");
    }
}

nestedTryCatch()

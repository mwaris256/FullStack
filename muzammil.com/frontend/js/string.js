let name = "Muzammil";
let sname = "Waris";
let number = "256";

console.log(name.length);

let sentence = "we are \"Pakistanis\" but live in Canada" //escape character
console.log(sentence);
/* 
\b backscape
\f form feed
\n new line
\r return
\t horizontal tabulator
\v vertical tabulator

.length  \\string method

*/

let char = sname.charAt(5);
console.log(char);

let charr = sname.charCodeAt(0);
console.log(charr);

/*

at()
codepointAt()
name[4];
*/

let country = "Pakistan";
let future = "win";
//concatenate

let sdf = country.concat(" ","will"," ",future);
console.log(sdf);

console.log(sdf.slice(8)); //  will win
console.log(sdf.substring(8)); //will win
console.log(name.toUpperCase()); //MUZAMMIL
console.log(sname.toLowerCase()); //waris

console.log(sentence.isWellFormed());
console.log(name.trimEnd());

let num = "5";
let padded = num.padStart(4, "0");
console.log(padded);
console.log(num.repeat(4));

//searching
console.log(sdf.lastIndexOf("will"));
console.log(sdf.indexOf("will"));
console.log(sdf.search("will"));

console.log(sdf.match("ill"));
console.log(sdf.matchAll("will"));

console.log(sdf.includes("will"));
console.log(sdf.includes("willl"));

console.log(sdf.startsWith("will"));
console.log(sdf.startsWith("Pakistan"));

console.log(sdf.endsWith("will"));
console.log(sdf.endsWith("win"));

//1. Store your full name in a string and print its length.

fullname = "Muzammil Waris"
console.log(fullname.length);

//2. Print the first and last character of a given string

console.log(fullname.charAt(0));
console.log(fullname.charAt(fullname.length - 1));

//3. Convert a string "hello world" into uppercase.

string1 = "hello world";
console.log(string1.toUpperCase());

//4. Convert a string "JAVASCRIPT" into lowercase.

string2 = "JAVASCRIPT";
console.log(string2.toLowerCase());

//5. Concatenate two strings: "Hello" and "Student".

string3 = "Hello";
string4 = "Student";

let sdg = string3.concat(" ",string4);
console.log(sdg);

//6. Extract "World" from "Hello World" using slice().

console.log(string1.slice(6,11));

//7. Extract "World" from "Hello World" using substring().

console.log(string1.substring(6,11));

//8. Extract "World" from "Hello World" using substr().

console.log(string1.substr(6,5));

//9. Replace "bad" wth "good" in "This is a bad day".

string5 = "This is a bad day";
console.log(string5.replace("bad","good"));

//10. Repeat "Hi" 5 times

string6 = "Hi";
console.log(string6.repeat(5));

//11. Trim the spaces from " Javascript " and print result

string7 = " Javascript ";
console.log(string7.trim());

//12. Pad the string "5" to make it "005".

let pad = num.padStart(3, "0");
console.log(pad);

//13. Pad the string "7" to make it "700" (from right).

num2 = "7";
let pad2 = num2.padEnd(3,"0");
console.log(pad2);

//14. Find the index of "world" in Hello world, welcome".

string8 = "Hello world, welcome"
console.log(string8.indexOf('world'));

//15. Check if welcome exists inside "Hello world, welcome"

console.log(string8.includes("welcome"));

//16. Find the last occurrence of "is" in "This is a test. It is fun."

string9 = "This is a test. It is fun."
console.log(string9.lastIndexOf("is"));

//17. Use startsWith() to check if 'Javascript" starts with "Java".

string10 = "Javascript"
console.log(string10.startsWith("Java"));

//18. Use endsWith() to check if "Learning.js" ends with ".js".

string11 = "Learning.js"

console.log(string11.endsWith(".js"));

//19. Split "apple,banana,orange" into an array of fruits

string12 = "apple,banana,orange"
console.log(string12.split(","));

//20. Join ["HTML","CSS","JS"] into a single string "HTML-CSS-JS"

languages = ["HTML","CSS","JS"]
console.log(languages.join("-"));

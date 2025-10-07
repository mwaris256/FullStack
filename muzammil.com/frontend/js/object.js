// object is a variable that stores many variables
/*
const car = {type: "sedan",
     color: "black",
      model: 2025};
console.log(car);
console.log(car.type);
console.log(car.color);
console.log(car.model);
*/

let student = {};

student.name = "Muzammil";
student.age = 20;
student.isStudent = true;

let student2 = {
name :"Muzammil",
age: 30,
isStudent: true};



console.log(student);
console.log(student.name);
console.log(student.age);
console.log(student.isStudent);

keys = Object.keys(student);
values = Object.values(student);
console.log(keys);
console.log(values);

for ([key,value] of Object.entries(student)){
    console.log(`${key}: ${value}`);
}

Object.assign(student,student2);
console.log(student);

/*
let person = new Object();
person.firstName = "John";
person.lastName = "Doe";
person.age = 25;


console.log(person);
console.log(person.firstName);
console.log(person.lastName);
console.log(person.age);


// delete object property
delete person.age;
console.log(person);
console.log(person.age); // undefined

console.log(person["firstName"]);
*/

// function constructor
function newPerson(fname, lname, age, color, language){
    this.firstName = fname;
    this.lastName = lname;
    this.age = age;
    this.color = color;
    this.language = language;
}

let person1 = new newPerson("Muzammil","Waris",20,"brown","English");
let person2 = new newPerson("Ali","Khan",22,"black","Urdu");
let person3 = new newPerson("Javed","Ahmed",21,"white","French");

//1.

let person = {};

person.name = "Muzammil";
person.age = 20;
person.city = "Toronto";

console.log(person.name);
console.log(person.age);
console.log(person.city);

//2.

person.country = "Canada";
console.log(person.country);

//3. 

delete person.city;
console.log(person);

//4.

let car = {};

car.brand = "Toyota";
car.model = "Corolla";
car.year = 2020;
console.log(`My car is a ${car.year} ${car.brand} ${car.model}`);

//5. 

let book = {};

book.title = "Harry Potter: The Philosopher's Stone";
book.author = "J.K. Rowling";
book.pages = 500;

console.log(`Book title: ${book.title} by Author: ${book.author}`);

//6. 
function Student (name){
    this.name = name;
}
/*greet()  // method
   console.log(`Hello, my name is ${this.name}`);
*/
Student.prototype.greet = function(){
    console.log(`Hello, my name is ${this.name}`);
}


let student1 = new Student("John");
console.log(student1.greet());

//7. 

let user = {};
user.name = "Muzammil";
user.email = "mwaris256@gmail.com"
user.address = {
    city: "Mississauga"
};

console.log(user.address.city);

//8. 



function Rectangle(width, height){
    this.width = width;
    this.height = height; 
}

Rectangle.prototype.area = function(){
    console.log(`Area is: ${this.width * this.height}`);
}

let rectangle1 = new Rectangle(5,10);
console.log(rectangle1.area());

//15.

mergedUser = {...student,...car};
console.log(mergedUser);




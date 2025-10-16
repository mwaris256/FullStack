// array is an object that stores data collections in a single variable
let fruits = ["apple","banana","mango","orange"];
console.log(fruits);
console.log(fruits[0]); //accessing array elements
console.log(fruits.length); // array length

fruits.unshift("banana");

let myarray = [""];
let mynewarray = new Array("corolla","civic","liana","A7");

console.log(mynewarray[2]);

mynewarray[1] = "BMW"; //modifying array elements
console.log(mynewarray);

//array methods
console.log(mynewarray.length); //length of array

let mynewarray2 = mynewarray.toString(); // array to string
console.log(mynewarray2, typeof mynewarray2);

console.log(mynewarray.at(2));

mynewarray.pop(); // removes last element from array
console.log(mynewarray);

mynewarray.push("A8"); // adds new element at the end of array
console.log(mynewarray);

mynewarray.shift(); // removes first element from array
console.log(mynewarray);

mynewarray.unshift("Toyota"); // adds new element at the beginning of array
console.log(mynewarray);

mynewarray[mynewarray.length] = "Lexus"; // adds new element at the end of array
console.log(mynewarray);

delete mynewarray[3];  // deletes element but does not change length of array;
console.log(mynewarray);

let num1 = [1,2,3];
let num2 = [4,5,6];
let mydigit = [7,8,9,];

let allnum = num1.concat(num2, mydigit);
console.log(allnum);

// search in array

console.log(fruits.indexOf("mango"));
console.log(fruits.indexOf("banana"));
console.log(fruits.indexOf("grape")); // returns -1 if element not found

console.log(fruits.includes("banana")); // returns true if element found otherwise false
console.log(fruits.indexOf("banana")); // returns index of first occurrence of element
console.log(fruits.lastIndexOf("banana")); // returns index of last occurrence of element

let finding = allnum.find(myfunc);
function myfunc(value , index , array ){
    return value > 5;
};

console.log(finding); // returns first value that matches the condition

fruits.sort(); // sorts array in ascending order
console.log(fruits);

console.log(allnum.reverse());
// reverses the order of array elements

const points = [40,100,1,5,25,10];
points.sort(function(a,b){return a-b});
console.log(points); // sorts array in ascending order

const points2 = [40,100,1,5,25,10];
points2.sort(function(a,b){return 0.5 - Math.random()});
console.log(points2); // randomizes the order of array elements

points.sort(function(a,b){return b-a});
console.log(points); // sorts array in descending order

//1. 

fruits1 = ["apple","banana", "mango"];
console.log(fruits1);

//2.

console.log(fruits1[0]);
console.log(fruits1[fruits1.length - 1]);

//3.

fruits1.push("orange");
console.log(fruits1);

//4.

fruits1.unshift("grapes");
console.log(fruits1);

//5. 

fruits1.pop();
console.log(fruits1);

//6. 

fruits1.shift();
console.log(fruits1);

//7. 

console.log(fruits1.length);

//8.

console.log(fruits1.indexOf("banana"));

//9.

console.log(fruits1.includes("mango"));

//10.

console.log(fruits1.join(","));

//11. 

console.log(fruits1.reverse());

//12.

numbers = [12,5,8,130,44];
console.log(numbers.sort(function(a,b){return a-b}));

//13. 

array1 = ["a","b"];
array2 = [1,2,3];
array3 = array1.concat(array2);
console.log(array3);

//14. 

for (let f =0; f < array2.length; f++){
    console.log(array2[f]);
}

//15.

for (value of array3){
    console.log(value);

}

//16. 

fruits.forEach(function(fruit){
    console.log(fruit.toUpperCase());

});

//17.

nums = [1,2,3,4,5,6,7,8];

for (i=0; i < nums.length; i++){
    if (nums[i] % 2 == 0){
        console.log(nums[i]);
    }
}

//18. 

sum = 0 
for (i=0; i < nums.length; i++){
    sum += nums[i];

}
console.log(sum);

//19. 

array19 = [10,60,20,80];
console.log(array19.find(number => number >50));

//20. 

array20 = [5,25,15,40,70];
numsgreaterthan20 = array20.filter(number => number > 20);
console.log(numsgreaterthan20);

//21. 

doubledNumbers = array19.map(function(number){
    return number * 2;
})

console.log(doubledNumbers);

//22. 

const students = [
    {name:"Ahmed", marks: 80},
    {name:"Ali", marks: 87},
    {name: "Sarmad", marks: 75},
    {name: "Afsar", marks: 84}]

for (let stu of students){
    if (stu.marks > 80) {
        console.log(stu.name);
    }
}


//23.

words = ['tables','basket','fan','computer']
count = 0

for (i=0; i < words.length; i ++){
    if (words[i].length > 5){
        count = count + 1
    }
}
console.log(count);

//24. 

numbers = [22,3,15,65,124,37];

function getMaxNumber(arr){
    return Math.max(...arr);
}

console.log(getMaxNumber(numbers));

//25.

myTypedArray = new Int16Array(4);

myTypedArray[0] = 10;
myTypedArray[1] = 20;
myTypedArray[2] = 30;
myTypedArray[3] = 40;

for (i=0; i < myTypedArray.length; i++){
    console.log(myTypedArray[i]);
}

//26. 

array10 = [10,10,20,30,30,40,50];
newarray = []

for (let arr of array10){
    if(!newarray.includes(arr)){
        newarray.push(arr);
    }
}
console.log(newarray);


//27. 

arraynum1 = [23,12,7,88,9]
arraynum2 = [76,43,2,29]

arraynum1.sort(function(a,b){return a-b});
arraynum2.sort(function(a,b){return a-b});

arraynum3 = arraynum1.concat(arraynum2);
arraynum3.sort(function(a,b){return a-b});
console.log(arraynum3);

//28. 

max = arraynum1[i]
for (i=0; i <arraynum1.length; i++){
    if (arraynum1[i] > max){
        max = arraynum1[i];
    }else{
        max = arraynum1[i+1];
    }
}
console.log(max);

//29. 
sum = 0
for (i=0; i < arraynum1.length; i++){
    sum = sum + arraynum1[i];
}
average = sum/arraynum1.length;
console.log(average);

//30.

const rnumbers = [];
for (let i=0; i <21; i++){
    rnumbers.push(Math.floor(Math.random() * 100));

}
console.log(rnumbers);

d3nums = [];

for (let rnum of rnumbers){
    if (rnum % 3 == 0){
        d3nums.push(rnum);
    }
}
console.log(d3nums);
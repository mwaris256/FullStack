//an object holding key value pair
//new Map

const car = new Map([
    ['brand', 'Toyota'],
    ['model', '2025'],
    ['color', 'black'],
    ['type','sedan'],
    ['price',50000]
]);

console.log(car);
console.log(car.size);

console.log(car.get('brand'));

car.set('price', 60000); //updates price
car.set('transmission', 'automatic') // adds new key value pair
console.log(car);

console.log(car.has('model'));
console.log(car.has('year'));

car.delete("color"); // deletes car from map
console.log(car);

//1. 

const data = new Map([
    ["name", "Ali"],
    ["age",20],
    ["city", "Lahore"]
])


//2. 

console.log(data.get('name'));

//3.

console.log(data.has('age'));

//4.

data.delete('city');
console.log(data);

//5.

console.log(data.size);

//6.

for (key of data.keys()){
    console.log(key);
}

//7.

for (value of data.values()){
    console.log(value);
}

//8. 

for (entry of data.entries()){
    console.log(entry);
}

//9. 

dataArray = [...data];
console.log(dataArray);

//10. 

const arr = [['id',1],['name','Sara']];

const mymap = new Map(arr);
console.log(mymap);

//C3.

evenNums = [2,4,6,8];
squares = evenNums.map(num => Math.pow(num,2));

console.log(squares);

//C4. 

console.log(Math.max(...squares));

//C5.

/*
const rnumbers = [];
for (let i=0; i <21; i++){
    rnumbers.push(Math.floor(Math.random() * 100));
*/

let numSet = new Set();

for (let i=0; i <5; i++){
    numSet.add(Math.floor(Math.random() * 100));
}
console.log(numSet)

//C6. 

const results = new Map([
    ['Tom', 81],
    ['Kim', 93],
    ['Ryan',78 ],
    ['Bob',86],
    ['Declan',76]
]);

//C7.

let topStudent = "";
let topScore = 0;

for (const [student, score] of results){
    if (score > topScore){
        topScore = score;
        topStudent = student;
    }
}
console.log(`Top student is ${topStudent} with score ${topScore}`);

//C8.

const tens = [10,20,30,40];

const average = tens.reduce((sum, value) => sum +value,0) / tens.length;

console.log(`Average is ${average}`);




/*nums = [10,20,30,40];
let sum = 0

for (i=0, i< nums.length; i++;){
    sum += nums[i];
}

average = sum/ nums.length;

console.log(average);

*/

//C9. 

let muzSet = new Set([4,5,2,2,8,4,9]);
console.log(muzSet);

let muzArray = Array.from(new Set(muzSet));
muzArray.sort();
console.log(muzArray);

//C10.

function MultiplicationTable(number, range=10){
    table = [];
    for (let i=1; i <= range; i++){
        table.push(`${number} x ${i} = ${number * i}`);

    }
    return table;
}

console.log(MultiplicationTable(6));
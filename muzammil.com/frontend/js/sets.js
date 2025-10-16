//collection of unique values

let mySet = new Set([32,55,76]);

mySet.add(1);
mySet.add(5);

mySet.add("some text");
let m = {a:1, b:2};
mySet.add(m);

mySet.add({a:1, b:2}); //different object reference

console.log(mySet);
console.log(mySet.size); //size of set

console.log(mySet.has(5));
console.log(mySet.has(7));

let arr = "";

for (let item of mySet){
    arr += item + " ";
}
console.log(arr);


text = ""; 
mySet.forEach(function(value){
    text += value + " ";
})
console.log(text);  

mySet.delete(5);
console.log(mySet);

mySet.clear();
console.log(mySet);

//convert set to array
let myArray = Array.from(new Set([1,2,3,4,5,1,2,3]));
console.log(myArray);

//convert array to set 
let mySet2 = new Set([1,2,3,4,5,1,2,3,4,5]);
console.log(mySet2);

let ab = new Set(['a','b','c']);
let bc = new Set(['b','c','d']);

//union

let union = ab.union(bc);
console.log(union);

//intersection
let intersection = ab.intersection(bc);
console.log(intersection);

//difference
let difference = ab.difference(bc);
console.log(difference);

//symmetric difference
let symDifference = ab.symmetricDifference(bc);
console.log(symDifference);

//1.

let mSet = new Set([10,20,30]);

console.log(mSet);

//2.

mSet.add(20);
mSet.add(30);
console.log(mSet);

//3. 

console.log(mSet.has(20));

//4.

mSet.delete(20);
console.log(mSet);

//5. 

console.log(mSet.size);

//6. 

arr2 = "";

for (let item of mSet){
    arr2 += item + " ";
}
console.log(arr2);

//7.

let fArray = Array.from(mSet);
console.log(fArray);

//8.

let fSet = new Set([1,2,3,3,4,4,5]);
console.log(fSet);

//9.

fSet.clear();
console.log(fSet);

//10.

let set1 = new Set([1,2,3]);
let set2 = new Set([3,4,5]);

mergedSet = new Set([...set1, ...set2]);
console.log(mergedSet);

//C2.

words = ['table','basket','computer','table','tv'];
let wordsSet = new Set(words);
console.log(wordsSet.size);
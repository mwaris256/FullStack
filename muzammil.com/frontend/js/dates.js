//year:2025
//month:9  // 0-11
//day:7
//hour:21
//minute:25
//seconds:30

let d = new Date();
console.log(d);
console.log(typeof d.toString());
console.log(d.toDateString());
console.log(d.toTimeString());

console.log(d.getDay());
console.log(d.getDate());
console.log(d.getMonth());
console.log(d.getFullYear());
console.log(d.getHours());
console.log(d.getMinutes());
console.log(d.getSeconds());
console.log(d.getMilliseconds());
console.log(d.getTime());

console.log(d.setDate(15));
console.log(d.setMonth(5));
console.log(d.setFullYear(2023));
console.log(d.setHours(10));
console.log(d.setMinutes(30));
console.log(d.setSeconds(45));
console.log(d.setMilliseconds(200));   

//1. 

let date = new Date();
console.log(date);

//2. 

console.log(date.getFullYear());

//3. 

console.log(date.getMonth());

//4. 

console.log(date.getDay());

//5.

let d1 = new Date("2000-01-01");
console.log(d1);

//6.

console.log(d1.getHours());
console.log(date.getMinutes());
console.log(date.getSeconds());

//7. 

date.setDate(date.getDate() + 7);
console.log(date);

//8. 

date1 = new Date();
date1.setDate(date1.getDate() - 30);
console.log(date1);


//9. 

if (date < date1){
    console.log(date.toDateString());
} else {
    console.log(date1.toDateString());

}

//10. 

today = new Date();
yyyy = today.getFullYear();
let mm  = today.getMonth() + 1;
let dd = today.getDate();

if (mm < 10) {
    mm = '0' + mm;
}
if (dd < 10) {
    dd = '0' + dd;
}

formattedDate = `${yyyy}-${mm}-${dd}`;
console.log(formattedDate);

let paragraph = "The quick brown fox jumps over the lazy dog. golg The quick blue hare speeds past the red chicken."


//Pattern to search for the word "quick"
let regex1 = /quick/g; //globally
let matches = paragraph.match(regex1);
console.log('Matches for quick', matches);

//Pattern to serach for words starting with b and ending with n
let regex2 = /\bb\w*n\b/g;
let matches2 = paragraph.match(regex2);
console.log('Matches for words starting with b and ending with n', matches2);

//Pattern to search for all three letter words
let regex3 = /\b\w{3}\b/g;
let matches3 = paragraph.match(regex3);
console.log('Matches for all three letter words', matches3);

//Pattern to serach for case insensitive for 'the'
let regex4 = /the/gi;
let matches4 = paragraph.match(regex4);
console.log('Case insensitive for "the"', matches4);

//Pattern to serach for words ending with y
let regex5 = /\b\w*y\b/g;
let matches5 = paragraph.match(regex5);
console.log('Matches for words ending with y', matches5);

//Pattern to search for whitespace characters
let regex6 = /\s/g;
let matches6 = paragraph.match(regex6);
console.log('whitespace characters found', matches6);

//Pattern to search for words with double consecutive letters
let regex7 = /\b\w*(\w)\1\w*\b/g;
let matches7 = paragraph.match(regex7);
console.log('Matches for words with double consecutive letters', matches7);

//Patten to search for words that contain 'o' followed by any character and then a 'g'
let regex8 = /\b\w*o.g\w*\b/g;
let matches8 = paragraph.match(regex8);
console.log("Matches for words that contain 'o' followed by any character then a 'g'");
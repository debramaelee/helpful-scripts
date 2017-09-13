// gets offset of UTC in minutes
var offset = new Date().getTimezoneOffset();

// gets current date formatted in YYYY-MM-DD and YYYYMMDD
var t = new Date(); 
t.setDate(t.getDate()); 
t.toISOString().slice(0,10).replace(/-/g,"");

console.log(t);
console.log(t.toISOString().slice(0,10).replace(/-/g,""));

// new Date().toISOString('en-US', { timeZone: 'EST'});
// console.log(Date);
console.log(offset/60);

// gets yesterdays date
// var t = new Date(); t.setDate(t.getDate()-1); t.toISOString().slice(0,10).replace(/-/g,"");

// offset UTC time to EST
var t2 = new Date(); 
t2.setHours(t2.getHours() - 4); 
t2.setDate(t2.getDate()); 
t2.toISOString().slice(0,10);
console.log(t2);
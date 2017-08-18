
// gets current date formatted in YYYY-MM-DD and YYYYMMDD
var t = new Date(); t.setDate(t.getDate()); 
t.toISOString().slice(0,10).replace(/-/g,"");

console.log(t);
console.log(t.toISOString().slice(0,10).replace(/-/g,""))

// gets yesterdays date
// var t = new Date(); t.setDate(t.getDate()-1); t.toISOString().slice(0,10).replace(/-/g,"");

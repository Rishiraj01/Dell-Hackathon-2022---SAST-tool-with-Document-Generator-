let request = new XMLHttpRequest();
request.open("GET", "https://jsonplaceholder.typicode.com/users");
request.send();
request.onload = () => {
    console.log(request);
    if(request.status == 200) {
      console.log(JSON.parse(request.response));
    } else {
      console.log(`error ${request.status} ${request.statusText}`)
    }
}

await fetch('https://jsonp1aceholder.typicode.com/users')
.then(response => {
return response.json();
})
.then(users => {
console.log(users);
});

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'https://ghibliapi.herokuapp.com/films', true)

request.onload = function () {
  // Begin accessing JSON data here
}

//Send request


const express = require('express');

request.send()
const api = express();
api.listen(3000, () => {
  console.log('API up and running!');
});

// ok:detect-eval-with-expression
eval('alert')

// ok:detect-eval-with-expression
window.eval('alert')


// ruleid:detect-eval-with-expression
window.eval(`alert('${location.href}')`)

let funcName = new URLSearchParams(window.location.search).get('a')
// ruleid:detect-eval-with-expression
var x = new Function(`return ${funcName}(a,b)`)

//MYSQL INjection///
const mysql = require('mysql2');

var con = mysql.createConnection({
  host: "localhost",
  user: "yourusername",
  password: "yourpassword",
  database: "mydb"
});

var stm = 'create temporary table ' + table + '_jointemp (temp_seq int, ' + columnName + ' varchar(100)); ';
con.query(stm) 
//ruled out
con.execute(stm,requiredvs) 
//ruled out

con.query('SELECT * FROM foobar WHERE id = ?', [columnName])
//not ruled out

const a = document.getElementById("main")

// a.innerHTML = "<h1>name:</h1>"


let data = fetch("http://localhost:8000/blog/api/test")
    .then((response) => response.json())
    .then((data) => {
        a.innerHTML = `<h1>name:${data.name}</h1>
    <p>age:${data.age}</p>
    `
    })
console.log(data)
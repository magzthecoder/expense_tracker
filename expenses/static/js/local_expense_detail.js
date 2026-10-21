const paramsString = window.location.search;
const errorMessage = document.querySelector("#error")
const index = new URLSearchParams(paramsString).get("index");

const exp_name = document.querySelector("#name");
const category = document.querySelector("#category");
const price = document.querySelector("#price");
const date = document.querySelector("#date");

let expenses = [];
let result = localStorage.getItem("expenses");
if(result){
    expenses = JSON.parse(result);
}else{
    expenses = []
}
if (expenses[index] != undefined){
    exp_name.textContent = `Name: ${expenses[index].name}`;
    category.textContent = `Category: ${expenses[index].category}`;
    price.textContent = `Price: ${expenses[index].price}`;
    date.textContent = `Date ${expenses[index].date}`;
}else{
    errorMessage.textContent = "Expense Not Found!!!"
}


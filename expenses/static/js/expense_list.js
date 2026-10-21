const saved = document.querySelector("#saved");

let expenses = [];
let result = localStorage.getItem("expenses");
if(result){
    expenses = JSON.parse(result);
}else{
    expenses = []
}
console.log(expenses);
for(let i = 0; i < expenses.length;i++){
    console.log(expenses[i].name);

    const name = document.createElement("p");
    name.textContent = expenses[i].name;
    saved.append(name);
}
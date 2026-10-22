const paramsString = window.location.search;
const errorMessage = document.querySelector("#error")
const index = new URLSearchParams(paramsString).get("index");
const exp_name = document.querySelector("#name");
const category = document.querySelector("#category");
const price = document.querySelector("#price");
const date = document.querySelector("#date");
const delButton = document.querySelector("#delete");
const backButton = document.querySelector("#back");
const edit = document.querySelector("#edit");
edit.href = `/expenses/local-edit/?index=${index}`;

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

    delButton.addEventListener("click",function(){
    expenses = JSON.parse(result);
    expenses.splice(index,1);

    localStorage.setItem("expenses",JSON.stringify(expenses));
    location.assign("/expenses/");
});

}else{
    errorMessage.textContent = "Expense Not Found!!!"
}


backButton.addEventListener("click",function(){
    location.assign("/expenses/");
});

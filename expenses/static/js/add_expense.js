const form = document.querySelector("#form");
const userId = document.body.dataset.userId;
const storageKey = `expenses_user_${userId}`;
const exp_name = document.querySelector("#id_expense_name");
const price = document.querySelector("#id_expense_price");
const category = document.querySelector("#id_category");
const date = document.querySelector("#id_date_bought");

form.addEventListener("submit",function(event){
    event.preventDefault();
    let expense ={
            "name":exp_name.value,
            "price":price.value,
            "category":category.options[category.selectedIndex].text,
            "date":date.value
        };
    let expenses = [];
    let result = localStorage.getItem(storageKey);
    if(result){
        expenses = JSON.parse(result);
    }else{
        expenses = []
    }
    expenses.push(expense);
    localStorage.setItem(storageKey, JSON.stringify(expenses))
    console.log(expenses);
    const saved_expenses = localStorage.getItem("expenses");
    const expense_object = JSON.parse(saved_expenses);
    for(let i = 0; i < expense_object.length;i++){
        console.log(expense_object[i].name);
        console.log(expense_object[i].price);
        console.log(expense_object[i].category);
        console.log(expense_object[i].date);
    }
});
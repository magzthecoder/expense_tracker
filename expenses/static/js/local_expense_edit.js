const paramsString = window.location.search;
const userId = document.body.dataset.userId;
const storageKey = `expenses_user_${userId}`;
const index = new URLSearchParams(paramsString).get("index");
const exp_name = document.querySelector("#name");
const category = document.querySelector("#category");
const price = document.querySelector("#price");
const date = document.querySelector("#date");
const errorMessage = document.querySelector("#error");
const cancelButton = document.querySelector("#cancel");
const form = document.querySelector("#form");


let expenses = [];
let result = localStorage.getItem(storageKey);
if(result){
    expenses = JSON.parse(result);
}else{
    expenses = []
}
if (expenses[index] != undefined){
    exp_name.value = expenses[index].name;
    category.value = expenses[index].category;
    price.value = expenses[index].price;
    date.value = expenses[index].date;
}else{
    errorMessage.textContent = "Expense Not Found!!!"
}

form.addEventListener("submit",function(event){
    event.preventDefault();
    if(result){
        expenses = JSON.parse(result);
    }else{
        expenses = []
    }
    if (expenses[index] != undefined){
        expenses[index].name =exp_name.value ;
        expenses[index].category = category.value;
        expenses[index].price = price.value;
        expenses[index].date =  date.value;

        localStorage.setItem(storageKey, JSON.stringify(expenses))
        location.assign("/expenses/");
    }else{
        errorMessage.textContent = "Expense Not Found!!!"
    }

});

cancelButton.addEventListener("click",function(event){
    event.preventDefault();
    console.log("Cancel");
    location.assign("/expenses/");
});



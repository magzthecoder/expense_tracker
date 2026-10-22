const userId = document.body.dataset.userId;
const storageKey = `expenses_user_${userId}`;
const list = document.querySelector("#list");
const searchBar = document.querySelector("#search");
const message = document.querySelector("#message")

let expenses = [];
let result = localStorage.getItem(storageKey);
if(result){
    expenses = JSON.parse(result);
}else{
    expenses = []
}
console.log(expenses);
for(let i = 0; i < expenses.length;i++){
    console.log(expenses[i].name);

    const name = document.createElement("p");
    const nameLink = document.createElement("a");
    nameLink.href = `/expenses/local-detail/?index=${i}`;

    nameLink.textContent = expenses[i].name;
    name.append(nameLink);
    list.append(name);
}

searchBar.addEventListener("input",function(){
    list.innerHTML = "";
    message.textContent = "";
    const searchResult = searchBar.value;
    const mapped = expenses.map((expenses,index) =>{
       return {expense:expenses,
        index:index}
    });
    const newResult = mapped.filter((expenses,i) =>{
        let newExpenses = expenses.expense.name.toLowerCase();
        return newExpenses.includes(searchResult.toLowerCase())
    });

    if(newResult.length > 0){
        for(let i = 0; i < newResult.length; i++){
            const paraName = document.createElement("p");
            const linkName = document.createElement("a");

            linkName.textContent = newResult[i].expense.name;
            linkName.href = `/expenses/local-detail/?index=${newResult[i].index}`

            paraName.append(linkName);
            list.append(paraName);
        }
    }else if(newResult.length === 0){
        message.textContent = "No expenses found";
    }
    
});
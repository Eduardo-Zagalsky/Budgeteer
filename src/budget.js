const Budget = () => {
    let tempIncome = 2000;
    let tempExpenses = 950;
    return (
        <div>
            <p>your income is {tempIncome}</p>
            <p>your expenses are {tempExpenses}</p>
            <p>ideally you would want your expenses to be less than 45% of your income so let's try to come up with some ways to make that true</p>

            <h1>currently your DTI is {(tempExpenses / tempIncome * 100)}</h1>
            <p>lets see your expenses</p>
            {/* {for(let x in expenses)} */}
            <p>looking at this, which of these could you cut back on to try to get on the best path to financial freedom?</p>

        </div>
    )
}
export default Budget;
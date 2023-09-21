const Budget = () => {
    let tempIncome = 2000;
    let tempExpenses = 950;
    return (
        <div>
            <p>Your income is <b>${tempIncome.toLocaleString()}</b> and your expenses are <b>${tempExpenses.toLocaleString()}</b>.</p>
            <h4>Currently your DTI is {(tempExpenses / tempIncome * 100)}%</h4>
            <p>Ideally you would want your expenses to be less than 45% of your income, so let's try to come up with some ways to make that true!
                Let's see your expenses and decide which of these you could cut back on to try to get on the best path to financial freedom.</p>
            {/* {for(let x in expenses)} */}
        </div>
    )
}
export default Budget;
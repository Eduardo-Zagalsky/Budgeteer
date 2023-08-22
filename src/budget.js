const Budget = (props) => {
    return (
        <div>
            <p>your income is {income}</p>
            <p>your expenses are {expenses}</p>
            <p>ideally you would want your expenses to be less than 45% of your income so let's try to come up with some ways to make that true</p>

            <h1>currently your DTI is {(expenses / income * 100)}</h1>
            <p>lets see your expenses</p>
            {/* {for(let x in expenses)} */}
            <p>looking at this which of these could you cut back on to try to get on the best path to financial freedom?</p>

        </div>
    )
}
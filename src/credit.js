const Credit = (props) => {
    return (
        <div>
            <p>credit bereaus can only see your credit once per month so there are some strategies to maximize your credit impact</p>
            <p>the best strategy for building credit is to figure out the due date and plan payments around it</p>
            <p>this means that your due date is: {due_date} and this month is {month} so this month you will pay the bill</p>
            <p>{month % 2 === 0 ? <b>before {due_date}</b> : <b>after {due_date}, when the bill arrives</b>}</p>
            <hr />
            <p>If you are planning on getting a new line of credit becareful hard inquiries go on your record for 2 full years and will lower your score</p>
        </div>
    )
}
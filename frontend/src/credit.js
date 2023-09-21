const Credit = () => {
    // hardcoded dueDate(due_date), month
    let date = 15;
    let suffix = ""
    let monthNum = 7;
    let month = ""
    switch (date) {
        case 1:
            suffix = "st"
            break;
        case 2:
            suffix = "nd"
            break;
        case 3:
            suffix = "rd"
            break;
        case 21:
            suffix = "st"
            break;
        case 22:
            suffix = "nd"
            break;
        case 23:
            suffix = "rd"
            break;
        case 31:
            suffix = "st"
            break;
        default:
            suffix = "th"
    };
    let dueDate = date + suffix;
    switch (monthNum) {
        case 1:
            month = "January"
            break;
        case 2:
            month = "February"
            break;
        case 3:
            month = "March"
            break;
        case 4:
            month = "April"
            break;
        case 5:
            month = "May"
            break;
        case 6:
            month = "June"
            break;
        case 7:
            month = "July"
            break;
        case 8:
            month = "August"
            break;
        case 9:
            month = "September"
            break;
        case 10:
            month = "October"
            break;
        case 11:
            month = "November"
            break;
        case 12:
            month = "December"
            break;
    };
    return (
        <div>
            <h1>Credit</h1>
            <h3>If you plan on borrowing money, whether a fixed loan or a revolving loan(credit cards) here are somethings to know.</h3>
            <h4>Every time a Creditor runs your Credit, it counts as a hard inquiry and hard inquiries go on your record and will lower your score,
                they will disappear on their own after 2 full years.</h4>
            <br />
            <h3>Credit Cards</h3>
            <p>Revolving Lines of Credit, such as credit cards and lines of credit, you can spend more than once and only pay interest on what you spend.</p>
            <h4>The most important thing to know here is that Credit Bereaus only see your credit once per month, when your creditors report it.
                So there is a strategy to maximize your credit impact.</h4>
            <p>The strategy for building credit is to figure out the due date and plan payments around it, this means that your due date is:
                the {dueDate} of this month, <b>{month}</b>, so this month you will pay the bill</p>
            <p>{month % 2 === 0 ? <b>Before the {dueDate}</b> : <b>After the {dueDate}, when the bill arrives!</b>}</p>
            <hr />
            <h3>Loans</h3>
            <p>Fixed Loans you receive a fixed amount once and pay it back over a certain time period</p>
            <h4>The most important thing happens when you pay it off!</h4>
            <p>When the loan is fully paid off, it disappears from your credit history for about 3 months while the history of the loan is analyzed.
                After, the loan will appear on your credit history as a closed loan and it will prove that you paid off a loan in it's entirity.</p>
        </div>
    )
}

export default Credit;
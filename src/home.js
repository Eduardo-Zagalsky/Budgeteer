const Home = (props) => {

    return (
        <div>
            <h1>Hello {props.user}!</h1>
            <ul>
                <h3>Your finances:</h3>
                <li>Income: {props.income}</li>
                <li>Expenses: {props.expenses}</li>
                {props.income - props.expenses >= 0 ? <li>Remaining: {props.remainder}</li> : <li>Short: {props.remainder}</li>}
                <li>Debts: {props.debts}</li>
            </ul>
        </div>
    );
}
export default Home;
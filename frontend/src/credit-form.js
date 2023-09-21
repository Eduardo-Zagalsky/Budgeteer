import axios from "axios"
import { useState, useEffect } from "react"
const INITIAL_VAL = { creditor: "", type: "", limit: "", balance: "", interestRate: "", dueDate: "" }

const CreditForm = () => {
    const [formData, setFormData] = useState(INITIAL_VAL);
    useEffect(
        async function mark() {
            const data = await axios.post('/credit-form', { formData });
            return data;
        })
    const handleSubmit = (e) => {
        e.preventDefault();
        setFormData(
            {
                creditor: e.target.creditor.value, type: e.target.type.value, limit: e.target.limit.value,
                balance: e.target.balance.value, interestRate: e.target.interestRate.value, dueDate: e.target.dueDate.value
            }
        )

    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="creditor">Creditor: </label>
                <input type="text" name="creditor" value={formData.creditor} />

                <label htmlFor="type">Type: </label>
                <input type="text" name="type" value={formData.type} />

                <label htmlFor="limit">Limit: </label>
                <input type="text" name="limit" value={formData.limit} />

                <label htmlFor="balance">Balance: </label>
                <input type="text" name="balance" value={formData.balance} />

                <label htmlFor="interestRate">Interest Rate: </label>
                <input type="text" name="interestRate" value={formData.interestRate} />

                <label htmlFor="dueDate">Due Date: </label>
                <input type="text" name="dueDate" value={formData.dueDate} />
            </form>
        </div>
    )
}
export default CreditForm;
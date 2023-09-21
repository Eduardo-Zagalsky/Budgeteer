import axios from "axios"
import { useState, useEffect } from "react"
const INITIAL_VAL = { name: "", type: "", amount: "", description: "", date: "" }

const ExpenseForm = () => {
    const [formData, setFormData] = useState(INITIAL_VAL);
    useEffect(
        async function mark() {
            const data = await axios.post('/expense-form', { formData });
            return data;
        })
    const handleSubmit = (e) => {
        e.preventDefault();
        setFormData(
            {
                name: e.target.name.value, type: e.target.type.value, amount: e.target.amount.value,
                description: e.target.description.value, date: e.target.date.value
            }
        )

    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name: </label>
                <input type="text" name="name" value={formData.name} />

                <label htmlFor="type">Type: </label>
                <input type="text" name="type" value={formData.type} />

                <label htmlFor="amount">Amount: </label>
                <input type="text" name="amount" value={formData.amount} />

                <label htmlFor="description">Description: </label>
                <input type="text" name="description" value={formData.description} />

                <label htmlFor="date">Date: </label>
                <input type="text" name="date" value={formData.date} />
            </form>
        </div>
    )
}
export default ExpenseForm;
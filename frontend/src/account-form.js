import axios from "axios"
import { useState, useEffect } from "react"
const INITIAL_VAL = { name: "", type: "", balance: "" }

const AccountForm = () => {
    const [formData, setFormData] = useState(INITIAL_VAL);
    useEffect(
        async function mark() {
            const data = await axios.post('/account-form', { formData });
            return data;
        })
    const handleSubmit = (e) => {
        e.preventDefault();
        setFormData(
            {
                name: e.target.name.value, type: e.target.type.value, balance: e.target.balance.value
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

                <label htmlFor="balance">Balance: </label>
                <input type="text" name="balance" value={formData.balance} />

            </form>
        </div>
    )
}
export default AccountForm;
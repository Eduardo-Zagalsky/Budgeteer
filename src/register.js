import axios from "axios"
import { useState, useEffect } from "react"
const INITIAL_VAL = { name: "", email: "", username: "", password: "", income: "", creditScore: "" }

const Register = () => {
    const [formData, setFormData] = useState(INITIAL_VAL);
    useEffect(
        async function signUp() {
            const data = await axios.post('/signup', { formData });
            return data;
        })
    const handleSubmit = (e) => {
        e.preventDefault();
        setFormData(
            {
                name: e.target.name.value, email: e.target.email.value, username: e.target.username.value,
                password: e.target.password.value, income: e.target.income.value, creditScore: e.target.creditScore.value
            }
        )

    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Full Name: </label>
                <input type="text" name="name" value={formData.name} />

                <label htmlFor="email">Email: </label>
                <input type="email" name="email" value={formData.email} />

                <label htmlFor="username">Username: </label>
                <input type="text" name="username" value={formData.username} />

                <label htmlFor="password">Password: </label>
                <input type="password" name="password" value={formData.password} />

                <label htmlFor="income">Income: </label>
                <input type="text" name="income" value={formData.income} />

                <label htmlFor="creditScore">Credit Score: </label>
                <input type="text" name="creditScore" value={formData.creditScore} />
            </form>
        </div>
    )
}
export default Register;
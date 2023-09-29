import axios from "axios"
import { useState } from "react"
const jwt = require("jsonwebtoken");

const INITIAL_VAL = { name: "", email: "", username: "", password: "", income: "", creditScore: "" }
const URL = process.env.FULL_URL;
const SECRET_KEY = process.env.SECRET_KEY;
const Register = () => {
    const [formData, setFormData] = useState(INITIAL_VAL);
    const handleChange = (e) => {
        let { name, value } = e.target;
        setFormData(data => ({ ...data, [name]: value }));
    }
    const handleSubmit = async (e) => {
        e.preventDefault();
        let token = jwt.sign(formData, SECRET_KEY);
        const data = await axios.post(`${URL}/signup`, { token });
        return data.json();
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Full Name: </label>
                <input type="text" name="name" value={formData.name} onChange={handleChange} />

                <label htmlFor="email">Email: </label>
                <input type="email" name="email" value={formData.email} onChange={handleChange} />

                <label htmlFor="username">Username: </label>
                <input type="text" name="username" value={formData.username} onChange={handleChange} />

                <label htmlFor="password">Password: </label>
                <input type="password" name="password" value={formData.password} onChange={handleChange} />

                <label htmlFor="income">Income: </label>
                <input type="text" name="income" value={formData.income} onChange={handleChange} />

                <label htmlFor="creditScore">Credit Score: </label>
                <input type="text" name="creditScore" value={formData.creditScore} onChange={handleChange} />
            </form>
        </div>
    )
}
export default Register;
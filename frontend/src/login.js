import axios from "axios"
import { useState, useEffect } from "react"
const INITIAL_VAL = { username: "", password: "" }

const Login = () => {
    const [formData, setFormData] = useState(INITIAL_VAL);
    useEffect(
        async function login() {
            const data = await axios.post('/login', { formData });
            return data;
        })
    const handleSubmit = (e) => {
        e.preventDefault();
        setFormData({ username: e.target.username.value, password: e.target.password.value })

    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username: </label>
                <input type="text" name="username" value={formData.username} />

                <label htmlFor="password">Password: </label>
                <input type="password" name="password" value={formData.password} />
            </form>
        </div>
    )
}
export default Login;
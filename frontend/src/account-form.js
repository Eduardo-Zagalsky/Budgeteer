import axios from "axios"
import { useState } from "react"
const local = require("localStorage")
const URL = process.env.FULL_URL;
const SECRET = process.env.SECRET_KEY;
const INITIAL_VAL = { name: "", type: "", balance: "" }
const jwt = require("jsonwebtoken")

const AccountForm = () => {
    const [formData, setFormData] = useState(INITIAL_VAL);
    const [loggedIn, setLoggedIn] = useState(false);
    const handleChange = (e) => {
        let { name, value } = e.target;
        setFormData(data => ({ ...data, [name]: value }));
    }
    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post(`${URL}/account-form`, { formData });
    }
    const validate = () => {
        const token = local.getItem("token");
        const data = jwt.verify(token, SECRET);
        if (data.username) {
            setLoggedIn(true);
        }
    }
    if (!loggedIn) {
        setTimeout(function () {
            window.location.replace('/login');
        }, 5000);
        return (
            <div>
                <h1>YOU ARE NOT LOGGED IN! LOG IN AND TRY AGAIN!</h1>
            </div>
        )
    } else {
        return (
            <div>
                <form onSubmit={handleSubmit}>
                    <label htmlFor="name">Name: </label>
                    <input type="text" name="name" value={formData.name} onChange={handleChange} />

                    <label htmlFor="type">Type: </label>
                    <input type="text" name="type" value={formData.type} onChange={handleChange} />

                    <label htmlFor="balance">Balance: </label>
                    <input type="text" name="balance" value={formData.balance} onChange={handleChange} />

                </form>
            </div>
        )
    }
}
export default AccountForm;
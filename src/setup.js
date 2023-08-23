import { PlaidLink } from "react-plaid-link";
import axios from "axios";
import { useState } from "react";

const Setup = () => {
    const [transactions, setTransactions] = useState(null)
    const handleOnSuccess = (public_token, metadata) => {
        //send token to client server
        axios.post("/auth/public_token", { public_token: public_token });
    }
    const handleOnExit = () => {
        //get back to this later
    }
    const handleClick = (res) => {
        axios.get("/transactions").then(res => {
            setTransactions(res.data)
        })
    }
    const publicKey = () => {
        axios.get("/sandbox/public_token/create").then(res => {
            return res['public_token']
        })
    }
    return (
        <div>
            <PlaidLink
                clientName="Budgeteer"
                env="sandbox"
                product={["transactions"]}
                publicKey={publicKey}
                onExit={handleOnExit}
                onSuccess={handleOnSuccess}
                className="test"
            >
                Connect with your bank account!
            </PlaidLink>
            <div>
                <button onClick={() => handleClick()}>Get Transactions</button>
            </div>
        </div>
    )
}
export default Setup;
const express = require('express');
const request = require('request');
const { receivePublicToken, getTransactions } = require("./controller/controller");

app = express();
const PORT = 3000;

app.use(express.json());

app.get('/home', function (req, res) {
    request('http://127.0.0.1:5000/flask', function (error, response, body) {
        console.error('error:', error);
        console.log('status code: ', response && response.statusCode);
        console.log('body: ', body);
        res.send(body);
    });
});
// get public token to exchange
app.post("/auth/public_token", receivePublicToken);
// get transactions
app.get("/transactions", getTransactions)

app.listen(PORT, function () {
    console.log('Listening on Port 3000');
});
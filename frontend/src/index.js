import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route } from 'react-router-dom';
import NavBar from './navbar';
import Home from './home';
import Credit from './credit';
import Savings from './savings';
import Budget from './budget';
import Register from './register';
import "./style.css";

const App = () => (
  <BrowserRouter>
    <NavBar />
    <Route exact path='/'>
      <Home />
    </Route>
    <Route exact path='/credit'>
      <Credit />
    </Route>
    <Route exact path='/savings'>
      <Savings />
    </Route>
    <Route exact path='/budget'>
      <Budget />
    </Route>
    <Route exact path='/register'>
      <Register />
    </Route>
  </BrowserRouter>
)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <App />
);
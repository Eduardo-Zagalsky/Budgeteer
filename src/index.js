import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route } from 'react-router-dom';
import NavBar from './navbar';
import Home from './home';
import Setup from './setup';
import "./style.css";

const App = () => (
  <BrowserRouter>
    <NavBar />
    <Route exact path='/'>
      <Home />
    </Route>
    <Route exact path='/link-plaid'>
      <Setup />
    </Route>
  </BrowserRouter>
)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <App />
);
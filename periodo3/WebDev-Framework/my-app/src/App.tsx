import React from 'react';
import logo from './logo.svg';
import './App.css';
import Menu from './layout/Menu';
import User from './user/user';

function App() {
  return(
    <div className='container'>
      <Menu></Menu>
      <User name='Giovani' age={18} birthdate='16/12/2006'></User>
    </div>
  )

}

export default App;

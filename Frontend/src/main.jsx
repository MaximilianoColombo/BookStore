import React from 'react'
import ReactDOM from 'react-dom/client'
import 'bootstrap/dist/css/bootstrap.min.css';

import './index.css'
import NavBar from './components/NavBar.jsx'
import App from './App.jsx'
import Footer from './components/Footer.jsx';



ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <div data-bs-theme="dark">
      <NavBar></NavBar>
      <Footer></Footer>
    </div>
  </React.StrictMode>,
)

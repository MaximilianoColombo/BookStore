// components/Layout.js
import React from 'react';
import Footer from './Footer.jsx'
import NavBar from './NavBar.jsx';

const Layout = ({ children }) => {
  return (
    <div>
      <NavBar></NavBar>
      <main>{children}</main>
      <Footer></Footer>
    </div>
  );
};

export default Layout;

import React from 'react';
import Footer from './components/footer';
import Header from './components/header';
import './LandingPage.css';

function LandingPage(props) {
  return (
    <div>
      <Header />
      <h2>Age</h2><input className='Age'></input>
      <Footer />
    </div>
  );
}

export default LandingPage;

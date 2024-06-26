import React from 'react';
import Footer from './components/footer';
import Header from './components/header';
import './LandingPage.css';

function LandingPage(props) {
  return (
    <div>
      <Header />
      <p1 className='AgeLabel'>Age12</p1>
      <input className='AgeInput'></input>
      <Footer />
    </div>
  );
}

export default LandingPage;

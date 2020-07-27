import React from 'react';
import logo from './logo.svg';
import './App.css';
import DoctorList from './Doctors/DoctorList'
import AddDoctor from './Doctors/AddDoctor'
function App() {
  return (
    <div className="container-fluid">
        <DoctorList/>
        <AddDoctor/>
    </div>
  );
}

export default App;

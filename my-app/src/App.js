import React,{useState,useEffect} from 'react';
import './App.css';
import { JsonToTable } from "react-json-to-table";
import "./styles.css";
import { makeStyles } from '@material-ui/core/styles';
import Countdown from "./Countdown";
import 'fontsource-roboto';

function App() {

  const d = require('./activities.json')

  const divStyle = {
    color: 'blue',
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgb(34, 34, 34)",
    background: "rgb(34, 34, 34",
    color: "rgb(104,104,104)"

  }

  return (

<div className="App">
  <div className="Countdown" >
      <h1 > Productivity Tracker </h1>
      <Countdown />
      <p style={{padding: 20}}></p>
  </div>
  <div className="Table" style={divStyle}>

    <JsonToTable json={d['activities']}/>

  </div>

</div>

  );
}

export default App;

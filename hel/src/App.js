import React from "react";
import Head from "./components/head";
import './App.css'
import Banner from "./components/banner";
import Movie  from "./components/movie";


    const App = ()=>{
        return(
            <div className="Filmy">
                <div style={{backgroundImage:"url('https://image.tmdb.org/t/p/original/lcTuggU70y6pt6x13Rv1Ffjs93K.jpg')",backgroundRepeat: "no-repeat"}}>
                  <Head />
                  <Banner />
                  
                </div>
                <Movie />
              </div>
           
        )
    }
export default  App;

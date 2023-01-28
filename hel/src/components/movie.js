import React,{Component} from "react";
import './movie.css'
import { Variables } from "./../variables"


export default class Movie extends Component {
    constructor (props) {
        super(props);
        this.state = {
            movies:[]
        }
    }
    refresh(){
        fetch(Variables.API_URL+"movie/")
        .then(response => response.json())
        .then(data => {
            this.setState({movies: data});  
        });
    }

    componentDidMount(){
        this.refresh();
    }
    render(){
        const {movies} = this.state;
       return( 
                <div className="main">
                  {movies.map((mov,ind) => (
                    <div className="movie">
                        <img src={mov.movieImg} alt="movie"></img>
                        <div className="movie-info">
                            <h3>{mov.movieName}</h3>
                            <span className="green">{mov.movieRating}</span>
                        </div>
                        <div class="overview">
					        <h3>Overview</h3>
                            {mov.movieOverview}
                        </div>
                    </div>
                  ))}
                </div>    
       )
    }

};
import React from "react";
import { Navbar, Nav } from 'react-bootstrap';
import './navItem.css'



class Head extends React.Component {
    render() {
        return(
          
           <Navbar bg="dark" expand="lg">
                <Navbar.Brand><h3 className="logo">FILMY</h3></Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarResponsive"></Navbar.Toggle>
                <Navbar.Collapse id="navbarResponsive">
                    <Nav className="navItem">
                        <Nav.Item>
                            <h5>Home</h5>
                        </Nav.Item>
                        <Nav.Item>
                            <h5>Tv Shows</h5>
                        </Nav.Item>
                        <Nav.Item>
                            <h5>Movies</h5>
                        </Nav.Item>
                        <Nav.Item>
                            <h5>Wish List</h5>
                        </Nav.Item>  
                    </Nav>
                </Navbar.Collapse>
           </Navbar>
        )
    }
}
export default Head;
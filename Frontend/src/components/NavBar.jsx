import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import navBarItems from '../data/NavBarItems'

const NavBar = () => {
  return (
    <Navbar expand="lg" className="bg-body-tertiary fixed-top w-100" >
      <Container>
        <Navbar.Brand href="#home">Biblioteca</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto d-flex justify-content-around w-100">
            {navBarItems.map((item, index) => (
            <Nav.Link key={index} href={item.href}>{item.name}</Nav.Link>
          ))}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;
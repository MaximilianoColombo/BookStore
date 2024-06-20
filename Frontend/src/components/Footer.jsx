import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const Footer = () => {
  return (
    <footer className="bg-dark text-light fixed-bottom">
      <Container fluid>
        <Row>
          <Col className="text-center py-3">
            <p>&copy; {new Date().getFullYear()} Maximiliano Colombo. Todos los derechos reservados.</p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;

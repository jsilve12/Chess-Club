import React from 'react';
import PropTypes from 'prop-types';
import ReactDOM from 'react-dom';

class Navbar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Pages: [{ url: '/', name: 'Home' },
              { url: '/about', name: 'About' },
              { url: '/tournaments', name: 'Tournaments' },
              { url: '/learning', name: 'Learning' },
              { url: '/calendar', name: 'Calendar' },],
    };
  };

  render() {
    return (

      <nav className="navbar navbar-dark navbar-expand-lg">
        <div className="container">
          <a href="/" className="navbar-brand michigan-colors rounded p-2"><h1>Umich Chess</h1></a>
          <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarSupported'>
            <span class='navbar-toggler-icon'></span>
          </button>
          <div class='collapse navbar-collapse' id='navbarSupported'>
            <ul className='nav justify-content-center ml-auto'>
              {this.state.Pages.map(Activity => (
                <li className='nav-item'>
                  <a href={Activity.url} className="nav-link text-light">{Activity.name}</a>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </nav>
    );
  }
}
Navbar.propTypes = {};
const Nav = document.getElementById('navbar');
if (Nav)
{
  ReactDOM.render(
    <Navbar/>, Nav
  );
}

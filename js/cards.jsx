import React from 'react';
import PropTypes from 'prop-types';
import ReactDOM from 'react-dom';

class Card extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Title: '',
      Cards: [],
    };
  }

  componentDidMount() {
    fetch(this.props.url, { method: 'GET', credentials: 'same-origin' })
    .then(response => response.json())
    .then(data => {
      this.setState({ Cards: data.Cards, Title: data.Title });
    });
  }

  render() {
    return (
    <div>
      <h3 class="p-3">{this.state.Title}</h3>
      <div class="card-deck pb-3">
      {this.state.Cards.map(Card => (
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">{Card.Title}</h4>
              {'Subtitle' in Card &&
              <div class="card-subtitle text-muted">{Card.Subtitle}</div>
              }
              {'Body' in Card &&
              <p class="card-text" dangerouslySetInnerHTML={{ __html: Card.Body }}></p>
              }
          </div>
        </div>
      ))}
      </div>
    </div>
    );
  }
}
Card.propTypes = {
  url: PropTypes.string.isRequired,
};
const cards = document.getElementsByClassName('react-card');
for (const i in cards) {
  const card = cards[i];
  ReactDOM.render(
    <Card url={card.innerHTML} />, card
  );
};

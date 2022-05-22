import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import Header from './components/Header.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }


    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                console.dir(response)
                    this.setState(
                  {
                      'users': users
                  }
                )
            }).catch(error => console.log(error))
    }

  render () {
    return (
      <div>
        <Header />
        <UserList users={this.state.users} />
        <Menu />
        <Footer />
      </div>
    )
  }
}

export default App;
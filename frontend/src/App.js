import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project';
import TodoList from './components/Todo';
import Header from './components/Header.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';
import {Route, Routes, BrowserRouter, Link} from 'react-router-dom'

class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }


    componentDidMount() {  
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => { 
              const users = response.data.results
                console.dir(response.data)
                    this.setState(
                  {
                      'users': users
                  }
                )
            }).catch(error => console.log(error))
        
        
            axios.get('http://127.0.0.1:8000/api/projects')
            .then(response => { 
              const projects = response.data.results
                console.dir(response.data)
                    this.setState(
                  {
                      'projects': projects
                  }
                )
            }).catch(error => console.log(error))  


            axios.get('http://127.0.0.1:8000/api/TODO')
            .then(response => { 
              const todos = response.data.results
                console.dir(response.data)
                    this.setState(
                  {
                      'todos': todos
                  }
                )
            }).catch(error => console.log(error))  
            
            
          
            
    }

  render () {
    return (
      <div className='App'>
        <BrowserRouter>
          <Header />
          <Menu />
          <nav>
            <ul>
              <li>
                <Link to="/">Users</Link>
                <Link to="/projects">Projects</Link>
                <Link to="/TODO">TODO</Link>
              </li>
            </ul>
          </nav>
            <Routes>
              <Route path="/" element={<UserList users={this.state.users} />
              } />
              <Route path="/projects" element={<ProjectList projects={this.state.projects} />
              } />
              <Route path="/TODO" element={<TodoList todos={this.state.todos} />
              } />
            </Routes>
        {/* <UserList users={this.state.users} /> */}
            {/* <ProjectList projects={this.state.projects} />  */}
          <Footer />
        </BrowserRouter>
      </div>
    )
  }
}

export default App;
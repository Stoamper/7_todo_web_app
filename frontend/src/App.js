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
import LoginForm from './components/Auth';
import Cookies from 'universal-cookie/es6';

class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    set_token(token) {
      const cookies = new Cookies()
      cookies.set('token', token)
      this.setState({'token': token})
    }

    is_authenticated() {
      return this.state.token != ''
    }

    logout() {
      this.set_token('')
    }

    get_token_from_storage() {
      const cookies = new Cookies()
      const token = cookies.get('token')
      this.setState({'token': token})
    }

    get_token(username, password) {
      axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
          this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
      }

    // get_token(username, password) {
    //   axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    //   .then(response => {
    //     console.log(response.data)
    //   }).catch(error => alert('Неверный логин или пароль'))
    // }

    load_data() {
      axios.get('http://127.0.0.1:8000/api/users')
        .then(response => {
          this.setState({users: response.data.results})
        }).catch(error => console.log(error))

      axios.get('http://127.0.0.1:8000/api/projects')
        .then(response => {
          this.setState({projects: response.data.results})
        }).catch(error => console.log(error)) 

      axios.get('http://127.0.0.1:8000/api/TODO')
        .then(response => {
          this.setState({todos: response.data.results})
        }).catch(error => console.log(error)) 
      }

    componentDidMount() {
      this.get_token_from_storage()
      this.load_data()
    }  


    // componentDidMount() {  
    //     axios.get('http://127.0.0.1:8000/api/users')
    //         .then(response => { 
    //           const users = response.data.results
    //             console.dir(response.data)
    //                 this.setState(
    //               {
    //                   'users': users
    //               }
    //             )
    //         }).catch(error => console.log(error))
        
        
    //         axios.get('http://127.0.0.1:8000/api/projects')
    //         .then(response => { 
    //           const projects = response.data.results
    //             console.dir(response.data)
    //                 this.setState(
    //               {
    //                   'projects': projects
    //               }
    //             )
    //         }).catch(error => console.log(error))  


    //         axios.get('http://127.0.0.1:8000/api/TODO')
    //         .then(response => { 
    //           const todos = response.data.results
    //             console.dir(response.data)
    //                 this.setState(
    //               {
    //                   'todos': todos
    //               }
    //             )
    //         }).catch(error => console.log(error))  
            
            
          
            
    // }

  render () {
    return (
      <div className='App'>
        <BrowserRouter>
          <Header />
          <Menu />
          <nav>
            <ul>
              <li> <Link to="/">Users</Link> </li>
              <li> <Link to="/projects">Projects</Link> </li>
              <li> <Link to="/TODO">TODO</Link> </li>
              {/* <li> <Link to="/login">Login</Link> </li> */}
              <li>{this.is_authenticated() ? <button onClick={() => 
              this.logout()}>Logout</button> : 
              <Link to='/login'>Login</Link>}</li>
            </ul>
          </nav>
            <Routes>
              <Route path="/" element={<UserList users={this.state.users} />
              } />
              <Route path="/projects" element={<ProjectList projects={this.state.projects} />
              } />
              <Route path="/TODO" element={<TodoList todos={this.state.todos} />
              } />
              <Route path="/login" element={<LoginForm get_token={(username,password) => this.get_token(username, password)}/>
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
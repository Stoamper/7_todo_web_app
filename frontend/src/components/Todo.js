import React from 'react'

const TodoItem = ({todo}) => {
    return (
        // <table>
        //     <thead>
                <tr>
                    {/* <td>{project.url}</td> */}
                    <td>{todo.todo_text}</td>
                    <td>{todo.created}</td>
                    <td>{todo.modified}</td>
                    <td>{todo.is_active}</td>
                    <td>{todo.project}</td>
                    <td>{todo.user}</td>
                </tr>
        //     </thead>
        // </table>
    )
}

const TodoList = ({todos}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>TODO_About</th>
                    <th>Created_at</th>
                    <th>Modified_at</th>
                    <th>Active task</th>
                    <th>Project</th>
                    <th>User</th>
                </tr>
            
            {/* {users.map((user, index) => <UserItem user={user} key={index} />)} */}
            {todos.map((todo) => <TodoItem todo={todo} />)}
            </thead>
        </table>
    )
}

export default TodoList
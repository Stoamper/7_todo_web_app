import React from 'react'

const UserItem = ({user}) => {
    return (
        // <table>
        //     <thead>
                <tr>
                    <td>{user.first_name}</td>
                    <td>{user.last_name}</td>
                    <td>{user.birthday_year}</td>
                </tr>
        //     </thead>
        // </table>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>First name</th>
                    <th>Last Name</th>
                    <th>Birthday year</th>
                </tr>
            
            {/* {users.map((user, index) => <UserItem user={user} key={index} />)} */}
            {users.map((user) => <UserItem user={user} />)}
            </thead>
        </table>
    )
}

export default UserList
import React from 'react'

const ProjectItem = ({project}) => {
    return (
        // <table>
        //     <thead>
                <tr>
                    {/* <td>{project.url}</td> */}
                    <td>{project.project_title}</td>
                    <td>{project.repo_link}</td>
                    <td>{project.users_in_project}</td>
                </tr>
        //     </thead>
        // </table>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Link</th>
                    <th>Users</th>
                </tr>
            
            {/* {users.map((user, index) => <UserItem user={user} key={index} />)} */}
            {projects.map((project) => <ProjectItem project={project} />)}
            </thead>
        </table>
    )
}

export default ProjectList
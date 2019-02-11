import React, { useState, useEffect } from 'react'
import { graphql, compose } from 'react-apollo'
import { getProjectQuery } from '../../queries/queries'
import { addProjectMutation, editProjectMutation } from '../../queries/queries'
import Editor from '../../components/Editor'
import { box, innerBox, img, title, button } from './styled.js'

const ProjectForm = (props) => {
  const projectData = props.data && props.data.project

  const initialFormState = {
    title: (projectData && projectData.title) || '',
    content: (projectData && projectData.content) || '',
    image: (projectData && projectData.image) || '',
  }

  const [ initialized, setInitialized ] = useState(false)
  const [ project, setProject ] = useState(initialFormState)

  useEffect(() => {
    if (!initialized && projectData) {
      setProject({
        ...projectData,
        content: projectData.content
      })
      setInitialized(true)
    }
  })

  const handleChange = (e) => {
    const { name, value } = e.target
    setProject({ ...project, [name]: value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!project.title || !project.content) return
    if (props.location.pathname === '/new') {
      props.addProjectMutation({
        variables: {
          ...project,
          content: project.content,
        }
      })
    } else {
      props.editProjectMutation({
        variables: {
          ...project,
          id: projectData && projectData.id,
          content: project.content,
        }
      })
    }
    setProject(initialFormState)
    props.history.push('/')
  }

  return (
    <div {...box}>
      <form {...innerBox} onSubmit={handleSubmit}>
        <input type="text" name="title" value={project.title} onChange={handleChange} placeholder="Enter Title" {...title} />
        <input type="text" name="image" value={project.image} onChange={handleChange} placeholder="Enter Image Link" {...img} />
        <Editor value={project.content} onChange={(e) => setProject({ ...project, ['content']: e }) } />
        <button {...button}>Submit</button>
      </form>
    </div>
  )
}

export default compose(
  graphql(addProjectMutation, { name: "addProjectMutation" }),
  graphql(editProjectMutation, { name: "editProjectMutation" }),
  graphql(getProjectQuery, {
    options: (props) => {
      console.log(props)
      const { match: { params: { id } } } = props
      return { variables: { id } }
    }
  })
)(ProjectForm)
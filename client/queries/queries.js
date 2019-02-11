import { gql } from 'apollo-boost'

export const getProjectsQuery = gql`
  {
    projects {
      title
      content
      image
      id
    }
  }
`

export const getProjectQuery = gql`
  query($id: ID!){
    project(id: $id) {
      id
      title
      content
      image
    }
  }
`

export const addProjectMutation = gql`
  mutation($title: String!, $content: String!, $image: String!) {
    addProject(title: $title, content: $content, image: $image) {
      id
      title
      content
      image
    }
  }
`

export const editProjectMutation = gql`
  mutation($id: ID!, $title: String!, $content: String!, $image: String!) {
    editProject(id: $id, title: $title, content: $content, image: $image) {
      id
      title
      content
      image
    }
  }
`
import React from 'react'
import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import { isNil } from 'ramda'
import Loader from 'react-loader-spinner'
import { getProjectQuery } from '../../queries/queries'
import Navigation from '../../components/Navigation'
import { box, innerBox, img, title, t, button } from './styled.js'

const ProjectPage = props => {
  const { project } = props.data
  return (
    <div {...box}>
      <Navigation />
      {!isNil(project)
        ? <div {...innerBox}>
            <img src={project && project.image} {...img} />
            <span {...title}>{project && project.title}</span>
            <div {...t} dangerouslySetInnerHTML={{ __html: project && project.content }} />
            <Link to={{pathname: `/project/${project && project.id}/edit`, id: project && project.id}}><button {...button}>Edit</button></Link>
          </div>
        : <div {...innerBox}>
            <Loader 
              type="ThreeDots"
              color="#607d8b"
              height="100"	
              width="100"
            />
          </div>}
    </div>
  )
}

export default graphql(getProjectQuery, {
  options: (props) => {
    const { match: { params: { id } } } = props
    return { variables: { id } }
  }
})(ProjectPage);
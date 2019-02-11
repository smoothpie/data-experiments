import React from 'react'
import { graphql } from 'react-apollo'
import { css } from 'glamor'
import { isNil } from 'ramda'
import Loader from 'react-loader-spinner'
import { getProjectsQuery } from '../../queries/queries'
import ProjectOverview from '../ProjectOverview';

let box = css({
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
})

const Projects = (props) => {
  const { projects } = props.data
  return (
    <div {...box}>
      {!isNil(projects)
        ? projects.map(p => (
          <ProjectOverview key={p.id} id={p.id} title={p.title} image={p.image} />
        ))
        : <Loader 
            type="ThreeDots"
            color="#607d8b"
            height="100"	
            width="100"
          />
      }
    </div>
  )
}

export default graphql(getProjectsQuery)(Projects)
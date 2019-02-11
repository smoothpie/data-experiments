import React from 'react'
import { Link } from 'react-router-dom'
import { box, innerBox } from './styled'

const ProjectOverview = ({ id, title, image }) => (
  <Link to={{pathname: `/project/${id}`, image: image, id}} {...box}>
    <img src={image} />
    <div {...innerBox}>{title}</div>
  </Link>
)

export default ProjectOverview
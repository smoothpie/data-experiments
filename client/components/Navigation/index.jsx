import React from 'react'
import { Link } from 'react-router-dom'
import { style } from 'glamor'

let box = style({
  display: 'flex',
  flexDirection: 'column',
  padding: '10px 30px'
})

let title = style({
  color: '#fff',
  fontSize: '36px',
})

let subtitle = style({
  color: '#607d8b',
  fontSize: '36px',
  lineHeight: 0.8
})

let link = style({
  color: '#fff',
  fontSize: '36px',
  textDecoration: 'none',
  marginRight: 10
})

const Navigation = () => (
  <div {...box}>
    <span {...title}>smoothpie prod</span>
    <span {...subtitle}>data experiments</span>
    <div>
      <Link {...link} to='/'>projects</Link>
      <Link {...link} to='/new'>new project</Link>
    </div>
  </div>
)

export default Navigation
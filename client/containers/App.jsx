import React from 'react'
import { Switch, Route } from 'react-router-dom'
import { hot } from 'react-hot-loader/root'
import { css } from 'glamor'
import Home from './Home'
import ProjectPage from './ProjectPage'
import ProjectForm from './ProjectForm'

css.global('html, body',  { margin: 0 })
css.global('span, p, a',  { fontFamily: 'Barlow' })

const App = () => [
  <Switch key="switch">
    <Route exact path="/" component={Home} />
    <Route exact path="/project/:id" component={ProjectPage} />
    <Route exact path="/project/:id/edit" component={ProjectForm} />
    <Route exact path="/new" component={ProjectForm} />
  </Switch>,
]

export default hot(App)
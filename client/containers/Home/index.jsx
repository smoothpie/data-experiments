import React from 'react'
import { css } from 'glamor'
import Navigation from '../../components/Navigation'
import Projects from '../Projects'

let box = css({
  width: '100%',
  height: '100%',
  minHeight: '100vh',
  backgroundColor: '#1c1a1a'
})

const Home = () => (
  <div {...box}>
    <Navigation />
    <Projects />
  </div>
)

export default Home
import { css } from 'glamor'

export const box = css({
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  backgroundColor: '#1c1a1a',
  height: '100vh',
  color: '#fff'
})

export const innerBox = css({
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  color: '#fff'
})

export const title = css({
  position: 'absolute',
  top: 10,
  width: 500,
  height: 35,
  border: 'none',
  borderRadius: 4,
  textAlign: 'center',
  fontSize: '16px',
  color: '#fff',
  outline: 'none',
  backgroundColor: 'transparent',
})

export const img = css({
  position: 'absolute',
  top: 50,
  width: 500,
  height: 35,
  border: 'none',
  borderRadius: 4,
  textAlign: 'center',
  fontSize: '16px',
  backgroundColor: 'transparent',
  outline: 'none',
  color: '#fff',
})

export const button = css({
  width: 150,
  height: 40,
  backgroundColor: '#fff',
  borderRadius: 4,
  fontSize: '16px',
  border: 'none',
  outline: 'none',
  marginTop: 100,
})
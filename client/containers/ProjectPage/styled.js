import { css } from 'glamor'

export const box = css({
  width: '100%',
  height: '100%',
  minHeight: '100vh',
  backgroundColor: '#1c1a1a',
  display: 'flex',
  flexDirection: 'column',
  paddingBottom: 20
})

export const innerBox = css({
  width: '100%',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  marginTop: 20
})

export const img = css({
  width: '45%',
  borderRadius: 8
})

export const title = css({
  color: '#fff',
  fontSize: '26px',
  marginTop: 20
})

export const t = css({
  color: '#fff',
  fontSize: '18px',
  marginTop: 20,
  marginBottom: 10,
  width: '95%'
})

export const button = css({
  width: 150,
  height: 40,
  backgroundColor: '#fff',
  borderRadius: 4,
  fontSize: '16px',
  border: 'none',
  outline: 'none',
  marginTop: 15,
})
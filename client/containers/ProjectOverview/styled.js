import { css } from 'glamor'

export const box = css({
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  width: '95%',
  maxWidth: 1600,
  height: 500,
  borderRadius: 4,
  overflow: 'hidden',
  margin: '20px 0',
  color: 'inherit',
  textDecoration: 'none'
})

export const innerBox = css({
  color: '#fff',
  position: 'absolute',
  width: '90%',
  maxWidth: 1500,
  height: 400,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  backgroundColor: 'rgba(96, 125, 139, 0.6)',
  fontSize: '30px'
})
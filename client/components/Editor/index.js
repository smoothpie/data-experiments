import React from 'react'
import ReactQuill from 'react-quill'
import { css } from 'glamor'

css.global('.quill', {
  maxHeight: 500
})

css.global('.ql-syntax', {
  backgroundColor: '#23241f',
  color: '#f8f8f2',
  overflow: 'visible',
  padding: '3px',
  borderRadius: '2px',
  width: 'fit-content'
})

const Editor = (props) => {

  let modules = {
    toolbar: [
      [{ 'header': [1, 2, false] }],
      ['bold', 'italic', 'underline','strike', 'blockquote', 'code-block'],
      [{'list': 'ordered'}, {'list': 'bullet'}, {'indent': '-1'}, {'indent': '+1'}],
      ['link', 'image'],
      ['clean']
    ],
  }

  let formats = [
    'header',
    'bold', 'italic', 'underline', 'strike', 'blockquote', 'code-block',
    'list', 'bullet', 'indent',
    'link', 'image'
  ]

  return (
    <ReactQuill
      value={props.value}
      onChange={props.onChange}
      modules={modules}
      formats={formats}
    />
  )
}

export default Editor
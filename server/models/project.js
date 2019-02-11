const mongoose = require('mongoose')
const Schema = mongoose.Schema

const projectSchema = new Schema({
  title: String,
  content: String,
  image: String,
})

module.exports = mongoose.model('Project', projectSchema)
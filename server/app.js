const express = require('express')
const graphqlHTTP = require('express-graphql')
const schema = require('./schema/schema')
const mongoose = require('mongoose')
const cors = require('cors')
const bodyParser = require('body-parser')

const app = express()

app.use(cors())

mongoose.connect('mongodb://smoothpie:freddydurst96@ds251179.mlab.com:51179/graphql')
mongoose.connection.once('open', () => {
  console.log('connected to database')
})

app.use(bodyParser.json({limit: '2mb'}));

app.use('/graphql', graphqlHTTP({
  schema,
  graphiql: true
}))

app.listen(4000, () => {
  console.log('listening on port 4000')
})
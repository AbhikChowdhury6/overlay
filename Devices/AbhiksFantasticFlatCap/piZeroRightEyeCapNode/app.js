const express = require('express')
const app = express()

const IPFS = require('ipfs')

const node = new IPFS()

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(3000, () => console.log('Example app listening on port 3000!'))

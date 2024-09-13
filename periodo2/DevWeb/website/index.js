var express = require('express');
const {request} = require("express");
var app = express();

var produtos = [];

app.use(express.static('./pages'));
app.use(express.json());

const port = 3000;
const router = express.Router();

router.get('/api/produtos', (req, res) => {
    console.log('entrou no /api/produtos');
    res.status(200).json(produtos);
});

router.post('/api/produtos', (req, res) => {
    const produto = req.body;
    console.log(produto);
    produto.id = produtos.length + 1;
    produtos.push(produto);
    res.status(201).json(produto);
});

router.delete('/api/produtos/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const index = produtos.findIndex(p => p.id === id);
        produtos.splice(index, 1);
        res.status(204).send('Produto excluido com sucesso');
});

app.use(router);
app.use(express.static('./pages'));

app.get('/hello', (req, res) => {
    res.send('Hello, World!');
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
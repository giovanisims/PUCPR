var express = require('express');
var app = express();

app.use(express.static('./pages'));

const port = 3000;
const router = express.Router();
app.use(express.json());

var produtos = [];
var usuarios = [];

router.post("/api/usuarios", (req, res) => {
    const usuario = req.body;
    usuario.id = usuarios.length + 1;
    usuarios.push(usuario);
    res.status(201).json(usuario);
});

router.get("/api/produtos", (req, res) => {
    res.status(200).json(produtos);
});

app.use(router);
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
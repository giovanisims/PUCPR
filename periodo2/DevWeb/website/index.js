var express = require('express');
var app = express();

app.use(express.static('./pages'));

const port = 3000;
const router = express.Router();
app.use(express.json());

var mysql = require('mysql2');

var con = mysql.createConnection({
    host: "127.0.0.1",
    user: "root",
    port: "3305",
    password: "PUC@1234",
    database: "aulaWeb"
});

con.connect((err) => {
        if (err) throw err;
        console.log("Connected!")
});

var produtos = [];
var usuarios = [];

router.post("/api/usuarios", (req, res) => {
    const usuario = req.body;
    
    var sql = `INSERT INTO usuario (nome, email, data, estado)
    VALUES
    ('${usuario.nome}',
    '${usuario.email}',
    '${usuario.data}',
    '${usuario.estado}')`;

    con.query(sql, function(err, result){
        if (err) throw err
    })

    response.status(201).json(usuario)
});

router.get("/api/usuarios", (req, res) => {
    var sql = 'SELECT id,nome,email,estado FROM usuario';
    con.query(sql,function (err, result) {
        if (err) throw err;
        res.status(200).json(result);
    })
});

router.post("/api/usuarios", (req, res) => {
    const usuario = req.body;
    usuario.id = usuarios.length + 1;
    usuarios.push(usuario);
    res.status(201).json(usuario);
});

router.get("/api/usuarios", (req, res) => {
    res.status(200).json(usuarios);
});

router.get("/api/produtos", (req, res) => {
    res.status(200).json(produtos);
});

app.use(router);
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
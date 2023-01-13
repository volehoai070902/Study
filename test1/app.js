const express = require("express");
const bodyParser = require('body-parser');
const bcrypt = require("bcrypt");
const hbs = require("hbs");
const app = express();
const mongoose = require("mongoose");
const router = require("./router/index");
let passwordDB;
const password = "lehoai123";
app.set('view engine', 'hbs');
app.use(express.json());
app.use(express.urlencoded({extended:false}));

mongoose.set('strictQuery', false);
mongoose.connect("mongodb://127.0.0.1:27017/Love", (err)=>{
    if (err)
        return;
    console.log("connected to database");
})

router(app);

app.listen(3000,()=>{
    console.log("xin chao");
})
const express = require("express");
const bodyParser = require('body-parser');
const bcrypt = require("bcrypt");
const hbs = require("hbs");
const app = express();
const mongoose = require("mongoose");
const router = require("./router/index");
const passport = require("passport");
const session = require('express-session');
const initializePassport = require("./config/passport-config");

app.set('view engine', 'hbs');
app.use(express.json());
app.use(express.urlencoded({extended:false}));

initializePassport(passport);

app.use(session({
    secret: 'secret',
    resave: false,
    saveUninitialized: false,
  }));

mongoose.set('strictQuery', false);
mongoose.connect("mongodb://127.0.0.1:27017/Love", (err)=>{
    if (err)
        return;
    console.log("connected to database");
})

app.use(passport.initialize());
app.use(passport.session());
passport.authenticate
router(app);

app.listen(3000,()=>{
    console.log("xin chao");
})
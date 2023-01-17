const express = require("express");
const bodyParser = require("body-parser");
const bcrypt = require("bcrypt");
const exphbs = require("express-handlebars").engine;
const app = express();
const path = require("path");
const mongoose = require("mongoose");
const router = require("./router/index");
const passport = require("passport");
const flash = require("express-flash");
const session = require("express-session");
const initializePassport = require("./config/passport-config");
const { options } = require("./router/homeRouter");


//view engine
app.set("views", path.join(__dirname, "views"));
app.engine('hbs',exphbs({
  extname:"hbs",
  defaultLayout:'layouts',
  partialsDir: __dirname + "/views/partials"
}))
app.set("view engine", "hbs");

app.use(express.static(path.join(__dirname, "/public")));

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(function(req,res,next){
  console.log("chào mừng các bạn đã đến với kỉ nguyên của chúng tôi")
  next();
})
initializePassport(passport);

mongoose.set("strictQuery", false);
mongoose.connect("mongodb://127.0.0.1:27017/Love", (err) => {
  if (err) return;
  console.log("connected to database");
});


app.use(
  session({
    secret: "secret",
    resave: false,
    saveUninitialized: false,
  })
);
app.use(passport.initialize());
app.use(passport.session());
app.use(flash());
router(app);

app.listen(3000, () => {
  console.log("xin chao");
});

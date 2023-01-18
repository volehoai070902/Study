const express = require("express");
const app = express();
const path = require("path");
const exphbs = require("express-handlebars").engine;

app.set("views", __dirname + path.join("/views"));
app.engine('hbs',exphbs({
    extname:"hbs",
    defaultLayout:'layouts',
    partialsDir: __dirname + "/views/partials"
}))
app.set("view engine", "hbs");

app.use(express.static(path.join(__dirname, "/public")));
app.get("/",(req,res)=>{
    res.render("addProduct");
})

app.listen(5000);

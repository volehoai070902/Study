const homeRouter = require("./homeRouter");
const loginRouter = require("./loginRouter");
const registerRouter = require("./registerRouter");
//const userRouter = require ("../router/userRouter");
const logoutRouter = require("./logOut");
function route(app){
    app.use("/", homeRouter);
    app.use("/login",loginRouter);
    app.use("/register",registerRouter);
    app.use("/logout", logoutRouter);
}

module.exports = route;
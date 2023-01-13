const homeRouter = require("../router/");
const loginRouter = require("../router/loginRouter");
const registerRouter = require("../router/registerRouter");
//const userRouter = require ("../router/userRouter");
function route(app){
    //app.use("/", homeRouter);
    app.use("/login",loginRouter);
    app.use("/register",registerRouter);
}

module.exports = route;
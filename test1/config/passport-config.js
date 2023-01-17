const LocalStrategy = require("passport-local").Strategy;
const async = require("hbs/lib/async");
const userModel = require("../model/userModel");
const bcrypt = require("bcrypt");
const { use } = require("passport");

async function initialize(passport) {
    const authenticate = async (email, password, done) => {
        const user = await userModel.findOne({ email: email })
        if (!user) { return done(null, false,{message: "email incorrect"}); }
        if (!await bcrypt.compare(password, user.password)) {
            return done(null,false,{message: "password incorrect"},);
        }
        return done(null,user);
    }
    passport.use(new LocalStrategy({ usernameField: 'email' }, authenticate));
    passport.serializeUser((user,done)=>{
        done(null,{
            email:user.email,
            id:user._id
        })});
    passport.deserializeUser((user, done)=>{
        done(null, user);
    });
}

module.exports = initialize;
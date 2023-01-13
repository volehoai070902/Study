const LocalStrategy = require("passport-local").Strategy;



function initialize(passport){
    const authenticate = async (email,password,done)=>{

    } 
    passport.use(new LocalStrategy({usernameField:'email'}), authenticate);
    passport.serializeUser((user,done)=>{});
    passport.deserializeUser((id, done)=>{});
}

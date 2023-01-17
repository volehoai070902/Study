const router = require("express").Router();
const loginController = require("../controller/loginController");
const passport = require("passport");

router.get("/", loginController.getLogin);
router.post("/", passport.authenticate('local', {
    successRedirect: '/',
    failureRedirect: '/login',
    failureFlash:true,
}),(req,res)=>{
    console.log("con cho nay");
});


module.exports = router;

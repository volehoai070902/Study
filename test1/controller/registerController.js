const userModel = require("../model/userModel");
const bcrypt = require("bcrypt");
const registerController = {
    getRegister: async(req,res) =>{
        res.render("register");
    },

    postRegister: async(req,res) =>{
        try {
            let hashPassword;
            const salt = await bcrypt.genSalt(10);
            hashPassword = await bcrypt.hash(req.body.password,salt);
        
            const user = new userModel({
                email: req.body.email,
                password:hashPassword
            })
            user.save();
            res.render("login");
        } catch (error) {
            
        }
    }
}

module.exports = registerController;
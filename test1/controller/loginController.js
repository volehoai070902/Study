const bcrypt = require("bcrypt");
const userModel = require("../model/userModel");

const loginController = {
    getLogin: async(req,res)=>{
        res.render('login');
    },

    postLogin: async(req,res)=>{
        
    }
}

module.exports = loginController;
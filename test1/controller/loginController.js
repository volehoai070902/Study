const bcrypt = require("bcrypt");
const userModel = require("../model/userModel");
const a = require("../test1");
const loginController = {
  getLogin: async (req, res) => {
    if (req.user) {
        console.log("hello các bạn")
        res.redirect("/");
    }
    res.render("login",{
        layout: false
    })
  },

  postLogin: async (req, res) => {},
};

module.exports = loginController;

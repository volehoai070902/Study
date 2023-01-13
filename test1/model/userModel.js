const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const User = new Schema({
    email: {
        type:String,
        require:true,
        unique:true,
    },
    password: {
        type: String,
        require:true,
    },
    
},{collection:"User"})

const model = mongoose.model("User", User);

module.exports = model;
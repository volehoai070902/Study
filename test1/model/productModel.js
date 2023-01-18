const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const product = new Schema({
    id: new Date.now(),
    name:String,
    price: Number,
    image: String,
    description: String,
})

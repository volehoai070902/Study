const router = require("express").Router();
const registerController = require("../controller/registerController");
router.get("/",registerController.getRegister);

router.post("/",registerController.postRegister);

module.exports = router;
const router = require("express").Router();
const loginController = require("../controller/loginController");

router.get("/", loginController.getLogin);
router.post("/", loginController.postLogin);
module.exports = router;

const homeController = {
    getHome: async(req,res)=>{
        if (req.user){
            res.render("home",{
                user: req.user
            });
        }
        else{
        res.render("home");
        }
    }
}

module.exports = homeController;
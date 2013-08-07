function handleLogout(){
    $.ajax(
        {
            url: "/logout",
            type: "POST",
            success: (function(){ window.location.href = "/";})
        });
}

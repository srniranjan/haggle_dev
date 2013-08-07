function removeAdmin(target) {
    var vendor_id = $("#vendor-id").val();
    $.ajax({
        url:"/api/vendors/" + vendor_id + "/admins",
        type:"POST",
        data:{remove_admin : target.id},
        success:function (data) {
            if (data.length > 0) {
                $("#error-remove").removeClass("hide-element");
            } else {
                window.location.reload();
            }
        },
        error:function () {
            $("#error-remove").removeClass("hide-element");
        }
    });
}

function addAdmin() {
    var vendor_id = $("#vendor-id").val();
    var name = $("#name").val();
    var email = $("#email").val();
    var role = $("#role").val();
    $.ajax({
        url:"/api/vendors/" + vendor_id + "/admins",
        type:"put",
        data:{email : email, name : name, role : role },
        success:function (data) {
            if (data.length > 0) {
                $("#error-add").removeClass("hide-element");
            } else {
                window.location.reload();
            }
        },
        error:function () {
            $("#error-add").removeClass("hide-element");
        }
    });
}
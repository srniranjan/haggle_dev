function addTPVendor(){
    var vendor_id = $("#vendor-id").val();
    var network = $("#tp-network").val();
    var url = $("#tp-url").val();
    var id = network + "|" + url;
    $.ajax({
        url:"/api/vendors/" + vendor_id + "/social_networks",
        type:"put",
        data:{add_vendors:id},
        success:function (data) {
            if(data.length >0){
                $("#error-add").removeClass("hide-element");
            }else{
                window.location.reload();
            }
        },
        error:function () {
            $("#error-add").removeClass("hide-element");
        }
    });
}


$(document).ready(function () {
    $("#social-networks").addClass('active');
    $("#update-tags").click(function(){
        var vendor_id = $("#vendor-id").val();
        $.ajax({
            url:"/api/vendors/" + vendor_id + "/social_networks",
            type:"put",
            data:{"tags":$("#tags").val()},
            success:function (data) {
                if(data.length >0){
                    $("#error-add").removeClass("hide-element");
                }else{
                    window.location.reload();
                }
            },
            error:function () {
                $("#error-add").removeClass("hide-element");
            }
        });
    });
});


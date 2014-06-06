function fetchResponse(event) {
    event.preventDefault();
    var fetch_url = $('#url').val();
    var method = "POST";
    var data = null;
    var endpoint = $("#endpoint").val();
    if( fetch_url == 'local') {
        fetch_url = endpoint;
        method = "GET";
        data = $("#params").serialize();
    } else {
        fetch_url = "/fetch_from_api_server";
        data = {"endpoint": endpoint, "data": $("#params").serialize(), "token": $("#token").val()};
    }
    $.ajax({
        type: method,
        url: fetch_url,
        data: data,
        beforeSend: function(){
            $('#response').hide();
            $('#loading_indicator').show();
        },
        success: function(data){
            var pretty_data = JSON.stringify(JSON.parse(data), undefined, 4);
            $('#response').html(pretty_data);
            $('#loading_indicator').hide();
            $('#response').show();
        }
    });
    return false;
}

$(document).ready(function(){
    $('.endpoints-table td a').click(function(event){
        event.preventDefault();
        var fetch_url = $(this).attr('href');
        $.ajax({
            type: "GET",
            url: fetch_url,
            beforeSend: function(){
                $('.tab-pane').hide();
            },
            success: function(data){
                $('#endpoint-view').html(data);
                $('#endpoint-view').show();
            }
        });
    });
});
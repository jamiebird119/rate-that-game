$("#group_by").change(function(){
    value = $('#group_by').val()
    if(value == "conf"){
    redirectURL = window.location.href.replace("div", value);
    }else if(value == 'div'){
    redirectURL = window.location.href.replace("conf", value);
    }
    window.location = redirectURL;
})
function GetLastMessages(){
    $.ajax({
        url : "/get-messages",
        type : "GET",
        success : function(res)
        {
            
        },
        error : function(res)
        {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        }
    })
}
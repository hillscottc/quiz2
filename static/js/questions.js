
$(document).ready(function() {
    $(".radio_answer").click(function(){
        q_id = this.name;
        a_id = this.value
        post_url = "/quiz/post_answer/" + a_id + "/"; 
		$.ajax({url:post_url, 
                success:function(result){
                    $("#result_" + q_id).html(result);
                    if (result.indexOf("Correct!") != -1) {
                        $("#result_" + q_id).css('color', 'green');
                    } else {
                        $("#result_" + q_id).css('color', 'red');    
                    }
                },
                error:function(xhr, textStatus, errorThrown){
                    error_msg = "Error!" + errorThrown + xhr.status + xhr.responseText
                    $("#result_" + q_id).html(error_msg);}                   
                }
        );        
    });
});

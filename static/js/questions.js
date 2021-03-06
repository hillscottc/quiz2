
$(document).ready(function() {
    $(".radio_answer").click(function(){
        q_id = this.name;
        a_id = this.value
        post_url = "/quiz/answer/post/" + a_id + "/";
		$.ajax({url:post_url, 
                success:function(result){
                    $("#result_" + q_id).html(result);
                    if (result.indexOf("Correct!") != -1) {
                        $("#result_" + q_id).attr('class', 'alert alert-success');
                    } else {
                        $("#result_" + q_id).attr('class', 'alert alert-danger')
                    }
                },
                error:function(xhr, textStatus, errorThrown){
                    error_msg = "Error!" + errorThrown + xhr.status + xhr.responseText
                    $("#result_" + q_id).html(error_msg);}                   
                }
        );        
    });
});


$(document).ready(function() {
    $(".radio_answer").click(function(){
        q_id = this.name;
        a_id = this.value
        post_url = "/quiz/post_answer/" + q_id + "/" + a_id + "/"; 
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

// function post_answer() {
//     var board = $('#game-board').attr('data-board-id');
//     $.ajax({
//         type: "POST",
//         url: $('#game-board').attr('data-done-ref'),  // or just url: "/my-url/path/"
//         data: {
//             csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
//             board: board,
//             move_list: move_list.join(','),
//         },
//         success: function(data) {
//             alert("Congratulations! You scored: "+data);
//         },
//         error: function(xhr, textStatus, errorThrown) {
//             alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
//         }
//     });
// }
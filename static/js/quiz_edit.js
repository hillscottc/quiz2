
$(document).ready(function() {


    $("#form1 :input").change(function() {
      $(this).closest('form').data('changed', true);
        alert("changed!")
//        $('.btn-submit').css("background-color", "yellow");
        $(".btn-submit").attr('class', 'btn btn-default btn-submit');
    });


});

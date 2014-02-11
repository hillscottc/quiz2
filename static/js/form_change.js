
$(document).ready(function() {

    // when form changes, change button from gray to active
    $("#form1 :input").change(function() {
      $(this).closest('form').data('changed', true);
        $(".change-submit").attr('class', 'btn btn-success change-submit');
        $(".change-cancel").attr('class', 'btn btn-warning change-cancel');
    });

});

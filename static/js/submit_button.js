
$(document).ready(function() {

    // when form changes, change button from gray to active
    $("#form1 :input").change(function() {
      $(this).closest('form').data('changed', true);
        $(".btn-submit").attr('class', 'btn btn-success btn-submit');
    });

});

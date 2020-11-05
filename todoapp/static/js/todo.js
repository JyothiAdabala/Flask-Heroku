$(function() {
    send_response = function(prop) {
        let val = $('#userinput').val()
        $('#userinput').parent('.form').replaceWith(`<span class="form">${val}</span>`)
        $.post("message", {key:prop, message:val})
        .done(function(response) {
            $('#chat main').append(response);
        })
    }

    get_summary = function() {
        $.ajax({url : 'summary'}).done(function(response) {
            $('#made_count').text(response.made);
            $('#kept_count').text(response.kept);
        })  
    }

})
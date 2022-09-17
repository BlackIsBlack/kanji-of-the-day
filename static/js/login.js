jQuery(function() { 

    // Login user with given credentials

    $("form[name=login]").submit(function(e) {
        e.preventDefault();
        var form = $(this);

        $.ajax({
            type: "POST",
            url: "/login_post",
            data: form.serialize(),
            success: function(data)
            {
                if (data.response == 200) {
                    window.location.href = data.redirect;
                } else {
                    $("#login-error").text(data.message);
                }
            }
        });
    }
    );
});
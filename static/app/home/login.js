




function check() {
    var password = $('#password').val();
    var newpassword = md5(password);
    $('#password').val(newpassword);
    return true;
}


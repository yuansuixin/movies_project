
function check() {

    var username = $('#username').val();
    var u_mail = $('#email').val();

    if (username == '' || u_mail == '') {
        return false
    }

    return true;
}

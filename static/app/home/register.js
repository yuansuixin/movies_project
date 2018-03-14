$(function () {
    $('#username').change(function () {
        var username = $(this).val();
        //$(selector).get(url,data,success(response,status,xhr),dataType)
        //可选。规定连同请求发送到服务器的数据。
        //可选。规定当请求成功时运行的函数,一定不要忘记传参数
        $.get('/app/checkuser/', {'username': username}, function (data) {
            console.log(data);
            if (data['status'] == '888') {
                $('#username_info').html(data['msg']).css('color', 'green');
            } else {
                $('#username_info').html(data['msg']).css('color', 'red');
            }
        })


        $('#password').change(function () {
            var password = $(this).val();
            if (password.length < 6 | password.length > 16) {
                $('#password_info').html('密码长度不符合规范').css('color', 'red');
            } else {
                $('#password_info').html('密码长度规范').css('color', 'green');
            }
        })

        $('#repassword').change(function () {
            var repassword = $(this).val();
            var password = $('#password').val();
            if (password == repassword) {
                $('#repsw_info').html('密码一致').css('color', 'green');
            } else {
                $('#repsw_info').html('密码不一致').css('color', 'red');
            }
        })
    })
})

//提交表单的时候进行摘要，信息更安全
function check() {

     var password = $('#password').val();
    var repassword = $('#repassword').val();
    var username = $('#username').val();

    if ((password != repassword) && password == '' && repassword == '' && username == '') {
        return false
    }


    var newpassword = md5(password);
    $('#password').val(newpassword);
    console.log('摘要后的', newpassword);
    return true;
}












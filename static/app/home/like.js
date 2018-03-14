$(function () {
    $('.movie_like').click(function () {
         //实现字体图标的改变
        //ajax请求实现收藏的操作，
        console.log(123214)
        var moviesid = $(this).attr('moviesid')

        console.log(moviesid);
        var movie = $(this);
        $.getJSON('/app/addlike/', {'id': moviesid}, function (data) {
            console.log(data)
            if (data['status'] == '302') {
                window.open('/app/login/', target = '_self');
            } else if (data['status'] == '200') {
                console.log("data['num']",data['num'])
                movie.children().eq(1).html(data['num'])
                movie.children().eq(0).toggle(function () {
                    movie.children().eq(0).css('color','green');
                },function (){
                     movie.children().eq(0).css('color','green');
                })
            }
        })
    })
})
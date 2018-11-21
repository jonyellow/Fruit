/**
 author: jon
 project: fruit
 action: common model
  **/

//加载主页的商品信息
function load_goods(){
    $.get('/goods_type/', function(data){

    }, 'json')
}

//register 页面检查手机号是否已注册
function check_tel(){
    var telstatus = 1;
    $('[name=tel]').blur(function(){
        if ($(this).val().trim().length == 0)//trim()去除两边的空格。
            return;
        $.get('/checkregister',{"tel":$(this).val()},function(data){
            var html = '<span>' + data.msg + '</span>';
            $('[name=tel]').after(html);
                if (data.status == 0){
                     telstatus = 0;
                }else{
                   telstatus = 1;
            }
            }, 'json')
    });
    //为表单绑定submit事件,注册成功后直接跳转到登录状态
    $('[type=submit]').submit(function(){

    })
}


//利用ajax检查用户的登录状态。
function loginstatus(){
    $.get('/loginstatus',function(data){
        if (data.status == 1){
             var html = '欢迎：'+ data.name;
             $('#rightNav>li>a:first').html(html);
             $('#rightNav>li>a:first').attr('href','#');
             $('#rightNav>li>a:last').html('退出');
             $('#rightNav>li>a:last').attr('href', data.logout);
        }else{
             $('#rightNav>li>a:first').html('[登录]&nbsp;&nbsp;&nbsp; ');
             $('#rightNav>li>a:first').attr('href',data.login);
             $('#rightNav>li>a:last').html('[注册，有惊喜]');
             $('#rightNav>li>a:last').attr('href', data.register);
        }
    }, 'json')
}
//网页加载完成后，立即执行loginstatus函数。
$(function(){
    loginstatus();
    check_tel();
});
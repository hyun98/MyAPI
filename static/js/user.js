function idCheck(){
    if(!$('#username').val()){
        alert("ID를 입력해 주세요.");
        return;
    }

    $.ajax({
        // console.log('dsf');
        type: "POST",
        url: "/api/auth/idcheck/",
        data: {
            'username' : $('#username').val(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response){
            $('#idcheck-result').html(response);
        },
    });
}

function cancleUserRegister() {
    var result = confirm("회원가입을 취소하시겠습니까?");

    if(result){
        $(location).attr('href', 'accountapp:login');
    }
}

function UserRegister() {
    if(!$('#username').val()){
        alert("아이디를 입력해 주시기 바랍니다.");
        return;
    }
    if(!$('#IDCheckResult').val()){
        alert("ID 중복체크를 먼저 진행해 주시기 바랍니다.");
        return;
    }
    if(!$('#password').val()){
        alert("비밀번호를 입력해 주시기 바랍니다.");
        return;
    }
    if($('#password').val() != $('#passwordcheck').val()){
        alert("비밀번호가 일치하지 않습니다.");
        return;
    }
    console.log("register");
    $('#register_form').submit();
}


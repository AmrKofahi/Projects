

$(document).ready(function() {
function validateForm() {

    let isValid = "yes";
    
    $(".fieldValidator").removeClass('invalid-feedback');
    $(".fieldValidator").html('');
    
    /*$("fnameValidator").removeClass('invalid-feedback');
    $("fnameValidator").html('');
    
    $("lnameValidator").removeClass('invalid-feedback');
    $("lnameValidator").html('');
    
    $("emailValidator").removeClass('invalid-feedback');
    $("emailValidator").html('');
    
    $("selectValidator").removeClass('invalid-feedback');
    $("selectValidator").html('');
    
    $("textValidator").removeClass('invalid-feedback');
    $("textValidator").html('');*/
    
    let fname = document.getElementById("fname").value;
    if(fname == null || fname == "") {
        $('#fnameValidator').addClass('invalid-feedback');
        $('#fnameValidator').html('Please enter your first name');
        isValid = "no";
        console.log("First name invalid");
    }

    let lname = document.getElementById("lname").value;
    if(lname == null || lname == "") {
        $("#lnameValidator").addClass('invalid-feedback');
        $("#lnameValidator").html('Please enter your last name');
        isValid = "no";
        console.log("Last name invalid");
    }

    let email = document.getElementById("email").value;
    if(email == null || email == "") {
        $("#emailValidator").addClass('invalid-feedback');
        $("#emailValidator").html('Please fill in your email');
        isValid = "no";
        console.log("Email invalid");
    }
    else if (!email.includes("@") || !email.includes(".")) {
        $("#emailValidator").addClass('invalid-feedback');
        $("#emailValidator").html('Please enter a correct email address');
        isValid = "no";
        console.log("Email invalid");
    }

    let reason = document.getElementById("reason");
    if(reason.selectedIndex === 0) {
        $("#selectValidator").addClass("invalid-feedback");
        $("#selectValidator").html("Please select the reason for contact");
        $("#selectValidator").css("display", "block");
        isValid = "no";
        console.log("Select invalid");
    }

    let message = document.getElementById("message").value;
    if(message == null || message == "") {
        $("#textValidator").addClass("invalid-feedback");
        $("#textValidator").html("Please enter your message in the text box above");
        isValid = "no";
        console.log("Message invalid");
    }

    if(isValid == "yes")
        return true;
    else
        return false;
    
}



$("button").click(function(event) {
    $(".contact_form").addClass('was-validated');
    if(!validateForm()) {
        event.preventDefault();
        event.stopPropagation();
    }

});

var banner = document.getElementById('cookie-banner');
    var button = document.getElementById('accept-cookies');

    if (!getCookie('cookies_accepted')) {
        banner.style.display = 'block';
    }

    button.onclick = function() {
        setCookie('cookies_accepted', true, 365);
        banner.style.display = 'none';
    };

    function setCookie(name, value, days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        var expires = "; expires=" + date.toUTCString();
        document.cookie = name + "=" + value + expires + "; path=/";
    }

    function getCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
        return null;
    }


});



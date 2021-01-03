console.log("start");
jQuery(document).ready(function(){
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let email;
    $('.confirm').hide();
    $('.btn-primary').on('click',function(){
       email = $('input[name=email]').val();
       let password = $('input[name=password]').val();
       $.ajax({
               url: $('input[name=url]').val(),
               type: 'post',
               data: {
                      email: email,
                      password:password,
                      action:"changeemailfirst",
                      csrfmiddlewaretoken:token
               },
               success: function(response){
                    if(response.success == "Vrai"){
                       $('.confirm').show();
                       $('#email-form').hide();
                       $('#change-email-link').hide();
                    }else{
                       $('erroremail').html(response.errorfirst)
                    }
               }
       });
    });
    $('#btn').on('click',function(){
        codse = $('input[name=code]').val();
        $.ajax({
               url: $('input[name=url]').val(),
               type: 'post',
               data: {
                      code:codse,
                      action:"changemailsecond",
                      csrfmiddlewaretoken:token
               },
               success: function(response){
                    if(response.success == "Vrai"){
                       $('.confirm').hide();
                       $('#email-form').show();
                       $('#erroremail').css("color:green;");
                       $('#erroremail').html("L'email a été très bien changé");
                       $('#change-email-link').show();
                       $('#mop').html(email)
                    }else{
                       $('.codeerror').html(response.errorfirst);
                       $('.codeerror').css("color:red;");

                    }
               }
       });

    });
    $('#btn1').on('click',function(){
        normalpass = $('input[name=normalpassword]').val();
        newpass = $('input[name=newpassword]').val();
        cnewpass = $('input[name=cnewpassword]').val();
        $.ajax({
               url: $('input[name=url]').val(),
               type: 'post',
               data: {
                      normalpassword:normalpass,
                      newpassword:newpass,
                      cnewpassword:cnewpass,
                      action:"changepassword",
                      csrfmiddlewaretoken:token
               },
               success: function(response){
                    if(response.success == "Vrai"){
                       $('#errorpassword').html("Le mote de passe a été changé avec succès");
                       $('input[name=normalpassword]').val("");
                       $('input[name=newpassword]').val("");
                       $('input[name=cnewpassword]').val("");
                    }else{
                       $('#errorpassword').html(response.errorsecond);
                    }
               }
        });


    });
    $('#change-email-form')

});
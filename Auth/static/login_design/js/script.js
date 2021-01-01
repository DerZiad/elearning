let erreurs;
let day,month,year;
let vars = new Map();
function addError(key,value){
 	erreurs.set(key,value)
}

function validate_date(date){
    year = parseInt(date.substr(0,4),10);
    month = parseInt(date.substr(5,2),10);
    day = parseInt(date.substr(8,2));
    if(isNaN(day)){
        addError("day","veuillez ne pas entrer une chaîne de caractère dans le jour")
    }
     if(isNaN(month)){
        addError("month","veuillez ne pas entrer une chaîne de caractère dans le mois")
    }
     if(isNaN(year)){
        addError("year","veuillez ne pas entrer une chaîne de caractère dans l'année")
    }

    if(day < 1 || day > 31){
          addError("day","le jour doit figurer entre 1 et 31");
    }

    if(month < 1 || day > 12){
        addError("month","le mois doit figurer entre 1 et 12");
    }
    if(year < 1940 || year > 2100){
              addError("year","l'année doit figurer entre 1941 et 2100");
    }
}

function verifier_Email_Telephone(email,telephone){
		if(email.length == 0){
            addError("email","Vous ne devez pas avoir un email vide")
		}else{
            if(!email.trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) || email.length <= 0) {
                addError("email","Veuillez entrer un email compatible")
            }
		}

		if(telephone.length == 0){
            addError("telephone","Vous ne devez pas avoir un numero de téléphone vide")
		}else{
            if(telephone.length <= 9) {
                addError("telephone","Veuillez entrer un numéro de telephone compatible")
            }
		}
}

function verifier_nom_prenom(nom,prenom){
	if(nom.length == 0){
		addError("nom","Le nom ne doit pas être vide")
	}else {
		if(nom.trim().length> 20 || nom.trim().length <= 2){
		addError("nom","Vous ne devez pas depasser 20 caractères");
		}
	}

	if(prenom.length == 0){
		addError("prenom","Le prenom ne doit pas être vide")
	}else {
		if(prenom.trim().length > 20 || prenom.trim().length <= 2){
		addError("prenom","Vous ne devez pas depasser 20 caractères");
		}
	}


}
function verifierUsername(username){
	if(username.length == 0){
        addError("username","Username doit avoir au plus 18 caractères");
	}else{
		if(username.length>18 || username.length <= 0 ){
			addError("username","Username doit avoir au plus 18 caractères");
		}
	}
}

function verifierPassword(password,cfpassword){
	let test1 = false
	let test2 = false

	if(password.length == 0){
		addError("password","Le mot de passe doit être rempli")
	}else{
		if(password.length > 20){
			addError("password","Le mot de passe doit avoir au plus 20 caractères")
		}else if(password.length <= 9){
			addError("password","Le mot de passe doit depasser au moins 9 caractères")
		}else{
			test1 = true
		}
	}


	if(cfpassword.length == 0){
		addError("cfpassword","La confirmation de mot de passe doit être rempli")
	}else{
		if(cfpassword.length > 20){
			addError("cfpassword","Le mot de passe doit avoir au plus 20 caractères")
		}else if(cfpassword.length <= 9){
			addError("cfpassword","Le mot de passe doit depasser au moins 9 caractères")
		}else{
			test2 = true
		}
	}

	if(test1 && test2){
		if( !(password == cfpassword)){
			addError("cfpassword","La confirmation doit être compatible")
		}
	}


}

function setErrors(){
    for (const [key, value] of erreurs){
					$("#" + key).html(value).show();
    }
}
function hideErrorsFirstPane(){
    $("#nom").hide();
    $("#prenom").hide();
    $("#day").hide();
    $("#month").hide();
    $("#year").hide();
    $("#telephone").hide();
    $("#email").hide();
}
function hideErrorsSecondPane(){
    $("#username").hide();
    $("#password").hide();
    $("#cfpassword").hide();
}

 class Personne{
	constructor( nom,prenom ,datedenaissance,telephone,username ,email ,password){
			  		this.nom = nom
			  		this.prenom = prenom
			  		this.datedenaissance = datedenaissance
			  		this.username = username
			  		this.email = email
			  		this.password = password
			  		this.telephone = telephone
	}
}

var personne = new Personne("","","","","","","","");

jQuery(document).ready(function(){
    $('#Precedent').hide();
    $('#Connector').hide();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    hideErrorsFirstPane();
	$('#Suivant').on('click',function(){
					erreurs = new Map();
					nom = $('input[name=prenom]').val();
					prenom = $('input[name=nom]').val();
					birthday = $('input[name=birthday]').val();
					telephone = $('input[name=telephone]').val();
					email = $('input[name=email]').val();

					verifier_nom_prenom(nom,prenom);
					verifier_Email_Telephone(email,telephone);
					//validatedate(birthday);
					validate_date(birthday);
                    $.ajax({
                                    url: '/Auth/signup',
                                    type: 'post',
                                    data: {
                                    id:"1",
                                    email: email,
                                    telephone:telephone,
                                    csrfmiddlewaretoken:token
                                           },
                                    success: function(response){
                                        count = Object.keys(response).length;
                                        if(count == 0){
                                              if(erreurs.size <= 0){
                                personne.nom = nom;
                                personne.prenom = prenom;
                                personne.datedenaissance = day + "-" + month + "-" + year;
                                personne.email = email;
                                personne.telephone = telephone;
                                $('#Precedent').show();
                                $('#Connector').show();
                                $('#ja-ss').hide();
                                $('#Suivant').attr("id", "Inscription");
                                $('#Suivant').html("Inscription");
                                hideErrorsSecondPane();
                                $('#Inscription').on('click',function(){
                                    erreurs = new Map();
                                    username = $('input[name=username]').val();
                                    password = $('input[name=password]').val();
                                    cfpassword = $('input[name=cfpassword]').val();
                                    verifierPassword(password,cfpassword);
                                    verifierUsername(username);
                                    $.ajax({
                                    url: '/Auth/signup',
                                    type: 'post',
                                    data: {
                                    id:"2",
                                    username: username,
                                    csrfmiddlewaretoken:token
                                           },
                                    success: function(response){
                                        count = Object.keys(response).length;
                                        if(count == 0){
                                                  if(erreurs.size <= 0){
                                                                personne.username = username;
                                                                personne.password = password;
                                                                console.log("i m here 2");
                                                                $.ajax({
                                                                        url: '/Auth/signup',
                                                                        type: 'post',
                                                                        data: {
                                                                        nom:personne.nom,
                                                                        prenom: personne.prenom,
                                                                        email: personne.email,
                                                                        datedenaissance:personne.datedenaissance,
                                                                        username:personne.username,
                                                                        password:personne.password,
                                                                        telephone:personne.telephone,
                                                                        csrfmiddlewaretoken:token
                                                                               },
                                                                        success: function(response){
                                                                            $("#Precedent").hide()
                                                                            $(".container-login100-form-btn").hide()
                                                                            $("#ja-ss").hide()
                                                                            $("#Connector").hide()
                                                                            $("#Error").html(response)
                                                                        }
                                                                });
                                                                console.log(z);

                                                            }else{
                                                                setErrors();
                                                            }
                                        }else{
                                            addError("username",response.username);
                                            setErrors();
                                        }
                                    }
                            });
                                        });
                            }else{
                                setErrors();
                            }
                                        }else{
                                            addError("email",response.email);
                                            addError("telephone",response.telephone)
                                            setErrors();
                                        }
                                    }
                            });

	});

	$('#Precedent').on('click',function(){
			  		$('#Precedent').hide();
			  		$('#ja-ss').show();
			  		$('#Connector').hide();
	});



});

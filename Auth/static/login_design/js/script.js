let erreurs;

function addError(key,value){
 	erreurs.set(key,value)
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

function validatedate(inputText)
  {
  var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;
  // Match the date format through regular expression
  if(inputText.match(dateformat))
  {
  document.form1.text1.focus();
  //Test which seperator is used '/' or '-'
  var opera1 = inputText.value.split('/');
  var opera2 = inputText.value.split('-');
  lopera1 = opera1.length;
  lopera2 = opera2.length;
  // Extract the string into month, date and year
  if (lopera1>1)
  {
  var pdate = inputText.value.split('/');
  }
  else if (lopera2>1)
  {
  var pdate = inputText.value.split('-');
  }
  var dd = parseInt(pdate[0]);
  var mm  = parseInt(pdate[1]);
  var yy = parseInt(pdate[2]);
  // Create list of days of a month [assume there is no leap year by default]
  var ListofDays = [31,28,31,30,31,30,31,31,30,31,30,31];
  if (mm==1 || mm>2)
  {
  if (dd>ListofDays[mm-1])
  {
   addError(inputText,'Invalid date format!');
  }
  }
  if (mm==2)
  {
  var lyear = false;
  if ( (!(yy % 4) && yy % 100) || !(yy % 400))
  {
  lyear = true;
  }
  if ((lyear==false) && (dd>=29))
  {
  addError(inputText,'Invalid date format!');
  }
  if ((lyear==true) && (dd>29))
  {
 addError(inputText,'Invalid date format!');
  }
  }
  }
	else{
   	addError(inputText,"Invalid date format!");
  	}
  }
function verifier_nom_prenom(nom,prenom){
	if(nom.length == 0){
		addError("nom","Le nom ne doit pas être vide")
	}else {
		if(nom.trim().length> 20 || nom.trim().length <= 9){
		addError("nom","Vous ne devez pas depasser 20 caractères");
		}
	}

	if(prenom.length == 0){
		addError("prenom","Le prenom ne doit pas être vide")
	}else {
		if(prenom.trim().length > 20 || prenom.trim().length <= 9){
		addError("prenom","Vous ne devez pas depasser 20 caractères");
		}
	}


}
function verifierUsername(username){
	if(username == null){

	}else{
		if(username.length>18 || username.length <= 0 ){
			addError(username,"Username doit avoir au plus 18 caractères")
		}
	}
}

function verifierPassword(password,cfpassword){
	let test1 = false
	let test2 = false

	if(password == null){
		addError(password,"Le mot de passe doit être rempli")
	}else{
		if(password.length > 20){
			addError(password,"Le mot de passe doit avoir au plus 20 caractères")
		}else if(password.length <= 9){
			addError(password,"Le mot de passe doit depasser au moins 9 caractères")
		}else{
			test1 = true
		}
	}


	if(cfpassword == null){
		addError(cfpassword,"La confirmation de mot de passe doit être rempli")
	}else{
		if(cfpassword.length > 20){
			addError(cfpassword,"Le mot de passe doit avoir au plus 20 caractères")
		}else if(cfpassword.length <= 9){
			addError(cfpassword,"Le mot de passe doit depasser au moins 9 caractères")
		}else{
			test2 = true
		}
	}

	if(test1 && test2){
		if(!(password == cfpassword)){
			addError(cfpassword,"La confirmation doit être compatible")
		}
	}


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
					console.log(erreurs.size);
                    				for (const [key, value] of erreurs) {
					console.log("ok");
					console.log(`${key} = ${value} okk`);
}

					if(erreurs.size <= 0){
						personne.nom = nom;
						personne.prenom = prenom;
						personne.datedenaissance = birthday;
						personne.email = email;
						personne.telephone = telephone;
						$('#Precedent').show();
				  		$('#Connector').show();
				  		$('#ja-ss').hide();
						$('#Suivant').attr("id", "Inscription");
						$('#Suivant').attr("value", "Inscription");
					}else{

					}
	});

	$('#Precedent').on('click',function(){
			  		$('#Precedent').hide();
			  		$('#ja-ss').show();
			  		$('#Connector').hide();
	});



	$('#Precedent').on('click',function(){
		erreurs = new Map();
		username = $('input[name=username]').val();
		password = $('input[name=password]').val();
		cfpassword = $('input[name=cfpassword]').val();
		verifierPassword(password,cfpassword);
		verifierUsername(username);
		if(erreurs.length <= 0){
			personne.username = username;
			personne.password = password;

		}else{
				let token = $('input[name=csrfmiddlewaretoken]').val();
				$.ajax({
					url: '/Auth',
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

				   	}
				});
		}
	});
});
let erreurs;
let day, month, year;
let vars = new Map();
function addError(key, value) {
	erreurs.set(key, value)
}
function validateAddress(adress){
    if (adress.length == 0) {
		addError("nom", "Le nom ne doit pas être vide")
	} else {
		if (adress.trim().length > 40 || adress.trim().length < 10) {
			addError("address", "L'addresse doit figurer entre 10 et 40 caractères");
		}
	}
}
function validate_date(date) {
	year = parseInt(date.substr(0, 4), 10);
	month = parseInt(date.substr(5, 2), 10);
	day = parseInt(date.substr(8, 2));
	if (isNaN(month) || isNaN(day) || isNaN(year)) {
		addError("dateerror", "Le format de la date est incompatible")
	} else {
		if (day < 1 || day > 31) {
			addError("dateerror", "le jour doit être entre 1 et 31");
		}

		if (month < 1 || month > 12) {
			addError("dateerror", "le mois doit être entre 1 et 12");
		}
		if (year < 1979 || year > 2012) {
			addError("dateerror", "l'année doit être entre 1980 et 2011");
		}
	}

}

function verifierEmail(email) {
	if (email.length == 0) {
		addError("email", "Vous ne devez pas avoir un email vide")
	} else {
		if (!email.trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) || email.length <= 0) {
			addError("email", "Veuillez entrer un email compatible")
		}
	}
}

function verifier_nom_prenom(nom, prenom) {
	if (nom.length == 0) {
		addError("nom", "Le nom ne doit pas être vide")
	} else {
		if (nom.trim().length > 20 || nom.trim().length <= 2) {
			addError("nom", "Vous ne devez pas depasser 20 caractères");
		}
	}

	if (prenom.length == 0) {
		addError("prenom", "Le prenom ne doit pas être vide")
	} else {
		if (prenom.trim().length > 20 || prenom.trim().length <= 2) {
			addError("prenom", "Vous ne devez pas depasser 20 caractères");
		}
	}


}
function verifierUsername(username) {
	if (username.length == 0) {
		addError("username", "Username doit avoir au plus 18 caractères");
	} else {
		if (username.length > 18 || username.length <= 0) {
			addError("username", "Username doit avoir au plus 18 caractères");
		}
	}
}
function verifierPassword(password, cfpassword) {
	let test1 = false

	if (password.length == 0) {
		addError("password", "Le mot de passe doit être rempli")
	} else {
		if (password.length > 20) {
			addError("password", "Le mot de passe doit avoir au plus 20 caractères")
		} else if (password.length <= 9) {
			addError("password", "Le mot de passe doit depasser au moins 9 caractères")
		} else {
			let cmp = 0
			for (let i = 0; i < password.length; i++) {
				if (!isNaN(parseInt(password.substr(i)))) {
					cmp = cmp + 1;
				}
			}
			if (cmp < 4) {
				addError("password", "Le mot de passe doit contenir au moins 4 chiffres")
			}
            var c = false;
            for (let i = 0; i < password.length; i++) {
				if(isNaN(parseInt(password.substr(i,1)))){
					if (password.substr(i,1) == password.substr(i,1).toUpperCase()) {
						c = true;
					}
				}
			}
			if(!c){
			    addError("password","Le mot de passe doit contenir au moins une lettre en majiscule");
				console.log("password","Le mot de passe doit contenir au moins une lettre en majiscule");
			}
		}

	}
	if (test1 == true) {
		if (!(password == cfpassword)) {
			addError("cfpassword", "La confirmation doit être identique")
		}
	}



}

function setErrors() {
	for (const [key, value] of erreurs) {
		$("#" + key).html(value).show();
	}
	erreurs = new Map();
}
function hideErrorsFirstPane() {
	$("#nom").hide();
	$("#prenom").hide();
	$("#dateerror").hide();
	$("#telephone").hide();
	$("#email").hide();
}
function hideErrorsSecondPane() {
	$("#username").hide();
	$("#password").hide();
	$("#cfpassword").hide();
}

class Personne {
	constructor(nom, prenom, datedenaissance, address, sexe, username, email, password) {
		this.nom = nom
		this.prenom = prenom
		this.datedenaissance = datedenaissance
		this.username = username
		this.email = email
		this.password = password
		this.address = address
		this.sexe = sexe

	}
}

var personne = new Personne("", "", "", "", "", "", "", "");

jQuery(document).ready(function() {
	$('#Precedent').hide();
	$('#Connector').hide();
	let token = $('input[name=csrfmiddlewaretoken]').val();
	hideErrorsFirstPane();
	$('#Suivant').on('click', function() {
		erreurs = new Map();
		nom = $('input[name=prenom]').val();
		prenom = $('input[name=nom]').val();
		birthday = $('input[name=birthday]').val();
		sexe = $('select[name=sexe]').val();
		address = $('input[name=address]').val();
		email = $('input[name=email]').val();

		verifier_nom_prenom(nom, prenom);
		verifierEmail(email);
		validateAddress(address);
		validate_date(birthday);
		$.ajax({
			url: '/Auth/signup',
			type: 'post',
			data: {
				id: "1",
				email: email,
				csrfmiddlewaretoken: token
			},
			success: function(response) {
				count = Object.keys(response).length;
				if (count == 0) {
					if (erreurs.size <= 0) {
						personne.nom = nom;
						personne.prenom = prenom;
						personne.datedenaissance = day + "-" + month + "-" + year;
						personne.email = email;
						personne.address = address;
						personne.sexe = sexe;
						$('#Precedent').show();
						$('#Connector').show();
						$('#ja-ss').hide();
						hideErrorsSecondPane();
					} else {
						setErrors();
					}
				} else {
					addError("email", response.email);
					setErrors();
				}
			}
		});
	});

    						$('#Inscription').on('click', function() {
							erreurs = new Map();
							username = $('input[name=username]').val();
							password = $('input[name=password]').val();
							cfpassword = $('input[name=cfpassword]').val();
							console.log("ok");
							verifierPassword(password, cfpassword);
							verifierUsername(username);
							console.log(password,cfpassword);
							if(erreurs.size <=0){
							$.ajax({
								url: '/Auth/signup',
								type: 'post',
								data: {
									id: "2",
									username: username,
									csrfmiddlewaretoken: token
								},
								success: function(response) {
								console.log("okkkk");
									count = Object.keys(response).length;
									if (count == 0) {
										if (erreurs.size <= 0) {
											personne.username = username;
											personne.password = password;
											$.ajax({
												url: '/Auth/signup',
												type: 'post',
												data: {
													nom: personne.nom,
													prenom: personne.prenom,
													email: personne.email,
													datedenaissance: personne.datedenaissance,
													username: personne.username,
													password: personne.password,
													sexe: personne.sexe,
													address: personne.address,
													csrfmiddlewaretoken: token
												},
												success: function(response) {
													if (response == 'You re trying to hack') {

													} else {
														$("#Precedent").hide()
														$(".container-login100-form-btn").hide()
														$("#ja-ss").hide()
														$("#Connector").hide()
														document.querySelector('html').innerHTML = response;
													}
												}
											});
										} else {
											setErrors();
										}
									} else {
										addError("username", response.username);
										setErrors();
									}
								}
							});
							}else{
							    setErrors();
							}
						});

	$('#Precedent').on('click', function() {
		$('#Precedent').hide();
		$('#ja-ss').show();
		$('#Connector').hide();
	});



});

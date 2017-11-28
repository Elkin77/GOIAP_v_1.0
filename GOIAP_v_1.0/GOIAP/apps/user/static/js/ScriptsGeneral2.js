$(document).ready(function(){

	/*if ($('#advertencia').show()) {
		$('#advertencia').fadeOut(2000);
	}*/
	$('#cerrar').click(function(e){
		$('#advertencia').fadeOut(1000);
	});

	$('#botonIngresar').click(function(e){
		if((document.getElementById("user").value).match(/^[_A-Za-z]/)){
			$('#user').attr('class','form-control');
			$('#user').attr('placeholder',"Escribe Nombre de Usuario");
			if(document.getElementById("user").value.length >= 6){
				$('#user').attr('class','form-control');
				$('#user').attr('placeholder',"Escribe Nombre de Usuario");
			}else{
				$('#user').attr('class','form-control invalid');
				$('#user').attr('placeholder',"El usuario debe tener por lo menos 6 caracteres");
				document.getElementById("user").value="";
				e.preventDefault();	
			}

		}else{
			$('#user').attr('class','form-control invalid');
			$('#user').attr('placeholder',"El usuario debe empezar por almenos una letra");
			document.getElementById("user").value="";
			e.preventDefault();
		}

		if(document.getElementById("password").value.length >= 6){
			$('#password').attr('class','form-control');
			$('#password').attr('placeholder',"Escribe contraseña");
		}else{
			$('#password').attr('class','form-control invalid');
			$('#password').attr('placeholder',"La contraseña debe tener por lo menos 6 caracteres");
			document.getElementById("password").value="";
			e.preventDefault();	
		}
	});

	$('#sinNumeral').click(function(e){
        e.preventDefault();
    });
});
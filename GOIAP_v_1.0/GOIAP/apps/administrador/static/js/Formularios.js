function validar(){
	
	var usuario, nombre, apellido, email, password;
	usuario  = document.getElementById("usuario").value;
	nombre = document.getElementById("nombre").value;
	apellido = document.getElementById("apellido").value;
	email = document.getElementById("email").value;
	password = document.getElementById("password").value;

	expresionCorreo = /\w+@\w+\.+[a-z]/;
	expresionNombre = /^([A-ZÁÉÍÓÚ]{1}[a-zñáéíóú]+[\s]*)+$/;
	expresionUsuario = /^[a-z\d_]{4,15}$/i;

	if(usuario === "" || nombre === "" || apellido === "" || password === "" ){
		alert("Faltan Campos por Completar!!");
		return false;
	}
	else if (nombre.length > 30 || usuario.length > 30 || apellido.length > 30){
		alert("Usuario, Nombre o Apellido demasiado largo!!");
		return false;
	}
	else if (password.length > 128 || email.length > 150 ){
		alert("Nombre o Apellido demasiado largo!!");
		return false;
	}
	else if (!expresionCorreo.test(email) && email != ""){
		alert("No es un correo valido!!");
		return false;
	}
	else if (!expresionNombre.test(nombre)){
		alert("No es un Nombre valido!!");
		return false;
	}
	else if (!expresionNombre.test(apellido)){
		alert("No es un Apellido valido!!");
		return false;
	}
	else if (!expresionUsuario.test(usuario)){
		alert("No es un Usuario valido!!");
		return false;
	}
}

function validarTwo(){
	var descripcion;
	descripcion = document.getElementById("descripcion").value;

	if(descripcion === ""){
		alert("Faltan descripción por Completar!!");
		return false;
	}
	else if (descripcion.length > 300){
		alert("Descripción demasiado larga!!");
		return false;
	}

}

function validarThree(){
	var nombre, tipoDoc, archivo, nroPag, descripcion;
	nombre  = document.getElementById("nombre").value;
	tipoDoc = document.getElementById("tipoDoc").value;
	archivo = document.getElementById("archivo").value;
	nroPag = document.getElementById("nroPag").value;
	descripcion = document.getElementById("descripcion").value;

	expresionCorreo = /\w+@\w+\.+[a-z]/;
	expresionNombre = /^([A-ZÁÉÍÓÚ]{1}[a-zñáéíóú]+[\s]*)+$/;
	expresionUsuario = /^[a-z\d_]{4,15}$/i;

	if(nombre === "" || tipoDoc === "" || archivo === "" || nroPag === "" || descripcion === "" ){
		alert("Faltan Campos por Completar!!");
		return false;
	}
	else if (nombre.length > 50){
		alert("Nombre muy largo!!");
		return false;
	}
	else if (descripcion.length > 300){
		alert("Descripción demasiado larga!!");
		return false;
	}
	else if (isNaN(nroPag)){
		alert("Numero de Páginas debe ser un numero!!");
		return false;
	}

}
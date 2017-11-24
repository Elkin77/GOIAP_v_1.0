$(document).ready(function(){
	$('#divArchivo').hide();
	$('#archivo').removeAttr("required");
	$('#cargarArchivo').click(function(e){
		$('#divArchivo').fadeIn(1000);
		$('#cargarArchivo').fadeOut(1000);
		$('#archivo').prop("required", true);
	});
});
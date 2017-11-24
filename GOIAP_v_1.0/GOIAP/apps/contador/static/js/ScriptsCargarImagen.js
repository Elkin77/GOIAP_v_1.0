$(document).ready(function(){
	$('#divImagen').hide();
	$('#imagen').removeAttr("required");
	$('#cargarImagen').click(function(e){
		$('#divImagen').fadeIn(1000);
		$('#cargarImagen').fadeOut(1000);
		$('#imagen').prop("required", true);
	});
});
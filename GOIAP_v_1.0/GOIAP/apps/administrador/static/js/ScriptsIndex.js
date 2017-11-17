$(document).ready(function(){
	$('#contenedor, #formLogin').hide();
	$('.navBar a').click(function(e){
        e.preventDefault()
    });
	$('#botonIngresar').click(function () {
        $('#contenedor, #formLogin').fadeIn(1000);
    });
    $('#contenedor').click(function () {
        $('#contenedor, #formLogin').fadeOut(1000);
    });

    if ($('#advertencia').show()) {
    	$('#advertencia').fadeOut(2000);
    }
   /* $('#cerrar').click(function(){
    	$('#advertencia').fadeOut(1000);
    });*/
});

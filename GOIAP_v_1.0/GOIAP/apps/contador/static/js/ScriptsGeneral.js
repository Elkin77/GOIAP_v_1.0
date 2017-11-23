$(document).ready(function(){

	if ($('#advertencia').show()) {
		$('#advertencia').fadeOut(2000);
	}

	$('#sinNumeral').click(function(e){
        e.preventDefault()
    });
});
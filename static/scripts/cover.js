var show_cover = function() {
	setTimeout(function(){ 
		$(".cover .container, .nav").hide().fadeIn(1000); 
	}, 1000);
}; 

$(document).ready(show_cover); 

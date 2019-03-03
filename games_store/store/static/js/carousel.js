const slide_time_ms = 5000

function next_image() {
	$('.carousel').carousel('next');
}

$(document).ready(function(){
	let options = {
		fullWidth: true,
		indicators: true,
		duration: 300,
		padding: 50,
	}
	$('.carousel').carousel(options);

	window.setInterval(next_image, slide_time_ms);
});

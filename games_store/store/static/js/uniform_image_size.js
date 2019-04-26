$(document).ready(resize_images);
$(window).resize(resize_images);

function resize_images() {
	let images = $("#game-store-box img");
	let min_height = $(images[0]).prop("height");
	for(let i = 1; i < images.length; i++) {
		let height = $(images[i]).prop("height");
		if(height < min_height) {
			min_height = height;
		}
	}

	for(let i = 0; i < images.length; i++) {
		$(images[i]).attr("height", min_height);
		$(images[i]).css("width", "auto");
		$(images[i]).css("margin", "0 auto");
		$(images[i]).css("display", "block");
	}
}


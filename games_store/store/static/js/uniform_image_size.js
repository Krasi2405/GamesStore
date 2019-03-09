function resize_images() {
	let images = $("#game-store-box img");
	let min_width = $(images[0]).prop("height");
	for(let i = 1; i < images.length; i++) {
		let width = $(images[i]).prop("height");
		if(width < min_width) {
			min_width = width;
		}
	}

	for(let i = 0; i < images.length; i++) {
		$(images[i]).attr("height", min_width);
		$(images[i]).css("width", "auto");
		$(images[i]).css("margin", "0 auto");
		$(images[i]).css("display", "block");
	}
}


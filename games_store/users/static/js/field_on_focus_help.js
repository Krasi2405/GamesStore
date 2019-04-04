$(document).ready(function() {
	let fields = $(".field");
	let selected_help = null

	for(let i = 0; i < fields.length; i++) {
		let field = fields[i];
		let input = $(field).find("input");
		let help = $(field).find(".help");

		if(help != null) {
			if(i == 0) {
				help.css("display", "block");
			}

			input.focus(function() {
				help.css("display", "block");
			});

			input.blur(function() {

				help.css("display", "none");
			})
		}
	}
})
let selected;

$(document).ready(function () {
	let selectors = $(".tab-selector");
	selected = $(".tab-items #" + $(selectors[0]).attr("id"));
	selected.css("display", "block");
	for(let i = 0; i < selectors.length; i++) {
		let selector = selectors[i];
		let id = $(selector).attr("id");

		$(selector).click(function() {
			select(id);
		});
	}
});

function select(id) {
	selected.css("display", "none");
	selected = $(".tab-items #" + id);
	selected.css("display", "block");
}
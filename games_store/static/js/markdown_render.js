$(document).ready(function() {
	let md = new Remarkable();
	let desc = $("#description-text");
	let markdown = md.render(desc.text());
	desc.html(markdown);
});

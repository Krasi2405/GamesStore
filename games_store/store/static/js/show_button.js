$(document).ready(function() {
	let content = $(".hidden-content");
	let display_setting = content.css("display");

	$(content).css("display", "none");

	$("#show-button").click(function() {
		$(content).css("display", display_setting);
	});

	$("#hide-button").click(function() {
		$(content).css("display", "none");
	});
});
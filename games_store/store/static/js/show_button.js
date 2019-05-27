$(document).ready(function() {
	let content = $(".hidden-content");

	$(content).css("display", "none");

	$("#show-button").click(function() {
		$(content).css("display", "block");
	});

	$("#hide-button").click(function() {
		$(content).css("display", "none");
	});
});
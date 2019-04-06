let stars_list = [];

$(document).ready(function () {
	let input = $("#rating");

	let stars = $(".star_container");
	for(let i = 0; i < 5; i++) {
		let star = stars[i];

		let filled_star = $(star).find(".filled-star");
		let unfilled_star = $(star).find(".unfilled-star");

		$(filled_star).click(function() {

			for(let j = 0; j < 5; j++) {
				let star = stars[j];
				$(input).attr("value", i + 1);
				if(j <= i) {
					$(star).find(".filled-star").css("display", "inline");
					$(star).find(".unfilled-star").css("display", "none");
				}
				else
				{
					$(star).find(".filled-star").css("display", "none");
					$(star).find(".unfilled-star").css("display", "inline");
				}
			}
		});


		$(unfilled_star).click(function() {
			for(let j = 0; j < 5; j++) {
				let star = stars[j];
				$(input).attr("value", i + 1);
				if(j > i) {
					$(star).find(".filled-star").css("display", "none");
					$(star).find(".unfilled-star").css("display", "inline");
				}
				else
				{
					$(star).find(".filled-star").css("display", "inline");
					$(star).find(".unfilled-star").css("display", "none");
				}
			}
		});

	}
});
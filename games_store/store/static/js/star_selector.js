let stars_list = [];


class Star {
	constructor(filled_star, unfilled_star) {
		this.filled_star = filled_star;
		this.unfilled_star = unfilled_star;
	}

	fill() {
		this.filled_star.css("display", "inline");
		this.unfilled_star.css("display", "none");
	}

	unfill() {
		this.filled_star.css("display", "none");
		this.unfilled_star.css("display", "inline");
	}
}

let stars = [];

$(document).ready(function () {
	let input = $("#rating");

	let star_containers = $(".star_container");
	for(let i = 0; i < 5; i++) {
		let star_container = star_containers[i];

		let filled_star = $(star_container).find(".filled-star");
		let unfilled_star = $(star_container).find(".unfilled-star");

		let star = new Star(filled_star, unfilled_star);
		stars.push(star);
		$(star_container).click(function() {
			stars.forEach(function(element) {
				element.unfill();
			});

			$("#rating").attr("value", i + 1);
			for(let j = 0; j <= i; j++) {
				stars[j].fill();
			}
		});
	}
});
$(document).ready(function()
{
	var target   = $("#services-twitter-container > div")
	var template = $("#template-tweet").html()
	var spinner_opts = {
						lines: 8, // The number of lines to draw
						length: 3, // The length of each line
						width: 3, // The line thickness
						radius: 5, // The radius of the inner circle
						color: '#000', // #rbg or #rrggbb
						speed: 1, // Rounds per second
						trail: 60, // Afterglow percentage
						shadow: false // Whether to render a shadow
						};
	var spinner = new Spinner(spinner_opts).spin(target[0]);

	$.ajax({
			url: "/services/twitter",
	   dataType: "json",
		success: function(data)
		{
			// pause for effect
			setTimeout(function()
			{
				spinner.stop()
				delete spinner
				
				for(;;)
				{
					tweet     = data.shift()
					var model = {"text": tweet.text}
					target.append(Mustache.to_html(template, model))

					if(data.length == 0)
					{
						break;
					}
				}
			}, 1500)
			
		}
	});
})
function makeImgTag(key) {
	$.get(key.gogo, function(cllct_img){
		var img_html = document.createElement("html");
		img_html.innerHTML = cllct_img;
		var all_meta = img_html.getElementsByTagName("meta");

		for (var i = 0; i < all_meta.length; i++) {
	        if ( all_meta[i].getAttribute("itemprop")) {
				var img_link = all_meta[i].getAttribute("content");
	        }    
		}
		
		var makeImg = [];

		if (img_link == undefined) {
			makeImg.push(`<img onerror="this.src='#';" src="${key.animeimg}" alt="${key.animedetailsh2}" />`);
		} else {
			makeImg.push(`<img onerror="this.src='${img_link}';" src="${key.animeimg}" alt="${key.animedetailsh2}" />`);
		}

		var makeTagHtml = makeImg.join(" ");
		return makeTagHtml
	});

	// $("#animeimg").html(imgTagHtml);
}
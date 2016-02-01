$(document).ready(function(){
		var asset_template = $('#asset-form-tmp').html();
		var template = $('#menu-tmp').html();
		var rendered = Mustache.render(template,{'form':asset_template});
		$('div.form-container').html(rendered);


		$('#bt1').on('click', function(event){ 
			var template = $('#stock-form-tmp').html();
			var rendered = Mustache.render(template);
			$('.form-container-asset').html(rendered);
		});
		$('#bt2').on('click', function(event){ 
			var template = $('#bond-form-tmp').html();
			var rendered = Mustache.render(template);
			$('.form-container-asset').html(rendered);
		});
		$('#bt3').on('click', function(event){ 
			var template = $('#etf-form-tmp').html();
			var rendered = Mustache.render(template);
			$('.form-container-asset').html(rendered);
		});
});
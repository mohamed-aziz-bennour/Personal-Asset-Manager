$(document).ready(function(){
        var asset_template = $('#asset-form-tmp').html();
        var template = $('#menu-tmp').html();
        var rendered = Mustache.render(template,{'form':asset_template});
        $('div.form-container').html(rendered);


        $('#bt1').on('click', function(event){ 
            $.get('/securities/list_stock', function(data){
                console.log(data['stocks']);
                $.each(data['stocks'], function (i, item) {
                    $('#stocks_choice').append($('<option>', { 
                        value: [item.symbol, item.id , item.company_name, item.sector, item.industry, item.market_capitalisation],
                        text : item.symbol
                    }));
                    // console.log(item);
                });

                var template = $('#stock-form-tmp').html();
                var rendered = Mustache.render(template, data);
                $('.form-container-asset').html(rendered);
        })
            var stock = $('#stocks_choice>option:selected').val()
            console.log(stock);
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
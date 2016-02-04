$(document).ready(function(){
        

        var asset_template = $('#asset-form-tmp').html();
        var template = $('#menu-tmp').html();
        var rendered = Mustache.render(template,{'form':asset_template});
        $('div.form-container').html(rendered);


        $('#bt1').on('click', function(event){ 
            $('.securities-container').empty();
            $.get('/securities/list_stock', function(data){
                $('#content-type').attr('value',data['content_type'])
                console.log(data['stocks']);
                $('#choice').find('option').remove().end();
                $.each(data['stocks'], function (i, item) {
                    $('#choice').append($('<option>', { 
                        value: [item.symbol, item.id , item.company_name, item.sector, item.industry, item.market_capitalisation],
                        // value: item.object,
                        text : item.symbol
                    }));
                    // console.log(item);
                });

                // var template = $('#stock-form-tmp').html();
                // var rendered = Mustache.render(template, data);
                // $('.form-container-asset').html(rendered);
        })
            var stock = $('#choice>option:selected').val()
            console.log(stock);
        });



        $('#bt2').on('click', function(event){ 
            $('.securities-container').empty();
            $.get('/securities/list_bond', function(data){
                $('#content-type').attr('value',data['content_type']) 
                // console.log(data['bonds']);
                $('#choice').find('option').remove().end();
                $.each(data['bonds'], function (i, item) {
                    $('#choice').append($('<option>', { 
                        value: [item.symbol, item.id , item.company_name, item.coupon, item.maturity_date, item.sp_rating, item.moody_rating],
                        text : item.symbol
                    }));
                    // console.log(item);
                });
                // var template = $('#bond-form-tmp').html();
                // var rendered = Mustache.render(template);
                // $('.form-container-asset').html(rendered);
            });
        });


        $('#bt3').on('click', function(event){ 
            $('.securities-container').empty();
            $.get('/securities/list_etf', function(data){
                $('#content-type').attr('value',data['content_type']) 
                // console.log(data['exchangeTradedFunds']);
                $('#choice').find('option').remove().end();
                $.each(data['exchangeTradedFunds'], function (i, item) {
                    $('#choice').append($('<option>', { 
                        value: [item.symbol, item.id , item.name, item.category, item.fund_family, item.beta, item.alpha, item.r_squared, item.sharpe_ratio],
                        text : item.symbol
                    }));
                    // console.log(item);
                });
                // var template = $('#etf-form-tmp').html();
                // var rendered = Mustache.render(template);
                // $('.form-container-asset').html(rendered);
            });
        });
        
       $("#choice").change(function() {
        // alert($("#choice option:selected").val());
        // $('#test_output').val($("#choice option:selected").val());
        $('.securities-container').empty();
        var items = [];
        var res = $("#choice option:selected").val().split(" ");
        $.each(res, function(i, item) {
        items.push('<li>' + item + '</li>');
                });  // close each()
        $('.securities-container').append( items.join('') );

        }); 


       var $portfolio_id = $('#portfolio_id').val();
        console.log($('#portfolio_id').val());
        var getAssets = function getAssets(port){
                $.get("/securities/list_asset/"+ port ,function(data){
                console.log(data);
                var template = $('#asset-tmp').html();
                var rendered = Mustache.render(template,data);
                $('div.asset-container').html(rendered);
          
            });
        }

        getAssets($portfolio_id);

});
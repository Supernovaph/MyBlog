$( "form.to_cart" ).submit(function( event ) {
  event.preventDefault();
  let target = $( event.target );
  let id = target.find("input.product_input").val();
  target.find("input[type^='submit']").after('Loading...');

  let posting = $.post( "/shop/buy", {id:id, csrfmiddlewaretoken: target.find("input[name='csrfmiddlewaretoken']").val()});
  
  posting.done(function( data ) { 
    target.find("input[type^='submit']").after('Добавлено в корзину!');
  });
  posting.fail(function(data){
  })

});
$(document).ready(function() {
    $('.images').magnificPopup({ 
      
      type: 'image',
      delegate: 'a',
      removalDelay: 300,
      mainClass: 'mfp-with-fade',
      
      gallery:{enabled:true}
      
    });
});
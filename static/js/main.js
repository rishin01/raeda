
const locationbutton = $('#locationbutton');
const destinationbutton = $('#destinationbutton');

const locationinput = $('#locationinput');
const destinationinput = $('#destinationinput');

locationbutton.click(function(){
	locationbutton.css('display','none');
	locationinput.css('display','flex');
});

destinationbutton.click(function(){
	destinationbutton.css('display','none');
	destinationinput.css('display','flex');
});

var fromInput = '';
var toInput = '';

locationinput.on("input", function() {
   fromInput = $(this).val(); 
	if (toInput!='' && fromInput!=''){
	
	}
});

destinationinput.on("input", function() {
   toInput = $(this).val();
   if (toInput!='' && fromInput!=''){
	   
   }
});
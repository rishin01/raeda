
const locationbutton = $('#locationbutton');
const destinationbutton = $('#destinationbutton');

const locationinputdiv = $('#locationinput');
const destinationinputdiv = $('#destinationinput');

const locationinput = $('#locationinput input');
const destinationinput = $('#destinationinput input');

const requesttaxi = $('#requesttaxi')

locationbutton.click(function(){
	locationbutton.css('display','none');
	locationinputdiv.css('display','flex');
});

destinationbutton.click(function(){
	destinationbutton.css('display','none');
	destinationinputdiv.css('display','flex');
});

var fromInput = '';
var toInput = '';

function ofLocationFormat(s){
	return s.length == 5 && parseInt(s[1])!=undefined && parseInt(s[3])!=undefined;
}

function checkValidInputs(){
	if (ofLocationFormat(toInput) && ofLocationFormat(fromInput)) 	requesttaxi.addClass('inputsentered');
}

locationinput.on('input',function() {
	fromInput = $(this).val(); 
	checkValidInputs();
});
locationinput.keypress(function(e) {
	if (e.which == 13) locationinput.blur();
});

locationinput.focusin(function(){
 	locationinputdiv.css('opacity','1');
});
locationinput.focusout(function(){
	if (ofLocationFormat(fromInput)) locationinputdiv.css('opacity','0.6');
});

destinationinput.on('input',function() {
	toInput = $(this).val();
	checkValidInputs();
});
destinationinput.keypress(function(e) {
	if (e.which == 13) destinationinput.blur();
});

destinationinput.focusin(function(){
	destinationinputdiv.css('opacity','1');
});
destinationinput.focusout(function(){
	if (ofLocationFormat(toInput)) destinationinputdiv.css('opacity','0.6');
});

requesttaxi.click(function(){
	fetch('/api/requesttaxi',{
		method: 'POST',
		headers: {
			'Content-Type':'application/json',
		},
		body: JSON.stringify({}),
	}).then((response) => response.json())
	.then((data) => {
		window.location.href = window.location.origin + '/waiting?fromx='+fromInput[1]+'&fromy='+fromInput[3]+'&tox='+toInput[1]+'&toy='+toInput[3];
	});

})


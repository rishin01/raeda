
const flatratebutton = $('#flatratebutton');
const priceminbutton = $('#priceminbutton');
const numcarsbutton = $('#numcarsbutton');

const flatrateinputdiv = $('#flatrateinput');
const pricemininputdiv = $('#pricemininput');
const numcarsinputdiv = $('#numcarsinput');

const flatrateinput = $('#flatrateinput input');
const pricemininput = $('#pricemininput input');
const numcarsinput = $('#numcarsinput input');

const inittaxi = $('#inittaxi')

flatratebutton.click(function(){
	flatratebutton.css('display','none');
	flatrateinputdiv.css('display','flex');
});

priceminbutton.click(function(){
	priceminbutton.css('display','none');
	pricemininputdiv.css('display','flex');
});

numcarsbutton.click(function(){
	numcarsbutton.css('display','none');
	numcarsinputdiv.css('display','flex');
});


var flatrateInput = '1';
var priceminInput = '1';
var numcarsInput = '5';

function intFormat(s){
	return parseInt(s)!=undefined;
}

function checkValidInputs(){
	if (intFormat(priceminInput) && intFormat(flatrateInput) && intFormat(numcarsInput))
		inittaxi.addClass('inputsentered');
}

flatrateinput.on('input',function() {
	flatrateInput = $(this).val(); 
	checkValidInputs();
});
flatrateinput.keypress(function(e) {
	if (e.which == 13) flatrateinput.blur();
});

flatrateinput.focusin(function(){
 	flatrateinputdiv.css('opacity','1');
});
flatrateinput.focusout(function(){
	if (intFormat(flatrateInput)) flatrateinputdiv.css('opacity','0.6');
});

pricemininput.on('input',function() {
	priceminInput = $(this).val();
	checkValidInputs();
});
pricemininput.keypress(function(e) {if (e.which == 13) pricemininput.blur();});
pricemininput.focusin(function(){pricemininputdiv.css('opacity','1');});
pricemininput.focusout(function(){if (intFormat(priceminInput)) pricemininputdiv.css('opacity','0.6');});

numcarsinput.on('input',function() {
	numcarsInput = $(this).val();
	checkValidInputs();
});
numcarsinput.keypress(function(e) {if (e.which == 13) numcarsinput.blur();});
numcarsinput.focusin(function(){numcarsinputdiv.css('opacity','1');});
numcarsinput.focusout(function(){if (intFormat(numcarsInput)) numcarsinputdiv.css('opacity','0.6');});

inittaxi.click(function(){
	fetch('/api/inittaxi',{
		method: 'POST',
		headers: {
			'Content-Type':'application/json',
		},
		body: JSON.stringify({
			flatrate:flatrateInput,
			pricemin:priceminInput,
			numcars:numcarsInput
		}),
	}).then((response) => response.json())
	.then((data) => {
		window.location.href = window.location.origin + '/taxiadded';//?taxi_id='+data['taxi_id']
	});
})
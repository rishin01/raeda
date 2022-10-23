
const flatratebutton = $('#flatratebutton');
const priceminbutton = $('#priceminbutton');

const flatrateinputdiv = $('#flatrateinput');
const pricemininputdiv = $('#pricemininput');

const flatrateinput = $('#flatrateinput input');
const pricemininput = $('#pricemininput input');

const inittaxi = $('#inittaxi')

flatratebutton.click(function(){
	flatratebutton.css('display','none');
	flatrateinputdiv.css('display','flex');
});

priceminbutton.click(function(){
	priceminbutton.css('display','none');
	pricemininputdiv.css('display','flex');
});

var flatrateInput = '1';
var priceminInput = '1';

function intFormat(s){
	return parseInt(s)!=undefined;
}

function checkValidInputs(){
	if (intFormat(priceminInput) && intFormat(flatrateInput))
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
pricemininput.keypress(function(e) {
	if (e.which == 13) pricemininput.blur();
});

pricemininput.focusin(function(){
	pricemininputdiv.css('opacity','1');
});
pricemininput.focusout(function(){
	if (intFormat(priceminInput)) pricemininputdiv.css('opacity','0.6');
});

inittaxi.click(function(){
	fetch('/api/inittaxi',{
		method: 'POST',
		headers: {
			'Content-Type':'application/json',
		},
		body: JSON.stringify({
			flatrate:flatrateInput,
			pricemin:priceminInput
		}),
	}).then((response) => response.json())
	.then((data) => {
		if (data['taxiadded']) window.location.href = window.location.origin + '/taxiadded';
	});
})
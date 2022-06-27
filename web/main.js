var title
var body
var datetime

function post(){
	if (document.querySelector('input[name="type"]:checked').value == "main") {
		title = document.querySelector('input[name="title"]').value;
		body = document.getElementById('body').value;
		eel.uploadpost(title, body);
	}
	else {
		title = document.querySelector('input[name="title"]').value;
		body = document.getElementById('body').value;
		datetime = document.querySelector('input[name="time"]').value;
		eel.uploadpost(title, body);
	}
}

eel.expose(shitsposted);
function shitsposted(){
	alert("Posted succesfully!")
	document.querySelector('input[name="title"]').value = "";
	document.getElementById('body').value = "";
	document.querySelector('input[name="time"]').value = "";
}

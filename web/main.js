var title
var body
var datetime

function post()
{
	title = document.querySelector('input[name="title"]').value;
	body = document.getElementById('body').value;
	eel.upload_new_post(title, body);
}

eel.expose(indicate_post);
function indicate_post()
{
	alert("Posted succesfully!")
	document.querySelector('input[name="title"]').value = "";
	document.getElementById('body').value = "";
	document.querySelector('input[name="time"]').value = "";
}

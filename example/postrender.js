function appendPost(title, body, time) {
	var table = document.createElement("table");
	table.setAttribute('border', '1px');
	var trone = document.createElement("tr");
	table.appendChild(trone);
	var tdtrone = document.createElement("td");
	trone.appendChild(tdtrone);
	tdtrone.insertAdjacentHTML("beforeend", "<b>" + title + "</b>");
	var trtwo = document.createElement("tr");
	table.appendChild(trtwo);
	var tdtrtwo = document.createElement("td");
	trtwo.appendChild(tdtrtwo);
	tdtrtwo.insertAdjacentHTML("beforeend", body);
	var trthree = document.createElement("tr");
	table.appendChild(trthree);
	var tdtrthree = document.createElement("td");
	var datetime = document.createTextNode(time)
	tdtrthree.appendChild(datetime);
	trthree.appendChild(tdtrthree);
	var div = document.getElementById("posts");
	div.appendChild(table);
	div.appendChild(document.createElement("br"))
	
}
fetch('./posts.json', {cache: "no-store"})
	.then(response => response.json())
	.then(data => {
		var i;
		for (i = Object.keys(data["_default"]).length; i > 0; i--) {
			if (i == Object.keys(data["_default"]).length) {
				appendPost(data["_default"][i.toString()]["title"], data["_default"][i.toString()]["body"], data["_default"][i.toString()]["date"]);
			}
			else {
			appendPost(data["_default"][i.toString()]["title"], data["_default"][i.toString()]["body"], data["_default"][i.toString()]["date"]);
			}
		}
	})
	.catch(err => console.error(err));

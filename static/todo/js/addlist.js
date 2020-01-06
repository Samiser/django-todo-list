function addList() {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// clear input fields
			document.getElementById('new_list_name').value = "";
			document.getElementById('new_list_description').value = "";

			// refresh list
			document.getElementById("list_list").innerHTML = this.responseText;
		}
	};
	xhttp.open("POST", "/add/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("name=" + document.getElementById('new_list_name').value 
		+ "&description=" + document.getElementById('new_list_description').value); 
}

function removeList(list_id) {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// refresh list
			document.getElementById("list_list").innerHTML = this.responseText;
			loadList();
		}
	};
	xhttp.open("POST", "/remove/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("list_id=" + String(list_id)); 
}

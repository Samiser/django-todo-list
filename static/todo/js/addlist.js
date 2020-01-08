function loadList(list_id) {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
			// refresh list
			document.getElementById("todo_list").innerHTML = this.responseText;
	  }
	};
	xhttp.open("GET", url + String(list_id) + "/list_only/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(); 
}

function loadLists() {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
			// refresh list
			document.getElementById("list_list").innerHTML = this.responseText;
	  }
	};
	xhttp.open("GET", url + "list_list/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(); 
}

function addList() {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// clear input fields
			document.getElementById('new_list_name').value = "";
			document.getElementById('new_list_description').value = "";

			// refresh lists
			loadList(this.responseText);
			loadLists();
		}
	};
	xhttp.open("POST", url + "add/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("name=" + document.getElementById('new_list_name').value 
		+ "&description=" + document.getElementById('new_list_description').value); 
}

function removeList(list_id) {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// refresh lists
			if (Number(this.responseText) == -1) {
				document.getElementById("todo_list").innerHTML = "<p>Try adding a list using the form below</p>";
			}
			else {
				loadList(Number(this.responseText));
			}
			loadLists();
		}
	};
	xhttp.open("POST", url + "remove/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("list_id=" + String(list_id)); 
}

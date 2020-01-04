function addItem(list_id) {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// clear input field
			document.getElementById('new_item_content').value = "";

			// refresh list
			document.getElementById("todo_list").innerHTML = this.responseText;
		}
	};
	xhttp.open("POST", "/todo/" + String(list_id) + "/add/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("content=" + document.getElementById('new_item_content').value); 
}

function doneItem(list_id, item_id) {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
			// refresh list
			document.getElementById("todo_list").innerHTML = this.responseText;
	  }
	};
	xhttp.open("POST", "/todo/" + String(list_id) + "/remove/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("item_id=" + String(item_id)); 
}

function deleteItem(list_id, item_id) {
	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
			// refresh list
			document.getElementById("todo_list").innerHTML = this.responseText;
	  }
	};
	xhttp.open("POST", "/todo/" + String(list_id) + "/delete/", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("item_id=" + String(item_id)); 
}

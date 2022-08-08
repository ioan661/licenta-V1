function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/notes";
    });
}


window.onload = setInterval(getDate, 1000);

function getDate(){
    var azi = new Date();

    var string = azi.getDate() + '.' + (azi.getMonth() + 1) + '.' + azi.getFullYear();
    var string1 = azi.getHours() + ":" + azi.getMinutes() + ":" + azi.getSeconds();

    var string2 = string + " " + string1;
    if(document.getElementById("data") != null)
    { 
        document.getElementById("data").innerHTML = "<b>Data si ora curenta: </b>" + string2;
    }
}

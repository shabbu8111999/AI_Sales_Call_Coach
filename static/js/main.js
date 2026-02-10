function uploadAudio() {
    const fileInput = document.getElementById("audioFile");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an audio file");
        return;
    }

    const formData = new FormData();
    formData.append("audio", file);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            alert("Backend error: " + data.error);
            return;
        }

        document.getElementById("transcript").innerText = data.transcript;
        document.getElementById("analysis").innerText = data.report;
    })
    .catch(err => {
        alert("Network or server error. Check Render logs.");
        console.error(err);
    });
}

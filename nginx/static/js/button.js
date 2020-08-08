const api_host = "http://localhost"

const btn = document.querySelector('button');
btn.addEventListener('click', saveWord);

const input = document.getElementById("word");
input.addEventListener('keyup', pressEnter);

function saveWord() {
    const word_max_len = 50;
    const word = document.getElementById('word').value;

    if (word.length == 0 || word.length > word_max_len) {
        document.getElementById('msg').innerText = "Please enter a word (at most 50 characters)";
        return;
    }

    let xhr = new XMLHttpRequest();
    let url = api_host + "/api/notes/words/";
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-type", "application/json");

    xhr.onreadystatechange = () => {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            let msg = "";
            if (xhr.status == 503) {
                msg = "Service is not available now.\n Please try it later.";
            } else if (xhr.status == 201) {
                msg = "Saved."
            }
            document.getElementById('msg').innerText = msg;
        }
    }
    const payload = JSON.stringify({"word": word});
    xhr.send(payload);
}

function pressEnter(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        btn.click();
    }
}

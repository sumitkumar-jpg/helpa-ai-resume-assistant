const sendButton = document.getElementById("sendButton");
const messageInput = document.getElementById("messageInput");
const chatSection = document.getElementById("chatSection");
const uploadButton = document.getElementById("uploadButton");
const fileInput = document.getElementById("fileInput");
const uploadedFileName = document.getElementById("uploadedFileName");

const sessionId = crypto.randomUUID();

sendButton.addEventListener("click", async function () {

    if (messageInput.value.trim() === "") {
        return;
    }

    const userText = messageInput.value;

    const userMessage = document.createElement("div");
    userMessage.className = "userMessage";
    userMessage.innerHTML = "<strong>You</strong><br>" + userText;

    chatSection.appendChild(userMessage);
    chatSection.scrollTop = chatSection.scrollHeight;

    const thinkingMessage = document.createElement("div");
    thinkingMessage.className = "botMessage";
    thinkingMessage.innerHTML = "<strong>Helpa</strong><br>Thinking...";

    chatSection.appendChild(thinkingMessage);
    chatSection.scrollTop = chatSection.scrollHeight;

    messageInput.value = "";
    messageInput.focus();

    sendButton.disabled = true;

    try {

        const response = await fetch("https://inspiring-harmony-production-020e.up.railway.app/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: userText,
                session_id: sessionId
            })

        });

        const data = await response.json();

        sendButton.disabled = false;

        thinkingMessage.innerHTML =
            "<strong>Helpa</strong><br>" + data.answer;

        chatSection.scrollTop = chatSection.scrollHeight;

    }
    catch (error) {

        sendButton.disabled = false;

        thinkingMessage.innerHTML =
            "<strong>Helpa</strong><br>Error connecting to the server.";

        chatSection.scrollTop = chatSection.scrollHeight;

        console.error(error);

    }

});

messageInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {
        sendButton.click();
    }

});

uploadButton.addEventListener("click", function () {

    fileInput.click();

});

fileInput.addEventListener("change", async function () {

    const file = fileInput.files[0];

    if (!file) {
        return;
    }

    const formData = new FormData();

    formData.append("session_id", sessionId);
    formData.append("file", file);

    try {

        const response = await fetch("https://inspiring-harmony-production-020e.up.railway.app/upload", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        if (data.error) {

            uploadedFileName.innerHTML =
                "❌ " + data.error;

        }
        else {

            uploadedFileName.innerHTML =
                "📄 <strong>" + file.name +
                "</strong><br>✅ Uploaded Successfully";

        }

    }
    catch (error) {

        uploadedFileName.innerHTML =
            "❌ Upload Failed";

        console.error(error);

    }

    fileInput.value = "";

});
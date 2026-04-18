const codeArea = document.getElementById("code");

codeArea.addEventListener("keydown", (e) => {
    if (e.key === "Tab") {
        e.preventDefault();
        const start = codeArea.selectionStart;
        const end = codeArea.selectionEnd;
        codeArea.value =
            codeArea.value.substring(0, start) + "\t" + codeArea.value.substring(end);
        codeArea.selectionStart = codeArea.selectionEnd = start + 1;
    }
});
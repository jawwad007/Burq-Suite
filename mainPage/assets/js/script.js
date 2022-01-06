function new_file() {
    const filename = prompt("Enter File Name");
    const li = document.createElement("li");
    const file = document.createElement("button");
    file.setAttribute("name", `${filename}`)
    file.setAttribute("onclick", "open_file()");
    document.getElementById("tree").appendChild(li).appendChild(file);
    eel.new_file(filename);
}
function open_file() {
    const filename = document.getElementsByClassName("file")
    const f = document.getElementsByName()
}
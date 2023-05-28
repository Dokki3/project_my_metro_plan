var a = 0
function click(id, line) {
    if (a % 2 == 0 && !(document.getElementById("input1").value == id) && !(document.getElementById("input2").value == id)){
        document.getElementById("input1").value = id;
        a = a + 1
        document.getElementById("button_in_1").style = "";
    }
    else if (!(a % 2 == 0) && !(document.getElementById("input1").value == id) && !(document.getElementById("input2").value == id)) {
        document.getElementById("input2").value = id;
        a = a + 1;
        document.getElementById("button_in_2").style = "";
    }
}
let screen = document.getElementById("calc");
function display(a) {
    document.calculator.evalresult.value += a;
}
function solve() {
    var exp = document.calculator.evalresult.value;
    if (exp) {
        try {
            document.calculator.evalresult.value = eval(exp)
        }
        catch {
            document.calculator.evalresult.value = "Error";
        }

    }
}
function back() {
    var exp = document.calculator.evalresult.value;
    document.calculator.evalresult.value = exp.substring(0, exp.length - 1);
}

function clean() {
    document.calculator.evalresult.value = "";
}
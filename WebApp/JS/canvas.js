var goodfeelings = ["great", "good", "spectacular", "cheerful", "excellent", "decent", "happy", "ecstatic", "positive", "joyful", "content"];
var badfeelings = ["bad", "awful", "dreadful", "depressed", "resentful", "jealous", "upset"];
var neutralfeelings = ["meh", "alright", "tired", "fine", "chill", "cool", "indifferent", "reserved"];

var username = "";

function pageLoad() {
    if(username == "") {
        document.getElementById("ms1").innerHTML = "Greetings internet user!";
        document.getElementById("ms2").innerHTML = "What is your name?";
        document.getElementById("bttn1").setAttribute("onclick", "getName()");

    } else if (username != "") {
        document.getElementById("ms1").innerHTML = "Hello again, " + username + "!";
        document.getElementById("ms2").innerHTML = "How are you feeling today?";
        document.getElementById("bttn1").setAttribute("onclick", "getFeelings()");
    }

    var input = document.getElementById("inp1");
    input.addEventListener("keyup", function(event) {
        event.preventDefault();
        if (event.keyCode === 13) {
            document.getElementById("bttn1").click();
        }
    });
}

function getName() {
    username = document.getElementById("inp1").value;
    if (username == "") {
        emptyInput();
    } else if (username != "") {
        replaceFormNaFe();
    } 
}

function clearForm() {
    document.getElementById("ms1").innerHTML = "";
    document.getElementById("ms2").innerHTML = "";
    document.getElementById("inp1").value = "";
}

function replaceFormNaFe() {
    clearForm();
    document.getElementById("ms1").innerHTML = "How are you feeling today, " + username + "?";
    document.getElementById("bttn1").setAttribute("onclick", "getFeelings()");
}

function getFeelings() {
    feeling = document.getElementById("inp1").value;
    feeling = feeling.toLowerCase();

    if (feeling == "") {
        emptyInput();
    } else if (feeling != "") {
        ginput = jQuery.inArray(feeling, goodfeelings);
        binput = jQuery.inArray(feeling, badfeelings);
        ninput = jQuery.inArray(feeling, neutralfeelings);

        if (ginput != -1) {
            clearForm();
            document.getElementById("ms1").innerHTML = "I'm glad you are feeling " + feeling + ", " + username + "!";
        } else if (binput != -1) {
            clearForm();
            document.getElementById("ms1").innerHTML = "I'm sorry you feel like this " + username + ". <br>Do you want to talk about it?";

        } else if (ninput != -1) {
            clearForm();
            document.getElementById("ms1").innerHTML = "Just " + feeling + "? Is there anything on your mind " + username + "?";

        } else if (ginput == -1 && binput == -1 && ninput == -1) {
            document.getElementById("ms1").innerHTML = "I don't know " + feeling;
        }
    }
}

function emptyInput() {
    document.getElementById("input-error").innerHTML = "The input field is blank. <br> Please try again!";
}

function refreshPage() {
    location.reload();
}
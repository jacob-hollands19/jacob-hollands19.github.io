function getScore(form) {
    var numQues = 10;
    var numChoi = 3;
    var answers = new Array(10);
    answers[0] = "Cascading Style Sheets";
    answers[1] = "4";
    answers[2] = "37 woods";
    answers[3] = ";";
    answers[4] = "Window";
    answers[5] = "yes";
    answers[6] = "a^2+b^2=c^2";
    answers[7] = "Wanda Maximoff";
    answers[8] = "WHY WOULD YOU EVER DO THAT YOU ABSOLUTE BUFFOON";
    answers[9] = "YESYES";



    var score = 0;
    var currElt;
    var currSelection;
    for (i=0; i<numQues; i++) {
        currElt = i*numChoi;
        answered=false; 
        for (j=0; j<numChoi; j++) {
        currSelection = form.elements[currElt + j];
        if (currSelection.checked) {
            console.log("it was true")
            answered=true;
            if (currSelection.value == answers[i]) {
            score++;
            break;
            }
        }
        }
        if (answered ===false){alert("Do answer all the questions, Please") ;return false;}
    }

    var scoreper = Math.round(score/numQues*100);
    form.percentage.value = scoreper + "%";
    form.mark.value=score;



}
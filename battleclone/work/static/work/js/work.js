var stopBtn = document.getElementById('stop-button');
var finishBtn = document.getElementById('finish-button');
var timeRemain = document.getElementById('time-remain').value;

function isZero(timePart) {
    return parseInt(timePart) === 0 || timePart === '00';
}

function parseDisplayedTime(timeRemainArray){
    // add 0 to string if element is 1....9
    var checkDoubleLength = function(element){
        var newElement = element.toString();
        if(newElement.length < 2){
            return '0' + newElement;
        }

        return newElement;
    };

    return timeRemainArray.map(checkDoubleLength);
}

function count(timeArray) {
    // timeArray= ['0', '1', '59'];
     var timeRemain = timeArray;
     var seconds = parseInt(timeArray[2]);
     var minutes = parseInt(timeArray[1]);
     var hours = parseInt(timeArray[0]);

     var timer = setInterval(function() {
            if(seconds === 0){
                minutes--;
                seconds = 60;
            }

            if(minutes === 0){
                if(hours === 0)
                    minutes = 0;
                else
                    minutes = 59;

                hours--;
            }

            if(hours <= 0) hours = 0;
            seconds--;

            timeRemain = [hours, minutes, seconds];
            // change this ID NAME
            var timeRemainDiv = document.getElementById('timetime');
            timeRemainDiv.innerText = parseDisplayedTime(timeRemain).join(":");

            if(timeRemain.every(isZero)){
                console.log('is zero');
                timeRemainDiv.innerText = 'Zakonczyles robote';
                clearInterval(timer);
                showFinishBtn();
                hideStopBtn();
            }
        }, 1000);
}

function counter() {
    console.log(timeRemain.split(":"));
    var time = timeRemain.split(":");
    if(!time.every(isZero)){
        hideFinishBtn();
        showStopBtn();
        count(timeRemain.split(":"));
    }
    else {
        showFinishBtn();
        hideStopBtn();
    }
}

function showStopBtn() {
    stopBtn.style.display = 'block';
}

function hideStopBtn() {
    stopBtn.style.display = 'none';
}

function showFinishBtn() {
    finishBtn.style.display = 'block';
}

function hideFinishBtn() {
    finishBtn.style.display = 'none';
}

function workMainFunction() {
    counter();
}

workMainFunction();
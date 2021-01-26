const button = document.getElementById('sb');
const osname = document.getElementById('d_');
const version = document.getElementById('v_');
const na = document.getElementById('n_');

var counter = 0;
const fields = [osname , version , na];

const submitbutton = document.getElementById('sub');

const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const recog = new SR();


recog.onstart = () => console.log('speak');

recog.onresult = function(event){

                 const current = event.resultIndex;
                 const transcript = event.results[current][0].transcript;
                 fields[counter].value = transcript;
                 counter += 1;
                 submitbutton.click();
};

function speak(msg){

    const speech = new SpeechSynthesisUtterance();
    speech.text = msg;
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;
    window.speechSynthesis.speak(speech);
}

const DEF_DELAY = 1000;
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms || DEF_DELAY));
}

//await sleep(100);

(async()=>{

   speak('Please tell your container image name');
   await sleep(4500);
   recog.start();
   await sleep(4500);
   speak('Please tell your image version');
   await sleep(4500);
   recog.start();
   await sleep(4500);
   speak('Please tell your container name');
   await sleep(4500);
   recog.start();

})()

const no_of_datanodes = document.getElementById('ni');
const no_of_tasktrackers = document.getElementById('nt');
const submitbutton = document.getElementById('dcc_submit');

var counter = 0;
const fields = [no_of_datanodes, no_of_tasktrackers];

const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const recog = new SR();


recog.onstart = () => console.log('speak');

recog.onresult = function(event){

                 const current = event.resultIndex;
                 const transcript = event.results[current][0].transcript;
                 fields[counter].value = transcript;
                 counter += 1;
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

   speak('What are the number of data nodes you want');
   await sleep(3500);
   recog.start();
   await sleep(3500);
   speak('What are the number of task trackers you want');
   await sleep(3500);
   recog.start();
   await sleep(3500);
  //submitbutton.click()

})()

const master_name = document.getElementById('mn_');
const worker1 = document.getElementById('w1n_');
const worker2 = document.getElementById('w2n_');
const CIDR = document.getElementById('cdb_');
//const na = document.getElementById('n_');

var counter = 0;
const fields = [master_name, worker1, worker2, CIDR];

//const submitbutton = document.getElementById('sublb');

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

   speak('Please tell your master node name');
   await sleep(4500);
   recog.start();
   await sleep(4500);
   speak('Please tell your first worker node name');
   await sleep(4500);
   recog.start();
   await sleep(4500);
   speak('Please tell your second worker node name');
   await sleep(4500);
   recog.start();
   await sleep(4500);
   speak('Type your CIDR');
// submitbutton.click()

})()


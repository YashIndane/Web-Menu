const ip_addr = document.getElementById('ip-');
const submitbutton = document.getElementById('sub');

const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const recog = new SR();

recog.onstart = () => console.log('speak');

recog.onresult = function(event){

                 const current = event.resultIndex;
                 const transcript = event.results[current][0].transcript;
                 ip_addr.value  = transcript;
                
                // submitbutton.click();
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

   speak('What is your remote system IP');
   await sleep(4500);
   recog.start();
   await sleep(5500);
   speak('Please type the remote system password');

 
})()

const button = document.getElementById('bn');
//const space = document.getElementById('sp');
const textfield = document.getElementById('t');
const submitbutton = document.getElementById('sub');

const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const recog = new SR();

recog.onstart = () => console.log('speak');

recog.onresult = function(event){
                 const current = event.resultIndex;
                 const transcript = event.results[current][0].transcript;
                 textfield.value = transcript;
                 submitbutton.click();
};

button.onclick = () => recog.start();

function speak(msg){

    const speech = new SpeechSynthesisUtterance();
    speech.text = msg;
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;
    window.speechSynthesis.speak(speech);
}

speak('Hi this is your tech assistant, how can I help you');


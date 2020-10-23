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

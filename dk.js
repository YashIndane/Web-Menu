const button = document.getElementById('sb');
//const space = document.getElementById('sp');
//const textfield = document.getElementById('t');
//const submitbutton = document.getElementById('sub');

//const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
//const recog = new SR();

//recog.onstart = () => console.log('speak');

//recog.onresult = function(event){
//                 const current = event.resultIndex;
//                 const transcript = event.results[current][0].transcript;
//                 textfield.value = transcript;
//                 submitbutton.click();
//};
//button.onclick = () => recog.start();

function speak(msg){
        
       const sph = new SpeechSynthesisUtterance();
       sph.text = msg;
       sph.volume = 1;
       sph.rate = 1;
       sph.pitch = 1;
       window.speechSynthesis.speak(sph);
}

button.onclick = () => speak("b");

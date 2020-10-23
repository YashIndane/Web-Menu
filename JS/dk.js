const button = document.getElementById('sb');
const osname = document.getElementById('d_')
const version = document.getElementById('v_');
const na = document.getElementById('n_');
const submitbutton = document.getElementById('ss');

const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const recog = new SR();
var counter = 0;
const fields = [osname , version , na];

recog.onstart = () => console.log('speak');

recog.onresult = function(event){
                 const current = event.resultIndex;
                 const transcript = event.results[current][0].transcript;
                 
                 fields[counter].value = transcript;

                 
                 //textfield.value = transcript;
                 //submitbutton.click();
};


function speak(msg){
        
       const sph = new SpeechSynthesisUtterance();
       sph.text = msg;
       sph.volume = 1;
       sph.rate = 1;
       sph.pitch = 1;
       window.speechSynthesis.speak(sph);
}



function getDetails(){

       speak("Please tell your OS");
       recog.start();
       counter += 1;
       speak("Please tell your version");
       recog.start();
       counter += 1;
       speak("What name you would like to give to the OS?");
       recog.start();
       speak("Launching the OS")
       submitbutton.click();

}

button.onclick = () => getDetails();
function stIns(){

 document.write("<form id = 'f' action = http://IP/cgi-bin/awsr.py>");
 document.write("<input type = 'text' value = 'start instance' name = 'i0'></br>")
 document.write("<input type = 'text' placeholder = 'Enter instance ID' name = 'i1'></br>");
 document.write("<input type = 'submit' value = 'Start'>");
 document.write('</form>');
 document.write("");  

}

function spIns(){

 document.write("<form id = 'f' action = http://IP/cgi-bin/awsr.py>");
 document.write("<input type = 'text' value = 'stop instance' name = 'i0'></br>")
 document.write("<input type = 'text' placeholder = 'Enter instance ID' name = 'i1'></br>")
 document.write("<input type = 'submit' value = 'Stop' >");
 document.write('</form>');
 document.write("");

}

function crSg(){

 document.write("<form id = 'f' action = http://IP/cgi-bin/awsr.py");
 document.write("<input type = 'text' value = 'create SG' name = 'i0'></br>")
 document.write("<input type = 'text' placeholder = 'Enter group name' name = 'i1'></br>");
 document.write("<input type 'text' placeholder = 'Enter description' name = 'i2'></br>")
 document.write("<input type = 'submit' value = 'Create' >");
 document.write('</form>');
 document.write("");

}

function crS3(){

 document.write("<form id = 'f' action = http://IP/cgi-bin/awsr.py>");
 document.write("<input type = 'text' value = 'create S3' name = 'i0'></br>")
 document.write("<input type = 'text' placeholder = 'Enter bucket name' name = 'i1'></br>");
 document.write("<input type 'text' placeholder = 'Enter region' name = 'i2'></br>");
 document.write("<input type = 'submit' value = 'Create' >");
 document.write('</form>');
 document.write("");

}

function upS3(){

 document.write("<form id = 'f' action = http://IP/cgi-bin/awsr.py>");
 document.write("<input type = 'text' value = 'upload to bucket' name = 'i0'></br>")
 document.write("<input type = 'text' placeholder = 'Enter bucket name' name = 'i1'></br>");
 document.write("<input type 'text' placeholder = 'Enter file path' name = 'i2'></br>")
 document.write("<input type = 'submit' value = 'Upload' >");
 document.write('</form>');
 document.write("");

}

function crDs(){

 document.write("<form id = 'f' action = http://IP/cgi-bin/awsr.py>");
 document.write("<input type = 'text' value = 'create cdn' name = 'i0'></br>")
 document.write("<input type = 'text' placeholder = 'Enter origin name' name = 'i1'></br>");
 document.write("<input type = 'submit' value = 'Create' >");
 document.write('</form>');
 document.write("");
 
}



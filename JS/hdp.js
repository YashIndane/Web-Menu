//function nn_create(){



//}

function dn_create(){ 
    
     
     document.write("<form action='---------IP-OF-YOUR-PAGE----------'>");
     document.write("<input type='text' placeholder='Enter Remote IP' name='ip_'></br>");
     document.write("<input type='text' placeholder='Enter master IP' name='mip_'></br>");      
     document.write("<input type='text' placeholder= 'Port no.' name='pn'></br>");
     document.write("<input type='text' placeholder='File name' name='fn_'></br>");
     
     
     
     document.write("<p> Do you want to add logical volume?</p>");
     document.write("<select name='lv'>");
     document.write("<option>Yes</option>"); 
     document.write("<option>No</option>");
     document.write("</select>");
     document.write("<p>Do you wan to create volume group?</p>");
     document.write("<select name='vg'>");
     document.write("<option>Yes</option>");
     document.write("<option>No</option>");
     document.write("</select>");
     document.write("<input type='text' name='vgn' placeholder='Volume group name'></br>");     
     document.write("<input type='text' name='nhd' placeholder='No of hard-disk'></br>");
     document.write("<input type='text' name='HDD' placeholder='Names of HD (space seperated)'></br>");
     document.write("<input type='text' name='lvn' placeholder='logical volume name'></br>");
     document.write("<input type='text' name='lvs' placeholder='logical volume size (GB)'></br>");
     document.write("<p>Do you want to add any space?</p>");
     document.write("<select name='ads'>");
     document.write("<option>Yes</option>");
     document.write("<option>No</option>");
     document.write("</select>");
     document.write("<input type='text' name='ADS' placeholder = 'additional space'>")     
     document.write("<p>Want to start the service?</p>")
     document.write("<select name='ssv'>");
     document.write("<option>Yes</option>");
     document.write("<option>No</option>");
     document.write("</select>");

     document.write("<input type='submit'>");
     document.write("</form>");
     document.write("");
 

}

function cl_create(){
    
    document.write("<form action='---------IP-OF-YOUR-PAGE----------'>");
    document.write("<input type='text' placeholder='Enter Remote IP' name='ip_'></br>");
    document.write("<input type='text' placeholder='Enter master IP' name='mip_'></br>");     
    document.write("<input type='text' placeholder= 'Port no.' name='pn'></br>");
    document.write("<input type='text' placeholder='File name' name='fn_'></br>");
    document.write("<input type='text' placeholder='Enter master IP' name='mip_'></br>");
    document.write("</form>");
    document.write("");
 
    document.write("<p>Want to change defualt replication and block size?</p>");
    document.write("<select name='ssv'>");
    document.write("<option>Yes</option>");
    document.write("<option>No</option>");
    document.write("</select>");

    document.write("<input type='text' placeholder='Replication factor' name='rf_'></br>");
    document.write("<input type='text' placeholder='Block size' name='bs'>");      


    
   

}

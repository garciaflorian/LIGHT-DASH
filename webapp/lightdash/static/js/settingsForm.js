window.onload = settingsForm;

function settingsForm(){
    
    var document = window.document;
    var console = window.console;
    
    var abonnementHPHC = document.getElementById("id_abonnementHPHC");
    var tarifHC = document.getElementById("id_tarifHC");
    var debutHC = document.getElementById("id_debutHC");
    var finHC = document.getElementById("id_finHC");

    function basculeHPHC(){
        if(abonnementHPHC.checked){
            tarifHC.disabled = false;
            tarifHC.value = 0.1228;
            debutHC.disabled = false;
            debutHC.value = "22:00:00";
            finHC.disabled = false;
            finHC.value = "06:00:00";
        }else{
            tarifHC.disabled = true;
            tarifHC.value = "";
            debutHC.disabled = true;
            debutHC.value = "";
            finHC.disabled = true;
            finHC.value = "";
        }
    }
    
    basculeHPHC();
    
    abonnementHPHC.onchange = function(){
        basculeHPHC();
    }
    
}
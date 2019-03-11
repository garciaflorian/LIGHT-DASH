window.onload = settingsForm;

function settingsForm()
{
    var document = window.document;
    var console = window.console;
    
    var abonnementHPHC = document.getElementById("id_abonnementHPHC");
    var tarifHC = document.getElementById("id_tarifHC");
    var debutHC = document.getElementById("id_debutHC");
    var finHC = document.getElementById("id_finHC")

    
    function bascule(){
        if(abonnementHPHC.checked){
            tarifHC.disabled = false;
            debutHC.disabled = false;
            finHC.disabled = false;
        }else{
            tarifHC.disabled = true;
            debutHC.disabled = true;
            finHC.disabled = true;
        }
    }
    
    bascule();
    
    abonnementHPHC.onchange = function() {
        bascule();
    }
}
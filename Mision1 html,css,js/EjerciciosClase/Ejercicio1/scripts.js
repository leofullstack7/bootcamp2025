

function verificarEdad(){
    
    const edadInput = document.getElementById("edadInput").value;

    let bienvenida = document.getElementById("msgVerificacion");
    let msg = ""
    if(edadInput < 18){
        msg += "<p>No puede ver el contenido, usted es menor de edad</p>";
    }else if(edadInput >= 18){
        msg += "Bienvenido, disfruta del contenido";
    }

    bienvenida.innerHTML = msg;
}
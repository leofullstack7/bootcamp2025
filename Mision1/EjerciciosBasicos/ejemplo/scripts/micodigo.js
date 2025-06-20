/* function mostraralerta(){
            alert('Hizo click');
        }

        function hacerclic(){
            document.getElementsByTagName("p")[1].onclick=mostraralerta;
        }
        window.onload=hacerclic; /*Cuando termine de cargar el documento, cargue esta funcion*/ 

let numTabla;
function multiplicar(){
    alert("Hola check");
    numTabla = prompt("Ingrese que tabla"+"de multiplicar quiere ver")
    console.log("La tabla es: ");
    for (let i = 1; i < 10; i++){
        console.log(numTabla*i);
    }
}
window.onload=multiplicar;
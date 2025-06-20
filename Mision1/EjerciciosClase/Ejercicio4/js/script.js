function cambiarColor(){
    let color = "#" + Math.floor(Math.random()* 16777215).toString(16); /* Floor convertir a entero */
    /* #fffff */
    /* console.log(Math.floor(Math.random()* 16777215).toString);
    console.log(Math.floor(Math.random()* 16777215).toString(16)); */

    document.body.style.backgroundColor = color;
    /* Acceder a todo el body para cambiar su color */
    

}
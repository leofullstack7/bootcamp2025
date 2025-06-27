/* let edad = prompt("¿Cuantos años tiene?")
alert("Tienes " + edad + " años");
console.log("El usuario dijo que tiene "+edad+" años");
 */

/* let num1;
let num2;
let suma;
let multi;
let resta;
let edades=[];

num1 = parseInt(prompt("digite el valor de num1"));
num2= parseInt(prompt("Digite el valor de num2"));
suma=num1+num2;
multi = parseInt(num1)*parseInt(num2);

if(num1<num2){
    resta=num2-num1;
}
if(num1==num2){
    resta=0;
}
else{
    resta=num1-num2
}

for (let i = 0; i < 10; i++) {
    edades[i] = num1*(i);   
    console.log("Edad "+i+": "+edades[i]); 
}

alert("😎 El resultado de la suma es: "+suma); /*Windows + punto = emoji
alert("El resultado de la multiplicacion es: "+multi);
alert("El resultado de la resta es: "+resta);
console.log(typeof(suma)); */


/*EJERCICIO 2*/
/* 
let temperatura = parseFloat(prompt("Ingrese la temperatura :"));

if (temperatura > 25) {
    alert("Mucho calor");
}else{
    alert("Más fresco");

} */

/*EJERCICIO 3*/
/* let edad;

edad = prompt("cuantos años tienes?");

if(edad>55){
    alert("Eres un adulto mayor");
}else if(edad >= 26 & edad< 55){
    alert("Eres un adulto");
}else if(edad < 26 & edad >=16){
    alert("Eres un adolescente");
}else if(edad>=2){
    alert("Eres un niño");
}else{
    alert("eres un bebé");
} */



/*EJERCICIO FOR */
/* for (let index = 10; index >=1; index--) {
    console.log(index);  
} */



 
function tunombre(){
    const nom = document.getElementById("nombre");
    alert("Tu nombre es: "+nom.nombre);
};
  
function calcularMasa(){
    const peso = document.getElementById("peso").value;
    const altura = document.getElementById("altura").value;
    const resultadodiv = document.getElementById("resultado");

    if(peso === ""){
        resultadodiv.innerHTML="<p class='error'>Ingresa tu peso</p>";
        return;
    }
    if(altura === ""){
        resultadodiv.innerHTML="<p class='error'>Ingresa tu altura</p>";
        return;
    }
    let valorCalculo = parseFloat(peso/(altura*altura)); 
    let MensajeCalculo = `<h2>Tu masa corporal es ${valorCalculo}</h2><br>`; 
    
    if(valorCalculo < 18,5)
        MensajeCalculo+=`<p>Tu indice de Masa Coporal indica que tienes un peso inferior al normal</p>`;

    else if(valorCalculo >= 18,5 && valorCalculo <= 24,9)
        MensajeCalculo+=`<p>Tu indice de Masa Coporal indica que tienes un peso normal</p>`;

    else if(valorCalculo >= 25 && valorCalculo <= 29)
        MensajeCalculo+=`<p>Tu indice de Masa Coporal indica que tienes un peso inferior al normal</p>`;
    

    MensajeCalculo+=`<br><img src="imc.webp">`
    resultadodiv.innerHTML=MensajeCalculo;
}
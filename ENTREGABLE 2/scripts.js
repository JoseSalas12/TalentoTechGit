const calculadora = (number_1, number_2, operation_math) => {
    if (operation_math == "suma") {
        return (number_1 + number_2);
    } 
    else if (operation_math == "resta") {
        return (number_1 - number_2);
    }
    else if (operation_math == "multiplicacion") {
        return (number_1 * number_2);
    }
    else if (operation_math == "division") {
        if (number_2 == 0) {
            return "No es posible realizar una division por cero"
        }

        return (number_1 / number_2);
    }
    else {
        return "La operacion matematica no es valida"
    }
}

let number_1, number_2, operation_math;
let quesiton;

while(operation_math != "salir") {
    number_1 = prompt("\nIngrese el primer numero \n");
    number_2 = prompt("Ingrese el segundo numero \n");
    
    operation_math = prompt("Ingrese la operacion (suma, resta, multiplicacion, division): \n");

    alert(`El Resultado es: ${calculadora(+number_1, +number_2, operation_math)}` );

    console.log("El resultado es: ")
    console.log(calculadora(+number_1, +number_2, operation_math))

    quesiton = prompt("\n\nDesea realizar otra operacion? \n")

    if (quesiton == "si") {
        continue
    } else {
        alert("Gracias por utilizar la calculadora!")
        console.log("Gracias por utilizar la calculadora!\n")
        break
    }
}
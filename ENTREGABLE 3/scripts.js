function validarFormulario(){
    let nombre = document.getElementById('nombre').value;
    let email = document.getElementById('email').value;
    let mensaje = document.getElementById('mensaje').value;

    if(nombre === "" || email === "" || mensaje === ""){
        return false;
    }else{
        return true;

    }
}

let formulario = document.getElementById('formulario');
formulario.addEventListener('submit', function(e){
    e.preventDefault();

    if(validarFormulario()){
        alert('Mensaje enviado correctamente');
        formulario.reset();
    }else{
        alert('Todos los campos son obligatorios');
    }


});
function obtenerDatos(id){
    // cambiando la accion del formulario
    document.getElementById('formulario').action ='/editar_persona/' + id
    document.getElementById('boton').innerHTML = 'Actualizar'
    
    //Se almacenan los datos para extraer los datos para actualizar en el formulario//
    nombreActual = document.getElementById('tabla_nombre'+id).innerHTML
    apellidoActual = document.getElementById('tabla_apellido'+id).innerHTML
    telefonoActual = document.getElementById('tabla_telefono'+id).innerHTML

        /*Se extraen los valores de la tabla*/
        document.getElementById('nombre').value = nombreActual
        document.getElementById('apellido').value = apellidoActual 
        document.getElementById('telefono').value = telefonoActual

}
const obj = {
    "empleados": [
        {
            "nombre": "Juan Perez",
            "apellido": "Lopez",
            nombreCompleto: function () {
                return this.nombre + " " + this.apellido
            }
        },
        {
            "nombre": "Ana",
            "apellido": "Gonzalez",
            nombreCompleto: function () {
                return this.nombre + " " + this.apellido
            }
        },
        {
            "nombre": "Pedro",
            "apellido": "Sanchez",
            nombreCompleto: function () {
                return this.nombre + " " + this.apellido
            }
        },
    ],

}

console.log(obj.empleados[2].apellido)
console.log(obj.nombreCompleto(2))
console.log(obj.empleados.length)
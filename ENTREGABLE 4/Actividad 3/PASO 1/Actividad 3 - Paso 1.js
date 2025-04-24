// Crear colección e insertar documentos
db.Estudiantes.insertMany([
    { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
    { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
    { "nombre": "Luis", "edad": 19, "ciudad": "Cali" }
]);

// Consultas básicas
db.Estudiantes.find(); // Todos los documentos
db.Estudiantes.find({ "ciudad": "Bogotá" }); // Filtrar por ciudad
db.Estudiantes.find({ "edad": { $gt: 20 } }); // Mayores de 20
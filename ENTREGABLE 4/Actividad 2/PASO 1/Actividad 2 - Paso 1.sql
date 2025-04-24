-- Crear tabla Estudiantes
CREATE TABLE Estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

-- Insertar datos
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES
('Juan', 20, 'Bogotá'),
('Ana', 22, 'Medellín'),
('Luis', 19, 'Cali');

-- Consultas básicas
SELECT * FROM Estudiantes; -- Todos los registros
SELECT * FROM Estudiantes WHERE ciudad = 'Bogotá'; -- Filtrar por ciudad
SELECT * FROM Estudiantes WHERE edad > 20; -- Mayores de 20
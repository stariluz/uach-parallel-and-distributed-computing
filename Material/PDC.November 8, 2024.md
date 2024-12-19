### listener.ora
Los servidores de oracle escuchan en el puerto 1521.

### tsnames.ora
Servicios.
Servicio FREE que apunta al puerto 1521 de la misma máquina. Para hacer que apunte a otra máquina, se coloca el IP de la otra máquina.

Así podemos hacer consultas a otro servidor.

Se deben agregar los servicios para conectarse a más máquinas.


# Database link
- Consultas distribuidas
- Replicación de datos
- Administración centralizada
- Acceso remoto

CREATE DATABASE LINK name_link
CONNECT TO user IDENTIFIED BY password
USING 'name_tns';

User and password from the server we want to connect to.

name_tns es el que hayamos agregado en el archivo tnsname.ora.

La otra forma de crearlo es:
```sql
CREATE DATABASE LINK name_link
CONNECT TO CURRENT_USER # CONNECT TO user IDENTIFIED BY password
USING 'DESCRIPTION = (ADDRESS= (PROTOCOL = TCP)(HOST = 0.0.0.0)(PORT=1521))
(CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = name_tns));
```

### Ejemplo de uso de database link
SELECT * FROM employees@name_link;

SELECT name, first_name, last_name
FROM departments AS d JOIN employees@name_link AS e
ON d.department_id = e.department_id;


### Transaccion distribuida
Una o varias operaciones, Update, Delete, Insert.

Una transaccion que afecta a varios servidores a la vez.

### Consultar databases links

#### SELECT * FROM USER_DB_LINKS;
#### SELECT * FROM DBA_DB_LINKS;
Todos los databases links de todas las bases de datos y todos los usuarios.

### Ventajas
- Acceso distribuido a datos.
- Consultas transparentes.
- Llamadas a repositorios remotos.
- Integración de datos.
- Administración centralizada.
- Seguridad y control de acceso.
- Acceso a bases de datos heterogeneas.
- Escalaibilidad.
- Reducción de tráfico de red.


### Desventajas
- Sobrecarga de rendimiento.
- Fiabilidd de la red.
- Riesgos de seguridad.
- Complejidad.
- Consistencia de datos. Hay que cuidar más para la consistencia transaccional.
- Licencias y costes.
- Dependencia del proveedor. No todas las bases de datos pueden conectarse así.
- Funcionalidad limitada.
- Mantenimiento y supervición.
- Probleas de compatibilidad.

### Transparencia
- Sinónimos.
- Vistas.
- Procedimientos almacenados.


GRANT DBA TO user;

Insertar datos de sucursales y prestamos.

Se prueban los database links

CREATE SYNONYM prestamo_A for prestamo@server_a;
CREATE SYNONYM sucursal_A for sucursal@server_a;
CREATE SYNONYM prestamo_B for prestamo@server_b;
CREATE SYNONYM sucursal_B for sucursal@server_b;

Queremos una vista global en un tercer servidor. 
CREATE OR REPLACE VIEW sucursales AS
SELECT * FROM sucursal_a
UNION ALL
SELECT * FROM sucursal_b;
CREATE OR REPLACE VIEW prestamos AS
SELECT * FROM prestamo_a
UNION ALL
SELECT * FROM prestamo_b;
Esto permite hacer consultas globales

SELECT * FROM prestamos;
SELECT * FROM sucursales;


Insertar en la sucursal A o B

CREATE OR REPLACE PROCEDURE alta_sucursal(
    ...
) AS
BEGIN
    IF p_region='A' THEN
        EXECUTE INMEDIATE 'INSERT INTO sucursal_a VALUES (....)
        USING ...;
    ELSIF p_region='B THEN
    ...
    ELSE
        RAISE_APPLICATION_ERROR(-20001, 'Región no válida');
    ENDIF;
END;

EXEC alta_sucursal(...);



Replicación
Replicar la información en un tercer servidor.

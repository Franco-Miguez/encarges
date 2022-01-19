CREATE DATABASE IF NOT EXISTS multicolor;
use multicolor;

CREATE TABLE IF NOT EXISTS productos(
    id INT(25) auto_increment NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT ,
    precio FLOAT(10,2) NOT NULL,
    categoria VARCHAR(255),
    CONSTRAINT pk_productos PRIMARY KEY(id),
    CONSTRAINT uq_nombre UNIQUE(nombre)
)ENGINE=InnoDb;

CREATE TABLE clientes(
    id INT(20) auto_increment NOT NULL,
    celular INT(15) NOT NULL,
    nombre VARCHAR(255),
    CONSTRAINT pk_clientes PRIMARY KEY(id)
)ENGINE=InnoDb;

CREATE TABLE pedidos(
    id INT(25) auto_increment NOT NULL,
    fecha DATE NOT NULL,
    entrega DATE,
    informcacion TEXT,
    seña FLOAT(10,2),
    clientes_id INT(20) NOT NULL,
    CONSTRAINT pk_pedidos PRIMARY KEY(id),
    CONSTRAINT fk_pedido_cliente FOREIGN KEY(clientes_id) REFERENCES clientes(id)
)ENGINE=InnoDb;

CREATE TABLE compras(
    id INT(50) auto_increment NOT NULL,
    nombre VARCHAR (255) NOT NULL,
    precio FLOAT(10,2) NOT NULL,
    cantidad INT(10) NOT NULL,
    descripcion TEXT,
    pedidos_id INT(25) NOT NULL,
    CONSTRAINT pk_compras PRIMARY KEY(id),
    CONSTRAINT fk_compra_pedido FOREIGN KEY(pedidos_id) REFERENCES pedidos(id)
)ENGINE=InnoDb;
/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.24-MariaDB : Database - edina
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`edina` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `edina`;

/*Table structure for table `arte` */

DROP TABLE IF EXISTS `arte`;

CREATE TABLE `arte` (
  `id_arte` int(11) NOT NULL AUTO_INCREMENT,
  `id_artista` int(11) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_arte`),
  KEY `id_artista` (`id_artista`),
  CONSTRAINT `arte_ibfk_1` FOREIGN KEY (`id_artista`) REFERENCES `artista` (`id_artista`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `artista` */

DROP TABLE IF EXISTS `artista`;

CREATE TABLE `artista` (
  `id_artista` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) DEFAULT NULL,
  `fecha_arte` date DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_artista`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `campanias` */

DROP TABLE IF EXISTS `campanias`;

CREATE TABLE `campanias` (
  `id_campanias` int(11) NOT NULL AUTO_INCREMENT,
  `anio_guia` int(11) DEFAULT NULL,
  `tipo_campania` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_campanias`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `ciudad` */

DROP TABLE IF EXISTS `ciudad`;

CREATE TABLE `ciudad` (
  `id_ciudad` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) DEFAULT NULL,
  `id_provincia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `cliente` */

DROP TABLE IF EXISTS `cliente`;

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `identificacion` varchar(14) DEFAULT NULL,
  `nombres` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `longitud` varchar(255) DEFAULT NULL,
  `latitud` varchar(255) DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `contrato` */

DROP TABLE IF EXISTS `contrato`;

CREATE TABLE `contrato` (
  `id_contrato` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) DEFAULT NULL,
  `id_vendedores` int(11) DEFAULT NULL,
  `id_ciudad` int(11) DEFAULT NULL,
  `id_campanias` int(11) DEFAULT NULL,
  `valor_cargo` int(11) DEFAULT NULL,
  `valor_venta` decimal(10,0) DEFAULT NULL,
  `fecha_contrato` date DEFAULT NULL,
  `estado_cargo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_contrato`),
  KEY `id_campanias` (`id_campanias`),
  KEY `id_ciudad` (`id_ciudad`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_vendedores` (`id_vendedores`),
  CONSTRAINT `contrato_ibfk_1` FOREIGN KEY (`id_campanias`) REFERENCES `campanias` (`id_campanias`),
  CONSTRAINT `contrato_ibfk_2` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`),
  CONSTRAINT `contrato_ibfk_3` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `contrato_ibfk_4` FOREIGN KEY (`id_vendedores`) REFERENCES `vendedores` (`id_vendedores`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `contrato_reserva` */

DROP TABLE IF EXISTS `contrato_reserva`;

CREATE TABLE `contrato_reserva` (
  `id_contrato_reserva` int(11) DEFAULT NULL,
  `id_contrato` int(11) DEFAULT NULL,
  `id_reserva` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Table structure for table `gestion` */

DROP TABLE IF EXISTS `gestion`;

CREATE TABLE `gestion` (
  `id_gestion` int(11) NOT NULL AUTO_INCREMENT,
  `id_planificacion` int(11) DEFAULT NULL,
  `fecha_gestion` date DEFAULT NULL,
  `tipo_gestion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_gestion`),
  KEY `id_planificacion` (`id_planificacion`),
  CONSTRAINT `gestion_ibfk_1` FOREIGN KEY (`id_planificacion`) REFERENCES `planificacion` (`id_planificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `planificacion` */

DROP TABLE IF EXISTS `planificacion`;

CREATE TABLE `planificacion` (
  `id_planificacion` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) DEFAULT NULL,
  `id_vendedores` int(11) DEFAULT NULL,
  `fecha_planificacion` date DEFAULT NULL,
  `hora_planificacion` varchar(200) DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `descripcion` varchar(200) DEFAULT NULL,
  `estado` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_planificacion`),
  KEY `id_vendedores` (`id_vendedores`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `planificacion_ibfk_1` FOREIGN KEY (`id_vendedores`) REFERENCES `vendedores` (`id_vendedores`),
  CONSTRAINT `planificacion_ibfk_2` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `planificacion_reserva` */

DROP TABLE IF EXISTS `planificacion_reserva`;

CREATE TABLE `planificacion_reserva` (
  `id_planificacion_reserva` int(11) NOT NULL AUTO_INCREMENT,
  `id_reserva` int(11) NOT NULL,
  `id_planificacion` int(11) NOT NULL,
  PRIMARY KEY (`id_planificacion_reserva`),
  KEY `id_planificacion` (`id_planificacion`),
  KEY `id_reserva` (`id_reserva`),
  CONSTRAINT `planificacion_reserva_ibfk_1` FOREIGN KEY (`id_planificacion`) REFERENCES `planificacion` (`id_planificacion`),
  CONSTRAINT `planificacion_reserva_ibfk_2` FOREIGN KEY (`id_reserva`) REFERENCES `reserva` (`id_reserva`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `premios` */

DROP TABLE IF EXISTS `premios`;

CREATE TABLE `premios` (
  `id_premios` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) DEFAULT NULL,
  `total_minimo` decimal(10,0) DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_premios`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `premiossemanales` */

DROP TABLE IF EXISTS `premiossemanales`;

CREATE TABLE `premiossemanales` (
  `id_premioSemaneles` int(11) NOT NULL AUTO_INCREMENT,
  `id_vendedores` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `total_venta` decimal(10,0) DEFAULT NULL,
  KEY `id_premioSemaneles` (`id_premioSemaneles`),
  KEY `id_vendedores` (`id_vendedores`),
  CONSTRAINT `premiossemanales_ibfk_1` FOREIGN KEY (`id_vendedores`) REFERENCES `vendedores` (`id_vendedores`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `provincias` */

DROP TABLE IF EXISTS `provincias`;

CREATE TABLE `provincias` (
  `id_provincia` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_provincia`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `redimientovendedores` */

DROP TABLE IF EXISTS `redimientovendedores`;

CREATE TABLE `redimientovendedores` (
  `id_rendimiento_vendedores` int(11) NOT NULL AUTO_INCREMENT,
  `proceso` varchar(100) DEFAULT NULL,
  `numero` varchar(100) DEFAULT NULL,
  `valor` varchar(100) DEFAULT NULL,
  `carteraPorTrabajar` varchar(100) DEFAULT NULL,
  `ventaCargo` varchar(100) DEFAULT NULL,
  `incrementoCargo` varchar(100) DEFAULT NULL,
  `id_vendedores` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_rendimiento_vendedores`),
  KEY `id_vendedores` (`id_vendedores`),
  CONSTRAINT `redimientovendedores_ibfk_1` FOREIGN KEY (`id_vendedores`) REFERENCES `vendedores` (`id_vendedores`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `reserva` */

DROP TABLE IF EXISTS `reserva`;

CREATE TABLE `reserva` (
  `id_reserva` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) DEFAULT NULL,
  `id_vendedores` int(11) DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id_reserva`),
  KEY `id_vendedores` (`id_vendedores`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`id_vendedores`) REFERENCES `vendedores` (`id_vendedores`),
  CONSTRAINT `reserva_ibfk_3` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `vendedores` */

DROP TABLE IF EXISTS `vendedores`;

CREATE TABLE `vendedores` (
  `id_vendedores` int(11) NOT NULL AUTO_INCREMENT,
  `id_campania` int(11) DEFAULT NULL,
  `nombres` varchar(255) DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `latitud` varchar(100) DEFAULT NULL,
  `longitud` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_vendedores`),
  KEY `id_campania` (`id_campania`),
  CONSTRAINT `vendedores_ibfk_1` FOREIGN KEY (`id_campania`) REFERENCES `campanias` (`id_campanias`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

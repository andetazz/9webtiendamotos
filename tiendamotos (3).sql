-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-05-2024 a las 05:17:15
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tiendamotos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `idcarrito` int(11) NOT NULL,
  `idproducto` int(11) DEFAULT NULL,
  `iduser` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`idcarrito`, `idproducto`, `iduser`, `cantidad`) VALUES
(6, 1, 2, 5),
(7, 1024, 2, 4),
(8, 1, 2, 7),
(9, 1038, 2, 1),
(10, 1, 2, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `idcategoria` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `img1` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idcategoria`, `nombre`, `img1`) VALUES
(1, 'FRENOS', '1f0ccd75e3964084b5c5b76374994ea7.jfif'),
(2, 'ACEITES', 'ea6d8434611040b0b5f886b9e7b606e0.jfif'),
(3, 'GUAYAS', 'd471010022e94b6f94a6a797f7545454.jfif'),
(4, 'GENERICO', 'categoria.png'),
(5, 'bujias', '184df3fc2a9943fea3e5ecf915f4d67f.jfif'),
(30, 'guantes', 'b4c739be53df4b4bb8be5de194579be2.jfif'),
(31, 'xxx', 'categoria.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `idproducto` int(11) NOT NULL,
  `precio` float NOT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  `img1` varchar(300) DEFAULT NULL,
  `img2` varchar(300) DEFAULT NULL,
  `img3` varchar(300) DEFAULT NULL,
  `img4` varchar(300) DEFAULT NULL,
  `idcategoria` int(11) DEFAULT NULL,
  `nombre` varchar(300) NOT NULL,
  `stock` int(11) NOT NULL,
  `pordes` int(11) NOT NULL,
  `descuento` float NOT NULL,
  `iva` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`idproducto`, `precio`, `descripcion`, `img1`, `img2`, `img3`, `img4`, `idcategoria`, `nombre`, `stock`, `pordes`, `descuento`, `iva`) VALUES
(1, 500000, 'https://docs.conecta.nequi.com.co/#!/Pagos32QR/post_services_paymentservice_generatecodeqr', 'd7fd357e99444982984bf2ed4e4483c1.jfif', '034f543e20ae4783a1300d42d81105c7.jfif', 'productos.png', 'productos.png', 1, 'PASTILLA DE FRENO ', 0, 0, 0, 0),
(4, 12000, 'bujia temperatura', '5d9fec73f3034520a78f40e589ae5c07.jfif', '69fa727f5b3748768d721df0ac4f072b.jfif', 'productos.png', 'productos.png', 5, 'BUJIAS ', 0, 20, 2400, 10),
(1001, 5700, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO PALMA\r', 0, 0, 0, 0),
(1005, 6000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO EN PALMA VAQUETA CON REFUERZO DEDO INDICE Y PULGAR\r', 0, 0, 0, 0),
(1007, 8500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO EN PALMA MANGA LARGA EN VAQUETA\r', 0, 0, 0, 0),
(1008, 7000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO VAQUETA REFUERZO PALMA EN VAQUETA MANGA LARGA EN CARNAZA\r', 0, 0, 0, 0),
(1010, 6200, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE VAQUETA EXTRA LARGO REFUERZO COMPLETO EN VAQUETA\r', 0, 0, 0, 0),
(1011, 5500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO MIXTO REFUERZO EN PALMA CARNAZA\r', 0, 0, 0, 0),
(1012, 6200, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO EXTRA GRANDE MIXTO REFUERZO COMPLETO EN VAQUETA\r', 0, 0, 0, 0),
(1013, 7500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO REFUERZO EN PALMA Y MANGA EN VAQUETA 3/4\r', 0, 0, 0, 0),
(1014, 7200, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO SENCILLO MANGA 3/4 VAQUETA\r', 0, 0, 0, 0),
(1015, 6700, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO REFORZADO EN PALMA VAQUETA Y MANGA EN CARNAZA 3/4\r', 0, 0, 0, 0),
(1016, 5500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO CARNAZA REFUERZO EN VAQUETA COMPLETO\r', 0, 0, 0, 0),
(1017, 5120, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO CARNAZA REFUERZO COMPLETO TRANSEJES\r', 0, 0, 0, 0),
(1018, 4000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO CARNAZA REFUERZO PALMA EN CARNAZA\r', 0, 0, 0, 0),
(1019, 6500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO SENCILLO MANGA 3/4 CARNAZA\r', 0, 0, 0, 0),
(1020, 14700, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO SENCILLO PEGADO A LA MANGA SOLDADOR\r', 0, 0, 0, 0),
(1021, 5900, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO BARRIDO\r', 0, 0, 0, 0),
(1022, 7500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE INGENIERO RECOLECCION\r', 0, 0, 0, 0),
(1023, 12000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE ESPECIAL PALMERO VAQUETA REFUERZO COMPLETO Y MANGA EN VAQUETA\r', 0, 0, 0, 0),
(1024, 6000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERCO COMPLETO VAQUETA CORTO\r', 0, 0, 0, 0),
(1025, 7500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERZO COMPLETO EN VAQUETA MANGA LARGA\r', 0, 0, 0, 0),
(1026, 7000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERZO COMPLETO EN VAQUETA MANGA 3/4\r', 0, 0, 0, 0),
(1027, 8700, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE PALMERO CARNAZA REFUERZO COMPLETO EN TULA\r', 0, 0, 0, 0),
(1028, 5500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE CARNAZA PALMERO REFUERZO COMPLETO EN CARNAZA MANGA CORTA\r', 0, 0, 0, 0),
(1029, 6000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE CARNAZA REFUERZO COMPLETO CARNAZA MANGA LARGA\r', 0, 0, 0, 0),
(1030, 9500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE SOLDADOR SENCILLO EN CARNAZA\r', 0, 0, 0, 0),
(1031, 12000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE SOLDADOR CARNAZA REFUERZO COMPLETO EN VAQUETA\r', 0, 0, 0, 0),
(1032, 4800, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE CICLISTA MIXTO\r', 0, 0, 0, 0),
(1033, 8000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE CICLISTA EN VAQUETA\r', 0, 0, 0, 0),
(1034, 7500, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE CICLISTA VAQUETA REFUERZO VAQUETA CON ESPUMA\r', 0, 0, 0, 0),
(1035, 10000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE PANADERO\r', 0, 0, 0, 0),
(1036, 15000, 'AnDy', 'productos.png', '0', '0', '', 30, 'GUANTE PARA MOTO\r', 0, 0, 0, 0),
(1037, 9500, 'AnDy', 'productos.png', '0', '0', '', 30, 'POLAINA EN CARNAZA CORTA\r', 0, 0, 0, 0),
(1038, 12000, 'AnDy', 'productos.png', '0', '0', '', 30, 'POLAINA EN CARNAZA LARGA\r', 0, 0, 0, 0),
(1039, 34000, 'AnDy', 'productos.png', '0', '0', '', 30, 'POLAINA TULA\r', 0, 0, 0, 0),
(1040, 9500, 'AnDy', 'productos.png', '0', '0', '', 30, 'PETO CARNAZA 90 X 60\r', 0, 0, 0, 0),
(1041, 19000, 'AnDy', 'productos.png', '0', '0', '', 30, 'PETO VAQUETA 90 X 60\r', 0, 0, 0, 0),
(1042, 25000, 'AnDy', 'productos.png', '0', '0', '', 30, 'PETO VAQUETA 60 X 120\r', 0, 0, 0, 0),
(1043, 12000, 'AnDy', 'productos.png', '0', '0', '', 30, 'PETO CARNAZA 60 X 120\r', 0, 0, 0, 0),
(1044, 28000, 'AnDy', 'productos.png', '0', '0', '', 30, 'PETO EN TULA 90 X 60\r', 0, 0, 0, 0),
(1045, 19000, 'AnDy', 'productos.png', '0', '0', '', 30, 'PETO CARNAZA DOBLE 90 X 60\r', 0, 0, 0, 0),
(1046, 29000, 'AnDy', 'productos.png', '0', '0', '', 30, 'CHAQUETA VAQUETA SOLDADOR\r', 0, 0, 0, 0),
(1047, 300, 'AnDy', 'productos.png', '0', '0', '', 30, 'TAPABOCAS COMPUTELL\r', 0, 0, 0, 0),
(1048, 9000, 'AnDy', 'productos.png', '0', '0', '', 30, 'MANGA CARNAZA\r', 0, 0, 0, 0),
(1049, 19000, 'AnDy', 'productos.png', '0', '0', '', 30, 'MANGA VAQUETA\r', 0, 0, 0, 0),
(1050, 28000, 'AnDy', 'productos.png', '0', '0', '', 30, 'MANGA TULA\r', 0, 0, 0, 0),
(1051, 5000, 'Administrador d', 'productos.png', '0', '0', '', 30, 'PETICION HORUN MOTORIZADO\r', 0, 0, 0, 0),
(1052, 40000, 'Administrador d', '1000', '0', '0', 'a12', 30, 'BODIARMO\r', 0, 0, 0, 0),
(1053, 130000, 'Administrador d', 'productos.png', '0', '0', 'I1', 30, 'OSOS\r', 0, 0, 0, 0),
(1054, 11000, 'Administrador d', 'productos.png', '0', '0', '', 30, 'CAJAS ZAPATERA\r', 0, 0, 0, 0),
(1055, 10000, 'Administrador d', 'productos.png', '0', '0', '', 30, 'GLOBOS\r', 0, 0, 0, 0),
(1056, 3000, 'Administrador d', 'productos.png', '0', '0', '', 30, 'BOMBAS\r', 0, 0, 0, 0),
(1057, 70000, 'Administrador d', 'productos.png', '0', '0', '', 30, 'EXTINTIOR DE 10 LIBRAS\r', 0, 0, 0, 0),
(1058, 30000, 'DAVID ALEJANDRO', 'productos.png', '0', '0', 'P1I2', 30, 'ACEITE MOTUL\r', 0, 0, 0, 0),
(1059, 14000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'DIRECCIONALES MOTOS\r', 0, 0, 0, 0),
(1060, 28000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE DICXOIL\r', 0, 0, 0, 0),
(1061, 28000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE ADVANCE\r', 0, 0, 0, 0),
(1062, 28000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE SUPER MOVIL\r', 0, 0, 0, 0),
(1063, 25000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE CASTROL\r', 0, 0, 0, 0),
(1064, 36000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE YAMALUBE\r', 0, 0, 0, 0),
(1065, 35000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE HAVOLINE\r', 0, 0, 0, 0),
(1066, 40000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE HONDA\r', 0, 0, 0, 0),
(1067, 37000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE MOTUL\r', 0, 0, 0, 0),
(1068, 25000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE CELERITY\r', 0, 0, 0, 0),
(1069, 22000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'CERA BRILLA MAX\r', 0, 0, 0, 0),
(1070, 22000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'LLANTYL\r', 0, 0, 0, 0),
(1071, 15000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'LIQUIDO DE FRENOS\r', 0, 0, 0, 0),
(1072, 25000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'ACEITE HIDRAULICO\r', 0, 0, 0, 0),
(1073, 10000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'GRASA DE CADENA\r', 0, 0, 0, 0),
(1074, 120000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'FRENO DE DISCO  PULSAR 180\r', 0, 0, 0, 0),
(1075, 180000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'RELACION COMPLETA PLATO, CADENA, PI?ON PULSAR 180\r', 0, 0, 0, 0),
(1076, 115000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'RELACION COMPLETA PULSAR 135\r', 0, 0, 0, 0),
(1077, 150000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'RELACION COMPLETA DT\r', 0, 0, 0, 0),
(1078, 120000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'FRENO DE DISCO 135\r', 0, 0, 0, 0),
(1079, 40000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'PLATO GENERICO\r', 0, 0, 0, 0),
(1080, 33000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'CADENA  428\r', 0, 0, 0, 0),
(1081, 35000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'CADENA 520\r', 0, 0, 0, 0),
(1082, 25000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'PASTILLAS DE FRENO DELANTERA\r', 0, 0, 0, 0),
(1083, 25000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'PASTILLA DE FRENO TRASERO\r', 0, 0, 0, 0),
(1084, 25000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'BANDAS DE FRENO\r', 0, 0, 0, 0),
(1085, 12000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'CAUCHOS CAMPANA FRENO\r', 0, 0, 0, 0),
(1086, 55000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'BOMBAS DE FRENO\r', 0, 0, 0, 0),
(1087, 60000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'DISCOS DE CLOSH\r', 0, 0, 0, 0),
(1088, 12000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'MANILARES\r', 0, 0, 0, 0),
(1089, 25000, 'ANDRES PE?A VEL', 'productos.png', '0', '0', '', 30, 'MANIGUETA\r', 0, 0, 0, 0),
(1090, 250000, 'caco cerrado con normas iso', '249297afa227479ca13db30440be88c3.webp', 'fe19dd16cd754534ab88024e1f8ae04f.webp', '60ea3b424cb84d86a8755247f75d1277.webp', '37c7ea491ae2494db74294cb4f20d82f.jfif', 4, 'caco cerrado certificado ', 0, 0, 0, 0),
(1091, 150000, 'impermedable general', '9abec08a8c5241459cc5804d8efbee5d.jfif', 'productos.png', 'productos.png', 'productos.png', 4, 'IMPERMEDABLE PLASTICO ', 1, 0, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `iduser` int(11) NOT NULL,
  `nameuser` varchar(90) NOT NULL,
  `passworduser` varchar(300) NOT NULL,
  `nombre` varchar(90) DEFAULT NULL,
  `telefono` varchar(90) DEFAULT NULL,
  `correo` varchar(90) DEFAULT NULL,
  `cedula` varchar(90) DEFAULT NULL,
  `imgper` varchar(300) DEFAULT NULL,
  `feccre` date DEFAULT NULL,
  `tipousu` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`iduser`, `nameuser`, `passworduser`, `nombre`, `telefono`, `correo`, `cedula`, `imgper`, `feccre`, `tipousu`) VALUES
(1, 'andy', '1234', 'andy', 'None', 'ANDETAZZ@GMAIL.COM', 'None', NULL, NULL, 2),
(2, 'andres', '1234', 'andres123', '12345', 'ANDETAZZ87@GMAIL.COM', '12356', 'usuario.png', NULL, 1),
(3, 'andres1', '123', 'andres1', '1234', 'ANDETAZZ@GMAIL.COM', '1234', 'usuario.png', NULL, 1),
(5, 'andy1', '123', 'andy1', '123', 'ANDETAZZ@GMAIL.COM', '123', NULL, NULL, NULL),
(6, 'paco', '1234', 'DD', '123', 'ANDETAZZ@GMAIL.COM', '123', 'usuario.png', NULL, NULL),
(7, 'pepe', '1234', 'DD', '123', 'ANDETAZZ@GMAIL.COM', '123', 'usuario.png', NULL, NULL),
(8, 'rosa', '1234', NULL, NULL, NULL, NULL, 'usuario.png', NULL, NULL),
(9, 'miguel1', '1234', NULL, NULL, NULL, NULL, 'usuario.png', NULL, NULL),
(10, 'manolo', '1234', NULL, NULL, NULL, NULL, 'usuario.png', NULL, NULL),
(11, 'prueba', '1234', NULL, NULL, NULL, NULL, 'prueba.jpg', NULL, NULL),
(12, 'PEDROP', '1234', 'DD', '123', 'ANDETAZZ@GMAIL.COM', '123', '123.png', NULL, NULL),
(13, 'PEDROPI', '1234', '123', '123', 'ANDETAZZ@GMAIL.COM', '123', 'usuario.png', NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_d`
--

CREATE TABLE `ventas_d` (
  `iddetalle` int(11) NOT NULL,
  `idventa` int(11) DEFAULT NULL,
  `idproducto` int(11) DEFAULT NULL,
  `nro_docu` varchar(90) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `precio` float NOT NULL,
  `cantidad` int(11) NOT NULL,
  `iva` int(11) DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_d`
--

INSERT INTO `ventas_d` (`iddetalle`, `idventa`, `idproducto`, `nro_docu`, `fecha`, `precio`, `cantidad`, `iva`, `descuento`, `total`) VALUES
(1, 1, 1024, NULL, NULL, 6000, 4, 0, 0, 24000),
(3, 2, 1024, NULL, NULL, 6000, 4, 0, 0, 24000),
(7, 5, 1024, NULL, NULL, 6000, 4, 0, 0, 24000),
(8, 5, 1038, NULL, NULL, 12000, 1, 0, 0, 12000),
(9, 6, 1024, NULL, NULL, 6000, 4, 0, 0, 24000),
(10, 6, 1, NULL, NULL, 500000, 5, 0, 0, 2500000),
(11, 7, 1038, NULL, NULL, 12000, 1, 0, 0, 12000),
(12, 7, 1, NULL, NULL, 500000, 7, 0, 0, 3500000),
(13, 8, 1, NULL, NULL, 500000, 7, 0, 0, 3500000),
(15, 10, 1038, NULL, '2025-03-15', 12000, 1, 0, 0, 12000),
(16, 10, 1, NULL, '2025-03-15', 500000, 7, 0, 0, 3500000),
(17, 11, 1038, NULL, '2025-03-15', 12000, 1, 0, 0, 12000),
(18, 11, 1, NULL, '2025-03-15', 500000, 7, 0, 0, 3500000),
(20, 12, 1024, NULL, '2025-03-15', 6000, 4, 0, 0, 24000),
(22, 13, 1024, NULL, '2025-03-28', 6000, 4, 0, 0, 24000),
(23, 14, 1024, NULL, '2025-03-28', 6000, 4, 0, 0, 24000),
(25, 15, 1024, NULL, '2025-03-28', 6000, 4, 0, 0, 24000),
(28, 17, 1024, NULL, '2025-03-28', 6000, 4, 0, 0, 24000),
(30, 18, 1024, NULL, '2025-03-28', 6000, 4, 0, 0, 24000),
(32, 19, 1024, NULL, '2025-03-28', 6000, 4, 0, 0, 24000),
(34, 20, 1024, NULL, '2025-03-28', 6000, 1, 0, 0, 6000),
(35, 21, 1, NULL, '2025-03-28', 500000, 1, 0, 0, 500000),
(37, 22, 1024, NULL, '2025-03-28', 6000, 2, 0, 0, 12000),
(39, 23, 1024, NULL, '2025-03-28', 6000, 7, 0, 0, 42000),
(41, 24, 1024, NULL, '2025-04-07', 6000, 4, 0, 0, 24000),
(42, 25, 4, NULL, '2025-04-28', 12000, 2, 1920, 4800, 21120);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_t`
--

CREATE TABLE `ventas_t` (
  `idventa` int(11) NOT NULL,
  `iduser` int(11) DEFAULT NULL,
  `nro_docu` varchar(90) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `f_vto` date DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `iva` float DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `observacion` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_t`
--

INSERT INTO `ventas_t` (`idventa`, `iduser`, `nro_docu`, `fecha`, `f_vto`, `subtotal`, `iva`, `descuento`, `total`, `observacion`) VALUES
(1, 2, NULL, NULL, NULL, 0, 0, 0, 24000, NULL),
(2, 2, NULL, NULL, NULL, 0, 0, 0, 176000, NULL),
(3, 2, NULL, NULL, NULL, 0, 0, 0, 27000, NULL),
(4, 2, NULL, NULL, NULL, 0, 0, 0, 125000, NULL),
(5, 2, NULL, NULL, NULL, 0, 0, 0, 36000, NULL),
(6, 2, NULL, NULL, NULL, 0, 0, 0, 2524000, NULL),
(7, 2, NULL, NULL, NULL, 3512000, 667280, 0, 4179280, NULL),
(8, 2, NULL, '2025-03-15', NULL, 3500000, 665000, 0, 4165000, NULL),
(9, 2, NULL, '2025-03-15', '2025-04-14', 21000, 3990, 0, 24990, 'dfdhdfghfg'),
(10, 2, NULL, '2025-03-15', '2025-04-14', 3512000, 667280, 0, 4179280, 'sgdgfg'),
(11, 2, NULL, '2025-03-15', '2025-04-14', 3512000, 667280, 0, 4179280, ''),
(12, 2, NULL, '2025-03-15', '2025-04-14', 149000, 28310, 0, 177310, ''),
(13, 2, NULL, '2025-03-28', '2025-04-27', 80000, 15200, 0, 95200, ''),
(14, 2, NULL, '2025-03-28', '2025-04-27', 258000, 49020, 0, 307020, ''),
(15, 2, NULL, '2025-03-28', '2025-04-27', 167000, 31730, 0, 198730, ''),
(16, 2, NULL, '2025-03-28', '2025-04-27', 125000, 23750, 0, 148750, ''),
(17, 2, NULL, '2025-03-28', '2025-04-27', 224000, 42560, 0, 266560, ''),
(18, 2, NULL, '2025-03-28', '2025-04-27', 274000, 52060, 0, 326060, ''),
(19, 2, NULL, '2025-03-28', '2025-04-27', 174000, 33060, 0, 207060, ''),
(20, 2, NULL, '2025-03-28', '2025-04-27', 181000, 34390, 0, 215390, ''),
(21, 2, NULL, '2025-03-28', '2025-04-27', 500000, 95000, 0, 595000, ''),
(22, 2, NULL, '2025-03-28', '2025-04-27', 37000, 7030, 0, 44030, ''),
(23, 2, NULL, '2025-03-28', '2025-04-27', 117000, 22230, 0, 139230, ''),
(24, 2, NULL, '2025-04-07', '2025-05-07', 149000, 28310, 0, 177310, ''),
(25, 2, NULL, '2025-04-28', '2025-05-28', 24000, 1920, 4800, 21120, '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`idcarrito`),
  ADD KEY `idproducto` (`idproducto`),
  ADD KEY `iduser` (`iduser`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`idcategoria`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idproducto`),
  ADD KEY `idcategoria` (`idcategoria`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`iduser`),
  ADD UNIQUE KEY `nameuser` (`nameuser`);

--
-- Indices de la tabla `ventas_d`
--
ALTER TABLE `ventas_d`
  ADD PRIMARY KEY (`iddetalle`),
  ADD KEY `idventa` (`idventa`),
  ADD KEY `idproducto` (`idproducto`);

--
-- Indices de la tabla `ventas_t`
--
ALTER TABLE `ventas_t`
  ADD PRIMARY KEY (`idventa`),
  ADD KEY `iduser` (`iduser`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `idcarrito` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `idcategoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idproducto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1092;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `iduser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `ventas_d`
--
ALTER TABLE `ventas_d`
  MODIFY `iddetalle` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `ventas_t`
--
ALTER TABLE `ventas_t`
  MODIFY `idventa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `carrito_ibfk_1` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`),
  ADD CONSTRAINT `carrito_ibfk_2` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`idcategoria`) REFERENCES `categoria` (`idcategoria`);

--
-- Filtros para la tabla `ventas_d`
--
ALTER TABLE `ventas_d`
  ADD CONSTRAINT `ventas_d_ibfk_1` FOREIGN KEY (`idventa`) REFERENCES `ventas_t` (`idventa`),
  ADD CONSTRAINT `ventas_d_ibfk_2` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`);

--
-- Filtros para la tabla `ventas_t`
--
ALTER TABLE `ventas_t`
  ADD CONSTRAINT `ventas_t_ibfk_1` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

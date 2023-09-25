-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 14-08-2023 a las 05:44:13
-- Versión del servidor: 8.0.30
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdconsultorio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `id` int NOT NULL,
  `rfc` text NOT NULL,
  `nombre` text NOT NULL,
  `apellidos` text NOT NULL,
  `cedula` int NOT NULL,
  `correo` text NOT NULL,
  `contraseña` char(102) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `rol` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `medicos`
--

INSERT INTO `medicos` (`id`, `rfc`, `nombre`, `apellidos`, `cedula`, `correo`, `contraseña`, `rol`) VALUES
(1, 'RALA0107092T1', 'Alan Uriel', 'Ramirez Labastida', 121040722, 'alancanelo.11@gmail.com', 'pbkdf2:sha256:600000$CcwiIWR59QqP15yH$9d2ee3ccdc9f4954126be6df2ec58e4ae508efd3a621f9a49a8da41e9d9118ed', 1),
(12, 'RALA230913TR1', 'Luis Jael', 'Ramirez Pérez', 20030826, 'Luis.Perez@gmail.com', 'pbkdf2:sha256:600000$B7gwsRlrbQcYi0tA$1f452e91b9cf77181604fed699fa900a45a6fb1d116ec9629415ce2e39a7ff09', 2),
(13, 'SALO051226DA', 'Ximena', 'Sanchez López', 20051226, 'Ximena26@gmail.com', 'pbkdf2:sha256:600000$SZcvnVmLKZkHnLqe$ffe17419daa4c6bb0b1b784f4d674a1992c55ed76a1df7a3e3790e1830dadc95', 2),
(16, 'BABR030906DFR1', 'Jessica Alejandra', 'Barradas breton', 121040793, 'jessica.barradas@gmail.com', 'pbkdf2:sha256:600000$8lEx2hpwZB80tQhp$c22bc803e4027a119dabb249686a8773407f50bc5c35b6de5d0ec893d03c38f0', 1),
(17, 'BOLE010626T43', 'Jonathan Raul ', 'Bocanegra Leyva', 121039246, 'Jonathan.Leyva@gmail.com', 'pbkdf2:sha256:600000$9nJiBZmSx7QuvWGg$c6cfdbf0e8545ac3dcb2bc9658d6b4668150f4e441842e8a554e0e92c99802fd', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int NOT NULL,
  `cedulamedico` int NOT NULL,
  `nombre` text NOT NULL,
  `apellidos` text NOT NULL,
  `fechanacimiento` date NOT NULL,
  `enfermedades` text NOT NULL,
  `alergias` text NOT NULL,
  `antecedentes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id`, `cedulamedico`, `nombre`, `apellidos`, `fechanacimiento`, `enfermedades`, `alergias`, `antecedentes`) VALUES
(1, 121040722, 'Jesus Arturo', 'Resendiz Perés', '2001-12-09', 'Artritis', 'Ninguna', 'Ninguno'),
(2, 121040722, 'Joana Berenice', 'Labastida Muñoz', '1982-01-01', 'Ninguna', 'Ninguna', 'Ninguno'),
(3, 121040722, 'Ricardo Jesus', 'Sanchez Servin', '1998-07-12', 'Otra', 'Otro', 'Ninguno'),
(4, 121040722, 'Ricardo Jesus', 'Sanchez Servin', '1998-06-13', 'Ninguna', 'Otro', 'Ninguno'),
(5, 121040722, 'Ricardo Jesus', 'Sanchez Servin', '1998-06-13', 'Ninguna', 'Otro', 'Ninguno'),
(6, 121040722, 'Ricardo Jesus', 'Sanchez Servin', '1998-06-13', 'Ninguna', 'Otro', 'Ninguno'),
(7, 121040722, 'Joana Berenice', 'Labastida Muñoz', '1981-01-01', 'Ninguna', 'Otro', 'Ninguno');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int NOT NULL,
  `descripcion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `descripcion`) VALUES
(1, 'Administrador'),
(2, 'Usuarios');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rol` (`rol`),
  ADD KEY `cedula` (`cedula`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cedulamedico` (`cedulamedico`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `medicos`
--
ALTER TABLE `medicos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD CONSTRAINT `medicos_ibfk_1` FOREIGN KEY (`rol`) REFERENCES `roles` (`id_rol`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`cedulamedico`) REFERENCES `medicos` (`cedula`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-02-2020 a las 07:01:05
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 5.6.39

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `recursos_humanos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuncio`
--

CREATE TABLE `anuncio` (
  `IdAnunio` int(11) NOT NULL,
  `Titulo_del_Puesto` varchar(50) NOT NULL,
  `Fecha_de_Cierre` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `IdArea` int(11) NOT NULL,
  `Area_Descripcion` varchar(150) NOT NULL,
  `Area_Nombre` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- Error leyendo datos de la tabla recursos_humanos.area: #1064 - Algo está equivocado en su sintax cerca 'FROM `recursos_humanos`.`area`' en la linea 1

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato`
--

CREATE TABLE `candidato` (
  `CURP` int(18) NOT NULL,
  `RFC` varchar(13) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Domicilio` varchar(100) NOT NULL,
  `Telefono` int(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Sexo` char(2) NOT NULL,
  `Edad` tinyint(2) NOT NULL,
  `NSS` varchar(11) NOT NULL,
  `Fotografia` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `IdCarrera` int(11) NOT NULL,
  `Descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `IdContacto` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Email_de_Contacto` varchar(50) NOT NULL,
  `Numero_Telefonico` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_de_empresa`
--

CREATE TABLE `datos_de_empresa` (
  `Nom_Empresa` varchar(100) NOT NULL,
  `Descripcion` varchar(150) NOT NULL,
  `Estructura_Juridica` varchar(50) NOT NULL,
  `Razon_Social` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Domicilio` varchar(100) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `Encargado` varchar(50) NOT NULL,
  `CIF_de_Empresa` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_civil`
--

CREATE TABLE `estado_civil` (
  `IdEstado_civil` int(11) NOT NULL,
  `Descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `experiencia`
--

CREATE TABLE `experiencia` (
  `IdExperiencia` int(11) NOT NULL,
  `Nombre_de_empresa` varchar(50) NOT NULL,
  `Descripcion_del_puesto` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad`
--

CREATE TABLE `habilidad` (
  `IdHabilidad` int(11) NOT NULL,
  `Descripcion` varchar(150) NOT NULL,
  `Nivel` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idioma`
--

CREATE TABLE `idioma` (
  `IdIdioma` int(11) NOT NULL,
  `Lenguaje` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- Error leyendo datos de la tabla recursos_humanos.idioma: #1064 - Algo está equivocado en su sintax cerca 'FROM `recursos_humanos`.`idioma`' en la linea 1

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medio_publicidad`
--

CREATE TABLE `medio_publicidad` (
  `IdMedio_Publicidad` int(11) NOT NULL,
  `Descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel_academico`
--

CREATE TABLE `nivel_academico` (
  `IdNivel_Academico` int(11) NOT NULL,
  `Descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel_academico_has_candidato`
--

CREATE TABLE `nivel_academico_has_candidato` (
  `CURP` varchar(18) NOT NULL,
  `IdNIvel_Academico` int(11) NOT NULL,
  `IdCarrera` int(11) NOT NULL,
  `Institucion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel_idioma`
--

CREATE TABLE `nivel_idioma` (
  `IdNivel_idioma` int(11) NOT NULL,
  `Descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

CREATE TABLE `perfil` (
  `IdPerfil` int(11) NOT NULL,
  `Descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `IdPuesto` int(11) NOT NULL,
  `Descripcion` varchar(150) NOT NULL,
  `Salario_Anual` decimal(7,0) NOT NULL,
  `Beneficios` varchar(100) NOT NULL,
  `Bonos` decimal(7,0) NOT NULL,
  `N_Vacantes` int(11) NOT NULL,
  `N_Solicitantes` int(11) NOT NULL,
  `Plazas` int(11) NOT NULL,
  `Localizacion` decimal(50,0) NOT NULL,
  `Autorización` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_usuario`
--

CREATE TABLE `registro_usuario` (
  `IdUsuario` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Correo` varchar(60) NOT NULL,
  `Contraseña` varchar(20) NOT NULL,
  `Puesto` varchar(25) NOT NULL,
  `Descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultado_candidato`
--

CREATE TABLE `resultado_candidato` (
  `Estatus_Proceso` varchar(15) NOT NULL,
  `Comentarios` varchar(150) NOT NULL,
  `Comentarios_Oferta_Salario` varchar(150) NOT NULL,
  `Comentarios_Area_Seleccion` varchar(150) NOT NULL,
  `Examen_Psicometrico` varchar(150) NOT NULL,
  `Examen_Psicologico` varchar(150) NOT NULL,
  `Examen_Conocimiento` varchar(150) NOT NULL,
  `Examen_Salud` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud_de_candidato`
--

CREATE TABLE `solicitud_de_candidato` (
  `IdSolicitud_Candidato` int(11) NOT NULL,
  `Fecha_de_Solicitud` date NOT NULL,
  `Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud_de_puesto`
--

CREATE TABLE `solicitud_de_puesto` (
  `Id` int(11) NOT NULL,
  `Puesto` varchar(50) NOT NULL,
  `Vacantes` int(11) NOT NULL,
  `Fecha_Solicitud` date NOT NULL,
  `Fecha_Estatus` date NOT NULL,
  `Solicitantes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anuncio`
--
ALTER TABLE `anuncio`
  ADD PRIMARY KEY (`IdAnunio`);

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`IdArea`);

--
-- Indices de la tabla `candidato`
--
ALTER TABLE `candidato`
  ADD PRIMARY KEY (`CURP`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`IdCarrera`);

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`IdContacto`);

--
-- Indices de la tabla `estado_civil`
--
ALTER TABLE `estado_civil`
  ADD PRIMARY KEY (`IdEstado_civil`);

--
-- Indices de la tabla `experiencia`
--
ALTER TABLE `experiencia`
  ADD PRIMARY KEY (`IdExperiencia`);

--
-- Indices de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  ADD PRIMARY KEY (`IdHabilidad`);

--
-- Indices de la tabla `idioma`
--
ALTER TABLE `idioma`
  ADD PRIMARY KEY (`IdIdioma`);

--
-- Indices de la tabla `medio_publicidad`
--
ALTER TABLE `medio_publicidad`
  ADD PRIMARY KEY (`IdMedio_Publicidad`);

--
-- Indices de la tabla `nivel_academico`
--
ALTER TABLE `nivel_academico`
  ADD PRIMARY KEY (`IdNivel_Academico`);

--
-- Indices de la tabla `nivel_academico_has_candidato`
--
ALTER TABLE `nivel_academico_has_candidato`
  ADD PRIMARY KEY (`CURP`,`IdNIvel_Academico`,`IdCarrera`),
  ADD KEY `IdNIvel_Academico` (`IdNIvel_Academico`),
  ADD KEY `IdCarrera` (`IdCarrera`);

--
-- Indices de la tabla `nivel_idioma`
--
ALTER TABLE `nivel_idioma`
  ADD PRIMARY KEY (`IdNivel_idioma`);

--
-- Indices de la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD PRIMARY KEY (`IdPerfil`);

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`IdPuesto`);

--
-- Indices de la tabla `registro_usuario`
--
ALTER TABLE `registro_usuario`
  ADD PRIMARY KEY (`IdUsuario`);

--
-- Indices de la tabla `solicitud_de_candidato`
--
ALTER TABLE `solicitud_de_candidato`
  ADD PRIMARY KEY (`IdSolicitud_Candidato`);

--
-- Indices de la tabla `solicitud_de_puesto`
--
ALTER TABLE `solicitud_de_puesto`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anuncio`
--
ALTER TABLE `anuncio`
  MODIFY `IdAnunio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `area`
--
ALTER TABLE `area`
  MODIFY `IdArea` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `candidato`
--
ALTER TABLE `candidato`
  MODIFY `CURP` int(18) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `IdCarrera` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `IdContacto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estado_civil`
--
ALTER TABLE `estado_civil`
  MODIFY `IdEstado_civil` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `experiencia`
--
ALTER TABLE `experiencia`
  MODIFY `IdExperiencia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  MODIFY `IdHabilidad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `idioma`
--
ALTER TABLE `idioma`
  MODIFY `IdIdioma` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `medio_publicidad`
--
ALTER TABLE `medio_publicidad`
  MODIFY `IdMedio_Publicidad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `nivel_academico`
--
ALTER TABLE `nivel_academico`
  MODIFY `IdNivel_Academico` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `nivel_idioma`
--
ALTER TABLE `nivel_idioma`
  MODIFY `IdNivel_idioma` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `perfil`
--
ALTER TABLE `perfil`
  MODIFY `IdPerfil` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `IdPuesto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registro_usuario`
--
ALTER TABLE `registro_usuario`
  MODIFY `IdUsuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `solicitud_de_candidato`
--
ALTER TABLE `solicitud_de_candidato`
  MODIFY `IdSolicitud_Candidato` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `solicitud_de_puesto`
--
ALTER TABLE `solicitud_de_puesto`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `nivel_academico_has_candidato`
--
ALTER TABLE `nivel_academico_has_candidato`
  ADD CONSTRAINT `nivel_academico_has_candidato_ibfk_1` FOREIGN KEY (`IdNIvel_Academico`) REFERENCES `nivel_academico` (`IdNivel_Academico`),
  ADD CONSTRAINT `nivel_academico_has_candidato_ibfk_2` FOREIGN KEY (`IdCarrera`) REFERENCES `carrera` (`IdCarrera`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

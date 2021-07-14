-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 05 juil. 2021 à 20:56
-- Version du serveur :  8.0.21
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `eco`
--

-- --------------------------------------------------------

--
-- Structure de la table `commentaire`
--

DROP TABLE IF EXISTS `commentaire`;
CREATE TABLE IF NOT EXISTS `commentaire` (
  `Commentaire disponible` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `commentaire`
--

INSERT INTO `commentaire` (`Commentaire disponible`) VALUES
('Très belle application');

-- --------------------------------------------------------

--
-- Structure de la table `dechet`
--

DROP TABLE IF EXISTS `dechet`;
CREATE TABLE IF NOT EXISTS `dechet` (
  `IdDechet` int NOT NULL AUTO_INCREMENT,
  `volume` float NOT NULL,
  `IdImage` int NOT NULL,
  `IDTypeDechet` int NOT NULL,
  PRIMARY KEY (`IdDechet`),
  KEY `dechet_Image_FK` (`IdImage`),
  KEY `dechet_typededechet0_FK` (`IDTypeDechet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `image`
--

DROP TABLE IF EXISTS `image`;
CREATE TABLE IF NOT EXISTS `image` (
  `IdImage` int NOT NULL AUTO_INCREMENT,
  `Lien` varchar(500) NOT NULL,
  `LattitudeGps` float NOT NULL,
  `LongitudeGps` float NOT NULL,
  `DateAjout` date NOT NULL,
  `IdUtilisateur` int NOT NULL,
  PRIMARY KEY (`IdImage`),
  KEY `Image_utilisateur_FK` (`IdUtilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `typededechet`
--

DROP TABLE IF EXISTS `typededechet`;
CREATE TABLE IF NOT EXISTS `typededechet` (
  `IDTypeDechet` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(500) NOT NULL,
  `Dangerosite` varchar(500) NOT NULL,
  `Recyclabilite` tinyint(1) NOT NULL,
  PRIMARY KEY (`IDTypeDechet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `IdUtilisateur` int NOT NULL,
  `Nom` varchar(500) NOT NULL,
  `Prenom` varchar(500) NOT NULL,
  `Password` varchar(500) NOT NULL,
  PRIMARY KEY (`IdUtilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`IdUtilisateur`, `Nom`, `Prenom`, `Password`) VALUES
(202001, 'Ballou', 'Sary', 'Sary@'),
(202002, 'Colard', 'Nathalie', 'Colard@'),
(202003, 'Crecel', 'Jean', 'Crecel@'),
(202004, 'Kaboré', 'Cédric', 'Kabore@'),
(202005, 'Kandiah', 'Arthy', 'Kandiah@'),
(202006, 'Kouamé', 'Olivia', 'Kouamé@');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `dechet`
--
ALTER TABLE `dechet`
  ADD CONSTRAINT `dechet_Image_FK` FOREIGN KEY (`IdImage`) REFERENCES `image` (`IdImage`),
  ADD CONSTRAINT `dechet_typededechet0_FK` FOREIGN KEY (`IDTypeDechet`) REFERENCES `typededechet` (`IDTypeDechet`);

--
-- Contraintes pour la table `image`
--
ALTER TABLE `image`
  ADD CONSTRAINT `Image_utilisateur_FK` FOREIGN KEY (`IdUtilisateur`) REFERENCES `utilisateur` (`IdUtilisateur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

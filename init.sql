SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS pygame;
USE pygame;

CREATE TABLE `userdata` (
  `id` int(10) UNSIGNED NOT NULL,
  `base` varchar(7000) NOT NULL,
  `gold` int(11) NOT NULL,
  `elixir` int(11) NOT NULL,
  `tag` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `userdata`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `userdata`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;
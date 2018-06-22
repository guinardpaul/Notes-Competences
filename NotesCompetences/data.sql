/* ----------------------------------
    	Classes
   ---------------------------------- */
INSERT INTO gestion_classe (id, cycle, nom) VALUES
(1, "Cycle 3", "6_G1"),
(2, "Cycle 3", "6_G2"),
(3, "Cycle 3", "6_G3"),
(4, "Cycle 3", "6_G4"),
(5, "Cycle 3", "6_G5"),
(6, "Cycle 4", "5_G3"),
(7, "Cycle 4", "5_G4"),
(8, "Cycle 4", "301"),
(9, "Cycle 4", "302"),
(10, "Cycle 4", "303"),
(11, "Cycle 4", "304");

/* ----------------------------------
 		Eleves
  ---------------------------------- */
-- eleves de la classe 6_G5
INSERT INTO gestion_eleve (nom, prenom, classe_id) VALUES
("ALBERT", "Maël", 5),
("BELINGAND - - DURAN", "Pierre", 5),
("CARPENTIER", "Maïana", 5),
("CATALA - BAILLY", "Iloni", 5),
("CATALA-CARRIE", "Rose", 5),
("CHABBERT", "Simon", 5),
("COMBES", "Anaïs", 5),
("CROS - - CASANOVA", "Léa", 5),
("JAUZION", "Nicolas", 5),
("JOUSSERAND", "Julian", 5),
("LE CAM", "Eliot", 5),
("LOEILLET-CABANIS", "Eva", 5),
("NOEL", "Arsène", 5),
("POUSTHOMIS", "Sarah", 5),
("ROCACHER", "Lola", 5),
("SANS", "Célène", 5),
("SENEGAS", "Zia", 5),
("WINDEL", "Camille", 5),
("ZNIBER", "Maïa", 5);

/* ----------------------------------
	gestion_domaine - Compétence
  ----------------------------------
	CYCLE 3
  ---------------------------------- */
-- Domaine 1
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(1, "D1", "les langages mathématiques, scientifiques et informatique pour penser et communiquer.", "Cycle 3");
-- gestion_competence domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(2, "CT 1.1", "Savoir décrire des observations, expériences, hypothèses, conclusions en utilisant un vocabulaire précis.", "Cycle 3", 1),
(3, "CT 1.2", "Savoir exploiter un document constitué de divers supports (texte, schéma, graphique, tableau, algorithme simple).", "Cycle 3", 1),
(4, "CT 1.3", "Utiliser différents modes de représentation (texte, schéma, graphique, tableau, algorithme simple).", "Cycle 3", 1),
(5, "CT 1.4", "Expliquer un phénomène à l’oral et / ou à l’écrit.", "Cycle 3", 1),
(6, "CT 1.5", "Savoir créer un programme de construction.", "Cycle 3", 1),
(7, "CT 1.6", "Se repérer et se déplacer dans l’espace en utilisant ou en élaborant des représentations.", "Cycle 3", 1);

-- Domaine 2
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(8, "D2", "les méthodes et outils pour apprendre", "Cycle 3");
-- gestion_competence domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(9, "CT 2.1", "Utiliser des outils numériques pour communiquer des résultats en respectant les règles de base, enregistrement, intégration de médias, collaboration.", "Cycle 3", 8),
(10, "CT 2.2", "Utiliser des outils numériques pour simuler des phénomènes.", "Cycle 3", 8),
(11, "CT 2.3", "Utiliser des outils numériques pour représenter des objets techniques.", "Cycle 3", 8),
(12, "CT 2.4", "Choisir ou utiliser le matériel adapté pour mener une observation, effectuer une mesure, réaliser une expérience ou une production.  Utiliser les bonnes unités.", "Cycle 3", 8),
(13, "CT 2.5", "Organiser seul ou en groupe un espace de réalisation expérimentale.", "Cycle 3", 8),
(14, "CT 2.6", "Extraire les informations pertinentes d’un document et les mettre en relation pour répondre à une question.", "Cycle 3", 8),
(15, "CT 2.7", "Utiliser les outils mathématiques adaptés.", "Cycle 3", 8);

-- Domaine 3
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(16, "D3", "La formation de la personne et du citoyen", "Cycle 3");
-- gestion_competence domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(17, "CT 3.1", "Exprimer des émotions ressenties. Formuler une opinion, prendre de la distance avec celle-ci, la confronter à celle d'autrui et en discuter.", "Cycle 3", 16),
(18, "CT 3.2", "Relier des connaissances acquises en sciences et technologie à des questions de santé, de sécurité et d’environnement.", "Cycle 3", 16);

-- Domaine 4
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(19, "D4", "les systèmes naturels et les systèmes techniques", "Cycle 3");

-- Sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(20, "D4.1", "Pratiquer des démarches scientifiques et technologiques", "Cycle 3", 19);
-- gestion_competence domaine 4-sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(21, "CT 4.1", "Proposer avec l’aide du professeur, une démarche pour résoudre un problème ou répondre à une question de nature scientifique ou technologique.", "Cycle 3", 19),
(22, "CT 4.2", "Formuler une question ou une problématique scientifique ou technologique simple", "Cycle 3", 19),
(23, "CT 4.3", "Proposer une ou des hypothèses pour répondre à une question ou un problème", "Cycle 3", 19),
(24, "CT 4.4", "Proposer des expériences simples pour tester une hypothèse", "Cycle 3", 19),
(25, "CT 4.5", "Interpréter un résultat, en tirer une conclusion", "Cycle 3", 19),
(26, "CT 4.6", "Formaliser une partie de sa recherche sous une forme écrite ou orale.", "Cycle 3", 19);

-- Sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(27, "D4.2", "Conception, création, réalisation", "Cycle 3", 19);
-- gestion_competence domaine 4-sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(28, "CT 4.7", "Identifier les évolutions des besoins et des objets techniques dans leur contexte.", "Cycle 3", 19),
(29, "CT 4.8", "Identifier les principales familles de matériaux.", "Cycle 3", 19),
(30, "CT 4.9", "Décrire le fonctionnement d’objets techniques, leurs fonctions et leurs composants.", "Cycle 3", 19),
(31, "CT 4.10", "Réaliser en équipe tout ou une partie d’un objet technique répondant à un besoin.", "Cycle 3", 19);

-- Sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(32, "D4.3", "Mettre en pratique des comportements simples respectueux des autres, de l'environnement, de sa santé", "Cycle 3", 19);
-- gestion_competence domaine 4-sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(33, "CT 4.11", "Appliquer les consignes, respecter les règles relatives à la sécurité et au respect de la personne et de l'environnement.", "Cycle 3", 19);

-- domaine 5
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(34, "D5", "Mettre en pratique des comportements simples respectueux des autres, de l'environnement, de sa santé", "Cycle 3");
-- gestion_competence domaine 4-sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(35, "CT 5.1", "Distinguer un événement d'une durée, mesurer des durées.", "Cycle 3", 34),
(36, "CT 5.2", "Connaître et situer dans le temps de grandes périodes historiques et quelques événements", "Cycle 3", 34),
(37, "CT 5.3", "Elaborer un raisonnement et l'exprimer en utilisant des langages divers", "Cycle 3", 34);

/* ----------------------------------
	CYCLE 4
  ---------------------------------- */
-- domaine 1
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(40, "D1", "les langages mathématiques, scientifiques et informatique pour penser et communiquer.", "Cycle 4");
-- gestion_competence domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(41, "CT 1.1", "Décrire, en utilisant les outils et langages de descriptions adaptés, la structure et le comportement des objets.", "Cycle 4", 40),
(42, "CT 1.2", "Savoir exploiter un document constitué de divers supports (texte, schéma, graphique, tableau, algorithme simple).", "Cycle 4", 40),
(43, "CT 1.3", "Produire et utiliser différents modes de représentation (texte, schéma, graphique, tableau, algorithme simple).", "Cycle 4", 40),
(44, "CT 1.4", "Se repérer et se déplacer dans l’espace en utilisant ou en élaborant des représentations.", "Cycle 4", 40);

-- domaine 2
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(45, "D2", "les méthodes et outils pour apprendre", "Cycle 4");

-- sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(46, "D2.1", "Organiser son travail personnel", "Cycle 4", 45);
-- gestion_competence domaine 2 - sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(47, "CT 2.1", "Anticiper, gérer, planifier, se constituer des outils personnels.Utiliser des outils numériques pour communiquer des résultats en respectant les règles de base, enregistrement, intégration de médias, collaboration.", "Cycle 4", 45);

-- sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(48, "D2.2", "Coopération et réalisation de projet.", "Cycle 4", 45);
-- gestion_competence domaine 2 - sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(49, "CT 2.2", "Savoir gérer un projet", "Cycle 4", 45),
(50, "CT 2.3", "Utiliser des outils numériques", "Cycle 4", 45),
(51, "CT 2.4", "Traiter les informations collectées, construire des connaissances à partir des informations collectées.", "Cycle 4", 45),
(52, "CT 2.5", "Choisir ou utiliser le matériel adapté pour mener une observation, effectuer une mesure, réaliser une expérience ou une production.  Utiliser les bonnes unités.", "Cycle 4", 45),
(53, "CT 2.6", "Organiser seul ou en groupe un espace de réalisation expérimentale.", "Cycle 4", 45);

-- sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(54, "D2.3", "S’approprier des outils et méthodes", "Cycle 4", 45);
-- gestion_competence domaine 2 - sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(55, "CT 2.7", "Exprimer sa pensée à l’aide d’outils de description adaptés : croquis, schémas, graphes, diagrammes, tableaux (représentations non normées).", "Cycle 4", 45),
(56, "CT 2.8", "Présenter à l’oral et à l’aide de supports numériques multimédia des solutions techniques au moment des revues de projet.", "Cycle 4", 45);

-- domaine 3
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(57, "D3", "La formation de la personne et du citoyen", "Cycle 4");
-- gestion_competence domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(58, "CT 3.1", "Exprimer des émotions ressenties. Formuler une opinion, prendre de la distance avec celle-ci, la confronter à celle d\'autrui et en discuter.", "Cycle 4", 57),
(59, "CT 3.2", "Relier des connaissances acquises en sciences et technologie à des questions de santé, de sécurité et d’environnement.", "Cycle 4", 57),
(60, "CT 3.3", "Analyser l’impact environnemental d’un objet et de ses constituants.", "Cycle 4", 57),
(61, "CT 3.4", "Responsabilité, sens de l’engagement et de l’initiative.", "Cycle 4", 57);

-- domaine 4
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(62, "D4", "les systèmes naturels et les systèmes techniques", "Cycle 4");

-- sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(63, "D4.1", "Pratiquer des démarches scientifiques et technologiques", "Cycle 4", 62);
-- gestion_competence domaine 4 - sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(64, "CT 4.1", "Savoir mener une démarche d’investigation.", "Cycle 4", 62),
(65, "CT 4.2", "Communiquer des résultats.", "Cycle 4", 62),
(66, "CT 4.3", "Interpréter ses résultats et rédiger une conclusion.", "Cycle 4", 62),
(67, "CT 4.4", "Imaginer, synthétiser, formaliser et respecter une procédure, un protocole.", "Cycle 4", 62);

-- sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(68, "D4.2", "Pratiquer des démarches scientifiques et technologiques", "Cycle 4", 62);
-- gestion_competence domaine 4 - sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(69, "CT 4.5", "Appliquer les consignes, respecter les règles relatives à la sécurité et au respect de la personne et de l'environnement.", "Cycle 4", 62),
(70, "CT 4.6", "Savoir les relations entre fonctions biologiques et santé.", "Cycle 4", 62),
(71, "CT 4.7", "Connaitre corps humain, vivant, espèces.", "Cycle 4", 62),
(72, "CT 4.8", "Connaître univers, matière, biosphère.", "Cycle 4", 62),
(73, "CT 4.9", "Connaitre énergie, mouvement, force", "Cycle 4", 62);

-- domaine 5
INSERT INTO gestion_domaine (id, ref, description, cycle) VALUES
(74, "D5", "les représentations du monde et l'activité humaine", "Cycle 4");
-- gestion_competence domaine 5
INSERT INTO gestion_competence (id, ref, description, cycle, domaine_id) VALUES
(75, "CT 5.1", "L’espace et le temps : Identifier les enjeux du développement humain, appréhender les problématiques du développement humain.", "Cycle 4", 74),
(76, "CT 5.2", "Découvertes scientifiques et techniques.", "Cycle 4", 74),
(77, "CT 5.3", "Regrouper des objets en familles et lignées.", "Cycle 4", 74),
(78, "CT 5.4", "Relier les évolutions technologiques aux inventions et innovations qui marquent des ruptures dans les solutions techniques.", "Cycle 4", 74);


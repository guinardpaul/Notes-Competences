/* ----------------------------------
    	Cycle
   ---------------------------------- */
INSERT INTO gestion_enumcycle (id, literal, value) VALUES
(1, "Cycle 3", 1),
(2, "Cycle 4", 2);

/* ----------------------------------
    	Trimestre
   ---------------------------------- */
INSERT INTO resultat_enumtrimestre (id, literal, value) VALUES
(1, "Trimestre 1", 1),
(2, "Trimestre 2", 2),
(3, "Trimestre 3", 3);

/* ----------------------------------
    	Resultat
   ---------------------------------- */
INSERT INTO resultat_enumresultat (id, literal, value) VALUES
(1, "++", 1),
(2, "+", 2),
(3, "+/-", 3),
(4, "-", 4);

/* ----------------------------------
    	Classes
   ---------------------------------- */
INSERT INTO gestion_classe (id, cycle_id, nom) VALUES
(1, 1, "6_G1"),
(2, 1, "6_G2"),
(3, 1, "6_G3"),
(4, 1, "6_G4"),
(5, 1, "6_G5"),
(6, 2, "5_G3"),
(7, 2, "5_G4"),
(8, 2, "301"),
(9, 2, "302"),
(10, 2, "303"),
(11, 2, "304");

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
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(1, "D1", "les langages mathématiques, scientifiques et informatique pour penser et communiquer.", 1);
-- gestion_competence domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(2, "CT 1.1", "Savoir décrire des observations, expériences, hypothèses, conclusions en utilisant un vocabulaire précis.", 1, 1),
(3, "CT 1.2", "Savoir exploiter un document constitué de divers supports (texte, schéma, graphique, tableau, algorithme simple).", 1, 1),
(4, "CT 1.3", "Utiliser différents modes de représentation (texte, schéma, graphique, tableau, algorithme simple).", 1, 1),
(5, "CT 1.4", "Expliquer un phénomène à l’oral et / ou à l’écrit.", 1, 1),
(6, "CT 1.5", "Savoir créer un programme de construction.", 1, 1),
(7, "CT 1.6", "Se repérer et se déplacer dans l’espace en utilisant ou en élaborant des représentations.", 1, 1);

-- Domaine 2
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(8, "D2", "les méthodes et outils pour apprendre", 1);
-- gestion_competence domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(9, "CT 2.1", "Utiliser des outils numériques pour communiquer des résultats en respectant les règles de base, enregistrement, intégration de médias, collaboration.", 1, 8),
(10, "CT 2.2", "Utiliser des outils numériques pour simuler des phénomènes.", 1, 8),
(11, "CT 2.3", "Utiliser des outils numériques pour représenter des objets techniques.", 1, 8),
(12, "CT 2.4", "Choisir ou utiliser le matériel adapté pour mener une observation, effectuer une mesure, réaliser une expérience ou une production.  Utiliser les bonnes unités.", 1, 8),
(13, "CT 2.5", "Organiser seul ou en groupe un espace de réalisation expérimentale.", 1, 8),
(14, "CT 2.6", "Extraire les informations pertinentes d’un document et les mettre en relation pour répondre à une question.", 1, 8),
(15, "CT 2.7", "Utiliser les outils mathématiques adaptés.", 1, 8);

-- Domaine 3
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(16, "D3", "La formation de la personne et du citoyen", 1);
-- gestion_competence domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(17, "CT 3.1", "Exprimer des émotions ressenties. Formuler une opinion, prendre de la distance avec celle-ci, la confronter à celle d'autrui et en discuter.", 1, 16),
(18, "CT 3.2", "Relier des connaissances acquises en sciences et technologie à des questions de santé, de sécurité et d’environnement.", 1, 16);

-- Domaine 4
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(19, "D4", "les systèmes naturels et les systèmes techniques", 1);

-- Sous_domaine 1
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(20, "D4.1", "Pratiquer des démarches scientifiques et technologiques", 1, 19);
-- gestion_competence domaine 4-sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(21, "CT 4.1", "Proposer avec l’aide du professeur, une démarche pour résoudre un problème ou répondre à une question de nature scientifique ou technologique.", 1, 20),
(22, "CT 4.2", "Formuler une question ou une problématique scientifique ou technologique simple", 1, 20),
(23, "CT 4.3", "Proposer une ou des hypothèses pour répondre à une question ou un problème", 1, 20),
(24, "CT 4.4", "Proposer des expériences simples pour tester une hypothèse", 1, 20),
(25, "CT 4.5", "Interpréter un résultat, en tirer une conclusion", 1, 20),
(26, "CT 4.6", "Formaliser une partie de sa recherche sous une forme écrite ou orale.", 1, 20);

-- Sous_domaine 2
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(27, "D4.2", "Conception, création, réalisation", 1, 19);
-- gestion_competence domaine 4-sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(28, "CT 4.7", "Identifier les évolutions des besoins et des objets techniques dans leur contexte.", 1, 27),
(29, "CT 4.8", "Identifier les principales familles de matériaux.", 1, 27),
(30, "CT 4.9", "Décrire le fonctionnement d’objets techniques, leurs fonctions et leurs composants.", 1, 27),
(31, "CT 4.10", "Réaliser en équipe tout ou une partie d’un objet technique répondant à un besoin.", 1, 27);

-- Sous_domaine 3
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(32, "D4.3", "Mettre en pratique des comportements simples respectueux des autres, de l'environnement, de sa santé", 1, 19);
-- gestion_competence domaine 4-sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(33, "CT 4.11", "Appliquer les consignes, respecter les règles relatives à la sécurité et au respect de la personne et de l'environnement.", 1, 32);

-- domaine 5
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(34, "D5", "Mettre en pratique des comportements simples respectueux des autres, de l'environnement, de sa santé", 1);
-- gestion_competence domaine 4-sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(35, "CT 5.1", "Distinguer un événement d'une durée, mesurer des durées.", 1, 34),
(36, "CT 5.2", "Connaître et situer dans le temps de grandes périodes historiques et quelques événements", 1, 34),
(37, "CT 5.3", "Elaborer un raisonnement et l'exprimer en utilisant des langages divers", 1, 34);

/* ----------------------------------
	CYCLE 4
  ---------------------------------- */
-- domaine 1
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(40, "D1", "les langages mathématiques, scientifiques et informatique pour penser et communiquer.", 2);
-- gestion_competence domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(41, "CT 1.1", "Décrire, en utilisant les outils et langages de descriptions adaptés, la structure et le comportement des objets.", 2, 40),
(42, "CT 1.2", "Savoir exploiter un document constitué de divers supports (texte, schéma, graphique, tableau, algorithme simple).", 2, 40),
(43, "CT 1.3", "Produire et utiliser différents modes de représentation (texte, schéma, graphique, tableau, algorithme simple).", 2, 40),
(44, "CT 1.4", "Se repérer et se déplacer dans l’espace en utilisant ou en élaborant des représentations.", 2, 40);

-- domaine 2
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(45, "D2", "les méthodes et outils pour apprendre", 2);

-- sous_domaine 1
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(46, "D2.1", "Organiser son travail personnel", 2, 45);
-- gestion_competence domaine 2 - sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(47, "CT 2.1", "Anticiper, gérer, planifier, se constituer des outils personnels.Utiliser des outils numériques pour communiquer des résultats en respectant les règles de base, enregistrement, intégration de médias, collaboration.", 2, 46);

-- sous_domaine 2
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(48, "D2.2", "Coopération et réalisation de projet.", 2, 45);
-- gestion_competence domaine 2 - sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(49, "CT 2.2", "Savoir gérer un projet", 2, 48),
(50, "CT 2.3", "Utiliser des outils numériques", 2, 48),
(51, "CT 2.4", "Traiter les informations collectées, construire des connaissances à partir des informations collectées.", 2, 48),
(52, "CT 2.5", "Choisir ou utiliser le matériel adapté pour mener une observation, effectuer une mesure, réaliser une expérience ou une production.  Utiliser les bonnes unités.", 2, 48),
(53, "CT 2.6", "Organiser seul ou en groupe un espace de réalisation expérimentale.", 2, 48);

-- sous_domaine 3
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(54, "D2.3", "S’approprier des outils et méthodes", 2, 45);
-- gestion_competence domaine 2 - sous_domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(55, "CT 2.7", "Exprimer sa pensée à l’aide d’outils de description adaptés : croquis, schémas, graphes, diagrammes, tableaux (représentations non normées).", 2, 54),
(56, "CT 2.8", "Présenter à l’oral et à l’aide de supports numériques multimédia des solutions techniques au moment des revues de projet.", 2, 54);

-- domaine 3
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(57, "D3", "La formation de la personne et du citoyen", 2);
-- gestion_competence domaine 3
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(58, "CT 3.1", "Exprimer des émotions ressenties. Formuler une opinion, prendre de la distance avec celle-ci, la confronter à celle d\'autrui et en discuter.", 2, 57),
(59, "CT 3.2", "Relier des connaissances acquises en sciences et technologie à des questions de santé, de sécurité et d’environnement.", 2, 57),
(60, "CT 3.3", "Analyser l’impact environnemental d’un objet et de ses constituants.", 2, 57),
(61, "CT 3.4", "Responsabilité, sens de l’engagement et de l’initiative.", 2, 57);

-- domaine 4
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(62, "D4", "les systèmes naturels et les systèmes techniques", 2);

-- sous_domaine 1
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(63, "D4.1", "Pratiquer des démarches scientifiques et technologiques", 2, 62);
-- gestion_competence domaine 4 - sous_domaine 1
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(64, "CT 4.1", "Savoir mener une démarche d’investigation.", 2, 63),
(65, "CT 4.2", "Communiquer des résultats.", 2, 63),
(66, "CT 4.3", "Interpréter ses résultats et rédiger une conclusion.", 2, 63),
(67, "CT 4.4", "Imaginer, synthétiser, formaliser et respecter une procédure, un protocole.", 2, 63);

-- sous_domaine 2
INSERT INTO gestion_domaine (id, ref, description, cycle_id, sous_domaine_id) VALUES
(68, "D4.2", "Pratiquer des démarches scientifiques et technologiques", 2, 62);
-- gestion_competence domaine 4 - sous_domaine 2
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(69, "CT 4.5", "Appliquer les consignes, respecter les règles relatives à la sécurité et au respect de la personne et de l'environnement.", 2, 68),
(70, "CT 4.6", "Savoir les relations entre fonctions biologiques et santé.", 2, 68),
(71, "CT 4.7", "Connaitre corps humain, vivant, espèces.", 2, 68),
(72, "CT 4.8", "Connaître univers, matière, biosphère.", 2, 68),
(73, "CT 4.9", "Connaitre énergie, mouvement, force", 2, 68);

-- domaine 5
INSERT INTO gestion_domaine (id, ref, description, cycle_id) VALUES
(74, "D5", "les représentations du monde et l'activité humaine", 2);
-- gestion_competence domaine 5
INSERT INTO gestion_competence (id, ref, description, cycle_id, domaine_id) VALUES
(75, "CT 5.1", "L’espace et le temps : Identifier les enjeux du développement humain, appréhender les problématiques du développement humain.", 2, 74),
(76, "CT 5.2", "Découvertes scientifiques et techniques.", 2, 74),
(77, "CT 5.3", "Regrouper des objets en familles et lignées.", 2, 74),
(78, "CT 5.4", "Relier les évolutions technologiques aux inventions et innovations qui marquent des ruptures dans les solutions techniques.", 2, 74);

#=====SC SEND BY > KALYAN KING
#=====TELIGERM :, OX CYBER TEAM
import os, re, time, json, random, threading
import requests
from faker import Faker
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from datetime import datetime
from rich import print 
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt

# Global name pools (will be initialized on first use)
_name_pools = {
    'filipino_male_first': [],
    'filipino_female_first': [],
    'filipino_last': [],
    'rpw_male_first': [],
    'rpw_female_first': [],
    'rpw_last': []
}

FILIPINO_FIRST_NAMES_MALE = [
    'Juan', 'Jose', 'Miguel', 'Gabriel', 'Rafael', 'Antonio', 'Carlos', 'Luis',
    'Marco', 'Paolo', 'Angelo', 'Joshua', 'Christian', 'Mark', 'John', 'James',
    'Daniel', 'David', 'Michael', 'Jayson', 'Kenneth', 'Ryan', 'Kevin', 'Neil',
    'Jerome', 'Renzo', 'Carlo', 'Andres', 'Felipe', 'Diego', 'Mateo', 'Lucas',
    'Adrian', 'Albert', 'Aldrin', 'Alfred', 'Allen', 'Alonzo', 'Amiel',
    'Andre', 'Andrew', 'Angelo', 'Anton', 'Arden', 'Aries', 'Arman', 'Arnel',
    'Arnold', 'Arthur', 'August', 'Avery', 'Benito', 'Benjamin', 'Bernard',
    'Blake', 'Bryan', 'Bryant', 'Caleb', 'Cameron', 'Cedric', 'Cesar',
    'Charles', 'Christianne', 'Clarence', 'Clark', 'Clint', 'Clyde', 'Colin',
    'Conrad', 'Crispin', 'Cyril', 'Damian', 'Darrel', 'Daryl', 'Darren',
    'Dean', 'Denver', 'Derrick', 'Dexter', 'Dominic', 'Dylan', 'Earl', 'Edgar',
    'Edison', 'Edward', 'Edwin', 'Eli', 'Elias', 'Elijah', 'Emil', 'Emmanuel',
    'Eric', 'Ernest', 'Eron', 'Ethan', 'Eugene', 'Ferdinand', 'Francis',
    'Frank', 'Fred', 'Frederick', 'Galen', 'Garry', 'Genesis', 'Geo', 'Gerald',
    'Gilbert', 'Giovanni', 'Greg', 'Gregory', 'Hans', 'Harold', 'Henry',
    'Hugh', 'Ian', 'Iñigo', 'Irvin', 'Isaac', 'Ivan', 'Jake', 'Jared',
    'Jarred', 'Jason', 'Jasper', 'Jay', 'Jayden', 'Jerald', 'Jericho',
    'Jethro', 'Jimmy', 'Joel', 'Jonas', 'Jonathan', 'Jordan', 'Joseph',
    'Julius', 'Justin', 'Karl', 'Kayden', 'Keith', 'Kelvin', 'Kiel', 'King',
    'Kirk', 'Kyle', 'Lance', 'Larry', 'Lawrence', 'Leandro', 'Leo', 'Leonard',
    'Levi', 'Liam', 'Lorenzo', 'Louie', 'Lucas', 'Lucio', 'Luisito', 'Macario',
    'Malcolm', 'Marcus', 'Mario', 'Martin', 'Marvin', 'Matthew', 'Max',
    'Melvin', 'Mico', 'Miguelito', 'Milan', 'Mitch', 'Nathan', 'Nathaniel',
    'Neilson', 'Nelson', 'Nicholas', 'Nico', 'Noel', 'Norman', 'Oliver',
    'Oscar', 'Owen', 'Patrick', 'Paulo', 'Peter', 'Philip', 'Pierre', 'Ralph',
    'Randall', 'Raymond', 'Reagan', 'Reggie', 'Rein', 'Reiner', 'Ricardo',
    'Rico', 'Riel', 'Robbie', 'Robert', 'Rodney', 'Roldan', 'Romeo', 'Ronald',
    'Rowell', 'Russell', 'Ryanne', 'Sam', 'Samuel', 'Santino', 'Sean', 'Seth',
    'Shawn', 'Simon', 'Stephen', 'Steven', 'Taylor', 'Terrence', 'Theo',
    'Timothy', 'Tomas', 'Tristan', 'Troy', 'Tyler', 'Vernon', 'Victor',
    'Vincent', 'Virgil', 'Warren', 'Wayne', 'Wilfred', 'William', 'Winston',
    'Wyatt', 'Xander', 'Zachary', 'Zion', 'Arvin', 'Dion', 'Harvey', 'Irvin',
    'Jeriel', 'Kennard', 'Levin', 'Randel', 'Ramil', 'Rendon', 'Rome', 'Roven',
    'Silas', 'Tobias', 'Uriel', 'Zandro', 'Axl', 'Brysen', 'Ced', 'Clarkson',
    'Deo', 'Eion', 'Errol', 'Franco', 'Gavin', 'Hansel', 'Isidro', 'Jiro',
    'Kiel', 'Loren', 'Matteo', 'Noelito', 'Omar', 'Paxton', 'Quinn', 'Ramon',
    'Renz', 'Sandy', 'Tyrone', 'Ulrich', 'Vince', 'Wesley', 'Yvan', 'Zed',
    'Alric', 'Brent', 'Caden', 'Dionel', 'Ethaniel', 'Fritz', 'Gerson',
    'Hansley', 'Ivar', 'Jeric', 'Kenzo', 'Lex', 'Morris', 'Nate', 'Orville',
    'Pio', 'Quentin', 'Rydel', 'Sergio', 'Tobit', 'Ulysses', 'Val', 'Wade',
    'Yohan', 'Zyren', 'Adley', 'Cairo', 'Drey', 'Enzo', 'Ferris', 'Gale',
    'Hector', 'Iven', 'Jaycee', 'Kaleb', 'Lyndon', 'Macky', 'Nash', 'Oren',
    'Pierce', 'Quino', 'Rustin', 'Sylvio', 'Tanner', 'Ulian', 'Vaughn',
    'Weston', 'Xeno', 'Yuri', 'Zandro', 'Andro', 'Basil', 'Crisanto', 'Derris',
    'Efrain', 'Florenz', 'Gael', 'Hanz', 'Ismael', 'Jeromey', 'Kielan',
    'Lucian', 'Marlo', 'Nerio', 'Osric', 'Patrik', 'Rion', 'Santino', 'Timo',
    'Vin', 'Wilmer', 'Zaim', 'Zen'
]

FILIPINO_FIRST_NAMES_FEMALE = [
    'Maria', 'Ana', 'Sofia', 'Isabella', 'Gabriela', 'Valentina', 'Camila',
    'Angelica', 'Nicole', 'Michelle', 'Christine', 'Sarah', 'Jessica',
    'Andrea', 'Patricia', 'Jennifer', 'Karen', 'Ashley', 'Jasmine', 'Princess',
    'Angel', 'Joyce', 'Kristine', 'Diane', 'Joanna', 'Carmela', 'Isabel',
    'Lucia', 'Elena', 'Abigail', 'Adeline', 'Adrienne', 'Agnes', 'Aileen', 'Aira', 'Aiza',
    'Alana', 'Alexa', 'Alexis', 'Alice', 'Allyson', 'Alyssa', 'Amara',
    'Amelia', 'Amirah', 'Anabelle', 'Anastasia', 'Andrea', 'Angela', 'Angelie',
    'Angelyn', 'Anita', 'Annabelle', 'Anne', 'Annie', 'Antoinette', 'April',
    'Ariana', 'Arlene', 'Aubrey', 'Audrey', 'Aurora', 'Ava', 'Bea', 'Bella',
    'Bernadette', 'Bianca', 'Blessy', 'Brianna', 'Bridget', 'Carla', 'Carmel',
    'Cassandra', 'Catherine', 'Cecilia', 'Celeste', 'Charisse', 'Charlene',
    'Charlotte', 'Chelsea', 'Cherry', 'Cheska', 'Clarice', 'Claudia', 'Coleen',
    'Colleen', 'Cristina', 'Cynthia', 'Dahlia', 'Danica', 'Daniela',
    'Danielle', 'Darlene', 'Diana', 'Dominique', 'Donna', 'Dorothy', 'Eden',
    'Elaine', 'Eleanor', 'Elisa', 'Eliza', 'Ella', 'Ellen', 'Eloisa', 'Elsa',
    'Emerald', 'Emily', 'Emma', 'Erica', 'Erin', 'Esme', 'Eunice', 'Faith',
    'Fatima', 'Felice', 'Flor', 'Frances', 'Francesca', 'Genevieve', 'Georgia',
    'Gillian', 'Giselle', 'Glenda', 'Grace', 'Gretchen', 'Gwen', 'Hailey',
    'Hannah', 'Hazel', 'Heather', 'Heidi', 'Helen', 'Helena', 'Hope', 'Iana',
    'Irene', 'Irish', 'Isabelle', 'Ivana', 'Ivory', 'Jacqueline', 'Jamie',
    'Jane', 'Janella', 'Janet', 'Janine', 'Janna', 'Jasmine', 'Jean',
    'Jeanine', 'Jem', 'Jenica', 'Jessa', 'Jillian', 'Joan', 'Joanna', 'Joanne',
    'Jocelyn', 'Jolina', 'Joy', 'Judith', 'Julia', 'Julianne', 'Juliet',
    'Justine', 'Kaila', 'Kaitlyn', 'Karen', 'Karina', 'Kate', 'Katrina',
    'Kayla', 'Keira', 'Kendra', 'Kim', 'Kimberly', 'Krisha', 'Krista',
    'Krystel', 'Kyla', 'Kylie', 'Lara', 'Larissa', 'Laura', 'Lauren', 'Lea',
    'Leanne', 'Lena', 'Leslie', 'Lexi', 'Lianne', 'Liza', 'Lorraine', 'Louisa',
    'Louise', 'Lovely', 'Lucille', 'Luna', 'Lyndsay', 'Lyra', 'Mae', 'Maggie',
    'Maja', 'Mandy', 'Marcia', 'Margaret', 'Marian', 'Mariel', 'Marilyn',
    'Marina', 'Marissa', 'Marites', 'Martha', 'Mary', 'Matilda', 'Maureen',
    'Maxine', 'May', 'Megan', 'Melissa', 'Mia', 'Mika', 'Mikayla', 'Mila',
    'Mira', 'Miranda', 'Mirella', 'Monica', 'Nadia', 'Naomi', 'Natalie',
    'Nathalie', 'Nerissa', 'Nika', 'Nina', 'Nora', 'Norma', 'Olivia',
    'Ophelia', 'Pamela', 'Patricia', 'Paula', 'Pauline', 'Pearl', 'Phoebe',
    'Pia', 'Precious', 'Queenie', 'Quiana', 'Rachelle', 'Rae', 'Rain', 'Raisa',
    'Ramona', 'Raven', 'Reina', 'Rhea', 'Rica', 'Richelle', 'Rina', 'Rochelle',
    'Rosa', 'Rosalie', 'Roseanne', 'Rowena', 'Ruth', 'Sabrina', 'Samantha',
    'Samira', 'Sandra', 'Sara', 'Selene', 'Serena', 'Shaira', 'Shaina',
    'Shanelle', 'Shanika', 'Sharon', 'Sheena', 'Sheila', 'Sherlyn', 'Shiela',
    'Shirley', 'Siena', 'Sierra', 'Sofia', 'Sophia', 'Steffany', 'Stephanie',
    'Summer', 'Susan', 'Suzette', 'Sylvia', 'Tanya', 'Tara', 'Tatiana',
    'Tessa', 'Thea', 'Theresa', 'Trisha', 'Trista', 'Valeria', 'Vanessa',
    'Veronica', 'Vicky', 'Victoria', 'Vina', 'Vivian', 'Wendy',
    'Whitney', 'Yasmin', 'Ysabel', 'Yvette', 'Yvonne', 'Zara', 'Zelda', 'Zia',
    'Zoe', 'Althea', 'Arya', 'Beatriz', 'Czarina', 'Dayanara', 'Elora',
    'Fiona', 'Gianna', 'Helena', 'Indira', 'Janine', 'Kalista', 'Larraine',
    'Maeve', 'Noelle', 'Odessa', 'Patrina', 'Rowan', 'Selina', 'Tahlia', 'Una',
    'Vienna', 'Willow', 'Xandra', 'Yanna', 'Zyra'
]

FILIPINO_LAST_NAMES = [
    'Santos', 'Reyes', 'Cruz', 'Bautista', 'Ocampo', 'Garcia', 'Mendoza', 'Torres',
    'Tomas', 'Andrada', 'Sarmiento', 'Villanueva', 'Ramos', 'Castro', 'Pineda',
    'Abad', 'Abueva', 'Agoncillo', 'Aguinaldo', 'Alcasid', 'Almazan', 'Alvarez',
    'Amorsolo', 'Andres', 'Angeles', 'Antonio', 'Aquino', 'Aragon', 'Aranas',
    'Arellano', 'Arnaiz', 'Asis', 'Atienza', 'Avelino', 'Ayala', 'Bacani',
    'Bagatsing', 'Balagtas', 'Baltazar', 'Banuelos', 'Barredo', 'Barrios',
    'Basilio', 'Batungbakal', 'Belmonte', 'Benitez', 'Bernardo', 'Blanco',
    'Bonifacio', 'Borja', 'Buenaventura', 'Buencamino', 'Bumanlag', 'Burgos',
    'Caballero', 'Cabañero', 'Cabrera', 'Cadsawan', 'Calaguas', 'Calderon',
    'Calungsod', 'Camacho', 'Canlas', 'Caparas', 'Capinpin', 'Carpio',
    'Carrasco', 'Casas', 'Castañeda', 'Castillo', 'Cayetano', 'Cervantes',
    'Chavez', 'Chu', 'Claudio', 'Cojuangco', 'Concepcion', 'Constantino',
    'Coronel', 'Corpuz', 'Cortez', 'Crisostomo', 'Cuenco', 'Cunanan', 'Custodio',
    'Dagohoy', 'Dandan', 'Datu', 'David', 'Dayrit', 'De Castro', 'De Guzman',
    'De Jesus', 'De Leon', 'De Mesa', 'De Vera', 'Del Mar', 'Del Pilar',
    'Del Rosario', 'Dela Cruz', 'Dela Fuente', 'Dela Rosa', 'Delgado', 'Diokno',
    'Dizon', 'Domingo', 'Dulay', 'Dumlao', 'Dy', 'Eala', 'Echiverri', 'Ejercito',
    'Enrile', 'Enriquez', 'Escaler', 'Escano', 'Escudero', 'Esguerra', 'Espina',
    'Espino', 'Espinosa', 'Espiritu', 'Estanislao', 'Estrada', 'Estrella',
    'Evangelista', 'Fabella', 'Fajardo', 'Faustino', 'Feliciano', 'Fernandez',
    'Ferrer', 'Florentino', 'Flores', 'Fonacier', 'Fontanilla', 'Francisco',
    'Gaddi', 'Galan', 'Galang', 'Gallardo', 'Galvan', 'Galvez', 'Gamboa',
    'Ganzon', 'Gapud', 'Garcellano', 'Gatchalian', 'Gatmaitan', 'Gaza', 'Geronimo',
    'Go', 'Gomez', 'Gonzaga', 'Gonzales', 'Gosiengfiao', 'Gotianun', 'Guerrero',
    'Guevarra', 'Guingona', 'Guinto', 'Gutierrez', 'Guzman', 'Henares', 'Henson',
    'Hermosa', 'Hernandez', 'Herrera', 'Hidalgo', 'Hizon', 'Honasan', 'Ibañez',
    'Ignacio', 'Ilagan', 'Imperial', 'Infante', 'Inocencio', 'Iñiguez', 'Isidro',
    'Jacinto', 'Jalandoni', 'Jao', 'Jara', 'Javier', 'Jimenez', 'Joaquin',
    'Jocson', 'Jose', 'Joson', 'Jovellanos', 'Juan', 'Juico', 'Kalaw', 'Katigbak',
    'Kho', 'Kintanar', 'Lacanilao', 'Lacson', 'Ladia', 'Lagman', 'Laguio',
    'Lampa', 'Lanuza', 'Lao', 'Lapid', 'Lapus', 'Laurel', 'Lava', 'Lazaro',
    'Ledesma', 'Legarda', 'Legaspi', 'Leoncio', 'Leonen', 'Lim', 'Liñan',
    'Lising', 'Liwanag', 'Llamas', 'Locsin', 'Lontoc', 'Lopez', 'Lorenzana',
    'Lorenzo', 'Loyola', 'Lozada', 'Lucero', 'Luciano', 'Lugtu', 'Luna',
    'Mabini', 'Macapagal', 'Macaraig', 'Magsaysay', 'Makalintal', 'Maliksi',
    'Malvar', 'Manahan', 'Manalac', 'Manalo', 'Manankil', 'Manglapus', 'Manicad',
    'Maningat', 'Maniquis', 'Manzano', 'Mapa', 'Maramba', 'Marasigan', 'Marcos',
    'Mariano', 'Marquez', 'Martinez', 'Masangkay', 'Mateo', 'Matias', 'Maturan',
    'Mañalac', 'Medalla', 'Medina', 'Melchor', 'Mercado', 'Miranda', 'Mitra',
    'Mojares', 'Molina', 'Monasterio', 'Montano', 'Monteclaro', 'Montelibano',
    'Montenegro', 'Montero', 'Montilla', 'Montinola', 'Morales', 'Moreno',
    'Mutuc', 'Nakpil', 'Nalupta', 'Narciso', 'Nava', 'Navarro', 'Nepomuceno',
    'Neri', 'Nicolas', 'Nieto', 'Noble', 'Nolasco', 'Ocampo', 'Ople', 'Orbos',
    'Ordonez', 'Oreita', 'Orosa', 'Ortigas', 'Osmeña', 'Ozamiz', 'Paderanga',
    'Padilla', 'Pagulayan', 'Paguia', 'Palanca', 'Palma', 'Panganiban',
    'Pangilinan', 'Panlilio', 'Pantaleon', 'Paraiso', 'Pardo', 'Pascual',
    'Pastor', 'Paterno', 'Pecson', 'Pelayo', 'Peña', 'Peralta', 'Perez',
    'Pernia', 'Pestaño', 'Pimentel', 'Pinlac', 'Placido', 'Platon', 'Poblador',
    'Poe', 'Ponce', 'Posadas', 'Prado', 'Pua', 'Puno', 'Punsalan', 'Puyat',
    'Que', 'Quezon', 'Quiazon', 'Quirino', 'Quisumbing', 'Quito', 'Ramirez',
    'Ramos', 'Razon', 'Recto', 'Regalado', 'Relosa', 'Resurreccion', 'Revilla',
    'Rey', 'Reynes', 'Ricahuerta', 'Ricarte', 'Rivera', 'Robledo', 'Robles',
    'Roces', 'Rodriguez', 'Rojo', 'Roldan', 'Romero', 'Romualdez', 'Romulo',
    'Roño', 'Roque', 'Rosales', 'Rosario', 'Roxas', 'Rubio', 'Rufino', 'Ruiz',
    'Sabalvaro', 'Sabido', 'Sacay', 'Salas', 'Salazar', 'Salcedo', 'Salgado',
    'Salonga', 'Salvador', 'Samonte', 'San Agustin', 'San Jose', 'San Juan',
    'San Pedro', 'Sanchez', 'Sandico', 'Sandejas', 'Sanguila', 'Santiago',
    'Santillan', 'Sanz', 'Sebastian', 'Segovia', 'Sempio', 'Seneres', 'Seno',
    'Serna', 'Sevilla', 'Sia', 'Sian', 'Sibal', 'Siguion-Reyna', 'Silang',
    'Silverio', 'Singson', 'Siochi', 'Sioson', 'Sison', 'Siy', 'Soler',
    'Soliman', 'Sotto', 'Sta. Maria', 'Sta. Romana', 'Suarez', 'Sumulong',
    'Sunico', 'Sy', 'Syjuco', 'Syquia', 'Tabuena', 'Tadiar', 'Tagle', 'Tamano',
    'Tan', 'Tancinco', 'Tanco', 'Tanjuatco', 'Tantoco', 'Tañada', 'Tayag',
    'Teodoro', 'Teves', 'Tinio', 'Tirol', 'Tirona', 'Tolentino', 'Tordesillas',
    'Torno', 'Trillanes', 'Trinidad', 'Tuason', 'Tugade', 'Tumbokon', 'Tungol',
    'Ty', 'Umali', 'Unas', 'Ungson', 'Uy', 'Valdez', 'Valencia', 'Valenciano',
    'Valenzuela', 'Valera', 'Valeroso', 'Varela', 'Vargas', 'Velasco',
    'Veloso', 'Ventura', 'Vergel', 'Vergara', 'Vibal', 'Vicencio', 'Victorino',
    'Villacorta', 'Villafuerte', 'Villalon', 'Villamor', 'Villareal',
    'Villarosa', 'Villavicencio', 'Villegas', 'Vinluan', 'Virata', 'Vitug',
    'Yabut', 'Yanga', 'Yanson', 'Yap', 'Ybañez', 'Yee', 'Yenko', 'Yonzon',
    'Yulo', 'Yusay', 'Yuson', 'Yuzon', 'Zabala', 'Zaide', 'Zaldivar', 'Zamora',
    'Zandueta', 'Zapanta', 'Zaragoza', 'Zerrudo', 'Zialcita', 'Zobel', 'Zosa', 'Zulueta'
]

RPW_FIRST_NAMES_MALE = [
    'Aries', 'Asher', 'Axel', 'Azrael', 'Blade', 'Blaze', 'Caden', 'Caleb',
    'Castiel', 'Dante', 'Darius', 'Dash', 'Drake', 'Elias', 'Enzo', 'Ezra',
    'Felix', 'Finn', 'Gael', 'Gideon', 'Griffin', 'Hunter', 'Jax', 'Jett',
    'Jude', 'Kai', 'Kaleb', 'Killian', 'Klaus', 'Knox', 'Kylo', 'Leo',
    'Levi', 'Liam', 'Luca', 'Lucas', 'Maddox', 'Malachi', 'Milo', 'Nico',
    'Noah', 'Oliver', 'Orion', 'Oscar', 'Owen', 'Pax', 'Phoenix', 'Quinn',
    'Rafael', 'Reed', 'Remy', 'Rhet', 'River', 'Rocco', 'Roman', 'Rowan',
    'Ryder', 'Ryker', 'Sawyer', 'Sebastian', 'Seth', 'Silas', 'Soren', 'Stellan',
    'Talon', 'Thatcher', 'Theo', 'Titan', 'Tobias', 'Tristan', 'Troy', 'Tybalt',
    'Uriel', 'Vance', 'Vaughn', 'Victor', 'Vincenzo', 'Vito', 'Weston', 'Wilder',
    'Wyatt', 'Xander', 'Xavier', 'Xeno', 'Yael', 'Yosef', 'Yuri', 'Zade',
    'Zane', 'Zavier', 'Zayn', 'Zeke', 'Zenith', 'Zephyr', 'Zion', 'Zoran'
]

RPW_FIRST_NAMES_FEMALE = [
    'Adelaide', 'Allegra', 'Amara', 'Amira', 'Aria', 'Artemis', 'Aspen', 'Aster',
    'Athena', 'Aubrey', 'Aurora', 'Ayla', 'Azalea', 'Bella', 'Bianca', 'Blair',
    'Briar', 'Callie', 'Calliope', 'Cassandra', 'Celeste', 'Celine', 'Cleo', 'Cora',
    'Dahlia', 'Daphne', 'Delilah', 'Demi', 'Elowen', 'Elsa', 'Ember', 'Esme',
    'Evangeline', 'Eve', 'Everly', 'Faye', 'Felicity', 'Fiona', 'Freya', 'Gia',
    'Giselle', 'Gwen', 'Harlow', 'Hazel', 'Hera', 'Iris', 'Isla', 'Ivy',
    'Jade', 'Jasmine', 'Juno', 'Kaia', 'Kira', 'Lana', 'Lark', 'Layla',
    'Leila', 'Lexi', 'Lilah', 'Luna', 'Lyra', 'Mabel', 'Maeve', 'Maya',
    'Mila', 'Mira', 'Nadia', 'Naomi', 'Nora', 'Nova', 'Nyx', 'Olive',
    'Ophelia', 'Paige', 'Pandora', 'Pearl', 'Penelope', 'Phoebe', 'Piper', 'Quinn',
    'Rain', 'Raven', 'Rhea', 'River', 'Rosalie', 'Rowan', 'Ruby', 'Saffron',
    'Sage', 'Scarlett', 'Selene', 'Seraphina', 'Sienna', 'Skye', 'Sloane', 'Stella',
    'Talia', 'Thea', 'Tiana', 'Veda', 'Vera', 'Vienna', 'Violet', 'Willow',
    'Wren', 'Xanthe', 'Xara', 'Xena', 'Yara', 'Yuna', 'Ysabel', 'Zara',
    'Zelda', 'Zia', 'Zoe', 'Zola', 'Zora', 'Zoya', 'Zuri', 'Zyra'
]

RPW_LAST_NAMES = [
    'Abeleda', 'Agpaoa', 'Almaden', 'Amistad', 'Aragon', 'Asuncion', 'Aurelio', 'Azcueta',
    'Balagtas', 'Banal', 'Baron', 'Basco', 'Belen', 'Belmonte', 'Benitez', 'Bernas',
    'Blanco', 'Bolante', 'Braganza', 'Briones', 'Buencamino', 'Cabañero', 'Cabreza', 'Calderon',
    'Camat', 'Cancino', 'Caparas', 'Cardona', 'Casiño', 'Castillo', 'Catacutan', 'Centeno',
    'Claravall', 'Claudio', 'Coronel', 'Cortes', 'Crisologo', 'Cuenca', 'Dacanay', 'Dancel',
    'Datumanong', 'De Guia', 'De Mesa', 'De Vera', 'Del Fierro', 'Dela Riva', 'Diamante', 'Diego',
    'Dimaculangan', 'Dimalanta', 'Dizon', 'Domantay', 'Duque', 'Echiverri', 'Elizalde', 'Enrile',
    'Escaler', 'Esguerra', 'Espiritu', 'Estanislao', 'Estrada', 'Evangelista', 'Fabella', 'Fajardo',
    'Faustino', 'Feliciano', 'Fernandez', 'Ferrer', 'Florentino', 'Flores', 'Fortun', 'Francisco',
    'Gabaldon', 'Galang', 'Gallardo', 'Galvan', 'Galvez', 'Gamboa', 'Ganzon', 'Garcia',
    'Gatchalian', 'Gatmaitan', 'Gaza', 'Geronimo', 'Goco', 'Goiti', 'Gonzaga', 'Gonzales',
    'Guerrero', 'Guevarra', 'Guingona', 'Guinto', 'Gutierrez', 'Guzman', 'Henares', 'Henson',
    'Hermosa', 'Hernandez', 'Herrera', 'Hidalgo', 'Hizon', 'Honasan', 'Ibañez', 'Ignacio',
    'Ilagan', 'Imperial', 'Infante', 'Inocencio', 'Iñiguez', 'Isidro', 'Jacinto', 'Jalandoni',
    'Jao', 'Jara', 'Javier', 'Jimenez', 'Joaquin', 'Jocson', 'Jose', 'Joson',
    'Jovellanos', 'Juan', 'Juico', 'Kalaw', 'Katigbak', 'Kho', 'Kintanar', 'Lacanilao',
    'Lacson', 'Ladia', 'Lagman', 'Laguio', 'Lampa', 'Lanuza', 'Lao', 'Lapid',
    'Lapus', 'Laurel', 'Lava', 'Lazaro', 'Ledesma', 'Legarda', 'Legaspi', 'Leoncio',
    'Leonen', 'Lim', 'Liñan', 'Lising', 'Liwanag', 'Llamas', 'Locsin', 'Lontoc',
    'Lopez', 'Lorenzana', 'Lorenzo', 'Loyola', 'Lozada', 'Lucero', 'Luciano', 'Lugtu',
    'Luna', 'Mabini', 'Macapagal', 'Macaraig', 'Magsaysay', 'Makalintal', 'Maliksi', 'Malvar',
    'Manahan', 'Manalac', 'Manalo', 'Manankil', 'Manglapus', 'Manicad', 'Maningat', 'Maniquis',
    'Manzano', 'Mapa', 'Maramba', 'Marasigan', 'Marcos', 'Mariano', 'Marquez', 'Martinez',
    'Masangkay', 'Mateo', 'Matias', 'Maturan', 'Mañalac', 'Medalla', 'Medina', 'Melchor',
    'Mercado', 'Miranda', 'Mitra', 'Mojares', 'Molina', 'Monasterio', 'Montano', 'Monteclaro',
    'Montelibano', 'Montenegro', 'Montero', 'Montilla', 'Montinola', 'Morales', 'Moreno', 'Mutuc',
    'Nakpil', 'Nalupta', 'Narciso', 'Nava', 'Navarro', 'Nepomuceno', 'Neri', 'Nicolas',
    'Nieto', 'Noble', 'Nolasco', 'Ocampo', 'Ople', 'Orbos', 'Ordonez', 'Oreita',
    'Orosa', 'Ortigas', 'Osmeña', 'Ozamiz', 'Paderanga', 'Padilla', 'Pagulayan', 'Paguia',
    'Palanca', 'Palma', 'Panganiban', 'Pangilinan', 'Panlilio', 'Pantaleon', 'Paraiso', 'Pardo',
    'Pascual', 'Pastor', 'Paterno', 'Pecson', 'Pelayo', 'Peña', 'Peralta', 'Perez',
    'Pernia', 'Pestaño', 'Pimentel', 'Pinlac', 'Placido', 'Platon', 'Poblador', 'Poe',
    'Ponce', 'Posadas', 'Prado', 'Pua', 'Puno', 'Punsalan', 'Puyat', 'Que',
    'Quezon', 'Quiazon', 'Quirino', 'Quisumbing', 'Quito', 'Ramirez', 'Ramos', 'Razon',
    'Recto', 'Regalado', 'Relosa', 'Resurreccion', 'Revilla', 'Rey', 'Reynes', 'Ricahuerta',
    'Ricarte', 'Rivera', 'Robledo', 'Robles', 'Roces', 'Rodriguez', 'Rojo', 'Roldan',
    'Romero', 'Romualdez', 'Romulo', 'Roño', 'Roque', 'Rosales', 'Rosario', 'Roxas',
    'Rubio', 'Rufino', 'Ruiz', 'Sabalvaro', 'Sabido', 'Sacay', 'Salas', 'Salazar',
    'Salcedo', 'Salgado', 'Salonga', 'Salvador', 'Samonte', 'San Agustin', 'San Jose', 'San Juan',
    'San Pedro', 'Sanchez', 'Sandico', 'Sandejas', 'Sanguila', 'Santiago', 'Santillan', 'Sanz',
    'Sebastian', 'Segovia', 'Sempio', 'Seneres', 'Seno', 'Serna', 'Sevilla', 'Sia',
    'Sian', 'Sibal', 'Siguion-Reyna', 'Silang', 'Silverio', 'Singson', 'Siochi', 'Sioson',
    'Sison', 'Siy', 'Soler', 'Soliman', 'Sotto', 'Sta. Maria', 'Sta. Romana', 'Suarez',
    'Sumulong', 'Sunico', 'Sy', 'Syjuco', 'Syquia', 'Tabuena', 'Tadiar', 'Tagle', 'Tamano',
    'Tan', 'Tancinco', 'Tanco', 'Tanjuatco', 'Tantoco', 'Tañada', 'Tayag', 'Teodoro',
    'Teves', 'Tinio', 'Tirol', 'Tirona', 'Tolentino', 'Tordesillas', 'Torno', 'Trillanes',
    'Trinidad', 'Tuason', 'Tugade', 'Tumbokon', 'Tungol', 'Ty', 'Umali', 'Unas',
    'Ungson', 'Uy', 'Valdez', 'Valencia', 'Valenciano', 'Valenzuela', 'Valera', 'Valeroso',
    'Varela', 'Vargas', 'Velasco', 'Veloso', 'Ventura', 'Vergel', 'Vergara', 'Vibal',
    'Vicencio', 'Victorino', 'Villacorta', 'Villafuerte', 'Villalon', 'Villamor', 'Villareal', 'Villarosa',
    'Villavicencio', 'Villegas', 'Vinluan', 'Virata', 'Vitug', 'Yabut', 'Yanga', 'Yanson',
    'Yap', 'Ybañez', 'Yee', 'Yenko', 'Yonzon', 'Yulo', 'Yusay', 'Yuson',
    'Yuzon', 'Zabala', 'Zaide', 'Zaldivar', 'Zamora', 'Zandueta', 'Zapanta', 'Zaragoza',
    'Zerrudo', 'Zialcita', 'Zobel', 'Zosa', 'Zulueta'
]

ua = UserAgent()
faker = Faker()
console=Console()
live = 0
cp = 0
#------------[colour]------------#
R = "[bold red]"
Y = "[bold yellow]"
G = "[bold green]"
B = "[bold blue]"
P = "[bold purple]"
C = "[bold cyan]"
W = "[bold white]"
#---------------------------#
def clear():
    os.system("clear")
#---------------------------#
def logo():
    logx=Panel(f"""{Y}
  ▗▄▄▄▄▖▗▖  ▗▖ ▗▄▖  ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖ 
     ▗▞▘▐▛▚▞▜▌▐▌ ▐▌▐▌     █  ▐▌   ▐▌ ▐▌
   ▗▞▘  ▐▌  ▐▌▐▛▀▜▌ ▝▀▚▖  █  ▐▛▀▀▘▐▛▀▚▖
  ▐▙▄▄▄▖▐▌  ▐▌▐▌ ▐▌▗▄▄▞▘  █  ▐▙▄▄▖▐▌ ▐▌{G}V1
     """, border_style="bold green")
    print(logx)


def fake_password(custom=None):
    if custom:
        return str(custom)
    return "PIN#KY1"

def get_temp_email(fname, lname, domain_choice=None):
    fname = re.sub(r'\W+', '', fname.lower())
    lname = re.sub(r'\W+', '', lname.lower())

    # Natural email patterns
    separators = ['.', '_', '']
    sep = random.choice(separators)

    patterns = [
        f"{fname}{sep}{lname}",
        f"{lname}{sep}{fname}",
        f"{fname[0]}{sep}{lname}",
        f"{fname}{sep}{lname[0]}",
        f"{fname}{sep}{lname}{random.randint(1990, 2005)}",
        f"{fname}{random.randint(10, 99)}"
    ]
    prefix = random.choice(patterns)

    if domain_choice == "1":
        domain = "yuennix.site"
    elif domain_choice == "2":
        domain = "weyn.store"
    else:
        domain = random.choice(['yuennix.site', 'weyn.store'])

    return f"{prefix}@{domain}"

def get_temp_code(email):
    try:
        sess = requests.Session()
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "accept": "application/json",
            "cookie": f"email={email}"
        }
        res = sess.get(f'https://tempmail.plus/api/mails?email={email}&first_id=0&epin', headers=headers)
        data = res.json()

        if data.get("result") and data.get("mail_list"):
            for mail in data["mail_list"]:
                if mail.get("is_new"):
                    subject = mail.get("subject", "")
                    code = re.search(r"(\d+)", subject)
                    return code.group(1) if code else subject
        return None
    except:
        return None

def get_bd_number():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+639%s%s%s' % (na, ni, nu)
    return nope

def extract_form(html):
    soup = BeautifulSoup(html, 'html.parser')
    return {tag.get("name"): tag.get("value") for tag in soup.find_all("input") if tag.get("name")}

def ugen():
    return ua.random

def save_result(uid, password, cookie):
    folder = "/sdcard/ZUYAN"
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/SUCCESS-OK.txt", "a") as f:
        f.write(f"{uid}|{password}|{cookie}\n")

def confirm_id(mail, uid, otp, data, ses, password):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
            'contact': mail,
            'type': "submit",
            'is_soft_cliff': "false",
            'medium': "email",
            'code': otp
        }
        fb_dtsg_match = re.search(r'"token":"([^"]+)"', str(data))
        fb_dtsg = fb_dtsg_match.group(1) if fb_dtsg_match else ""

        jazoest_match = re.search(r'name="jazoest" value="(\d+)"', str(data))
        jazoest = jazoest_match.group(1) if jazoest_match else ""

        lsd_match = re.search(r'name="lsd" value="([^"]+)"', str(data))
        lsd = lsd_match.group(1) if lsd_match else ""

        payload = {
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd,
            '__dyn': "",
            '__csr': "",
            '__req': "4",
            '__fmt': "1",
            '__a': "",
            '__user': uid
        }
        headers = {
        'User-Agent': ugen(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            # print(Panel(f"{G}[{Y}✓{G}]{W}ID : {R}{uid}", title="DISABLED",border_style="bold green"))
            pass
        else:
            cookie = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
            print(Panel(f"{G}[{Y}✓{G}]{W} UID: {G}{uid}\n{G}[{Y}✓{G}]{W} PASS: {G}{password}\n{G}[{Y}✓{G}]{W} COOKIE: {G}{cookie}\n", title="SUCCESS",border_style="bold green"))
            save_result(uid, password, cookie)
    except Exception:
        # print(Panel(f"{G}[{Y}✓{G}]{W} OTP Confirmation Failed"))
        pass

def register_account(domain_choice, name_option, gender_option):
    global live, cp
    # time.sleep(random.uniform(0.03, 0.05)) # Slow down initial request
    while True:
        try:
            ses = requests.Session()
            res = ses.get('https://touch.facebook.com/reg')
            # time.sleep(random.uniform(0.03, 0.05)) # Human-like delay after loading page
            form = extract_form(res.text)

            # Gender Selection
            if gender_option == "1": # Male
                gender = "2"
                g_type = "male"
            elif gender_option == "2": # Female
                gender = "1"
                g_type = "female"
            else: # Mixed
                if random.random() < 0.5:
                    gender = "2"
                    g_type = "male"
                else:
                    gender = "1"
                    g_type = "female"

            # Name Selection
            if name_option == "1": # Filipino
                first_names = FILIPINO_FIRST_NAMES_MALE if g_type == "male" else FILIPINO_FIRST_NAMES_FEMALE
                last_names = FILIPINO_LAST_NAMES
            else: # RPW
                first_names = RPW_FIRST_NAMES_MALE if g_type == "male" else RPW_FIRST_NAMES_FEMALE
                last_names = RPW_LAST_NAMES

            fname = random.choice(first_names)
            lname = random.choice(last_names)

            email = get_temp_email(fname, lname, domain_choice)
            password = fake_password(globals().get('CUSTOM_PASS'))

            # time.sleep(random.uniform(0.05,0.08)) # Delay while "typing" info

            payload = {
            'ccp': '2',
            'reg_instance': form.get('reg_instance'),
            'reg_impression_id': form.get('reg_impression_id'),
            'logger_id': form.get('logger_id'),
            'firstname': fname,
            'lastname': lname,
            'birthday_day': str(random.randint(1, 28)),
            'birthday_month': str(random.randint(1, 12)),
            'birthday_year': str(random.randint(1990, 2005)),
            'reg_email__': email,
            'reg_passwd__': password,
            'sex': gender,
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{password}',
            'submit': 'Sign Up',
            'fb_dtsg': form.get('fb_dtsg', ''),
            'jazoest': form.get('jazoest'),
            'lsd': form.get('lsd'),
            '__dyn': '', '__csr': '', '__req': 'q', '__a': '', '__user': '0'
            }
            headers = {'authority': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    'dpr': '2',
                    'referer': 'https://m.facebook.com/login/save-device/',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ugen(),
                    'viewport-width': '980'

            }
            reg = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)
            cookies = ses.cookies.get_dict()
            if "c_user" in cookies:
                uid = cookies["c_user"]
                print(Panel(f"{G}[{Y}✓{G}]{W} LIVE ID CREATED: {G}{uid}\n{G}[{Y}✓{G}]{W} PASS: {G}{password}\n{G}[{Y}✓{G}]{W} NAME: {G}{fname} {lname}\n{G}[{Y}✓{G}]{W} MAIL: {G}{email}",border_style="bold green"))

                # time.sleep(random.uniform(0.03, 0.05)) # Removed wait for code
                code = get_temp_code(email)
                if code:
                    # time.sleep(random.uniform(0.03, 0.05)) # Human delay before confirming
                    confirm_id(email, uid, code, reg.text, ses, password)
                live += 1
                break
            else:
                cp += 1
                # Silent retry logic
                continue

            # time.sleep(random.uniform(0.03, 0.05)) # Removed break between creations
        except requests.exceptions.ConnectionError:
            # Silent retry on connection error too
            time.sleep(1)
            continue
        except Exception:
            cp += 1
            continue

def main():
    while True:
        clear()
        logo()
        info = f"""
        {G}[{Y}✓{G}]{W} OWNER : {G}HULAAN MO
        {G}[{Y}✓{G}]{W} TOOLS : {G}FB ACCOUNT CREATOR 
        {G}[{Y}✓{G}]{W} VERSION : {G} TESTERS
        """
        print(Panel(info,border_style="bold green"))

        # Name selection
        print(Panel(f"{G}[1] {W}Filipino Names\n{G}[2] {W}RPW Names\n{G}[b] {W}Back", title="NAME OPTION", border_style="bold green"))
        name_option = Prompt.ask(f"{G}[{Y}✓{G}]{W} Choose Name Option ", choices=["1", "2", "b"], default="1")
        if name_option == 'b': break

        # Gender selection
        clear(); logo()
        print(Panel(f"{G}[1] {W}Male\n{G}[2] {W}Female\n{G}[3] {W}Mixed (50% M / 50% F)\n{G}[b] {W}Back", title="GENDER OPTION", border_style="bold green"))
        gender_option = Prompt.ask(f"{G}[{Y}✓{G}]{W} Choose Gender Option ", choices=["1", "2", "3", "b"], default="3")
        if gender_option == 'b': continue

        # Custom password feature
        clear(); logo()
        print(Panel(f"{G}[ b ] {W}Back to Main Menu", border_style="bold green"))
        custom_pass_input = Prompt.ask(f"{G}[{Y}✓{G}]{W} Enter Custom Password (leave blank for default) ", default="")
        if custom_pass_input.lower() == 'b': continue
        global CUSTOM_PASS
        CUSTOM_PASS = custom_pass_input if custom_pass_input else None

        # Email domain selection
        clear(); logo()
        print(Panel(f"{G}[1] {W}yuennix.site\n{G}[2] {W}weyn.store\n{G}[3] {W}Mixed (Random)\n{G}[b] {W}Back", title="DOMAIN SELECTION", border_style="bold green"))
        domain_choice = Prompt.ask(f"{G}[{Y}✓{G}]{W} Choose Email Option ", choices=["1", "2", "3", "b"], default="3")
        if domain_choice == 'b': continue

        # Account limit
        clear(); logo()
        limit_str = Prompt.ask(f"{G}[{Y}✓{G}]{W} How many accounts to create? (or 'b' to back) ", default="10")
        if limit_str.lower() == 'b': continue
        try:
            limit = int(limit_str)
        except ValueError:
            limit = 10

        threads = []
        for _ in range(limit):
            t = threading.Thread(target=register_account, args=(domain_choice, name_option, gender_option))
            t.start()
            threads.append(t)
            time.sleep(1) # Small stagger to avoid overwhelming or instant block

        for t in threads:
            t.join()

        print(Panel(f"{G}COMPLETED!{W}\n{G}LIVE: {live}\n{R}CP: {cp}", border_style="bold green"))
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

import csv
import random

# Predefined lists of first names and last names
first_names = ["Giuditta", "Pierson", "Alvinia", "Zachary", "Minetta", "Leontine", "Jeno", "Nye", "Ced", "Issiah", "Jeannine", "Antonietta", "Caria", "Toby", "Armin", "Hildegaard", "Cecilla", "Horst", "Trevor", "Mitzi", "Angelo", "Georgi", "Leopold", "Christina", "Maris", "Meier", "Coreen", "Morena", "Regen", "Renato", "Antonio", "Lori", "Bertie", "Nell", "Van", "Codi", "Arnoldo", "Franky", "Ketti", "Kevyn", "Griffie", "Sergent", "Mercedes", "Gayelord", "Jacki", "Hedy", "Ofilia", "Abbey", "Randall", "Ilyssa", "Leonard", "Cross", "Ada", "Dalston", "Stillmann", "Tabina", "Ruthie", "Alecia", "Lucien", "Bonnee", "Janna", "Shalna", "Whitby", "Curcio", "Esta", "Ira", "Aviva", "Margaretta", "Kent", "Joel", "Nelle", "Jessalyn", "Cherilyn", "Siobhan", "Almeria", "Clarette", "Dun", "Giffard", "Pincas", "Britt", "Arabele", "Orren", "Auberta", "Winni", "Corabel", "Marinna", "Patty", "Bay", "Emlynn", "Gilly", "Olympe", "Brit", "Alvan", "Hyacintha", "Donnamarie", "Shem", "Kristan", "Sansone", "Batholomew", "Timi", "Syd", "Haily", "Ramona", "Kaylyn", "Charmain", "Dalenna", "Agace", "Jany", "Daffy", "Weider", "Carol", "Wald", "Sorcha", "Susan", "Gasper", "Jean", "Heriberto", "Fabiano", "Micah", "Harland", "Ellissa", "Wilt", "Donnajean", "Ema", "Jo", "Panchito", "Farly", "Cullen", "Winston", "Vinni", "Cari", "Shae", "Jess", "Brit", "Alie", "North", "Alejoa", "Reynolds", "Osbourn", "Amerigo", "Frasco", "Enrique", "Erica", "Erskine", "Ninon", "Rouvin", "Nappie", "Lauree", "Moreen", "Wilma", "Lenee", "Bjorn", "Winnie", "Willi", "Netty", "Siouxie", "Minni", "Bliss", "Denys", "Berny", "Lemuel", "Roddie", "Gerald", "Chloe", "Jedd", "Didi", "Oliviero", "Nikoletta", "Northrup", "Chrysa", "Symon", "Janeczka", "Ashly", "Jeremie", "Bonita", "Jasmina", "Beale", "Elsinore", "Carline", "Tabor", "Eli", "Wandis", "Gare", "Pauline", "Raddie", "Dav", "Chane", "Collie", "Tudor", "Shannon", "Stanfield", "Wrennie", "Patton", "Karon", "Salmon", "Adrienne", "Brana", "Eldredge", "Any", "Phebe", "Arni", "Eolanda", "Koral", "Ravi", "Bell", "Dionisio", "Stevana", "Clemmy", "Alexia", "Bondon", "Victoir", "Lena", "Ram", "Herminia", "Abigael", "Wilden", "Marie", "Dun", "Halimeda", "Odey", "Gib", "Cully", "Muffin", "Lorain", "Hillyer", "Trina", "Bordie", "Goldie", "Courtney", "Koren", "Lyn", "Boyd", "Suzanne", "Vivienne", "Aggi", "Clarisse", "Tina", "Brina", "Chanda", "Stanford", "Prue", "Moses", "Celestine", "Trude", "Koren", "Marrissa", "Lauri", "Gerty", "Stevena", "Irwin", "Beckie", "Blake", "Georgeanna", "Baudoin", "Cleveland", "Yorker", "Corrinne", "Hadrian", "Quentin", "Dasi", "Margarete", "Ottilie", "Onofredo", "Norbie", "Marcile", "Georgie", "Robinson", "Roderic", "Ivette", "Upton", "Diandra", "Jacob", "Harald", "Trip", "Andrea", "Granny", "Georgeta", "Annice", "Mathias", "Abby", "Marie-ann", "Andree", "Lonnie", "Laurel", "Nerta", "Danya", "Bowie", "Marina", "Byran", "Gannie", "Agretha", "Hieronymus", "Callean", "Jacinta", "Calli", "Modesty", "Tootsie", "Natal", "Skip", "Lucilia", "Gabrila", "Preston", "Micki", "Cristie", "Shaughn", "Margie", "Locke", "Corey", "Modestia", "Benni", "Erda", "Curry", "Korey", "Sampson", "Sandy", "Archibald", "Teri", "Allissa", "Wadsworth", "Tobit", "Urban", "Evered", "Fairleigh", "Will", "Lucine", "Shaina", "Edan", "Barth", "Rickert", "Nathanial", "Jolie", "Meridith", "Janka", "Courtnay", "Hayward", "Lauretta", "Patten", "Malina", "Maddi", "Carma", "Zerk", "Loleta", "Troy", "Hernando", "Fay", "Aluino", "Murial", "Giffer", "Corliss", "Lee", "Olivier", "Kimberlee", "Augy", "Flemming", "Kessiah", "Herold", "Clemmie", "Sascha", "Kevyn", "Vinny", "Grant", "Cosme", "Julienne", "Franky", "Sonia", "Dominga", "Laurent", "Samuel", "Bree", "Reynolds", "Bobby", "Amabel", "Emmy", "Christina", "Merralee", "Dani", "Bruis", "Kennith", "Velma", "Garner", "Avram", "Cecily", "Edita", "Phillip", "Wiley", "Zita", "Merrilee", "Emmalynn", "Alva", "Fidelity", "Camel", "Leilah", "Breanne", "Michelle", "Costa", "Skippy", "Bryan", "Diannne", "Anetta", "Dalston", "Marthena", "Grantham", "Anne-corinne", "Tracie", "Genevieve", "Rossie", "Moina", "Werner", "Ode", "Lucias", "Leon", "Karie", "Nixie", "Alphonse", "Vinson", "Alma", "Elisha", "Jakob", "Leisha", "Bambi", "Erasmus", "Nicol", "Stephanus", "Jude", "Denys", "Benyamin", "Nathanial", "Benita", "Bernetta", "Shanda", "Franchot", "Mercie", "Minna", "Millie", "Antony", "Eyde", "Carena", "Grady", "Averell", "Freda", "Lin", "Susanetta", "Renault", "Horten", "Butch", "Mick", "Amandie", "Brynne", "Vick", "Inesita", "Marianna", "Patrizio", "Ruthi", "Ivar", "Milli", "Ruthann", "Cindelyn", "Carlos", "Sallyanne", "Tybi", "Kiele", "Corbett", "Mildrid", "Townie", "Reagen", "Bernhard", "Devondra", "Sharline", "Hillard", "Darsey", "Elinore", "Bertrand", "Windham", "Osmund", "Kliment", "Caye", "Cathie", "Eward", "Chris", "Zacharia", "Gladi", "Godfry", "Nat", "Oren", "Lonny", "Melamie", "Levin", "Cull", "Sylas", "Cinnamon", "Ody", "Audra", "Dorris", "Ber", "Julina", "Weston", "Broddie", "Beauregard", "Hartley", "May", "Astra", "Tiff", "Pammi", "Raff", "Robby", "Kellia", "Nichols", "Gustav", "Toma", "Jordon", "Dewie", "Michaeline", "Glennie", "Edwin", "Emili", "Vince", "Barbaraanne", "Mel", "Erl", "Pen", "Nichole", "Nelle", "Esteban", "Marisa", "Albina", "Westbrook", "Ariadne", "Tom", "Yanaton", "Darice", "Germain", "Rustin", "Roscoe", "Pierre", "Aura", "Johannes", "Coleman", "Vikki", "Matelda", "Fidel", "Mommy", "Dede", "Willie", "Averil", "Bevan", "Bourke", "Ruperto", "Elsworth", "Wynny", "Rose", "Athene", "Candi", "Der", "Parnell", "Johnnie", "Georgetta", "Nissy", "Cass", "Pearce", "Angil", "Robbi", "Cassandre", "Thacher", "Bearnard", "Carmelle", "Bradley", "Dell", "Archy", "Kit", "Lonnie", "Randy", "Carena", "Andee", "Valentine", "Briano", "Nerita", "Giorgia", "Locke", "Courtnay", "Amil", "Yale", "Flint", "Hortense", "Dulcine", "Earle", "Lothaire", "Vasili", "Sigismund", "Anne-corinne", "Waylin", "Gregoor", "Jacky", "Dannye", "Adrian", "Korella", "Dagny", "Colette", "Dotty", "Kalina", "Pall", "Yale", "Haley", "Saudra", "Van", "Lucila", "Anthea", "Shurlock", "Frederic", "Harriet", "Warner", "Rolfe", "Adolphe", "Ame", "Kaycee", "Edsel", "Maxie","Lew", "Web", "Ramon", "Marijo", "Leroi", "Nels", "Marshal", "Blanca", "Dallis", "Prue", "Rice", "Marianne", "Sandy", "Hale", "Nero", "Toddy", "Virgie", "Collete", "Jo-anne", "Sherrie", "Lenka", "Filippa", "Janetta", "Nolana", "Jasun", "Dill", "Norby", "Ellyn", "Andris", "Harwell", "Kermy", "Aura", "Merwyn", "Jennica", "Jarid", "Ike", "Levy", "Emmerich", "Jenine", "Dione", "Buddy", "Sarah", "Byrann", "William", "Barbee", "Gail", "Nanete", "Eric", "Gerome", "Hayward", "Neille", "Michaeline", "Robina", "Troy", "Alla", "Ellery", "Clifford", "Concordia", "Albina", "Innis", "Linet", "Nathan", "Ellswerth", "Staci", "Quinta", "Swen", "Goldia", "Leigha", "Carrol", "Clemmie", "Alfonse", "Marilyn", "Aprilette", "Giffer", "Hoebart", "Case", "Kacie", "Alika", "Electra", "Natividad", "Jeff", "Temp", "Adey", "Janetta", "Dennis", "Janis", "Deeann", "Barrie", "Ealasaid", "Nikkie", "Dalt", "Kelbee", "Caddric", "Loralyn", "Charity", "Reinhold", "Mara", "Lucais", "Etheline", "Carmon", "Bordie", "Jena", "Hedy", "Godwin", "Monte", "Leila", "Ursola", "Gill", "Averyl", "Klarrisa", "Gustavus", "Nichole", "Ingram", "Edin", "Olympia", "Lewiss", "Quinton", "Wesley", "Dionne", "Nicola", "Fay", "Nadya", "Ewell", "Wilburt", "Ave", "Micheal", "Sylas", "Giralda", "Hildegaard", "Leontyne", "Efren", "Javier", "Clark", "Jules", "Rubin", "Wake", "Demetri", "Felic", "Paxton", "Katine", "Alfreda", "Leroi", "Merv", "Pooh", "Franni", "Steffen", "Tisha", "Brinn", "Hebert", "Hatty", "Hillier", "Zacharia", "Dennie", "Atalanta", "Delaney", "Robenia", "Gardie", "Carr", "Beltran", "Emily", "Horatio", "Ardene", "Lowell", "Kattie", "Sandro", "Yardley", "Emelen", "Kiel", "Stefanie", "Dacie", "Vivyan", "Genevra", "Karrie", "Felix", "Tobie", "Trina", "Ado", "Flory", "Neale", "Meara", "Claudio", "Kele", "Antin", "Elfrieda", "Simon", "Othello", "Anjela", "Corey", "Eb", "Madlin", "Nicola", "Ilsa", "Aleda", "Dorie", "Walt", "Delores", "Erny", "Zia", "Ellerey", "Hoyt", "Delilah", "Scottie", "Celestyna", "Paxon", "Mariejeanne", "Malvin", "Hersh", "Jackelyn", "Karolina", "Montgomery", "Karoly", "Erskine", "Emmalynne", "Sonni", "Jorry", "Ave", "Ilse", "Amery", "Whitby", "Janie", "Stearn", "Clo", "Kristos", "Sapphira", "Nestor", "Sadye", "Thibaud", "Banky", "Kerstin", "Cicily", "Carly", "Brody", "Hershel", "Kerianne", "Hubert", "Quent", "Cammy", "Sheelah", "Arri", "Cecil", "Micah", "Cristy", "Elihu", "Gerri", "Ginger", "Bancroft", "Dani", "Fancie", "Valentino", "Norbie", "Austina", "Fifine", "Giana", "Demetris", "Amery", "Arabele", "Anatollo", "Danyette", "Gun", "Kelley", "Louisette", "Ulla", "Jere", "Livvie", "Iolanthe", "Magdalena", "Vanna", "Joceline", "Emlen", "Bren", "Lenard", "Arlena", "Berkie", "Findlay", "Heriberto", "Dawna", "Nedda", "Corette", "Melly", "Wilhelm", "Carlyle", "Barbra", "Wilfrid", "Verge", "Nikaniki", "Erinn", "Cammie", "Kaja", "Marlon", "Kirsti", "Amelita", "Candra", "Dorothee", "Sumner", "Rod", "Tallia", "Nat", "Torrance", "York", "Alister", "Erek", "Jacklin", "Timotheus", "Filippa", "Ruprecht", "Joanna", "Ynes", "Janos", "Alie", "Shalom", "Lolly", "Burr", "Claudia", "Luciano", "Otha", "Balduin", "Dotti", "Renaldo", "Stillmann", "Waylen", "Jenine", "Lane", "Abbey", "Corbin", "Yule", "Branden", "Herrick", "Giovanni", "Ambrosio", "Corri", "Lydie", "Garland", "Reid", "Sallyanne", "Bertrand", "Kore", "Gottfried", "Vaclav", "Carmella", "Marrilee", "Wadsworth", "Elset", "Ogden", "Katey", "Farrand", "Bamby", "Eddy", "Ellsworth", "Marley", "Wylie", "Roger", "Stacia", "Alethea", "Rickard", "Bridgette", "Jere", "Herschel", "Van", "Udale", "Graehme", "Jasper", "Lanny", "Danyette", "Umeko", "Grantham", "Rollie", "Sigismond", "Zebulen", "Cassaundra", "Eugene", "Kenton", "Warren", "Angy", "Patrizio", "Idelle", "Chrotoem", "Gonzales", "Cornie", "Britni", "Phaidra", "Isaiah", "Crystal", "Chas", "Anthiathia"]
last_names = ["Mogford", "Piesing", "Gerrietz", "Crang", "Schwander", "D'Orsay", "Cheves", "Jakubovski", "Brockest", "De Paoli", "Barkes", "Leachman", "Leal", "Crosdill", "Charte", "Budnk", "Goundsy", "Klainer", "Golightly", "Pittoli", "Belbin", "Mackieson", "Anstee", "Zamorano", "Lermit", "De Witt", "Kibblewhite", "Kedslie", "Brockington", "Elijah", "Reap", "Scottesmoor", "Sieve", "Trustey", "Geydon", "Breslau", "Labadini", "Scougall", "Shovel", "Brodest", "Rolinson", "Beesley", "Harget", "Scallan", "Batrick", "Jeeks", "Gellibrand", "Blanchet", "Tremolieres", "Kiellor", "Chrestien", "Haswall", "Matoshin", "Botright", "Whittington", "Kitchiner", "Puddan", "Coldbathe", "Hawthorne", "Gayforth", "Venour", "Piccard", "Pally", "Hunnaball", "Boggs", "Guiett", "Flaonier", "Largan", "Cornelisse", "Devereux", "Warlawe", "Hattigan", "Frenzel;", "Gages", "Dunrige", "Feldmesser", "Edge", "Ditzel", "McGeechan", "Hurlestone", "Lillistone", "Cotsford", "Oiller", "Rowbury", "Cloney", "Girardeau", "Frackiewicz", "Diggens", "Perone", "Surby", "Barg", "Seamen", "Haggus", "Dable", "Castanho", "Matthews", "Angier", "Healy", "Caplis", "De Laspee", "Windrass", "Benasik", "Clemmey", "Jurkowski", "O'Kane", "Fulks", "Enderby", "O'Hagirtie", "Huke", "Utteridge", "Brayshaw", "Le Brum", "Fiennes", "Champagne", "Adanet", "Garter", "M'Quharge", "Fallow", "Steagall", "Rait", "Cleve", "Carnall", "Thursby", "Gegay", "Morpeth", "Summersett", "Brosnan", "Potell", "Menco", "Kinsell", "Tolwood", "Dron", "Kobiela", "Ladel", "Dishman", "Maffulli", "Lockyear", "Wimmer", "Kirkness", "Reisen", "Chantillon", "Quail", "Gerrietz", "Melanaphy", "Manuello", "Vosper", "Gosnoll", "Romanski", "Benallack", "Tebbet", "Heino", "Bener", "Luard", "Lusher", "Pimlott", "Fearenside", "Messingham", "Overstreet", "Dust", "Rispine", "Bowness", "Seabrocke", "Hartup", "Larking", "Spofford", "Goodin", "Hay", "Scotchmur", "Danihel", "Chafney", "Besset", "Dimic", "Peasey", "Hover", "Isacke", "O'Scandall", "Sambedge", "Walder", "Dady", "Skeermer", "Goadby", "Torrijos", "Rollin", "Beak", "Glasbey", "Semeradova", "Sand", "Stopher", "Vogeler", "Melmoth", "Meneghelli", "Fairley", "Lovewell", "Fowkes", "Volker", "L'argent", "Markus", "Kenningley", "Borge", "Conachie", "Dedden", "Bamell", "Bachnic", "Minihan", "Dunk", "Halgarth", "Barensky", "Hartright", "Behninck", "Slimme", "Hearnden", "Simmans", "Benyon", "Iffe", "Maun", "Hacket", "Matterson", "Sawney", "Ivanchenkov", "Gawthorpe", "Ormond", "Ivel", "Allonby", "Verney", "Flaverty", "Lindman", "Bendley", "Campkin", "Messer", "Rangell", "Naish", "Massie", "McPaik", "Organ", "Rentcome", "Death", "Nyland", "Bockmaster", "Bennett", "Munt", "Miles", "Broome", "Skevington", "Leddie", "Itzhaiek", "Revans", "Fawks", "Sudell", "Meikle", "Samarth", "Pennock", "Robroe", "Pylkynyton", "Swinerd", "Lafferty", "Greiswood", "Klimkiewich", "Darville", "Gluyus", "Armytage", "Batcock", "Emanueli", "Callf", "Ccomini", "Ollet", "O'Rudden", "Golland", "Shakesby", "Heartfield", "Boddice", "Scamerden", "Comoletti", "Spreag", "Applin", "Gregori", "Steptoe", "Askew", "Proud", "Kember", "Skittles", "Georgel", "Medforth", "Burehill", "Walesa", "Attenborrow", "Bradane", "Perch", "Owen", "McMorland", "Epdell", "Enrrico", "Hove", "Southard", "Hallatt", "Westhead", "Rolfs", "Ackers", "Scarffe", "Enion", "Dooley", "Daniell", "McPeck", "Kubasek", "Reinbeck", "Komorowski", "Chevers", "Dorant", "MacFarlan", "Ivashin", "Healings", "Tapenden", "Wheelan", "McAnellye", "Ciccotto", "Hatrey", "Mingauld", "Kampshell", "Lapwood", "Lyle", "McGawn", "Philler", "Sparry", "Swabey", "Davidovici", "Brash", "Phinn", "Alexsandrev", "Baroc", "Berrington", "Derrett", "Strank", "Pellew", "Cawston", "Connell", "Gabotti", "Bassett", "Ketley", "Marquis", "Hammer", "Brownsword", "Iacopo", "Marcroft", "Kingscote", "Scala", "Middup", "Cleiment", "Philpot", "Choupin", "Peschmann", "O'Geneay", "Newis", "Jennaroy", "Kochs", "Nickell", "Prichet", "MacDearmaid", "Dawks", "Flatman", "Plumm", "Ivashin", "Cruickshanks", "Blesing", "Frohock", "Church", "Pantry", "Simo", "Ilyin", "Binton", "Speak", "Danjoie", "Hyman", "Gerasch", "Creavin", "Cleeve", "Endle", "Mirando", "Gambell", "Oag", "Londsdale", "Monard", "McWard", "Ternouth", "McGuinness", "Dowderswell", "Presnell", "Bloyes", "McCay", "Manger", "Riden", "Plumbe", "Parmiter", "Gauntley", "Meddick", "Surcombe", "Pedlar", "de Amaya", "Artingstall", "Varndall", "Hackleton", "Sacaze", "Atlay", "Cornejo", "Hornbuckle", "Ryam", "Knowller", "Longbone", "Mandifield", "Killough", "Bussetti", "Rablan", "Sier", "Daintith", "Shaughnessy", "Sibthorpe", "Pencot", "Chippendale", "Able", "Cauldfield", "Desquesnes", "Pantlin", "Tegler", "Gladman", "Hynd", "Puffett", "Dogg", "Chaffey", "Hannent", "Chrispin", "Higbin", "Jimenez", "Juliff", "Geggus", "Bennedick", "Rossander", "Troughton", "Simenet", "Deely", "Stratford", "Drewet", "Turbern", "Sargood", "Abramamov", "Van der Linde", "Colebourne", "Rowter", "Peagram", "Wasteney", "Fay", "Spileman", "Bradbury", "Edworthye", "Harder", "Oneill", "Willetts", "Whiteford", "Bessey", "Folbigg", "Junkison", "Wannell", "Defew", "Hinks", "Escalero", "Curness", "Gouny", "Hassell", "McCrum", "Howood", "Demange", "Burchatt", "Gittus", "Kinig", "Maccaig", "Cleghorn", "Saxon", "Joder", "Mewes", "Carlucci", "Rampton", "Vanelli", "Derle", "Barnson", "McVitie", "Dennis", "Brandham", "Dryden", "Olivelli", "Hamments", "McKaile", "Pappin", "Brydson", "Strattan", "Dallimare", "Coole", "Sancto", "Taks", "Reaveley", "Jirousek", "Fawcitt", "Balcombe", "Goublier", "Inkpen", "Dowles", "Everil", "Issacoff", "Bollum", "Sutcliffe", "Capponeer", "Froment", "Purseglove", "O'Keaveny", "Emig", "Percy", "Lockie", "McConigal", "Lednor", "O'Lehane", "Saphir", "Luttgert", "Bixley", "McVity", "McBrearty", "Brownrigg", "Catherine", "Thurlborn", "Rex", "Cuardall", "Breeze", "Kynforth", "Greenard", "Dawidowicz", "Brownett", "Newport", "Stevings", "Gleed", "Harradine", "Cariss", "Lofting", "McAsgill", "Calladine", "Slorach", "Skeermer", "Kares", "Fowls", "Munslow", "Gianninotti", "Audley", "Janikowski", "Gosford", "Copas", "Mongain", "Harston", "Churm", "Cridge", "Kydd", "Willson", "Gilleson", "Yankishin", "Serjeant", "Chopy", "Linguard", "Wilstead", "Sacase", "Budleigh", "Deans", "Lamasna", "Timmins", "Bugs", "Lucius", "Abramovic", "Braddick", "Vasilyevski", "Gietz", "Mawson", "Atrill", "Pietranek", "Stapells", "Moyer", "Le Sarr", "Ganter", "Beaglehole", "Cattroll", "Hartnell", "Schild", "Frodsam", "Greenly", "Gibberd", "Lissemore", "Dover", "Cady", "Stoll", "Cowen", "Dwyer", "Groven", "Jobling", "Cattle", "Grut", "Cleworth", "Deehan", "Mishow", "Brewitt", "Bringloe", "Tarling", "Upfold", "Quittonden", "Weightman", "Keveren", "Glinde", "Nolan", "Simkovitz", "Colenutt", "Sherlock", "Clarae", "Ebi", "Metheringham", "Poytress", "Postill", "Beachamp", "Talboy", "Southard", "Hawksley", "Carlill", "Lawrinson", "Follacaro", "Harbour", "Maccrea", "Bedford", "Cramphorn", "Ellington", "Penhearow", "Sallan", "Josh", "McNickle", "Rollo", "Tomasino", "Wilmut", "Brito", "Craigg", "Trubshaw", "Francais", "Orniz", "Overthrow", "Litton", "Tolchard", "Spurrett", "Hanning", "Illyes", "Colliford", "Jewes", "Howton", "Spear", "Druitt", "Priestley", "Freak", "Inskipp", "Fenny", "Claridge", "Sifflett", "Bardey", "Willarton", "Fancott", "Kepling", "Goomes", "Teresia", "Husset", "Lyfe", "Lambricht", "Grigsby", "Ocheltree", "Butte", "Mougel", "Wrotham", "Proud", "Balcon", "Flew", "Hackey", "Gebhard", "Beecham", "Youles", "Secrett", "Lebarree", "Budnk", "Greenset", "Ceney", "Gwynne", "Cadding", "Fernant", "Ebbrell", "Clowser", "Liddell", "Entwisle", "Punt", "Ivanchikov", "Hort", "Pendry", "Bosward", "Stubbley", "Cozens", "Milella", "Hiddersley", "Fasse", "Kingswold", "Noads", "Sedgwick", "Roland", "Muldrew", "Loyd", "Goodnow", "Topper", "Sharpe", "Palk", "Frankiewicz", "Tatchell", "Maffezzoli", "Kochel", "Ferrino", "Traher", "O'Carran", "Urwen", "Monier", "Dutson", "Linkie", "Brimble", "Carvill", "Longhirst", "Bernolet", "Beefon", "Le Houx", "Fassam", "Gilliland", "Conyard", "Pouton", "Ballam", "Pettyfar", "Farnes", "MacRorie", "Kyd", "Northway", "Grace", "Hember", "Dobeson", "Shackesby", "Lempel", "Treacy", "Cucuzza", "Imesson", "Fumagalli", "Brenton", "Burtwistle", "Galfour", "Kiendl", "Charrington", "Mongenot", "Collisson", "Sammars", "MacMurray", "Redpath", "Raisher", "Pisculli", "Sinfield", "Melliard", "Velasquez", "Byatt", "Batch", "McBrady", "Wilber", "Records", "Paskell", "Swindley", "Loveland", "Ledwich", "Reed", "O'Scollee", "MacKall", "Avis", "Lorkin", "Tabb", "O'Sherrin", "Korneichuk", "McVeagh", "Weekes", "Faiers", "Durrant", "Russe", "Roark", "Craft", "Brokenshire", "Patis", "Rickford", "Spraggs", "Persich", "Brosi", "Glyde", "Adamkiewicz", "Hirthe", "Gipp", "Veltman", "Massel", "Testo", "Turrell", "Dallimore", "Dog", "Garoghan", "Ellingham", "Fechnie", "Davenhall", "Crowden", "Blunt", "Benam", "Karsh", "Puddefoot", "Biddles", "Chapier", "Heintz", "Cartan", "Garroch", "Necolds", "O'Doherty", "Shutte", "Shortt", "Avramovic", "Metherell", "Mousdall", "Mogg", "Grover", "Godding", "Billingsley", "Casier", "Morecombe", "Lipman", "Merrgen", "Branthwaite", "Waything", "Eaves", "Bourthouloume", "Thowes", "Gossipin", "Makey", "Akram", "Petegrew", "Serraillier", "Brehault", "Diviney", "Good", "Menilove", "O'Shaughnessy", "Brailsford", "Samsonsen", "Aland", "Clouston", "Jackett", "Marguerite", "Izkovicz", "Palay", "Harmeston", "Drake", "Treweela", "Southall", "Fabri", "Rosnau", "Ladds", "Chapple", "Moodie", "Lartice", "Moodey", "Kissack", "Grist", "Messager", "Howselee", "Munsey", "Grissett", "Frome", "Sampey", "Humpherson", "Joselovitch", "Milberry", "Clipsham", "Ply", "Miere", "Bergin", "Elsmore", "Ambrosio", "Cowles", "Petrillo", "Nickels", "Louche", "Lghan", "Neem", "De Rechter", "Friedank"]
cities = ["Delhi", "Lucknow", "Jaipur", "Chandigarh", "Amritsar", "Varanasi", "Agra", "Kanpur", "Ludhiana", "Allahabad","Prayagraj"]       # Your list of cities
loan_types = ["personal_loan", "mortage_loan","vehicle_loan","education_loan","business_loan"]   # Your list of loan types

# Generate CSV data for 100 records
num_records = 10000
output_filename = 'generated_data.csv'

with open(output_filename, mode='w', newline='') as csv_file:
    fieldnames = ['First Name', 'Last Name', 'Email', 'Phone Number', 'Gender', 'Credit Score', 'City', 'Income', 'Loan Exists', 'Loan Eligibility', 'Loan Type', 'Loan Amount']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for _ in range(num_records):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        phone_number = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        gender = random.choice(['Male', 'Female'])
        credit_score = random.randint(300, 850)
        city = random.choice(cities)
        income = random.randint(5000, 100000)
        loan_exists = random.choice([True, False])
        loan_eligibility = 'Yes' if loan_exists else 'No'
        loan_type = random.choice(loan_types)
        loan_amount = random.randint(10000, 100000)

        writer.writerow({
            'First Name': first_name,
            'Last Name': last_name,
            'Email': email,
            'Phone Number': phone_number,
            'Gender': gender,
            'Credit Score': credit_score,
            'City': city,
            'Income': income,
            'Loan Exists': loan_exists,
            'Loan Eligibility': loan_eligibility,
            'Loan Type': loan_type,
            'Loan Amount': loan_amount
        })

print(f"{num_records} records generated and saved to {output_filename}.")
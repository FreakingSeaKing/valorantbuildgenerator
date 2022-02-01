class Item:

    def __init__(self, name, price, buycap, item_type):
        self.name = name
        self.price = price
        self.buycap = buycap
        self.item_type = item_type


class Agent:

    def __init__(self, name, ability_1, ability_2):
        self.name = name
        self.ability_1 = ability_1
        self.ability_2 = ability_2


class Purchase:

    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


purchase_list = [
    #    Name            Price Buycap  Type
    Item("Classic",      0,      1,    "pistol"),
    Item("Shorty",       150,    1,    "pistol"),
    Item("Frenzy",       450,    1,    "pistol"),
    Item("Ghost",        500,    1,    "pistol"),
    Item("Sheriff",      800,    1,    "pistol"),
    Item("Stinger",      950,    1,    "smg"),
    Item("Spectre",      1600,   1,    "smg"),
    Item("Bucky",        850,    1,    "shotgun"),
    Item("Judge",        1850,   1,    "shotgun"),
    Item("Bulldog",      2050,   1,    "rifle"),
    Item("Guardian",     2250,   1,    "rifle"),
    Item("Phantom",      2900,   1,    "rifle"),
    Item("Vandal",       2900,   1,    "rifle"),
    Item("Marshal",      950,    1,    "sniper"),
    Item("Operator",     4700,   1,    "sniper"),
    Item("Ares",         1600,   1,    "heavy"),
    Item("Odin",         3200,   1,    "heavy"),
    Item("Light Shield", 400,    1,    "shield"),
    Item("Heavy Shield", 1000,   1,    "shield")
]
agent_list = [
    #     Agent        A_1  Name           Price Cap             A_2  Name          Price Cap
    Agent("Astra",     Item("Star",          150, 3, "ability"), Item("",               0, 1, "ability")),
    Agent("Breach",    Item("Aftershock",    200, 1, "ability"), Item("Flashpoint",   250, 2, "ability")),
    Agent("Brimstone", Item("Stim Beacon",   100, 2, "ability"), Item("Incendiary",   250, 1, "ability")),
    Agent("Chamber",   Item("Trademark",     150, 2, "ability"), Item("Headhunter",   100, 1, "ability")),
    Agent("Cypher",    Item("Trapwire",      200, 2, "ability"), Item("Cyber Cage",   100, 2, "ability")),
    Agent("Jett",      Item("Cloudburst",    200, 2, "ability"), Item("Updraft",      100, 2, "ability")),
    Agent("KAY/O",     Item("FRAG/ment",     200, 1, "ability"), Item("FLASH/drive",  250, 2, "ability")),
    Agent("Killjoy",   Item("Alarmbot",      200, 1, "ability"), Item("Nanoswarm",    200, 2, "ability")),
    Agent("Neon",      Item("Fast Lane",     300, 1, "ability"), Item("Relay Bolt",   200, 2, "ability")),
    Agent("Omen",      Item("Shrouded Step", 150, 2, "ability"), Item("Paranoia",     300, 1, "ability")),
    Agent("Phoenix",   Item("Blaze",         200, 1, "ability"), Item("Curveball",    250, 2, "ability")),
    Agent("Raze",      Item("Boom Bot",      300, 1, "ability"), Item("Blast Pack",   200, 2, "ability")),
    Agent("Reyna",     Item("Leer",          250, 2, "ability"), Item("Devour",       200, 1, "ability")),
    Agent("Sage",      Item("Barrier Orb",   400, 1, "ability"), Item("Slow Orb",     200, 2, "ability")),
    Agent("Skye",      Item("Regrowth",      200, 1, "ability"), Item("Trailblazer",  250, 1, "ability")),
    Agent("Sova",      Item("Owl Drone",     400, 1, "ability"), Item("Shock Bolt",   150, 2, "ability")),
    Agent("Viper",     Item("Snake Bite",    200, 2, "ability"), Item("Poison Cloud", 200, 1, "ability")),
    Agent("Yoru",      Item("Fakeout",       100, 2, "ability"), Item("Blindside",    250, 2, "ability"))
]

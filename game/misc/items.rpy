define shopitems = {
    0: (200, Item.PokeBall),
    1: (200, Item.Potion),
    2: (200, Item.Antidote),
    3: (200, Item.BurnHeal),
    4: (200, Item.IceHeal),
    5: (200, Item.Awakening),
    6: (200, Item.ParalyzeHeal),
    7: (300, Item.PokeDoll),
    8: (400, Item.FullHeal),
    9: (500, Item.Repel),
    10: (600, Item.GreatBall),
    11: (700, Item.SuperPotion),
    12: (750, Item.SuperRepel),
    13: (800, Item.UltraBall),
    14: (1500, Item.HyperPotion),
    15: (1500, Item.MaxRepel),
    16: (2000, Item.Revive),
    17: (2500, Item.MaxPotion),
    18: (3000, Item.FullRestore),
    19: (5000, Item.MaxRevive)
}

#To Update from spreadsheet:
#Find: ([0-9,]+)\t([0-9,]+)\t([A-z \-']+)\t([A-z 0-9,'.é]+)
#Replace: $1: ($2, "$3", "$4"),
#Find: ([0-9]+),([0-9]+)
#Replace: $1$2

define marketitems = {
    1000: (500, Item.EnergyPowder),
    2000: (300, Item.HealPowder),
    5000: (5000, Item.OvalStone),
    7000: (2500, Item.UnremarkableTeacup),
    10000: (5000, Item.Lawnmower),
    13337: (5000, Item.UpGrade),
    15000: (5000, Item.DeepSeaTooth),
    17000: (5000, Item.Protector),
    20000: (5000, Item.Fan),
    21000: (5000, Item.DeepSeaScale),
    23000: (1000, Item.TamatoSmoothie),
    26000: (2500, Item.CrackedPot),
    28000: (5000, Item.GalaricaCuff),
    30000: (5000, Item.Sachet),
    33000: (1000, Item.HondewSmoothie),
    35000: (30000, Item.ZincConcentrate),
    37000: (5000, Item.Electirizer),
    39000: (5000, Item.Refrigerator), 
    40000: (5000, Item.WhippedDream),
    43000: (1000, Item.KelpsySmoothie),
    44444: (4444, Item.ReaperCloth),
    45000: (30000, Item.HPUpConcentrate),
    47000: (5000, Item.GalaricaWreath),
    50000: (1200, Item.EnergyRoot),
    53000: (1000, Item.PomegSmoothie),
    55000: (30000, Item.IronConcentrate),
    57000: (5000, Item.Magmarizer),
    59347: (5000, Item.DubiousDisc),
    60000: (5000, Item.Microwave),
    63000: (1000, Item.QualotSmoothie),
    65000: (30000, Item.ProteinConcentrate),
    67000: (5000, Item.AuspiciousArmor),
    70000: (5000, Item.RazorClaw),
    73000: (1000, Item.GrepaSmoothie),
    74000: (5000, Item.DragonScale),
    75000: (30000, Item.CalciumConcentrate),
    77000: (50000, Item.MasterpieceTeacup),
    80000: (5000, Item.WashingMchn),
    83000: (5000, Item.MaliciousArmor),
    85000: (30000, Item.CarbosConcentrate),
    87000: (50000, Item.ChippedPot),
    90000: (5000, Item.RazorFang),
    93000: (5000, Item.KingsRock),
    95000: (2800, Item.RevivalHerb),
    97000: (5000, Item.EscapeRope),
    99000: (5000, Item.MetalAlloy),
    100000: (10000, Item.LinkCable)
}

define investmentthresholds = [0, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000]

define elementitems = {
    Item.SilkScarf: "Normal",
    Item.Charcoal: "Fire",
    Item.MysticWater: "Water",
    Item.MiracleSeed: "Grass",
    Item.Magnet: "Electric",
    Item.NeverMeltIce: "Ice",
    Item.BlackBelt: "Fighting",
    Item.PoisonBarb: "Poison",
    Item.SoftSand: "Ground",
    Item.SharpBeak: "Flying",
    Item.TwistedSpoon: "Psychic",
    Item.SilverPowder: "Bug",
    Item.HardStone: "Rock",
    Item.SpellTag: "Ghost",
    Item.BlackGlasses: "Dark",
    Item.DragonFang: "Dragon",
    Item.MetalCoat: "Steel",
    Item.FairyFeather: "Fairy"
}

init python:
    def GetItem(itemid, count = 1, text = None, audio = True, removing=False):
        if isinstance(itemid, str):
            itemname = itemid
            itemid = GetItemEntryFromName(itemname)[0]
        else:
            itemname = GetItemEntry(itemid)[1]
        
        if (not removing):
            if (audio):
                PlaySound("item_get.ogg")
            DisplayGetItem(itemid)

        if (itemid in inventory.keys()):
            inventory[itemid] += count
        else:
            inventory[itemid] = count

        if (not removing and text != None):
            if (text.lower() != "default"):
                renpy.say((None if not InDungeon() else dungeonnarrator), text)
            elif (text.lower() == "default"):
                preposition = "an" if itemname[0].lower() in ["a", "e", "i", "o", "u"] else "a"
                renpy.say((None if not InDungeon() else dungeonnarrator), "You got {} {}!".format(preposition, itemname))

    def LoseItem(item, count = 1):
        if isinstance(item, str):
            item = GetItemEntryFromName(item)[0]
        
        if (item in inventory and inventory[item] >= count):
            inventory[item] -= count

            if (inventory[item] <= 0):
                del inventory[item]
            
            return True

        return False

    def RemoveItem(pkmn):
        if (inbattle):
            renpy.invoke_in_new_context(renpy.say, None, "Please wait until the battle is over to unequip items.")
        else:
            GetItem(pkmn.Item, 1, audio = False, removing=True)
            pkmn.Item = None
            if (SecureShareAndEggAmount()):
                renpy.notify("An error occurred, and your number of Exp Shares/Lucky Eggs has been set back to 1. Please report this bug, as well as when this showed up, in the discord. TRIGGERED ON REMOVEITEM")

    def GetItemCount(item):
        if isinstance(item, str):
            item = GetItemEntryFromName(item)[0]
        
        for otheritem, amount in inventory.items():
            if (item == otheritem):
                return amount
        return 0

    def GiveItem(partymon, item):
        global activemon
        global invoverwrite
        activemon = partymon
        monnickname = partymon.GetNickname()
        olditem = partymon.GetItem()
        if (olditem == None):
            if (LoseItem(item)):
                partymon.GiveItem(item)
                invoverwrite = "{} was given the {}.".format(monnickname, GetItemName(item))
        else:
            invoverwrite = "{} is already holding the {}. Swap it for the {}?".format(monnickname, GetItemName(olditem), GetItemName(item))

    def SwapItems(item):
        global invoverwrite
        olditem = activemon.GetItem()
        if (LoseItem(item)):
            GetItem(olditem, removing = True)
            activemon.TakeItem()
            activemon.GiveItem(item)
            invoverwrite = "{} was given the {}, and you put the {} in your bag.".format(activemon.GetNickname(), GetItemName(item), GetItemName(olditem))
    
    def GetGiftValue(character, item):
        global giftedmysterygift
        if (character == "Leaf" and item == 80):
            return -1
        elif (character == "Misty" and item == 89):
            return -1
        elif (character == "Gardenia" and item == 91):
            return -1
        
        if (character in classdex.keys()):
            for shopitem in shopitems.values() or marketitems.value():
                if (item == shopitem[1]):
                    if (shopitem[0] < 500):
                        return 2
                    elif (shopitem[0] < 800):
                        return 3
                    elif (shopitem[0] < 1001):
                        return 4
                    elif (shopitem[0] < 5001):
                        return 5
                    else:
                        return 10
            
            if item in elementitems.keys() and elementitems[item] in GetCharTypes(character):
                return 5

            if item in treatboosts.keys() and treatboosts[item] in GetCharTypes(character):
                return 5

        elif (character == "Janine"):
            if (ItemHasTag(item, "likedByJanine")):
                return 5
        elif (character == "Professor Cherry"):
            if ItemHasTag(item, "rotom catalog"):
                return 20
            elif ItemHasTag(item, "move boost item"):
                return 5
        elif (character == "Ethan"):
            return 5

        return GetItemEntry(item)[7]

    def GetItemSellValue(item):
        global soldmysterygift
        returnvalue = 100
        for shopitem in list(shopitems.values()) + list(marketitems.values()) + list(treatitems.values()):
            if (item == shopitem[1]):
                returnvalue = shopitem[0] / 4.0
                break
        if (item in elementitems.keys()):
            returnvalue = 250
        if (item == 226):
            returnvalue = 2000
        return math.floor(returnvalue)

    def HasItem(item):
        if isinstance(item, str):
            item = GetItemEntryFromName(item)[ItemdexMacros.Id]
        return item in inventory.keys()

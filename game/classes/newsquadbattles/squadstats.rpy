#<Name> : {"Stats": {"Courage": num, "Wit": num, "Knowledge": num, "Patience": num, "Charm": num}, "Skills": ["skill1", "skill2", "skill3"], "Class": "name" } 

init python:
    def GetSkill(character, skill, total=False):
        charactername = character.GetFormatName()
        bonus = (0 if not total else GetSquadStat(character, GetSkillStat(skill)))
        if (character.Name == "red" and skill in dungeonskills):
            return 3 + bonus
        elif (charactername not in squadstats.keys() or skill not in squadstats[charactername]["Skills"]):
            return bonus
        else:
            return 3 + bonus

    def GetSquadStat(character, stat):
        charactername = character.GetFormatName()
        if (character.Name == "red"):
            return 5 - GetRankOfStat(stat)
        elif (charactername not in squadstats.keys() or stat not in squadstats[charactername]["Stats"].keys()):
            return 0
        else:
            return squadstats[charactername]["Stats"][stat]

    def RankPlayerSquadStats(rank):
        return sorted(personalstats.items(), key=lambda x:x[1], reverse=True)[rank][0]
    
    def GetRankOfStat(stat):
        for i in range(5):
            if (RankPlayerSquadStats(i) == stat):
                return i

    def GetSkillStat(skill):
        if (skill in ["Risk-Taking", "Resilience", "Physicality"]):
            return "Courage"
        elif (skill in ["Cunning", "Adaptability", "Strategy"]):
            return "Wit"
        elif (skill in ["Pokémon Smarts", "Lore Smarts", "World Smarts"]):
            return "Knowledge"
        elif (skill in ["Learning", "Healing", "Leadership"]):
            return "Patience"
        elif (skill in ["Persuasion", "Deception", "Pokémon Handling"]):
            return "Charm"
        else:
            return "ERROR. Typo, probably."

    def GetClass(squadder):
        return squadder.GetDungeonClass()

define squadstats = {
    "Yellow" : {"Stats": {"Courage": 1, "Wit": 2, "Knowledge": 3, "Patience": 5, "Charm": 4}, "Skills": ["Resilience", "Pokémon Handling", "Healing"], "Class": "Life Cleric" },
    "Ethan" : {"Stats": {"Courage": 2, "Wit": 4, "Knowledge": 3, "Patience": 5, "Charm": 1}, "Skills": ["Risk-Taking", "Deception", "Cunning"], "Class": "Twinblade Rogue" },
    "Leaf" : {"Stats": {"Courage": 2, "Wit": 4, "Knowledge": 3, "Patience": 1, "Charm": 5}, "Skills": ["Strategy", "Persuasion", "World Smarts"], "Class": "Black Mage" },
    "Cheren" : {"Stats": {"Courage": 3, "Wit": 4, "Knowledge": 5, "Patience": 2, "Charm": 1}, "Skills": ["Leadership", "Cunning", "Lore Smarts"], "Class": "Justice Cleric" },
    "Skyla" : {"Stats": {"Courage": 5, "Wit": 1, "Knowledge": 3, "Patience": 2, "Charm": 4}, "Skills": ["Physicality", "Adaptability", "Learning"], "Class": "Valiant Hero" },
    "Silver" : {"Stats": {"Courage": 5, "Wit": 4, "Knowledge": 3, "Patience": 2, "Charm": 1}, "Skills": ["Physicality", "Cunning", "Leadership"], "Class": "Shadowsplitter" },
    "Whitney" : {"Stats": {"Courage": 2, "Wit": 4, "Knowledge": 1, "Patience": 3, "Charm": 5}, "Skills": ["Healing", "World Smarts", "Persuasion"], "Class": "Charming Bard" },
    "Flannery" : {"Stats": {"Courage": 5, "Wit": 4, "Knowledge": 3, "Patience": 1, "Charm": 2}, "Skills": ["Adaptability", "Risk-Taking", "Pokémon Smarts"], "Class": "Wild Mage" },
    "Nessa" : {"Stats": {"Courage": 1, "Wit": 4, "Knowledge": 3, "Patience": 5, "Charm": 2}, "Skills": ["Resilience", "Learning", "Strategy"], "Class": "Gilded Shield" },
    "Sonia" : {"Stats": {"Courage": 1, "Wit": 3, "Knowledge": 5, "Patience": 4, "Charm": 2}, "Skills": ["Lore Smarts", "Learning", "Pokémon Handling"], "Class": "Scholar" },
    "Rosa" : {"Stats": {"Courage": 4, "Wit": 3, "Knowledge": 2, "Patience": 1, "Charm": 5}, "Skills": ["Deception", "Risk-Taking", "Adaptability"], "Class": "Idol" },
    "Raihan" : {"Stats": {"Courage": 5, "Wit": 3, "Knowledge": 1, "Patience": 2, "Charm": 4}, "Skills": ["Persuasion", "Physicality", "World Smarts"], "Class": "Badass" }
}
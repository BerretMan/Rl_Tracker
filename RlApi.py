import json
from os import stat
import cloudscraper

class RLTRACKER:
    
    def bypass(self,arg):
        self.scraper = cloudscraper.create_scraper()
        self.url = self.scraper.get("https://api.tracker.gg/api/v2/rocket-league/standard/profile/epic/"+arg+"")
        self.jsonObject = json.loads(self.url.content)
        return self.jsonObject



#mode normal
    def solo(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][1]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][2]["stats"]['tier']['metadata']['name'])
    def duo(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][2]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][3]["stats"]['tier']['metadata']['name'])
    def trio(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][3]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][4]["stats"]['tier']['metadata']['name'])
        
    def solo_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][1]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][2]["stats"]['rating']['percentile'])
    def duo_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][2]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][3]["stats"]['rating']['percentile'])
    def trio_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][3]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][4]["stats"]['rating']['percentile'])

    def solo_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][1]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][2]["stats"]['rating']['value'])
    def duo_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][2]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][3]["stats"]['rating']['value'])
    def trio_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][3]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][4]["stats"]['rating']['value'])

    def solo_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][1]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][2]["stats"]['division']['metadata']['name'])
    def duo_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][2]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][3]["stats"]['division']['metadata']['name'])
    def trio_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][3]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][4]["stats"]['division']['metadata']['name'])

    def solo_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][1]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][2]["stats"]['matchesPlayed']['value'])
    def duo_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][2]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][3]["stats"]['matchesPlayed']['value'])
    def trio_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][3]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][4]["stats"]['matchesPlayed']['value'])

    def solo_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][1]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][2]["stats"]["winStreak"]["displayValue"])
    def duo_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][2]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][3]["stats"]["winStreak"]["displayValue"])
    def trio_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][3]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][4]["stats"]["winStreak"]["displayValue"])





#mode extra
    def panier(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][4]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][5]["stats"]['tier']['metadata']['name'])
    def rumble(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][5]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][6]["stats"]['tier']['metadata']['name'])
    def dropshot(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][6]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][7]["stats"]['tier']['metadata']['name'])
    def palet(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][7]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][8]["stats"]['tier']['metadata']['name'])
    def tournoi(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][8]["stats"]['tier']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][9]["stats"]['tier']['metadata']['name'])

    def panier_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][4]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][5]["stats"]['rating']['percentile'])
    def rumble_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][5]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][6]["stats"]['rating']['percentile'])
    def dropshot_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][6]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][7]["stats"]['rating']['percentile'])
    def palet_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][7]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][8]["stats"]['rating']['percentile'])
    def tournoi_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][8]["stats"]['rating']['percentile'])
        else:
            return(self.jsonObject['data']['segments'][9]["stats"]['rating']['percentile'])


    def panier_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][4]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][5]["stats"]['rating']['value'])
    def rumble_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][5]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][6]["stats"]['rating']['value'])
    def dropshot_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][6]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][7]["stats"]['rating']['value'])
    def palet_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][7]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][8]["stats"]['rating']['value'])
    def tournoi_mmr(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][8]["stats"]['rating']['value'])
        else:
            return(self.jsonObject['data']['segments'][9]["stats"]['rating']['value'])

    def panier_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][4]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][5]["stats"]['division']['metadata']['name'])
    def rumble_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][5]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][6]["stats"]['division']['metadata']['name'])
    def dropshot_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][6]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][7]["stats"]['division']['metadata']['name'])
    def palet_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][7]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][8]["stats"]['division']['metadata']['name'])
    def tournoi_div(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][8]["stats"]['division']['metadata']['name'])
        else:
            return(self.jsonObject['data']['segments'][9]["stats"]['division']['metadata']['name'])

    def panier_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][4]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][5]["stats"]['matchesPlayed']['value'])
    def rumble_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][5]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][6]["stats"]['matchesPlayed']['value'])
    def dropshot_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][6]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][7]["stats"]['matchesPlayed']['value'])
    def palet_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][7]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][8]["stats"]['matchesPlayed']['value'])
    def tournoi_nb(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][8]["stats"]['matchesPlayed']['value'])
        else:
            return(self.jsonObject['data']['segments'][9]["stats"]['matchesPlayed']['value'])

    def panier_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][4]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][5]["stats"]["winStreak"]["displayValue"])
    def rumble_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][5]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][6]["stats"]["winStreak"]["displayValue"])
    def dropshot_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][6]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][7]["stats"]["winStreak"]["displayValue"])
    def palet_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][7]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][8]["stats"]["winStreak"]["displayValue"])
    def tournoi_ws(self, arg):
        RLTRACKER.bypass(self, arg)
        check=self.jsonObject['data']['segments'][1]["metadata"]['name']
        if check=="Ranked Duel 1v1":
            return(self.jsonObject['data']['segments'][8]["stats"]["winStreak"]["displayValue"])
        else:
            return(self.jsonObject['data']['segments'][9]["stats"]["winStreak"]["displayValue"])






#info joueur
    def user_id(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['userId'])
    def premium(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['isPremium'])
    def verifier(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['isVerified'])
    def influencer(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['isInfluencer'])
    def partner(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['isPartner'])
    def pays(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['countryCode'])
    def compte(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['socialAccounts']) 
    def profil(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['pageviews']) 
    def louche(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['userInfo']['isSuspicious']) 
    def player_id(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['metadata']['playerId']) 






#stats
    def wins(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['wins']['value'])   
    def wins_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['wins']['percentile'])  

    def goals(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['goals']['value'])   
    def goals_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['goals']['percentile'])   

    def MVPs(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['mVPs']['value'])   
    def MVPs_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['mVPs']['percentile'])  

    def saves(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['saves']['value'])   
    def saves_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['saves']['percentile'])   

    def assists(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['assists']['value'])   
    def assists_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['assists']['percentile'])   

    def shots(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['shots']['value'])   
    def shots_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['shots']['percentile'])  

    def goalShotRatio(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['goalShotRatio']['value'])   
    def goalShotRatio_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['goalShotRatio']['percentile'])  

    def seasonReward(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['seasonRewardLevel']['metadata']['rankName'])   
    def seasonReward_pourcent(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['seasonRewardLevel']['percentile'])   
    def seasonReward_wins(self, arg):
        RLTRACKER.bypass(self, arg)
        return(self.jsonObject['data']['segments'][0]['stats']['seasonRewardWins']['value'])   





#info saison
    def saison(self):
        self.scraper = cloudscraper.create_scraper()
        self.url = self.scraper.get("https://api.tracker.gg/api/v2/rocket-league/standard/profile/epic/vorace32")
        self.jsonObject = json.loads(self.url.content)
        return(self.jsonObject['data']['metadata']['currentSeason'])
    






rltracker = RLTRACKER()

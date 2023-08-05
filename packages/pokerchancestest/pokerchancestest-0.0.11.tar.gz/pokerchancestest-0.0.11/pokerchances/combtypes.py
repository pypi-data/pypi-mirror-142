class combtypes:
    def combtypes(self):
        self.cards = ["A_spades", "K_spades", "Q_spades", "J_spades","10_spades",
                    "9_spades", "8_spades", "7_spades", "6_spades", "5_spades",
                    "4_spades", "3_spades", "2_spades",
                        
                    "A_clubs","K_clubs", "Q_clubs", "J_clubs", "10_clubs",
                    "9_clubs", "8_clubs", "7_clubs", "6_clubs", "5_clubs",
                    "4_clubs", "3_clubs", "2_clubs",
                        
                    "A_diamonds", "K_diamonds", "Q_diamonds", "J_diamonds", "10_diamonds",
                    "9_diamonds", "8_diamonds", "7_diamonds", "6_diamonds", "5_diamonds",
                    "4_diamonds", "3_diamonds", "2_diamonds",
                        
                    "A_hearts", "K_hearts", "Q_hearts", "J_hearts", "10_hearts",
                    "9_hearts", "8_hearts", "7_hearts", "6_hearts", "5_hearts",
                    "4_hearts", "3_hearts", "2_hearts"]

        self.straights_1 = ["A","K","Q","J","10"]
        self.straights_2 = ["K","Q","J","10","9"]
        self.straights_3 = ["Q","J","10","9","8"]
        self.straights_4 = ["J","10","9","8","7"]
        self.straights_5 = ["10","9","8","7","6"]
        self.straights_6 = ["9","8","7","6","5"]
        self.straights_7 = ["8","7","6","5","4"]
        self.straights_8 = ["7","6","5","4","3"]
        self.straights_9 = ["6","5","4","3","2"]
        self.straights_10 = ["5","4","3","2","A"]
        self.spades_flush = ["A_spades", "K_spades", "Q_spades", "J_spades","10_spades",
                                "9_spades", "8_spades", "7_spades", "6_spades", "5_spades",
                                "4_spades", "3_spades", "2_spades"]

        self.clubs_flush = ["A_clubs","K_clubs", "Q_clubs", "J_clubs", "10_clubs",
                            "9_clubs", "8_clubs", "7_clubs", "6_clubs", "5_clubs",
                            "4_clubs", "3_clubs", "2_clubs"]

        self.diamonds_flush = ["A_diamonds", "K_diamonds", "Q_diamonds", "J_diamonds", "10_diamonds",
                               "9_diamonds", "8_diamonds", "7_diamonds", "6_diamonds", "5_diamonds",
                               "4_diamonds", "3_diamonds", "2_diamonds"]

        self.hearts_flush = ["A_hearts", "K_hearts", "Q_hearts", "J_hearts", "10_hearts",
                             "9_hearts", "8_hearts", "7_hearts", "6_hearts", "5_hearts",
                             "4_hearts", "3_hearts", "2_hearts"]
        
        self.spades_straightflush = [["A_spades", "K_spades", "Q_spades", "J_spades","10_spades"], ["K_spades", "Q_spades", "J_spades", "10_spades", "9_spades"],
                                     ["Q_spades", "J_spades", "10_spades", "9_spades", "8_spades"], ["J_spades", "10_spades", "9_spades", "8_spades", "7_spades"],
                                     ["10_spades", "9_spades", "8_spades", "7_spades", "6_spades"], ["9_spades", "8_spades", "7_spades", "6_spades", "5_spades"],
                                     ["8_spades", "7_spades", "6_spades", "5_spades", "4_spades"], ["7_spades", "6_spades", "5_spades", "4_spades", "3_spades"],
                                     ["6_spades", "5_spades", "4_spades", "3_spades", "2_spades"], ["5_spades", "4_spades", "3_spades", "2_spades", "A_spades"]]

        #self.spades_straightflush = ["A_spades", "K_spades", "Q_spades", "J_spades","10_spades"]
        #self.spades_straightflush1 = ["K_spades", "Q_spades", "J_spades", "10_spades", "9_spades"]
        #self.spades_straightflush2 = ["Q_spades", "J_spades", "10_spades", "9_spades", "8_spades"]
        #self.spades_straightflush3 = ["J_spades", "10_spades", "9_spades", "8_spades", "7_spades"]
        #self.spades_straightflush4 = ["10_spades", "9_spades", "8_spades", "7_spades", "6_spades"]
        #self.spades_straightflush5 = ["9_spades", "8_spades", "7_spades", "6_spades", "5_spades"]
        #self.spades_straightflush6 = ["8_spades", "7_spades", "6_spades", "5_spades", "4_spades"]
        #self.spades_straightflush7 = ["7_spades", "6_spades", "5_spades", "4_spades", "3_spades"]
        #self.spades_straightflush8 = ["6_spades", "5_spades", "4_spades", "3_spades", "2_spades"]
        #self.spades_straightflush9 = ["5_spades", "4_spades", "3_spades", "2_spades", "A_spades"]

        self.clubs_straightflush = [["A_clubs","K_clubs", "Q_clubs", "J_clubs", "10_clubs"], ["K_clubs", "Q_clubs", "J_clubs", "10_clubs", "9_clubs"],
                                    ["Q_clubs", "J_clubs", "10_clubs", "9_clubs", "8_clubs"], ["J_clubs", "10_clubs", "9_clubs", "8_clubs", "7_clubs"],
                                    ["10_clubs", "9_clubs", "8_clubs", "7_clubs", "6_clubs"], ["9_clubs", "8_clubs", "7_clubs", "6_clubs", "5_clubs"],
                                    ["8_clubs", "7_clubs", "6_clubs", "5_clubs", "4_clubs"], ["7_clubs", "6_clubs", "5_clubs", "4_clubs", "3_clubs"],
                                    ["6_clubs", "5_clubs", "4_clubs", "3_clubs", "2_clubs"], ["5_clubs", "4_clubs", "3_clubs", "2_clubs", "A_clubs"]]

        #self.clubs_straightflush = ["A_clubs","K_clubs", "Q_clubs", "J_clubs", "10_clubs"]
        #self.clubs_straightflush1 = ["K_clubs", "Q_clubs", "J_clubs", "10_clubs", "9_clubs"]
        #self.clubs_straightflush2 = ["Q_clubs", "J_clubs", "10_clubs", "9_clubs", "8_clubs"]
        #self.clubs_straightflush3 = ["J_clubs", "10_clubs", "9_clubs", "8_clubs", "7_clubs"]
        #self.clubs_straightflush4 = ["10_clubs", "9_clubs", "8_clubs", "7_clubs", "6_clubs"]
        #self.clubs_straightflush5 = ["9_clubs", "8_clubs", "7_clubs", "6_clubs", "5_clubs"]
        #self.clubs_straightflush6 = ["8_clubs", "7_clubs", "6_clubs", "5_clubs", "4_clubs"]
        #self.clubs_straightflush7 = ["7_clubs", "6_clubs", "5_clubs", "4_clubs", "3_clubs"]
        #self.clubs_straightflush8 = ["6_clubs", "5_clubs", "4_clubs", "3_clubs", "2_clubs"]
        #self.clubs_straightflush9 = ["5_clubs", "4_clubs", "3_clubs", "2_clubs", "A_clubs"]

        self.diamonds_straightflush = [["A_diamonds", "K_diamonds", "Q_diamonds", "J_diamonds", "10_diamonds"], ["K_diamonds", "Q_diamonds", "J_diamonds", "10_diamonds", "9_diamonds"],
                                       ["Q_diamonds", "J_diamonds", "10_diamonds", "9_diamonds", "8_diamonds"], ["J_diamonds", "10_diamonds", "9_diamonds", "8_diamonds", "7_diamonds"],
                                       ["10_diamonds", "9_diamonds", "8_diamonds", "7_diamonds", "6_diamonds"], ["9_diamonds", "8_diamonds", "7_diamonds", "6_diamonds", "5_diamonds"],
                                       ["8_diamonds", "7_diamonds", "6_diamonds", "5_diamonds", "4_diamonds"], ["7_diamonds", "6_diamonds", "5_diamonds", "4_diamonds", "3_diamonds"],
                                       ["6_diamonds", "5_diamonds", "4_diamonds", "3_diamonds", "2_diamonds"], ["5_diamonds", "4_diamonds", "3_diamonds", "2_diamonds", "A_diamonds"]]

        #self.diamonds_straightflush = ["A_diamonds", "K_diamonds", "Q_diamonds", "J_diamonds", "10_diamonds"]
        #self.diamonds_straightflush1 = ["K_diamonds", "Q_diamonds", "J_diamonds", "10_diamonds", "9_diamonds"]
        #self.diamonds_straightflush2 = ["Q_diamonds", "J_diamonds", "10_diamonds", "9_diamonds", "8_diamonds"]
        #self.diamonds_straightflush3 = ["J_diamonds", "10_diamonds", "9_diamonds", "8_diamonds", "7_diamonds"]
        #self.diamonds_straightflush4 = ["10_diamonds", "9_diamonds", "8_diamonds", "7_diamonds", "6_diamonds"]
        #self.diamonds_straightflush5 = ["9_diamonds", "8_diamonds", "7_diamonds", "6_diamonds", "5_diamonds"]
        #self.diamonds_straightflush6 = ["8_diamonds", "7_diamonds", "6_diamonds", "5_diamonds", "4_diamonds"]
        #self.diamonds_straightflush7 = ["7_diamonds", "6_diamonds", "5_diamonds", "4_diamonds", "3_diamonds"]
        #self.diamonds_straightflush8 = ["6_diamonds", "5_diamonds", "4_diamonds", "3_diamonds", "2_diamonds"]
        #self.diamonds_straightflush9 = ["5_diamonds", "4_diamonds", "3_diamonds", "2_diamonds", "A_diamonds"]

        self.hearts_straightflush = [["A_hearts", "K_hearts", "Q_hearts", "J_hearts", "10_hearts"], ["K_hearts", "Q_hearts", "J_hearts", "10_hearts", "9_hearts"],
                                     ["Q_hearts", "J_hearts", "10_hearts", "9_hearts", "8_hearts"], ["J_hearts", "10_hearts", "9_hearts", "8_hearts", "7_hearts"],
                                     ["10_hearts", "9_hearts", "8_hearts", "7_hearts", "6_hearts"], ["9_hearts", "8_hearts", "7_hearts", "6_hearts", "5_hearts"],
                                     ["8_hearts", "7_hearts", "6_hearts", "5_hearts", "4_hearts"], ["7_hearts", "6_hearts", "5_hearts", "4_hearts", "3_hearts"],
                                     ["6_hearts", "5_hearts", "4_hearts", "3_hearts", "2_hearts"], ["5_hearts", "4_hearts", "3_hearts", "2_hearts", "A_hearts"]]
        
        return self.cards, self.straights_1, self.straights_2, self.straights_3, self.straights_4, self.straights_5, self.straights_6, self.straights_7, self.straights_8, self.straights_9, self.straights_10,self.spades_flush, self.clubs_flush, self.diamonds_flush, self.hearts_flush, self.spades_straightflush, self.clubs_straightflush, self.diamonds_straightflush, self.hearts_straightflush
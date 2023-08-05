#from combtypes import *

class chances:
    def __init__(self,enemy_count, player_card1, player_card2):
        
        cb = combtypes()
        

        self.cards, self.straights_1, self.straights_2, self.straights_3, self.straights_4, self.straights_5, self.straights_6, self.straights_7, self.straights_8, self.straights_9, self.straights_10,self.spades_flush, self.clubs_flush, self.diamonds_flush, self.hearts_flush, self.spades_straightflush, self.clubs_straightflush, self.diamonds_straightflush, self.hearts_straightflush = cb.combtypes()

        self.straight_chances = []
        self.straight_num = []

        self.straight_count_1 = 0
        self.straight_count_2 = 0
        self.straight_count_3 = 0
        self.straight_count_4 = 0
        self.straight_count_5 = 0
        self.straight_count_6 = 0
        self.straight_count_7 = 0
        self.straight_count_8 = 0
        self.straight_count_9 = 0
        self.straight_count_10 = 0
        self.ccc_1 = 4
        self.ccc_2 = 4
        self.ccc_3 = 4
        self.ccc_4 = 4
        self.ccc_5 = 4
        self.ccc_6 = 4
        self.ccc_7 = 4
        self.ccc_8 = 4
        self.ccc_9 = 4
        self.ccc_10 = 4

        #self.straights = [("A","K","Q","J","10"), ("K","Q","J","10","9"), ("Q","J","10","9","8"), ("J","10","9","8","7"),
                          #("10","9","8","7","6"), ("9","8","7","6","5"), ("8","7","6","5","4"), ("7","6","5","4","3"),
                          #("6","5","4","3","2"), ("5","4","3","2", "A")]

        self.enemy_num_for_straights = 0

        self.count_to_fix_pair_chance = 0

        

        
        self.enemy_count = enemy_count
        self.enemy_count_double = enemy_count*2
        self.player_card1 = player_card1
        self.player_card2 = player_card2
        self.player_hand_card_list  =[]

        self.type_of_card_list = []
        self.type_of_card_list2 = []
        self.amount_of_card_types_list = []
        self.amount_of_card_types_list2 = []
        

        split_first_card = self.player_card1.split("_")
        split_second_card = self.player_card2.split("_")

        self.player_1st_card_type =  split_first_card[0]
        self.player_1st_card_type1 = split_first_card[1]
        self.player_2nd_card_type = split_second_card[0]
        self.player_2nd_card_type1 = split_second_card[1]
        self.player_hand_card_list.append(self.player_1st_card_type)
        self.player_hand_card_list.append(self.player_2nd_card_type)
        print(self.player_1st_card_type)

        self.straightflush_chances = []
        self.straightflush_types = []
        
        self.jjj = 0


        self.count_for_flush = 0
        self.count_of_flushcards = 13

        


        #self.hearts_straightflush = ["A_hearts", "K_hearts", "Q_hearts", "J_hearts", "10_hearts"]
        #self.hearts_straightflush1 = ["K_hearts", "Q_hearts", "J_hearts", "10_hearts", "9_hearts"]
        #self.hearts_straightflush2 = ["Q_hearts", "J_hearts", "10_hearts", "9_hearts", "8_hearts"]
        #self.hearts_straightflush3 = ["J_hearts", "10_hearts", "9_hearts", "8_hearts", "7_hearts"]
        #self.hearts_straightflush4 = ["10_hearts", "9_hearts", "8_hearts", "7_hearts", "6_hearts"]
        #self.hearts_straightflush5 = ["9_hearts", "8_hearts", "7_hearts", "6_hearts", "5_hearts"]
        #self.hearts_straightflush6 = ["8_hearts", "7_hearts", "6_hearts", "5_hearts", "4_hearts"]
        #self.hearts_straightflush7 = ["7_hearts", "6_hearts", "5_hearts", "4_hearts", "3_hearts"]
        #self.hearts_straightflush8 = ["6_hearts", "5_hearts", "4_hearts", "3_hearts", "2_hearts"]
        #self.hearts_straightflush9 = ["5_hearts", "4_hearts", "3_hearts", "2_hearts", "A_hearts"]

        self.table_cards_list =[]

        self.spades_straightflush_count = 0
        self.clubs_straightflush_count = 0
        self.diamonds_straightflush_count = 0
        self.hearts_straightflush_count = 0


        self.cards.remove(player_card1)
        self.cards.remove(player_card2)
        if player_card1 in self.spades_flush:
            self.spades_flush.remove(player_card1)

        if player_card1 in self.clubs_flush:
            self.clubs_flush.remove(player_card1)

        if player_card1 in self.diamonds_flush:
            self.diamonds_flush.remove(player_card1)

        if player_card1 in self.hearts_flush:
            self.hearts_flush.remove(player_card1)

        if player_card2 in self.spades_flush:
            self.spades_flush.remove(player_card2)

        if player_card2 in self.clubs_flush:
            self.clubs_flush.remove(player_card2)

        if player_card2 in self.diamonds_flush:
            self.diamonds_flush.remove(player_card2)

        if player_card2 in self.hearts_flush:
            self.hearts_flush.remove(player_card2)

        self.count_for_flush_spades = 0
        self.count_for_flush_clubs = 0
        self.count_for_flush_diamonds = 0
        self.count_for_flush_hearts = 0

    def enemy_fold(self,enem_count):
        self.enemy_count = self.enemy_count - enem_count
        print("the new enemy count still playing is: ", self.enemy_count)

    def straightflush(self, table_card1):
        for self.straight_flush in self.spades_straightflush:
            if table_card1 in self.straight_flush:
                self.straight_flush.remove(table_card1)

        for self.straight_flush1 in self.clubs_straightflush:
            if table_card1 in self.straight_flush1:
                self.straight_flush1.remove(table_card1)
                
        for self.straight_flush2 in self.diamonds_straightflush:
            if table_card1 in self.straight_flush1:
                self.straight_flush2.remove(table_card1)
                
        for self.straight_flush3 in self.hearts_straightflush:
            if table_card1 in self.straight_flush1:
                self.straight_flush3.remove(table_card1)

    def straights(self,table_card_type):
        if table_card_type in self.straights_1:
            self.straight_count_1 += 1
            self.straights_1.remove(table_card_type)
            
        if table_card_type in self.straights_2:
            self.straight_count_2 += 1
            self.straights_2.remove(table_card_type)
            
        if table_card_type in self.straights_3:
            self.straight_count_3 += 1
            self.straights_3.remove(table_card_type)
            
        if table_card_type in self.straights_4:
            self.straight_count_4 += 1
            self.straights_4.remove(table_card_type)
            
        if table_card_type in self.straights_5:
            self.straight_count_5 += 1
            self.straights_5.remove(table_card_type)
            
        if table_card_type in self.straights_6:
            self.straight_count_6 += 1
            self.straights_6.remove(table_card_type)
            
        if table_card_type in self.straights_7:
            self.straight_count_7 += 1
            self.straights_7.remove(table_card_type)
            
        if table_card_type in self.straights_8:
            self.straight_count_8 += 1
            self.straights_8.remove(table_card_type)
            
        if table_card_type in self.straights_9:
            self.straight_count_9 += 1
            self.straights_9.remove(table_card_type)
            
        if table_card_type in self.straights_10:
            self.straight_count_10 += 1
            self.straights_10.remove(table_card_type)

    def pair_cards(self,cc2,split_table_card_type2):
        self.range_for_pair_cards = 0
        amount_of_cards_left_pairs = len(self.cards)
        self.hhh = 5
        self.amount_of_card_types_list2.append(cc2)
        self.type_of_card_list2.append(split_table_card_type2)
        for l in range(self.hhh*self.enemy_count):
                
            if self.amount_of_card_types_list2[self.range_for_pair_cards] != 0:
                chance_for_pair = (self.amount_of_card_types_list2[self.range_for_pair_cards]/amount_of_cards_left_pairs)*2
                print("chance for 1 person of having a: ",self.type_of_card_list2[self.range_for_pair_cards]," is: ", chance_for_pair)
                self.amount_of_card_types_list2[self.range_for_pair_cards] -= 1
                amount_of_cards_left_pairs -= 1
                self.count_to_fix_pair_chance +=1
                #self.range_for_pair_cards += 1
            
                
            if self.amount_of_card_types_list2[self.range_for_pair_cards] == 0 or self.amount_of_card_types_list2[self.range_for_pair_cards] <= 0:
                try:
                    self.type_of_card_list2.pop(self.range_for_pair_cards)
                    self.amount_of_card_types_list2.pop(self.range_for_pair_cards)
                    #print("juu",self.amount_of_card_types_list[self.range_for_pair_cards])
                    amount_of_cards_left_pairs = amount_of_cards_left_pairs + self.count_to_fix_pair_chance
                    self.count_to_fix_pair_chance = 0

                except:
                    break
            if len(self.amount_of_card_types_list2) == 0:
                break


        
    def table_cards(self,table_card):
        
        self.cards.remove(table_card)
        self.table_cards_list.append(table_card)

        
        
        cc = 3
        jj = 0
        self.split_table_card = table_card.split("_")
        self.split_table_card_type = self.split_table_card[0]
        self.type_of_card_list.append(self.split_table_card_type)
         
        for j in self.player_hand_card_list:
            if self.split_table_card_type == j:
                jj += 1


        cc -= jj
        self.amount_of_card_types_list.append(cc)
        #print(cc)

        if table_card in self.spades_flush:
            self.spades_flush.remove(table_card)
            self.count_for_flush_spades += 1

        if table_card in self.clubs_flush:
            self.clubs_flush.remove(table_card)
            self.count_for_flush_clubs += 1

        if table_card in self.diamonds_flush:
            self.diamonds_flush.remove(table_card)
            self.count_for_flush_diamonds += 1

        if table_card in self.hearts_flush:
            self.hearts_flush.remove(table_card)
            self.count_for_flush_hearts += 1


        self.pair_cards(cc, self.split_table_card_type)

        
        if len(self.table_cards_list) == 5:
            print('there are now 5 cards on the table, use the command: "end_round()", to see the odds')

        self.straights(self.split_table_card_type)
        self.straightflush(table_card)


    def end_round(self): 
        flush_chance1 =0
        self.amount_of_cards_of_spades_left = len(self.spades_flush)
        self.amount_of_cards_of_clubs_left = len(self.clubs_flush)
        self.amount_of_cards_of_diamonds_left = len(self.diamonds_flush)
        self.amount_of_cards_of_hearts_left = len(self.hearts_flush)
        self.amount_of_cards_in_pack = len(self.cards)
        self.range_for_pair_cards = 0
        amount_of_cards_left_pairs = len(self.cards)
        self.hhh = 5


        if self.count_for_flush_spades == 3:
            self.count_of_flushcards = self.amount_of_cards_of_spades_left
            self.count_for_flush = 3

            
        if self.count_for_flush_clubs == 3:
            self.count_of_flushcards = self.amount_of_cards_of_clubs_left
            self.count_for_flush = 3
            
        if self.count_for_flush_diamonds == 3:
            self.count_of_flushcards = self.amount_of_cards_of_diamonds_left
            self.count_for_flush = 3
            
        if self.count_for_flush_hearts == 3:
            self.count_of_flushcards = self.amount_of_cards_of_hearts_left
            self.count_for_flush = 3


        if self.count_for_flush_spades == 4:
            self.count_of_flushcards = self.amount_of_cards_of_spades_left
            self.count_for_flush = 4
            
        if self.count_for_flush_clubs == 4:
            self.count_of_flushcards = self.amount_of_cards_of_clubs_left
            self.count_for_flush = 4
            
        if self.count_for_flush_diamonds == 4:
            self.count_of_flushcards = self.amount_of_cards_of_diamonds_left
            self.count_for_flush = 4

            
        if self.count_for_flush_hearts == 4:
            self.count_of_flushcards = self.amount_of_cards_of_hearts_left
            self.count_for_flush = 4




        if self.count_for_flush == 3:
            for y in range(self.enemy_count_double):
                flush_chance = self.count_of_flushcards/self.amount_of_cards_in_pack
                b = (y+1)/2
                if b.is_integer() == False:
                    self.count_of_flushcards -= 1
                    self.amount_of_cards_in_pack -= 1
                    flush_chance1 = (flush_chance*(self.count_of_flushcards/self.amount_of_cards_in_pack))*2
                    self.count_of_flushcards -= 1
                    self.amount_of_cards_in_pack -= 1
                if b.is_integer() == True:
                    print("odds of ",b, "enemy of having a flush: ", flush_chance1)
                if self.count_of_flushcards == 0 or self.count_of_flushcards <= 0:
                    print("no more possible cards for a flush, rest of the players cant have a flush")
                    break
                
        if self.count_for_flush == 4:
            for ll_cards in range(self.enemy_count):
                flush_chance_one = self.count_of_flushcards/self.amount_of_cards_in_pack
                print(self.amount_of_cards_in_pack)
                print("odds of number ",(ll_cards+1),"enemy of having a flush: ", flush_chance_one)
                self.count_of_flushcards -= 1
                self.amount_of_cards_in_pack -= 1
                if self.count_of_flushcards == 0 or self.count_of_flushcards <= 0:
                    print("no more possible cards for a flush, rest of the players cant have a flush")
                    break

        print(self.amount_of_card_types_list)

        for l in range(self.hhh*self.enemy_count):
                
            if self.amount_of_card_types_list[self.range_for_pair_cards] != 0:
                chance_for_pair = (self.amount_of_card_types_list[self.range_for_pair_cards]/amount_of_cards_left_pairs)*2
                print("chance for 1 person of having a: ",self.type_of_card_list[self.range_for_pair_cards]," is: ", chance_for_pair)
                self.amount_of_card_types_list[self.range_for_pair_cards] -= 1
                amount_of_cards_left_pairs -= 1
                self.count_to_fix_pair_chance +=1
                #self.range_for_pair_cards += 1
            
                
            if self.amount_of_card_types_list[self.range_for_pair_cards] == 0 or self.amount_of_card_types_list[self.range_for_pair_cards] <= 0:
                try:
                    self.type_of_card_list.pop(self.range_for_pair_cards)
                    self.amount_of_card_types_list.pop(self.range_for_pair_cards)
                    #print("juu",self.amount_of_card_types_list[self.range_for_pair_cards])
                    amount_of_cards_left_pairs = amount_of_cards_left_pairs + self.count_to_fix_pair_chance
                    self.count_to_fix_pair_chance = 0

                except:
                    break
            if len(self.amount_of_card_types_list) == 0:
                break

        if self.straight_count_1 == 3 and self.straight_count_1 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(1)
                if self.player_1st_card_type in self.straights_1[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_1[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_1[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_1[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_2 == 3 and self.straight_count_2 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(2)
                if self.player_1st_card_type in self.straights_2[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_2[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_2[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_2[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_3 == 3 and self.straight_count_3 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(3)
                if self.player_1st_card_type in self.straights_3[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_3[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_3[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_3[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_4 == 3 and self.straight_count_4 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(4)
                if self.player_1st_card_type in self.straights_4[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_4[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_4[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_4[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_5 == 3 and self.straight_count_5 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(5)
                if self.player_1st_card_type in self.straights_5[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_5[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_5[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_5[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_6 == 3 and self.straight_count_6 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(6)
                if self.player_1st_card_type in self.straights_6[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_6[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_6[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_6[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_7 == 3 and self.straight_count_7 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(7)
                if self.player_1st_card_type in self.straights_7[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_7[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_7[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_7[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_8 == 3 and self.straight_count_8 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(8)
                if self.player_1st_card_type in self.straights_8[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_8[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_8[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_8[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_9 == 3 and self.straight_count_9 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(9)
                if self.player_1st_card_type in self.straights_9[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_9[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_9[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_9[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_10 == 3 and self.straight_count_10 <=3:
            self.straight_cards_left = 4
            self.straight_cards_left1 = 4
            for i in range(self.enemy_count):
                self.straight_num.append(10)
                if self.player_1st_card_type in self.straights_10[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_10[0]:
                    self.straight_cards_left -= 1
                if self.player_1st_card_type in self.straights_10[1]:
                    self.straight_cards_left1 -= 1
                if self.player_2nd_card_type in self.straights_10[1]:
                    self.straight_cards_left1 -= 1
                self.straight_chance = (self.straight_cards_left/45 * self.straight_cards_left1/44)*2
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                self.straight_cards_left1 -= 1
                if self.straight_cards_left == 0:
                    break
                if self.straight_cards_left1 == 0:
                    break

        if self.straight_count_1 == 4 and self.straight_count_1 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(1)
                if self.player_1st_card_type in self.straights_1[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_1[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                
        if self.straight_count_2 == 4 and self.straight_count_2 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(2)
                if self.player_1st_card_type in self.straights_2[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_2[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                
        if self.straight_count_3 == 4 and self.straight_count_3 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(3)
                if self.player_1st_card_type in self.straights_3[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_33[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                
                
        if self.straight_count_4 == 4 and self.straight_count_4 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(4)
                if self.player_1st_card_type in self.straights_4[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_4[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                
                
        if self.straight_count_5 == 4 and self.straight_count_5 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(5)
                if self.player_1st_card_type in self.straights_5[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_5[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                
        if self.straight_count_6 == 4 and self.straight_count_6 <= 4:
            self.straight_cards_left = 4
            self.straight_num.append(6)
            for i in range(self.enemy_count):
                if self.player_1st_card_type in self.straights_6[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_6[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                

        if self.straight_count_7 == 4 and self.straight_count_7 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(7)
                if self.player_1st_card_type in self.straights_7[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_7[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                

        if self.straight_count_8 == 4 and self.straight_count_8 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(8)
                if self.player_1st_card_type in self.straights_8[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_8[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                

        if self.straight_count_9 == 4 and self.straight_count_9 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(9)
                if self.player_1st_card_type in self.straights_9[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_9[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                
                
        if self.straight_count_10 == 4 and self.straight_count_10 <= 4:
            self.straight_cards_left = 4
            
            for i in range(self.enemy_count):
                self.straight_num.append(10)
                if self.player_1st_card_type in self.straights_10[0]:
                    self.straight_cards_left -= 1
                if self.player_2nd_card_type in self.straights_10[0]:
                    self.straight_cards_left -= 1
                self.straight_chance = self.straight_cards_left/45
                self.straight_chances.append(self.straight_chance)
                self.straight_cards_left -= 1
                if self.straight_cards_left == 0:
                    break
                
            

        self.straight_chances_length = len(self.straight_chances)
        self.straight_types_count = len(self.straight_num)
        #amount_of_chances_per_straight_type = self.straight_chances_length/self.straight_types_count
        straight_chance_cycles = 0
        for straight_chances_count in self.straight_chances:
            print("the chance for 1 of the opponents to have a straight number ", self.straight_num[straight_chance_cycles],": ", straight_chances_count)
            straight_chance_cycles += 1
            #if straight_chance_cycles == amount_of_chances_per_straight_type or straight_chance_cycles >= amount_of_chances_per_straight_type:
                #self.enemy_num_for_straights += 1

        for straight_flush_chance in self.spades_straightflush:
            self.spades_cards_left1 = 2
            self.spades_cards_left2 = 2
            if len(straight_flush_chance) == 2:
                if self.player_card1 in self.straight_flush[0]:
                    self.spades_cards_left1 -= 1
                if self.player_card1 in self.straight_flush[1]:
                    self.spades_cards_left2 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.spades_cards_left1 -= 1
                if self.player_card2 in self.straight_flush[1]:
                    self.spades_cards_left2 -= 1


                self.spades_straightflush_chance = (self.spades_cards_left1/45 * self.spades_cards_left2/44)*2
                self.straightflush_chances.append(self.spades_straightflush_chance)
                self.straightflush_types.append("spades_straightflush")
                self.spades_cards_left1 -= 1
                self.spades_cards_left2 -= 1

                if self.spades_cards_left1 == 0:
                    break
                if self.spades_cards_left2 == 0:
                    break

        for straight_flush_chance in self.clubs_straightflush:
            self.clubs_cards_left1 = 2
            self.clubs_cards_left2 = 2
            if len(straight_flush_chance) == 2:
                if self.player_card1 in self.straight_flush[0]:
                    self.clubs_cards_left1 -= 1
                if self.player_card1 in self.straight_flush[1]:
                    self.clubs_cards_left2 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.clubs_cards_left -= 1
                if self.player_card2 in self.straight_flush[1]:
                    self.clubs_cards_left2 -= 1

                self.clubs_straightflush_chance = (self.clubs_cards_left1/45 * self.clubs_cards_left2/44)*2
                self.straightflush_types.append("clubs_straightflush")
                self.straightflush_chances.append(self.clubs_straightflush_chance)
                if self.clubs_cards_left1 == 0:
                    break
                if self.clubs_cards_left2 == 0:
                    break
        for straight_flush_chance in self.diamonds_straightflush:
            self.diamonds_cards_left1 = 2
            self.diamonds_cards_left2 = 2
            if len(straight_flush_chance) == 2:
                if self.player_card1 in self.straight_flush[0]:
                    self.diamonds_cards_left1 -= 1
                if self.player_card1 in self.straight_flush[1]:
                    self.diamonds_cards_left2 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.diamonds_cards_left1 -= 1
                if self.player_card2 in self.straight_flush[1]:
                    self.diamonds_cards_left2 -= 1

                self.diamonds_straightflush_chance = (self.diamonds_cards_left1/45 * self.diamonds_cards_left2/44)*2
                self.straightflush_chances.append(self.diamonds_straightflush_chance)
                self.straightflush_types.append("diamonds_straightflush")
                self.diamonds_cards_left1 -= 1
                self.diamonds_cards_left2 -= 1

                if self.diamonds_cards_left1 == 0:
                    break
                if self.diamonds_cards_left2 == 0:
                    break
        for straight_flush_chance in self.hearts_straightflush:
            self.hearts_cards_left1 = 2
            self.hearts_cards_left2 = 2
            if len(straight_flush_chance) == 2:
                if self.player_card1 in self.straight_flush[0]:
                    self.hearts_cards_left1 -= 1
                if self.player_card1 in self.straight_flush[1]:
                    self.hearts_cards_left2 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.hearts_cards_left1 -= 1
                if self.player_card2 in self.straight_flush[1]:
                    self.hearts_cards_left2 -= 1

                self.hearts_straightflush_chance = (self.hearts_cards_left1/45 * self.hearts_cards_left2/44)*2
                self.straightflush_chances.append(self.hearts_straightflush_chance)
                self.straightflush_types.append("hearts_straightflush")
                self.hearts_cards_left1 -= 1
                self.hearts_cards_left2 -= 1

                if self.hearts_cards_left1 == 0:
                    break
                if self.hearts_cards_left2 == 0:
                    break

        for straight_flush_chance in self.spades_straightflush:
            self.spades_cards_left1 = 1
            if len(straight_flush_chance) == 1:
                if self.player_card1 in self.straight_flush[0]:
                    self.spades_cards_left1 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.spades_cards_left1 -= 1

                if self.spades_cards_left1 == 0:
                    break

                self.spades_straightflush_chance = self.spades_cards_left1/45
                self.straightflush_chances.append(self.spades_straightflush_chance)
                self.straightflush_types.append("spades_straightflush")
                self.spades_cards_left1 -= 1
                
        for straight_flush_chance in self.clubs_straightflush:
            self.clubs_cards_left1 = 1
            if len(straight_flush_chance) == 1:
                if self.player_card1 in self.straight_flush[0]:
                    self.clubs_cards_left1 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.clubs_cards_left1 -= 1

                if self.clubs_cards_left1 == 0:
                    break

                self.spades_straightflush_chance = self.clubs_cards_left1/45
                self.straightflush_chances.append(self.clubs_straightflush_chance)
                self.straightflush_types.append("clubs_straightflush")
                self.clubs_cards_left1 -= 1


        for straight_flush_chance in self.diamonds_straightflush:
            self.diamonds_cards_left1 = 1
            if len(straight_flush_chance) == 1:
                if self.player_card1 in self.straight_flush[0]:
                    self.diamonds_cards_left1 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.diamonds_cards_left1 -= 1

                if self.diamonds_cards_left1 == 0:
                    break

                self.spades_straightflush_chance = self.diamonds_cards_left1/45
                self.straightflush_chances.append(self.diamonds_straightflush_chance)
                self.straightflush_types.append("diamonds_straightflush")
                self.diamonds_cards_left1 -= 1

        for straight_flush_chance in self.hearts_straightflush:
            self.hearts_cards_left1 = 1
            if len(straight_flush_chance) == 1:
                if self.player_card1 in self.straight_flush[0]:
                    self.hearts_cards_left1 -= 1
                if self.player_card2 in self.straight_flush[0]:
                    self.hearts_cards_left1 -= 1

                if self.hearts_cards_left1 == 0:
                    break

                self.spades_straightflush_chance = self.hearts_cards_left1/45
                self.straightflush_chances.append(self.hearts_straightflush_chance)
                self.straightflush_types.append("hearts_straightflush")
                self.hearts_cards_left1 -= 1



        self.straightflush_type_cycle_count = 0
        for straightflush_chances_count in self.straightflush_chances:
            print("the chance for 1 of the opponents to have a straightflush of type: ", self.straightflush_types[self.straightflush_type_cycle_count], " is: ", straightflush_chances_count)
            self.straightflush_type_cycle_count += 1
                           
                
                
print(__name__)

if __name__ == "__main__":              
    h = chances(10,"J_diamonds", "4_spades")
    h.enemy_fold(2)
    h.table_cards("Q_spades")
    h.table_cards("J_spades")
    h.table_cards("A_spades")
    h.table_cards("K_hearts")
    h.table_cards("3_diamonds")
    h.end_round()

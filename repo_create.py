import os

# Level 0

path_1 = './level_0/cave_of_questions/cave_of_apparel/cave_of_pants/cave_of_jorts'
path_2 = './level_0/cave_of_questions/cave_of_apparel/cave_of_pants/jeans.txt'
path_3 = './level_0/cave_of_questions/cave_of_apparel/cave_of_pants/leggings.txt'
path_4 = './level_0/cave_of_questions/cave_of_apparel/cave_of_pants/khaki.txt'
path_5 = './level_0/cave_of_questions/cave_of_apparel/cave_of_pants/cave_of_jorts/clothes_of_shame.txt'
path_6 = './level_0/cave_of_questions/cave_of_apparel/cave_of_headwear/cave_of_sportscaps/'
path_6b = './level_0/cave_of_questions/cave_of_apparel/cave_of_headwear/cave_of_fabulous_hats/'
path_7 = './level_0/cave_of_questions/cave_of_apparel/cave_of_headwear/cave_of_sportscaps/sport_hat1.txt'
path_8 = './level_0/cave_of_questions/cave_of_apparel/cave_of_headwear/cave_of_sportscaps/sport_hat2.txt'
path_9 = './level_0/cave_of_questions/cave_of_apparel/cave_of_headwear/cave_of_fabulous_hats/the_green_hat_of_greatness.txt'

paths = [path_1, path_2, path_3, path_4, path_5, path_6,path_6b, path_7, path_8, path_9]


for path in paths:
    if 'txt' not in path:
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)

    else: 
        print(path)
        open(path, 'w')

# Level 1

path_1 = './level_1/cave_of_tools/cave_of_dentistry/'
path_2 = './level_1/cave_of_tools/cave_of_dentistry/tooth_decay.exe'
path_3 = './level_1/cave_of_tools/cave_of_destiny/make_your_own'
path_4 = './level_1/cave_of_tools/cave_of_destiny/make_your_own/find_a_sword.txt'
path_5 = './level_1/cave_of_tools/cave_of_destiny/make_your_own/get_an_education.exe'
path_6a = './level_1/cave_of_tools/cave_of_destiny/up_to_fate/'
path_6b = './level_1/cave_of_tools/cave_of_destiny/up_to_fate/dust_in_the_wind_lyrics.txt'
path_7a = './level_1/cave_of_omens/crystal_cave/'
path_7b = './level_1/cave_of_omens/crystal_cave/king_arthur.txt'
path_8 = './level_1/cave_of_omens/crystal_cave/arthurs_items'
path_9 = './level_1/cave_of_omens/crystal_cave/arthurs_items/sword_of_destiny.txt'
path_10 = './level_1/cave_of_omens/crystal_cave/arthurs_items/holy_grail.txt'

paths = [path_1,path_2,path_3,path_4,path_5,path_6a, path_6b,path_7a, path_7b,path_8,path_9,path_10]

for path in paths:
    if 'txt' not in path and 'exe' not in path:
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)

    else: 
        print(path)
        open(path, 'w')


# Level 2

path_1 = './level_2/cave_of_questions/cave_of_choices/cave_of_questionable_choices'
path_2 = './level_2/cave_of_questions/cave_of_choices/cave_of_questionable_choices/last_night.txt'
path_3a = './level_2/cave_of_questions/cave_of_choices/cave_of_questionable_choices/last_three_romantic_partners/'
path_3b = './level_2/cave_of_questions/cave_of_choices/cave_of_questionable_choices/last_three_romantic_partners/genna.txt'
path_4 = './level_2/cave_of_questions/cave_of_choices/cave_of_questionable_choices/last_three_romantic_partners/darrel.txt'
path_5 = './level_2/cave_of_questions/cave_of_choices/cave_of_questionable_choices/last_three_romantic_partners/name_i_cannot_remember.txt'
path_6 = './level_2/cave_of_questions/cave_of_choices/Key-to-forgotten-realms.txt'
path_7a = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/metaphors/'
path_7b = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/metaphors/doors.txt'
path_8 = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/metaphors/windows.txt'
path_9 = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/metaphors/paths.txt'
path_10 = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/metaphors/key_to_forgotten_realms.txt'
path_11a = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/cave_of_keys/dj_kaleed_quotes/'
path_11b = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/cave_of_keys/dj_kaleed_quotes/have_a_lot_of_pillows.txt'
path_12 = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/cave_of_keys/dj_kaleed_quotes/stop_and_smell_the_flowers.txt'
path_13 = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/cave_of_keys/dj_kaleed_quotes/dont_play_yourself.txt'
path_14 = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/cave_of_keys/dj_kaleed_quotes/keep_it_fresh.txt'
path_15 = './level_2/cave_of_questions/cave_of_choices/cave_of_new_beginnings/cave_of_keys/key-to-forgotten-realms.txt'

paths_l2 = [path_1, path_2, path_3a, path_3b, path_4, path_5, 
            path_6, path_7a, path_7b, path_8, path_9, path_10, 
            path_11a, path_11b, path_12, path_13, path_14, path_15]

for path in paths_l2:
    if 'txt' not in path and 'exe' not in path:
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)

    else: 
        print(path)
        open(path, 'w')

 
# Level 3
path_1 = './level_3/cave_of_cliches/dark_and_stormy_night'
path_2 = './level_3/cave_of_cliches/dark_and_stormy_night/unanswered_life_questions'
path_3 = './level_3/cave_of_cliches/dark_and_stormy_night/a_stranger_comes_to_town.txt'
path_4 = './level_3/cave_of_cliches/dark_and_stormy_night/man_goes_on_a_journey.txt'
path_5 = './level_3/cave_of_cliches/dark_and_stormy_night/Monster.exe'
path_6a = './level_3/cave_of_cliches/cave_of_deception/'
path_6b = './level_3/cave_of_cliches/cave_of_deception/nothing_here.txt'
path_7a = './level_3/cave_of_tropes/animal/'
path_7b = './level_3/cave_of_tropes/animal/best_muppet.exe'
path_8 = './level_3/cave_of_tropes/vegetable'
path_9 = './level_3/cave_of_tropes/mineral'
path_10a = './level_3/cave_of_tropes/dark_matter/scary_creatures/'
path_10b = './level_3/cave_of_tropes/dark_matter/scary_creatures/mom_when_mad.exe'
path_11 = './level_3/cave_of_tropes/dark_matter/scary_creatures/monster.exe'
path_11b = './level_3/cave_of_tropes/dark_matter/scary_creatures/sword_of_destruction.txt'
path_12a = './level_3/cave_of_plot_points/cave_of_loot/cave_of_fruit/'
path_12b = './level_3/cave_of_plot_points/cave_of_loot/cave_of_fruit/apple_of_appeasement.txt'
path_13 = './level_3/cave_of_plot_points/cave_of_loot/cave_of_fruit/banana_of_bygone_days.txt'
path_14 = './level_3/cave_of_plot_points/cave_of_loot/Apple_Of_Appeasement.txt'
path_15 = './level_3/cave_of_plot_points/cave_of_loot/orange_you_glad.txt'
path_16 = './level_3/cave_of_plot_points/cave_of_loot/armor.exe'

paths_l3 = [path_1, path_2, path_3, path_4, path_5, 
            path_6a, path_6b, path_7a, path_7b , path_8, 
            path_9, path_10a, path_10b, path_11, path_11b,
             path_12a, path_12b, path_13, path_14, path_15, path_16]

for path in paths_l3:
    if 'txt' not in path and 'exe' not in path:
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)

    else: 
        print(path)
        open(path, 'w')

# Level 4

path_1 = './level_4/cave_of_common_law/cave_a/cave_of_repetition/cave_of_heroes'
path_2a = './level_4/cave_of_common_law/cave_a/cave_of_repetition/cave_last_question/'
path_2b = './level_4/cave_of_common_law/cave_a/cave_of_repetition/cave_last_question/this_exerise_went_longer_than_anticipated.txt'
path_3 = './level_4/cave_of_common_law/cave_a/cave_of_repetition/cave_last_question/is_this_joke_over_yet.txt'
path_4a = './level_4/cave_of_common_law/cave_a/cave_of_suspicion/'
path_4b = './level_4/cave_of_common_law/cave_a/cave_of_suspicion/lame_jokes.txt'
path_5a = './level_4/cave_of_common_law/cave_h/cave_of_palace/east_wing/'
path_5b = './level_4/cave_of_common_law/cave_h/cave_of_palace/east_wing/princess.py'
path_6 = './level_4/cave_of_common_law/cave_h/cave_of_palace/east_wing/jester.ignore'
path_7a = './level_4/cave_of_common_law/cave_h/cave_of_palace/west_wing/'
path_7 = './level_4/cave_of_common_law/cave_h/cave_of_palace/west_wing/president.exe'
path_8 = './level_4/cave_of_common_law/cave_h/cave_of_palace/west_wing/monster.exe'
path_9 = './level_4/cave_of_common_law/cave_h/cave_of_palace/hereditary_power.py'
path_10 = './level_4/cave_of_common_law/cave_far_away/cave_of_protective_services'
path_11 = './level_4/cave_of_common_law/cave_far_away/cave_of_protective_services/donuts.txt'
path_12 = './level_4/cave_of_common_law/cave_far_away/cave_of_protective_services/forests.txt'
path_13 = './level_4/cave_of_common_law/cave_far_away/cave_of_protective_services/firewall.exe'
path_14a = './level_4/cave_of_common_law/cave_of_distractions/'
path_14b = './level_4/cave_of_common_law/cave_of_distractions/MONSTER.exe'
path_15 = './level_4/cave_of_common_law/cave_of_distractions/executive.py'
path_16a = './level_4/cave_of_common_law/cave_of_distractions/princess/'
path_16b = './level_4/cave_of_common_law/cave_of_distractions/princess/purple_rain.txt'
path_17 = './level_4/cave_of_common_law/cave_of_distractions/princess.exe'

paths_l4 = [path_1, path_2a, path_2b, path_3, path_4a, path_4b, 
         path_5a, path_5b, path_6, path_7a, path_8, path_9, 
         path_10, path_11, path_12, path_13, path_14a, 
         path_14b, path_15, path_16a,path_16b, path_17]
for path in paths_l4:
    if 'txt' not in path and 'exe' not in path and '.py' not in path and '.ignore not in path':
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)

    else: 
        print(path)
        open(path, 'w')
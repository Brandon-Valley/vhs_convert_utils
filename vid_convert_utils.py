import subprocess
# file_name = "2003_3_8_-_2003_4_20__Easter.mp4"
# file_name = "2000__2__5---2000__4_23------Easter.mp4"
# file_name = "1999_12_25---2000__1__7------Xmas_99.mp4"
# file_name = "1999_11_25---1999_12_25------Tgiving-Xmas_99.mp4"
# file_name = "1999__9__5---1999_11_25------Tgiving_99.mp4"
# file_name = "1999__8__1---1999__9__5------BV_2nd_Bday_Party.mp4"
# file_name = "1999_11__4---1999__7_30------NO_TITLE.mp4"
# file_name = "1999__2_27---1999__4_11------Arena_Demolition.mp4"
# file_name = "1998_12_25---1999__1_22------NO_TITLE.mp4"
# file_name = "1998_12__5---1998_12_25------NO_TITLE.mp4"
# file_name = "1998__8_16---1998_12__5------BV_1st_Haircut.mp4"
# file_name = "1998__8__9---1998__8_16------BAV_1st_Bday_Party.mp4"
# file_name = "1998__7__8---1998__8__9------BAV_1st_Bday_Party.mp4"           # yes, same name as ^^^
# file_name = "1998__6_17---1998__6_28------NO_TITLE.mp4"                     # start of 2nd row
# file_name = "1998__5__3---1998__6_17------NO_TITLE.mp4"
# file_name = "1998__4__4---1998__4_28------Brandon.mp4"
# file_name = "1998__3_14---1998__4__3------NO_TITLE.mp4"
# file_name = "1998__2__1---1998__3_14------Brandon.mp4"
# file_name = "1997_12_25---1998__1_29------Brandon.mp4"
# file_name = "1997_12__7---1997_12_25------Brandon.mp4"
# file_name = "1997_11_16---1997_11_27------Brandon.mp4"
# file_name = "1997_10_13---1997_11_16------Brandon.mp4"
# file_name = "1997__9_20---1997_10_13------Brandon.mp4"
# file_name = "1997__8_25---1997__9_20------Brandon.mp4"
# file_name = "1997__8_15---1997__8_23------Brandon.mp4"
# file_name = "1997__8__4---1997__8_14------Brandon.mp4"

# file_name = "2003__8__9---2003_11_18-----BV_Bday_party---1st_Day_of_1st_Grade---Halloween.mp4"
# file_name = "2003__5__0---2003__8__9-----KR_and_GV_Bath---BV_Bday_Party.mp4"
# file_name = "2003__5_22---2003__5_22-----2nd_Half_of_BV_Graduation_and_Play.mp4"
# file_name = "2003__4_20---2003__5_22-----Easter---BV_Graduation_and_Play_1st_Half.mp4"
# file_name = "2003__3__8---2003__4_20-----Easter.mp4"
# file_name = "2003__2__6---2003__3__7.mp4"
# file_name = "2002_12_25---2003__2__1.mp4"                                              # NO VID !!!!!!!!!!!!!!!!??????????????????????????????????????????????
# file_name = "2002_12_23---2002_12_25.mp4"                                              # NO VID !!!!!!!!!!!!!!!!
# file_name = "2002_12_12---2002_12_14-----BV_2nd_Half_Christmas_Play.mp4"
# file_name = "2002_11_27---2002_12_12-----Tgiving---1st_Half_of_BV_Christmas_Play.mp4"
# file_name = "2002_10_25---2002_11_27-----Pumpkin_Guts---House_Demolition.mp4"
# file_name = "2002_10__3---2002_10_25-----New_Kitchen---Snowbell.mp4"
# file_name = "2002__8__4---2002__9_30.mp4"
# file_name = "2002__8__4---2002__8_22.mp4"
# file_name = "2002__7_13---2002__8__3-----Bday_at_McD_for_BV.mp4"
# file_name = "2002__5_31---2002__7_13.mp4"
# file_name = "2002__4_27---2002__5_31-----BV_Pre-K_Graduation.mp4"
# file_name = "2002__3_31---2002__4_25-----Easter_at_Als---Easter_Egg_Hung_at_Church---Various_Kid_Footage.mp4"
# file_name = "2002__2__6---2002__3_31-----Easter_2002---Brandon_Bike_Riding.mp4"
# file_name = "2001_12_23---2002__1_19-----Christmas_2001---Kristen_and_Garrett_at_Home.mp4"
# file_name = "2001_11_17---2001_12_23-----Basement---Tgiving_at_Grandma_Roses---Hospital_12_4-12_5.mp4"
# file_name = "2001_10_25---2001_11_10-----Basement_and_Halloween_Costume.mp4"
# file_name = "2001__1_14---2001__9_10-----Easter.mp4"
# file_name = "2000_12_25---2001__1__7-----Xmas.mp4"
# file_name = "2000_11_23---2000_12_25-----Tgiving---Xmas.mp4"
# file_name = "2000__8__5---2000_11_23-----Bday_Party---Tgiving.mp4"


# file_name = "__________---__________-----Wrestling.mp4"
# file_name = "2005_12_25---2005__1_16-----Xmas---Sleding.mp4"
# file_name = "2005_10_16---2006__3_12-----Old_New_Busch_Stadium---Pumpkin_Carving---Halloween---Christmas---Snow_People---KRV_Swinging_By_Herself.mp4"
# file_name = "2005__7_17---2005__7_29-----Carlyle_Lake.mp4"
# file_name = "2004_12__6---2004_12_25-----K_and_G_Christmas_Presentation---Christmas_Eve_and_Next_Morning.mp4"
# file_name = "2004__9_13---2004_12__1-----BV_Open_House---Halloween_Treating---Carving_Pumpkin---BV_Choir_and_Advent_Consert---Decorate_Christmas_Tree.mp4"
# file_name = "2004__6_10---2004__9_13.mp4"
# file_name = "2004__4_11---2004__5_17-----Easter---BV_1st_Grade_Play---Neuman_the_Rooster.mp4"
# file_name = "2004__1_31---2004__4_11-----BV_Wrestling_Easter.mp4"
# file_name = "2003_12_25---2004__1_31-----Christmas_Morning_and_Afternoon---Jesse_Simmons_and_BV_Wrestling.mp4"
# file_name = "2003_11_28---2003_12_25-----GV_and_KR_2nd_Bday_Party---BV_1st_Wrestling_Matches.mp4"
# file_name = "Y_M_D---Y_M_D-----.mp4"

























RAW_VIDS_DIR_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\vhs_convert\\big_data\\raw_vids\\"

file_name = "2002_12_25---2003__2__1.mp4"









# file_name = "YEAR_M_D_-_YEAR_M_D__TITLE.mp4"


cmd = 'ffmpeg -framerate 25 -vsync 1 -video_size 640x480 -f dshow -rtbufsize 250000k -crossbar_video_input_pin_number 1 -crossbar_audio_input_pin_number 4  -i video="VIDBOX NW03 USB Video":audio="VIDBOX NW03 USB Video"   -t 0:31:30 -vf "fps=25,yadif=0:0:0,crop=w=640:h=480,hqdn3d=6:4:14:10,scale=640x480"   -c:v libx264 -preset medium -tune film -profile:v main -level 3.1 -pix_fmt yuv420p   -crf 25 -maxrate 1750k -bufsize 3500k -af "aresample=async=1000,highpass=200,lowpass=3500"  -c:a aac -b:a 96k -strict -2 -r 25 "' + RAW_VIDS_DIR_PATH  + file_name + '"'
print(cmd)
subprocess.call(cmd, shell = True)









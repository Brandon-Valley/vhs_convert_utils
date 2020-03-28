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














RAW_VIDS_DIR_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\vhs_convert\\big_data\\raw_vids\\"


file_name = "2000__2__5---2000__4_23------Easter.mp4"
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

# file_name = "YEAR_M_D_-_YEAR_M_D__TITLE.mp4"


cmd = 'ffmpeg -framerate 25 -vsync 1 -video_size 640x480 -f dshow -rtbufsize 250000k -crossbar_video_input_pin_number 1 -crossbar_audio_input_pin_number 4  -i video="VIDBOX NW03 USB Video":audio="VIDBOX NW03 USB Video"   -t 0:30:30 -vf "fps=25,yadif=0:0:0,crop=w=640:h=480,hqdn3d=6:4:14:10,scale=640x480"   -c:v libx264 -preset medium -tune film -profile:v main -level 3.1 -pix_fmt yuv420p   -crf 25 -maxrate 1750k -bufsize 3500k -af "aresample=async=1000,highpass=200,lowpass=3500"  -c:a aac -b:a 96k -strict -2 -r 25 "' + RAW_VIDS_DIR_PATH  + file_name + '"'
print(cmd)
subprocess.call(cmd, shell = True)









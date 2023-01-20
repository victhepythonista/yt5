import os 
from os.path import join 


data_dir = "./data"
images_dir = join(data_dir , "images")
icons_dir = join(images_dir,"icons")

make_icon_path = lambda x:join(icons_dir,x)

settings96 = join(icons_dir , "settings96.png")
exit50 = join(icons_dir , "exit50.png")
downloads50 = join(icons_dir, "downloads50.png")
exit100 = join(icons_dir ,"exit100.png")
downloads100 = join(icons_dir , "downloads100.png")
video50 = join(icons_dir , "video50.png")
audio50 = join(icons_dir , "audio50.png")
remove60 = join(icons_dir , "remove60.png")
remove20 = join(icons_dir ,"remove20.png")
add100 = make_icon_path("add100.png")
download100 = make_icon_path("download100.png")
minus64 = make_icon_path("minus64.png")
minus32 = make_icon_path("minus32.png")
desert50 = make_icon_path("desert50.png")
warning96 = make_icon_path("warning96.png")

icons = {
	"desert50":desert50,
	"minus32":minus32,
	"minus64":minus64,
	"download100":download100,
	"remove20":remove20,
	"remove60":remove60,
	"settings96":settings96,
	"downloads50":downloads50,
	"downloads100":downloads100,
	"add100":add100,
	"exit50":exit50,
	"exit100":exit100,
	"video50":video50,
	"audio50":audio50,
	"warning96":warning96,

}



class Paths:

	icons = icons


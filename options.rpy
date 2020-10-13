





define config.developer = "auto"



translate None style say_thought:
    line_spacing 0
    line_leading 0
translate None style say_dialogue:
    line_spacing 0
    line_leading 0
translate None style confirm_prompt_text:
    line_spacing 0
    line_leading 0
translate None style say_label:
    bold False

init python:

    build.archive("scripts", "all")
    build.archive("assets", "all")


    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.rpymc", "scripts")

    build.classify("game/**.rpy",None)
    build.classify("game/**.rpym", None)

    build.classify("game/**.ogg", "assets")
    build.classify("game/**.png", "assets")
    build.classify("game/**.ttf", "assets")
    build.classify("game/**.otf", "assets")
    build.classify("game/**.jpg", "assets")



init python:
    config.has_quicksave = False
    config.has_autosave = False


init python:
    config.end_splash_transition = Fade(0.5,0.5,0.5)









define config.name = ("one night, hot springs")





define gui.show_name = True



define config.version = "1.45"


















define build.google_play_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAimFAZuTtTmVqLcy+Eyk33JErMV1hwZfpcCkxDub5GI+zyC4xeVEr3kPYEmP8h6tvqBW9p7ADrgq79hyw7pCnzGCdVIa4o/6A/Dvfeb8HJ4saQITOZpONzKTxPDVKjMx46JSlJuph1U8RWKGGdKbGYNORatUNTZj22XC/JXMDXKuzX0r9ZkfqJHd7oRrPlQ9kJEkj+XdU5TcF4ciZvyPVsbuWuvDshAouE3+iysH+LGMSZaOp7sZLhW/YwxavxsKKzZ3LhNbWrWmxKp5WFThfdIbQomX+mhGNf2lQTpCfswyy6WtzijyShSGixcWCxZLg7sV6bzKWYl79BGXjDWFp2QIDAQAB"

define build.google_play_salt = (12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)




define gui.about = _p("""
A young transgender woman goes to the hot springs.

Haru is invited by her old friend Manami to spend a night at the hot springs. All Haru wants to do is enjoy the hot springs like everyone else, but she doesn't want to cause any trouble...

ONE NIGHT, HOT SPRINGS is a visual novel. Play as Haru, a young transgender woman, and join her at the hot springs in Japan.

Content warning: This game is for all ages, but it discusses issues that a transgender women in Japan might face, which is a topic that can be sensitive and personal. Also, please keep in mind that this takes place in Japan with Japanese characters.

Play time is ~30 minutes with seven endings total.
""")





define build.name = "onsengame"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "music/title.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = fade




define config.end_game_transition = fade
















define config.window = "hide"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15
















define config.save_directory = "onsengame-1517489131"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')

















define build.itch_project = "npckc/one-night-hot-springs"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

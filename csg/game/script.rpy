define m = Character('マグロ', color="#c8ffc8")
define x = Character('?', color="#c8ffc8")
define y = Character('あなた', color="#c8c8ff")

label start:

    $ others = 0
    $ academic = 0
    $ buildings = 0

    play music "./songs/bgm_maoudamashii_piano27.ogg"
    $ renpy.music.set_volume(0.5)

    call opening from _call_opening

    return

label others:
    if others == 1:
        $ others = 0
        call others_menu from _call_others_menu
    
    if academic == 1:
        $ academic = 0
        call academic_menu from _call_academic_menu
    
    if buildings == 1:
        $ buildings = 0
        call buildings_menu from _call_buildings_menu

    call end1 from _call_end1
       
    return 

label others_menu:
    menu :
        m "次はどこについて聞きたい？"
        "アカデミックシアター":
            $ academic = 1
            call academic from _call_academic
        "校舎":
            $ buildings = 1
            call buildings from _call_buildings 
    return

label academic_menu:
    menu :
        m "次はどこについて聞きたい？"
        "校舎":
            call buildings from _call_buildings_1
    return

label buildings_menu:
    menu :
        m "次はどこについて聞きたい？"
        "アカデミックシアター":
            call academic from _call_academic_1
    return
    
label end1:
    play music "songs/bgm_maoudamashii_piano_milkeyway.ogg"
    y "ありがとう、マグロさん！近畿大学の事がよく分かったよ！"
    m "それはよかった！"
    m "是非君がまたここに来ることを願ってるよ！それじゃあ、またね！"
    y "ありがとうマグロさん!"

    "End1: ありがとう"
    return
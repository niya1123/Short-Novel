# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

define m = Character('マグロ', color="#c8ffc8")
define x = Character('?', color="#c8ffc8")
define y = Character('あなた', color="#c8c8ff")
label start:

    $ others = 0
    $ academic = 0
    $ buildings = 0

    play music "./songs/bgm_maoudamashii_piano27.ogg"
    $ renpy.music.set_volume(0.5)

    call opening

    return

label others:
    if others == 1:
        $ others = 0
        call others_menu
    
    if academic == 1:
        $ academic = 0
        call academic_menu
    
    if buildings == 1:
        $ buildings = 0
        call buildings_menu

    call end
       
    return 

label others_menu:
    menu :
        m "次はどこについて聞きたい？"
        "アカデミックシアター":
            $ academic = 1
            call academic
        "校舎":
            $ buildings = 1
            call buildings 
    return

label academic_menu:
    menu :
        m "次はどこについて聞きたい？"
        "校舎":
            call buildings
    return

label buildings_menu:
    menu :
        m "次はどこについて聞きたい？"
        "アカデミックシアター":
            call academic
    return
    
label end:
    play music "songs/bgm_maoudamashii_piano_milkeyway.ogg"
    m "それじゃあ君がまたここに来ることを願ってるよ！それじゃあ、またね！"
    return
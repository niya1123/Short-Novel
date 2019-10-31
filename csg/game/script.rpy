# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

define m = Character('マグロ', color="#c8ffc8")
define x = Character('?', color="#c8ffc8")


# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。

# ゲームは start ラベルからスタートします。

label start:

    $ others = 0
    $ academic = 0
    $ buildings = 0

    scene bg kindai
    show magro at right
    with fade

    play music "./songs/bgm_maoudamashii_piano27.ogg"
    $ renpy.music.set_volume(0.5)


    x "やあ！近畿大学に遊びに来てくれてどうもありがとう！"
    x "え？突然出てきてお前は誰だって？見てわからないかい？近畿大学のマスコットのマグロだよ！(非公認)"

    m "ま、僕のことは置いておいてこれから近畿大学の紹介をしていこうと思うよ！"
    m "まず、このゲームを作った電気計算機研究会（通称: 電算）について君は知りたいかい？"

    menu :
        "電算の説明を聞きますか？"
        "はい":
            jump d_yes
        "いいえ":
            $ others = 1
            call others

    return

label d_yes:
    m "それじゃあ、電算について説明するよ！"

    $ others = 1
    call others

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
    
label academic:
    m "アカデミックシアターというのは"
    call others
    return

label buildings:
    m "基本的に校舎は大まかに文系と理系の場所に分かれていて、"  
    call others
    return
    
label end:
    m "それじゃあ君がまたここに来ることを願ってるよ！それじゃあ、またね！"
    return
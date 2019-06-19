# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

define zero = Character('ゼロ?', color="#c8ffc8")
define f = Character('企業スパイ', color='#e2aae2')
define fx = Character('???', color='#e2aae2')
define fxsad = Character('???', color='#e2aae2')


define nare = Character(' ',color='#ffffff')

image bg room green tata = im.Scale("bg room green tata.png", 1360, 1300)
image bg gra = im.Scale("bg gra.jpg", 1280, 940)


# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。

# ゲームは start ラベルからスタートします。


label start:

    # 背景を表示します。デフォルトではプレースホルダー（仮画像）を使用しますが、
    # images ディレクトリーにファイル（ファイル名は "bg room.png" や "bg room.jpg"）
    # を追加することにより表示できます。

    scene bg gra
    with fade

    # スプライト（立ち絵）を表示します。ここではプレースホルダーを使用していますが、
    # images ディレクトリーに "eileen happy.png" などと命名したファイルを追加すると
    # 表示することができます。

    # at ステートメントは画像の表示する位置を調整します。
    # at center は中央に下揃えで表示します。これは省略しても同じ結果になります。
    # その他に at right、at left などがデフォルトで定義されています。
    nare "ナナリーを取り戻してから、数日が経った。"
    
    show zero at center with dissolve
    zero "・・・・・・"
    hide zero with dissolve

    show fx at center with dissolve
    fx "ただいま……"
    hide fx with dissolve

    show fxsad at center with dissolve
    fxsad "・・・・・・"

    # トランジション（画面遷移効果）を使って表示を画面に反映させます。
    # 台詞を表示するか with None を使うと、トランジション無しで直ちに表示します。

  

    # 音楽を再生します。ここではタグを利用して無音を再生していますが、
    # game ディレクトリーに "music.ogg" などと命名したファイルを追加すると
    # play music "music.ogg" の形で再生することができます。

    # 効果音を再生する時は play audio "filename" を使用します。
    # play music とは違って複数の効果音を同時に再生することができます。

    play music "<silence .5>"

    # 以下は台詞を表示します。

    

    # return でゲームを終了します。

    return


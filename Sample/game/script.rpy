# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

define higasi = Character('東山 浩太郎', color="#E8E12E")
define sion = Character('涼宮紫音', color="#EB10B9")
define w_s = Character('????', color="#EB10B9")
# define w_h = Character('????', color="#E8E12E")

image bg school room = im.Scale("bg school room.jpg", 1280, 940)
image sion = im.FactorScale("sion.png", .45, .45)

# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。

# ゲームは start ラベルからスタートします。

label start:

    # 背景を表示します。デフォルトではプレースホルダー（仮画像）を使用しますが、
    # images ディレクトリーにファイル（ファイル名は "bg room.png" や "bg room.jpg"）
    # を追加することにより表示できます。

    scene bg school room

    play music "musics/BGM/brightening.mp3"

    # スプライト（立ち絵）を表示します。ここではプレースホルダーを使用していますが、
    # images ディレクトリーに "eileen happy.png" などと命名したファイルを追加すると
    # 表示することができます。

    # at ステートメントは画像の表示する位置を調整します。
    # at center は中央に下揃えで表示します。これは省略しても同じ結果になります。
    # その他に at right、at left などがデフォルトで定義されています。

    "ある日の昼下がりの教室。"

    "突然、勢いよく教室のドアが開かれた。"
    
    # show sion at right with dissolve
    w_s "よお！東山はいるか？"

    "大きな声で発せられたその声に否応なしに、クラス全員の視線が向く."

    show sion at right with dissolve

    "そこには、派手な服装をした女子生徒が立っていた。"

    show higasi at left with dissolve
    higasi "なにか用かい? 紫音さん?"

    "その女子生徒の声に応えるのは、けだるそうな男子生徒。"
    
    


    # return でゲームを終了します。

    return


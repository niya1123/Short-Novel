#########################################
# Defines
# ゲーム中で使うオブジェクトやショートカットを定義します。
# init python でも定義できますが、define を使用した場合には
# navigate script に登録されます。

# ダイアログを呼び出すキャラクターオブジェクトを定義します。
define e = Character('Eileen', color="#c8ffc8", image="eileen")

#########################################
# Labels
# 実際のストーリーはラベルに記述していきます。
# ラベル間の移動は基本的に jump で行いますが、
# 同じファイル内では連続するラベルは順番に実行されます。    
# start はメインメニューから最初に実行されるラベルです。

label start:

    e "ゲームを作成しました"

    return

label buildings:
    scene bg building
    show magro at right
    with fade
    play music "songs/bgm_maoudamashii_piano_noapusa.ogg"
    m "近畿大学には色々校舎があるんだけど、まずは英語村について説明するね！"
    m "じゃあ移動するよ！"
    call ecube from _call_ecube
    call blossom from _call_blossom
    call classroom from _call_classroom
    call others from _call_others_1 
    return
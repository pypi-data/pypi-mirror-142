
# ブラウザーでのゲームプレー [browser_arena]
# 【動作確認 / 使用例】

import ezpip
ezRL = ezpip.load_develop("ezRL", "../../../")
game = ezRL.catcher_game

# ブラウザーでのゲームプレー [browser_arena]
ezRL.browser_arena(game, game_params = {})

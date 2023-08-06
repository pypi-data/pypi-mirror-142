
# ブラウザーでのゲームプレー [browser_arena]

import sys
import random
from sout import sout

# ブラウザーでのゲームプレー [browser_arena]
def browser_arena(game, game_params):
	import flask
	import cv2
	# flaskの初期化
	app = flask.Flask(__name__)
	all_action_ls = game.all_actions(game_params = game_params)	# action一覧
	game_memo_dict = {}
	# ホームページ
	@app.route("/")
	def home():
		# パラメータ取得
		inp = flask.request.args.get("inp")
		gameid = flask.request.args.get("gameid")
		# パラメータがない場合は新ゲーム開始
		if (inp is None) or (gameid is None):
			action, state = "initial_action", game.gen_init_state(game_params = {})	# state, actionの初期化
			inp = ""
			gameid = str(int(random.random()*1000000))
			step_cnt = -1
			reward_sum = 0
		else:
			action_history = inp.split("_")
			prev_state_key = "%s_%s"%(gameid, "_".join(action_history[:-1]))
			action_id = int(action_history[-1])
			action = all_action_ls[action_id]
			memo = game_memo_dict[prev_state_key]
			state, step_cnt, reward_sum = memo["state"], memo["step_cnt"], memo["reward_sum"]
		# ゲーム進行
		state, reward = game.game_step(state, action)	# ゲーム進行
		step_cnt += 1
		reward_sum += reward
		finished = state["finished"]
		# 画像生成
		img = game.human_obs(state)
		state_key = "%s_%s"%(gameid, inp)
		cv2.imwrite("static/obs_%s.png"%state_key, img)
		# メモに登録
		game_memo_dict[state_key] = {"state": state, "step_cnt": step_cnt, "reward_sum": reward_sum}
		# html生成
		row_ls = ["<b>browser_human_agent</b>"]
		row_ls.append('<img src = "static/obs_%s.png">'%state_key)
		row_ls.append('<a href = "/">next game</a>')
		if finished is False:
			for idx, a in enumerate(all_action_ls):
				new_inp = (idx if inp == "" else "%s_%d"%(inp, idx))
				row_ls.append('<a href = "?gameid=%s&inp=%s">%s</a>'%(gameid, new_inp, a))
		row_ls.append("reward: %.1f (sum: %.1f)"%(reward, reward_sum))
		row_ls.append("step_cnt: %d"%step_cnt)
		row_ls.append("finished: %s"%finished)
		# 行をまとめる
		html = "".join([e+"<br>\n" for e in row_ls])
		return html
	# サーバー立ち上げ
	app.run(host = "0.0.0.0", debug = False, port = 80)
	sys.exit()

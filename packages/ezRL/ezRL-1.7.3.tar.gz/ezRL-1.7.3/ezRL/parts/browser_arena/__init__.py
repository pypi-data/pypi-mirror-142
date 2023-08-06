
# ブラウザーでのゲームプレー [browser_arena]

import sys
import random
from sout import sout, souts

# stateをhtml文字列に変換
def state_to_html(state):
	raw_s = souts(state, None)
	s = raw_s.replace("\n", "<br>").replace(" ", "&nbsp;")
	return  s

# ランダムID生成
def gen_rand_id(digits_n):
	ls = [
		str(int(random.random() * 10))
		for _ in range(digits_n)
	]
	return "".join(ls)

# 双方向引当辞書
dual_dic = {}

# long_key(state_key)をshort_keyに直す
def long2short(state_key):
	if state_key in dual_dic: return dual_dic[state_key]
	short_key = gen_rand_id(digits_n = 16)	# ランダムID生成
	dual_dic[short_key] = state_key
	dual_dic[state_key] = short_key
	return short_key

# short_keyをlong_key(state_key)に戻す
def short2long(short_key):
	state_key = dual_dic[short_key]
	return state_key

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
		short_key = flask.request.args.get("short_key")
		# パラメータがない場合は新ゲーム開始
		if short_key is None:
			action, state = "initial_action", game.gen_init_state(game_params = game_params)	# state, actionの初期化
			inp = ""
			gameid = gen_rand_id(digits_n = 6)	# ランダムID生成
			step_cnt = -1
			reward_sum = 0
		else:
			state_key = short2long(short_key)	# short_keyをlong_key(state_key)に戻す
			div_ls = state_key.split("_")
			gameid = div_ls[0]
			inp = "_".join(div_ls[1:])
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
		cv2.imwrite("static/obs_%s.png"%long2short(state_key), img)	# long_key(state_key)をshort_keyに直す
		# メモに登録
		game_memo_dict[state_key] = {"state": state, "step_cnt": step_cnt, "reward_sum": reward_sum}
		# html生成
		row_ls = ["<b>browser_human_agent</b>"]
		row_ls.append('<img src = "static/obs_%s.png">'%long2short(state_key))
		row_ls.append('<a href = "/">next game</a>')
		if finished is False:
			for idx, a in enumerate(all_action_ls):
				new_inp = (str(idx) if inp == "" else "%s_%d"%(inp, idx))
				row_ls.append('<a href = "?short_key=%s">%s</a>'%(long2short(gameid+"_"+new_inp), a))	# long_key(state_key)をshort_keyに直す
		row_ls.append("reward: %.1f (sum: %.1f)"%(reward, reward_sum))
		row_ls.append("step_cnt: %d"%step_cnt)
		row_ls.append("finished: %s"%finished)
		row_ls.append("state:<br>%s"%state_to_html(state))	# stateをhtml文字列に変換
		# 行をまとめる
		html = "".join([e+"<br>\n" for e in row_ls])
		return html
	# サーバー立ち上げ
	app.run(host = "0.0.0.0", debug = False, port = 80)
	sys.exit()


# Catcherゲーム [catcher_game]

import sys
import copy
import fies
import random
import numpy as np
from sout import sout

# 全てのアクション [catcher_game]
def all_actions(game_params):
	return ["Right", "NoMove", "Left"]

# 初期状態の生成 [catcher_game]
def gen_init_state(game_params):
	# 手動指定の場合
	if "specified_stage" in game_params:
		json_fname = game_params["specified_stage"]
		return fies[json_fname, "json"]	# jsonファイル読み込み
	# 画面サイズが指定されている場合
	if "board_size" in game_params:
		board_size = game_params["board_size"]
	else:
		# 画面のサイズのデフォルト値
		board_size = {"w": 7, "h": 7}
	w, h = board_size["w"], board_size["h"]
	# パドルの定義
	paddle_size = 3	# パドルサイズ
	paddle_pos = int(random.random() * (w - paddle_size))	# パドル位置
	# フルーツの数・位置に関する定義
	fruits_n = 20
	fruits_delta = h // 3	# フルーツ同士の間隔
	head_margin, tail_margin = h // 2, h # テープ両端のフルーツがない部分の長さ
	# フルーツ位置を保持するテープの生成
	random_pos = lambda: random.choice(list(range(w)))	# フルーツの場所のランダム生成
	none_ls = lambda n: [None for _ in range(n)]	# Noneのリストを生成 (要素数n)
	tape_info = []
	tape_info += none_ls(n = head_margin)
	for fruits_idx in range(fruits_n - 1):
		tape_info.append(random_pos())
		tape_info += none_ls(n = fruits_delta - 1)
	tape_info.append(random_pos())
	tape_info += none_ls(n = tail_margin)
	# 初期state
	init_state = {
		"finished": False,
		"cursor": 0,
		"board_size": board_size,
		"paddle_size": paddle_size,
		"paddle_pos": paddle_pos,
		"tape_info": tape_info,
	}
	return init_state

# ゲーム進行関数 [catcher_game]
def game_step(state, action):
	# ゲーム開始時の空打ちのaction
	if action == "initial_action":
		return state, 0
	# stateからの情報の取り出し
	paddle_pos = state["paddle_pos"]
	paddle_size = state["paddle_size"]
	w = state["board_size"]["w"]
	cursor = state["cursor"]
	tape_info = state["tape_info"]
	# 通常のゲーム進行
	if action == "Left":
		next_paddle_pos = max(0, paddle_pos - 1)
	elif action == "Right":
		next_paddle_pos = min(w - paddle_size, paddle_pos + 1)
	elif action == "NoMove":
		next_paddle_pos = paddle_pos
	else:
		raise Exception("[error] 不正なaction(%s)が指定されました"%action)
	next_cursor = cursor + 1
	# 次のstateの作成
	next_state = {k:state[k] for k in state}	# Shallow copy
	next_state["cursor"] = next_cursor
	next_state["paddle_pos"] = next_paddle_pos
	# ゲーム終了条件
	if next_cursor == len(tape_info):
		next_state["finished"] = True
		return next_state, 0
	# フルーツ獲得の判定
	reward = 0
	roi_tape = tape_info[next_cursor]	# 注視領域
	if roi_tape is not None:
		# パドルの領域にフルーツが入っていた場合
		if (next_paddle_pos <= roi_tape) & (roi_tape < next_paddle_pos + paddle_size):
			reward = 1
		else:
			reward = -1
	return next_state, reward

# AI用の観測関数 [catcher_game]
def ai_obs(state):
	# stateからの情報の取り出し
	w, h = state["board_size"]["w"], state["board_size"]["h"]
	paddle_pos = state["paddle_pos"]
	paddle_size = state["paddle_size"]
	tape_info = state["tape_info"]
	cursor = state["cursor"]
	# 返す画像の初期化
	ret_img = np.zeros((h, w, 3), dtype = "float64")
	# フルーツの描画
	partial_tape = tape_info[cursor:cursor + h]
	fruit_info = [(i, p) for i, p in enumerate(partial_tape) if p is not None]
	for one_info in fruit_info:
		i, p = one_info
		ret_img[- i - 1, p, :] = [0.5, 0.25, 1.0]
	# パドルの描画
	ret_img[- 1, paddle_pos:paddle_pos + paddle_size, :] = [1.0, 1.0, 1.0]
	return ret_img

# float64型からuint8型への変換
def float2uint8(float_img):
	clipped_img = copy.deepcopy(float_img)
	clipped_img[clipped_img < 0] = 0
	clipped_img[clipped_img > 1] = 1
	uint_img = np.array(clipped_img * 255, dtype = "uint8")
	return uint_img

# 人間用の観測関数 [catcher_game]
def human_obs(state):
	import cv2
	float_img = ai_obs(state)	# AI用の観測関数 [catcher_game]
	uint_img = float2uint8(float_img)	# float64型からuint8型への変換
	resized = cv2.resize(uint_img, None, fx = 20, fy = 20, interpolation = cv2.INTER_NEAREST)
	return resized
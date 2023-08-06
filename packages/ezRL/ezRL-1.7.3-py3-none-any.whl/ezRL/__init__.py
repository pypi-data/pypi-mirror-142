
import sys
from sout import sout
# 共通部品 [utils.py]
from .parts.utils import TileArt
# デバッグ用のプレーヤー [debug_players.py]
from .parts.debug_players import RandomPlayer, HumanPlayer
# ブラウザーでのゲームプレー [browser_arena]
from .parts.browser_arena import browser_arena
# Deep Q Network AI [DQN_Agent]
from .parts.DQN_Agent import DQN_Agent
# Catcherゲーム [catcher_game]
from .parts import catcher_game
# # 紅白ゲーム [rw_game]
# from .parts import rw_game
# デモ [demo.py]
from .parts.demo import demo
# エピソード関係処理 [episode.py]
from .parts.episode import do_episode, do_episodes
# 棋譜の画像化 (デフォルトは入力棋譜と同じディレクトリに置かれる)
from .parts.history import history2img

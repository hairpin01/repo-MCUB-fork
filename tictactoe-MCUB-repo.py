# SPDX-License-Identifier: MIT

from __future__ import annotations

import copy
import enum
import html
import uuid
from random import choice
from typing import Any

from telethon.utils import get_display_name

from core.lib.loader.module_base import ModuleBase, callback, command

PHRASES = [
    "Your brain is just a joke... Use it!",
    "What a nice move...",
    "Try to overcome me!",
    "I'm irresistible, you have no chances!",
    "The clock is ticking... Hurry up.",
    "Don't act, stop to think!",
    "It was your choice, not mine...",
]


class Player(enum.Enum):
    x = 1
    o = 2

    @property
    def other(self):
        return Player.x if self == Player.o else Player.o


class Choice:
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth


class AbBot:
    def __init__(self, player):
        self.player = player

    def alpha_beta_search(self, board, is_max, current_player, depth, alpha, beta):
        winner = board.has_winner()
        if winner == self.player:
            return Choice(board.last_move(), 10 - depth, depth)
        if winner == self.player.other:
            return Choice(board.last_move(), -10 + depth, depth)
        if len(board.moves) == 9:
            return Choice(board.last_move(), 0, depth)

        candidates = board.get_legal_moves()
        max_choice = None
        min_choice = None
        for row, col in candidates:
            newboard = copy.deepcopy(board)
            newboard.make_move(row, col, current_player)
            result = self.alpha_beta_search(
                newboard, not is_max, current_player.other, depth + 1, alpha, beta
            )
            result.move = newboard.last_move()

            if is_max:
                alpha = max(result.value, alpha)
                if alpha >= beta:
                    return result
                if max_choice is None or result.value > max_choice.value:
                    max_choice = result
            else:
                beta = min(result.value, beta)
                if alpha >= beta:
                    return result
                if min_choice is None or result.value < min_choice.value:
                    min_choice = result

        return max_choice if is_max else min_choice

    def select_move(self, board):
        return self.alpha_beta_search(board, True, self.player, 0, -100, 100).move


MARKER_TO_CHAR = {None: ".", Player.x: "x", Player.o: "o"}


class Board:
    def __init__(self):
        self.dimension = 3
        self.grid = [
            [None for _ in range(self.dimension)] for _ in range(self.dimension)
        ]
        self.moves = []

    def has_winner(self):
        if len(self.moves) < 5:
            return None
        for row in range(self.dimension):
            values = set(self.grid[row])
            if len(values) == 1 and None not in values:
                return values.pop()
        for col in range(self.dimension):
            values = {self.grid[row][col] for row in range(self.dimension)}
            if len(values) == 1 and None not in values:
                return values.pop()
        d1 = {self.grid[0][0], self.grid[1][1], self.grid[2][2]}
        if len(d1) == 1 and None not in d1:
            return d1.pop()
        d2 = {self.grid[2][0], self.grid[1][1], self.grid[0][2]}
        if len(d2) == 1 and None not in d2:
            return d2.pop()
        return None

    def make_move(self, row, col, player):
        if self.grid[row][col] is not None:
            raise ValueError("Occupied")
        self.grid[row][col] = player
        self.moves.append([row, col])

    def last_move(self):
        return self.moves[-1]

    def get_legal_moves(self):
        return [
            [row, col]
            for row in range(self.dimension)
            for col in range(self.dimension)
            if self.grid[row][col] is None
        ]


class TicTacToe(ModuleBase):
    name = "tictactoe"
    description = {"en": "Play Tic-Tac-Toe in chat", "ru": "Кpecтики-нoлики в чaтe"}
    version = "1.0.0"
    author = "@Hairpin00"

    strings = {
        "ru": {
            "start": "🧠 <b>Игpa нaчaлacь!</b>\n<i>Ждeм втopoгo игpoкa...</i>",
            "start_ai": "🐻 <b>Mишкa гoтoв игpaть</b>",
            "start_ai_wait": "🧠 <b>Игpa c ИИ нaчaлacь</b>",
            "not_your_game": "Этo нe твoя игpa",
            "wait_turn": "Пoдoжди cвoй xoд",
            "no_move": "Этa клeткa зaнятa",
            "discarded": "Игpa oтмeнeнa",
            "draw": "🤝 <b>Hичья!</b>",
            "no_self": "Heльзя игpaть c caмим coбoй",
        },
        "en": {
            "start": "🧠 <b>Game started!</b>\n<i>Waiting for second player...</i>",
            "start_ai": "🐻 <b>Bear is ready to play</b>",
            "start_ai_wait": "🧠 <b>AI game started</b>",
            "not_your_game": "It is not your game",
            "wait_turn": "Wait for your turn",
            "no_move": "This cell is not empty",
            "discarded": "Game discarded",
            "draw": "🤝 <b>Draw!</b>",
            "no_self": "You can't play with yourself",
        },
    }

    async def on_load(self) -> None:
        self._games: dict[str, dict[str, Any]] = {}
        self._me = await self.client.get_me()

    def _caller_id(self, call: Any) -> int | None:
        return getattr(getattr(call, "from_user", None), "id", None) or getattr(
            call, "sender_id", None
        )

    def _winner(self, score: list[list[str]], mark: str) -> bool:
        lines = []
        lines.extend(score)
        lines.extend([[score[r][c] for r in range(3)] for c in range(3)])
        lines.append([score[i][i] for i in range(3)])
        lines.append([score[i][2 - i] for i in range(3)])
        return any(all(cell == mark for cell in line) for line in lines)

    def _render_text(self, score: list[list[str]]) -> str:
        board = [[c.replace(".", " ") for c in row] for row in score]
        return (
            f"{board[0][0]} | {board[0][1]} | {board[0][2]}\n"
            "----------\n"
            f"{board[1][0]} | {board[1][1]} | {board[1][2]}\n"
            "----------\n"
            f"{board[2][0]} | {board[2][1]} | {board[2][2]}"
        )

    def _render(self, uid: str) -> dict[str, Any] | None:
        game = self._games.get(uid)
        if not game:
            return None
        score = game["score"].split("|")
        win_x = self._winner(score, "x")
        win_o = self._winner(score, "o")
        rmap = {v: k for k, v in game["mapping"].items()}

        if win_x or win_o:
            winner = rmap["x" if win_x else "o"]
            self._games.pop(uid, None)
            winner_name = (
                game["name"]
                if winner != self._me.id
                else html.escape(get_display_name(self._me))
            )
            return {
                "text": f"🏆 <b>Winner:</b> {winner_name} ({'❌' if win_x else '⭕'})\n<code>{self._render_text(score)}</code>",
                "parse_mode": "html",
            }

        if game["score"].count(".") == 0:
            self._games.pop(uid, None)
            return {"text": self.strings("draw"), "parse_mode": "html"}

        text = (
            f"🧠 <b>{choice(PHRASES)}</b>\n"
            f"<i>Playing with <b>{game['name']}</b></i>\n\n"
            f"<i>Turn: <b>{html.escape(get_display_name(self._me)) if game['turn'] == self._me.id else game['name']}</b></i>"
        )
        allowed_users = [self._me.id, game["2_player"]]
        buttons = []
        for i, row in enumerate(score):
            buttons.append(
                [
                    self.Button.inline(
                        line.replace(".", " ").replace("x", "❌").replace("o", "⭕"),
                        self.cb_move,
                        data=f"{uid}:{i}:{j}",
                        allow_user=allowed_users,
                        style="primary",
                    )
                    for j, line in enumerate(row)
                ]
            )
        return {"text": text, "buttons": buttons, "parse_mode": "html"}

    def _render_ai(self, uid: str) -> dict[str, Any] | None:
        game = self._games.get(uid)
        if not game:
            return None

        score = [[MARKER_TO_CHAR[cell] for cell in row] for row in game["board"].grid]
        win_x = self._winner(score, "x")
        win_o = self._winner(score, "o")

        if win_x or win_o:
            winner = "x" if win_x else "o"
            human_mark = game["mapping"][game["user_id"]]
            winner_name = game["name"] if human_mark == winner else "🐻 Bear"
            self._games.pop(uid, None)
            return {
                "text": f"🏆 <b>Winner:</b> {winner_name} ({'❌' if win_x else '⭕'})\n<code>{self._render_text(score)}</code>",
                "parse_mode": "html",
            }

        if game["board"].moves and len(game["board"].moves) >= 9:
            self._games.pop(uid, None)
            return {"text": self.strings("draw"), "parse_mode": "html"}

        human_mark = game["mapping"][game["user_id"]]
        text = (
            f"🧠 <b>{choice(PHRASES)}</b>\n"
            f"<i>{game['name']} vs <b>🐻 Bear</b></i>\n\n"
            f"<i>You are <b>{'❌' if human_mark == 'x' else '⭕'}</b></i>"
        )
        buttons = []
        for i, row in enumerate(score):
            buttons.append(
                [
                    self.Button.inline(
                        line.replace(".", " ").replace("x", "❌").replace("o", "⭕"),
                        self.cb_move_ai,
                        data=f"{uid}:{i}:{j}",
                        allow_user=game["user_id"],
                        style="primary",
                    )
                    for j, line in enumerate(row)
                ]
            )
        return {"text": text, "buttons": buttons, "parse_mode": "html"}

    @callback()
    async def cb_start(self, call: Any, data: str | None = None) -> None:
        uid = str(data or "")
        if not uid:
            return
        caller = self._caller_id(call)
        if caller is None or caller == self._me.id:
            await call.answer(self.strings("no_self"), alert=True)
            return

        other = await self.client.get_entity(caller)
        first = choice([caller, self._me.id])
        self._games[uid] = {
            "2_player": caller,
            "turn": first,
            "mapping": {first: "x", (caller if caller != first else self._me.id): "o"},
            "name": html.escape(get_display_name(other)),
            "score": "...|...|...",
        }
        payload = self._render(uid)
        if payload:
            await call.edit(**payload)

    @callback()
    async def cb_move(self, call: Any, data: str | None = None) -> None:
        raw = str(data or "")
        parts = raw.split(":")
        if len(parts) != 3:
            return
        uid, i_s, j_s = parts
        game = self._games.get(uid)
        if not game:
            await call.answer(self.strings("discarded"), alert=True)
            return

        caller = self._caller_id(call)
        if caller not in [self._me.id, game["2_player"]]:
            await call.answer(self.strings("not_your_game"), alert=True)
            return
        if caller != game["turn"]:
            await call.answer(self.strings("wait_turn"), alert=True)
            return

        i, j = int(i_s), int(j_s)
        score = game["score"].split("|")
        if score[i][j] != ".":
            await call.answer(self.strings("no_move"), alert=True)
            return

        row = score[i]
        mark = game["mapping"][caller]
        score[i] = row[:j] + mark + row[j + 1 :]
        game["score"] = "|".join(score)
        game["turn"] = self._me.id if caller != self._me.id else game["2_player"]

        payload = self._render(uid)
        if payload:
            await call.edit(**payload)

    @callback()
    async def cb_start_ai(self, call: Any, data: str | None = None) -> None:
        uid = str(data or "")
        if not uid:
            return
        caller = self._caller_id(call)
        if caller is None:
            return

        other = await self.client.get_entity(caller)
        human_first = choice([True, False])
        human_player = Player.x if human_first else Player.o
        ai_player = human_player.other

        board = Board()
        bot = AbBot(ai_player)
        if not human_first:
            board.make_move(*bot.select_move(board), ai_player)

        self._games[uid] = {
            "mode": "ai",
            "user_id": caller,
            "name": html.escape(get_display_name(other)),
            "board": board,
            "bot": bot,
            "human_player": human_player,
            "ai_player": ai_player,
            "mapping": {
                caller: "x" if human_player == Player.x else "o",
                "bear": "o" if human_player == Player.x else "x",
            },
        }

        payload = self._render_ai(uid)
        if payload:
            await call.edit(**payload)

    @callback()
    async def cb_move_ai(self, call: Any, data: str | None = None) -> None:
        raw = str(data or "")
        parts = raw.split(":")
        if len(parts) != 3:
            return
        uid, i_s, j_s = parts
        game = self._games.get(uid)
        if not game:
            await call.answer(self.strings("discarded"), alert=True)
            return

        caller = self._caller_id(call)
        if caller != game["user_id"]:
            await call.answer(self.strings("not_your_game"), alert=True)
            return

        i, j = int(i_s), int(j_s)
        score = [[MARKER_TO_CHAR[cell] for cell in row] for row in game["board"].grid]
        if score[i][j] != ".":
            await call.answer(self.strings("no_move"), alert=True)
            return

        game["board"].make_move(i, j, game["human_player"])

        winner_after_human = game["board"].has_winner()
        if winner_after_human is None and len(game["board"].moves) < 9:
            try:
                game["board"].make_move(
                    *game["bot"].select_move(game["board"]),
                    game["ai_player"],
                )
            except Exception:
                pass

        payload = self._render_ai(uid)
        if payload:
            await call.edit(**payload)

    @command("tictactoe", doc_en="start tic tac toe", doc_ru="нaчaть игpy")
    async def cmd_tictactoe(self, event: Any) -> None:
        uid = uuid.uuid4().hex
        await self.inline(
            event.chat_id,
            self.strings("start"),
            buttons=[
                [
                    self.Button.inline(
                        "💪 Play",
                        self.cb_start,
                        data=uid,
                        allow_user="all",
                        style="success",
                    )
                ]
            ],
            ttl=15 * 60,
            parse_mode="html",
        )

    @command("tictacai", doc_en="play with AI", doc_ru="игpa c ИИ")
    async def cmd_tictacai(self, event: Any) -> None:
        uid = uuid.uuid4().hex
        await self.inline(
            event.chat_id,
            self.strings("start_ai"),
            buttons=[
                [
                    self.Button.inline(
                        "🧠 Let's go!",
                        self.cb_start_ai,
                        data=uid,
                        allow_user="all",
                        style="success",
                    )
                ]
            ],
            ttl=15 * 60,
            parse_mode="html",
        )

# Title: Maze of Screams
# Author: TAK RAIDEN
# Author site: https://www.raidenjpn.com/
# Desc: A Pyxel Maze Horror Game
# Pyxel site: https://github.com/kitao/pyxel
# This project is licensed under the MIT License / URL「https://opensource.org/licenses/mit-license.php 」
# Version: 1.0

import math
import random
import copy
import pyxel

# ======================
#  MAP DATA (31x31)
# ======================

# ---- Floor 4 (初期階層・地図あり・スタートあり) ----
MAP_4 = [
"1111111111111411111111111111111",
"1000000000000000000000000000001",
"1010100011100111111011101000101",
"1011101010101110100010101110111",
"1010101110111010111010111011101",
"1000100000100010000010100000001",
"1011101110101110111110111011101",
"1000000010100010100000100010001",
"1010111010111010111011101110101",
"1000100010000010100000100000001",
"1011101011111010111110111111101",
"1000101000001010000000100000001",
"1010101011101010111010111011101",
"1000101000101010100010000010001",
"1010101110101010111110111110101",
"1000100010100010000000100010001",
"1011101110101110111011101110101",
"1000000010100010000010100000001",
"1011111010111010111010111111101",
"1000000010000010000010000000001",
"1011101111111110111110111111101",
"1000100000000010000010000000101",
"1010111011111010111010111010101",
"1000100010000010000010000010101",
"1011101010111111111110111010101",
"1000001010000000000010100010101",
"1011101010111111111010111110161",  
"1000001010000000000010000000101",
"1011111010111110111110111111101",
"1000000000000000000000000000021",
"1111111111111111111111111111111"
]

# ---- Floor 3（中難易度）----
MAP_3 = [
"1111111111111111411111111111111",
"1000100000100000000011110000001",
"1010111010111111011010010111101",
"1000001010000001010011000000101",
"1111101010111101011111011110101",
"1000101010000100000000010010101",
"1011101011100111111111010010101",
"1010000000100000000010010110101",
"1010111110111110111011110010101",
"1010000010000010001000000010101",
"1011111011111011111011111110101",
"1000000010001010000000000010101",
"1111111010111010111111111010101",
"1000001010000010000010001010101",
"1011101011111011111010111010101",
"1010001000001000000010000010101",
"1010111111101111111110111010101",
"1010000000100010000000000010101",
"1010111110111010111110111110101",
"1000000000000010000000000000001",
"1111111111111011111111111111101",
"1000000000001010000000000000101",
"1011111111101010111110111110101",
"1000000000101010000010000010101",
"1011111110101011111010111010101",
"1000000010001010000010000010101",
"1011111011101010111110111010101",
"1010001000000010000010000010101",
"1010111011111110111110111110101",
"1000000000000000000000000000021",
"1111111111111111111111111111111"
]

# ---- Floor 2（難しい）----
MAP_2 = [
"1111111111111141111111111111111",
"1000000000000001000000000000001",
"1011111110111101111110111111101",
"1001000010100000000010100000101",
"1011011010111011111010111010101",
"1000010010000000010010000010101",
"1011111011111011011011111010101",
"1000010000010010000000010010101",
"1011011111000011111111011010101",
"1010010000010010000000010010101",
"1011010111111110111111111010101",
"1000010100000010000010000010101",
"1111010101111011111010111110101",
"1000010101000010000010100010101",
"1011110101011111111011101010101",
"1000010001000000010000000010101",
"1011111011111111111011111110001",
"1010000000001000000000000010101",
"1010111111101011101110111010101",
"1010100000100010000010000010101",
"1010101110111010111010111110101",
"1010101000100010100010000000101",
"1010101111111010111111111100001",
"1010100000000010000000000100101",
"1010111111111110111111111100101",
"1010100000000010000000010000101",
"1010101111111110111111011110101",
"1010101000000000100010000000101",
"1010101011111111111010111110101",
"1000000000000000000000000000021",
"1111111111111111111111111111111"
]

# ---- Floor 1（最終階層）----
MAP_1 = [
"1111111111111113111111111111111",
"1000000000000000000000000000001",
"1011111110111101111110111111101",
"1000000010100000000010100000101",
"1111111010111011111010111110001",
"1000001010000000010010000010101",
"1011101011111011011101111010101",
"1000100000010010000000010010101",
"1010111111010011111111011010101",
"1010000010010010000000010010101",
"1011111010111110111110111010101",
"1000001010000010000010000010111",
"1111101011111011011010111110101",
"1000101010000010000010100010101",
"1011101010111111111011101010101",
"1000100010000000010000000010001",
"1011110111111101111111111110101",
"1010000000001000000000000010101",
"1010111111101111111111111010101",
"1010100000100010000010000010101",
"1010101110111010111010111110101",
"1010101000100010100010000000101",
"1010101111111010111111111100101",
"1010100000000010000000000100101",
"1010111111111110111111111100101",
"1010100000000010000000010000101",
"1010101111111110111111011110101",
"1010101000000000100010000000101",
"1010101011111111111010111110101",
"1000101000000000000010000000021",
"1111111111111111111111111111111"
]

# ======================
#  MAP CONFIG
# ======================
ORIGINAL_MAPS = {4: MAP_4, 3: MAP_3, 2: MAP_2, 1: MAP_1}
MAPS = {f: copy.deepcopy(ORIGINAL_MAPS[f]) for f in ORIGINAL_MAPS}

current_floor = 4
MAP = MAPS[current_floor]

# ======================
#  GAME SETTINGS
# ======================
W, H = 160, 120

px = py = pa = 0.0

show_map = False
map_timer = 0
map_cooldown = 0

last_enemy_dist = None
last_enemy_angle = None

# 敵スプライト関連
ENEMY_IMG_BANK = 0
ENEMY_W = 56
ENEMY_H = 120
ENEMY_FRONT_X = 0
ENEMY_FRONT_Y = 0

MAX_ENEMY_DRAW_SIZE = 110
MIN_ENEMY_SIZE = 20
MAX_RENDER_DISTANCE = 10

# ==== Elevator animation ====
elevator_active = False
elevator_stage = 0   # 0=閉,1=半開,2=全開
elevator_timer = 0.0

# ==== Goal Door animation ====
goal_active = False
goal_stage = 0
goal_timer = 0.0

black_screen = False

white_alpha = 0

TITLE_W = 128   # ← タイトル画像の横幅（必要なら120→128へ変更）
TITLE_H = 64    # ← 縦幅（変更なければそのまま）

game_state = "title"  # title, playing, gameover, clear


def find_player_spawn():
    global px, py, pa
    for y, row in enumerate(MAP):
        for x, t in enumerate(row):
            if t == "2":
                px, py = x + 0.5, y + 0.5
                pa = -math.pi / 2
                return

find_player_spawn()

# Items
has_key = False
has_map = True
flashlight = True
flashlight_cone = 0.25

# Enemy
def random_spawn(min_dist=6):
    while True:
        x = random.randint(1, len(MAP[0]) - 2)
        y = random.randint(1, len(MAP) - 2)
        if MAP[y][x] != "0":
            continue
        dist = math.hypot(x - px, y - py)
        if dist >= min_dist:
            return x + 0.5, y + 0.5

enemy_x, enemy_y = random_spawn()
enemy_speed = 0.03
enemy_state = "patrol"
enemy_detect_distance = 7
enemy_tile_x, enemy_tile_y = int(enemy_x), int(enemy_y)
stuck_timer = 0
start_time = 0
clear_time = 0

game_over = False
game_clear = False
FOV = math.radians(60)

# ===== Utility =====
def is_wall(x, y):
    if x < 0 or y < 0 or y >= len(MAP) or x >= len(MAP[0]):
        return True
    return MAP[int(y)][int(x)] not in ("0", "2", "3", "4", "5", "6")

def get_tile():
    return MAP[int(py)][int(px)]

def tile_in_front():
    """プレイヤーの正面 0.5 マス先のタイル"""
    fx = px + math.cos(pa) * 0.5
    fy = py + math.sin(pa) * 0.5
    if fy < 0 or fy >= len(MAP) or fx < 0 or fx >= len(MAP[0]):
        return "1"
    return MAP[int(fy)][int(fx)]

def pickup_item():
    global has_key, has_map, MAP
    t = get_tile()
    if t in ("5", "6"):
        if t == "5":
            has_key = True
        if t == "6":
            has_map = True
        row = MAP[int(py)]
        MAP[int(py)] = row[:int(px)] + "0" + row[int(px)+1:]

def change_floor():
    global current_floor, MAP
    global enemy_x, enemy_y, enemy_tile_x, enemy_tile_y, enemy_state
    global map_timer, map_cooldown, show_map

    if current_floor > 1:
        current_floor -= 1
        MAP = MAPS[current_floor]

        # プレイヤー位置再配置
        find_player_spawn()

        # 敵も再配置
        enemy_x, enemy_y = random_spawn()
        enemy_tile_x, enemy_tile_y = int(enemy_x), int(enemy_y)
        enemy_state = "patrol"

        # 🆕 --- Floor 移動時 MAP 使用リセット --
        map_timer = 0
        map_cooldown = 0
        show_map = False

# === ここ既存の exit_check の代わりに置き換え ===
def exit_check():
    global goal_active, goal_timer, goal_stage

    if get_tile() == "3" and not goal_active:
        goal_active = True
        goal_timer = 0
        goal_stage = 0


def get_neighbors(x, y):
    d = []
    if not is_wall(x+1, y): d.append((x+1, y))
    if not is_wall(x-1, y): d.append((x-1, y))
    if not is_wall(x, y+1): d.append((x, y+1))
    if not is_wall(x, y-1): d.append((x, y-1))
    return d

def find_path_step():
    target = (int(px), int(py))
    start = (enemy_tile_x, enemy_tile_y)
    if start == target:
        return None

    q = [start]
    v = {start: None}
    found = False

    while q:
        cx, cy = q.pop(0)
        if (cx, cy) == target:
            found = True
            break
        for nx, ny in get_neighbors(cx, cy):
            if (nx, ny) not in v:
                v[(nx, ny)] = (cx, cy)
                q.append((nx, ny))

    if not found:
        return None

    step = target
    while v[step] is not None and v[step] != start:
        step = v[step]
        if step not in v:
            return None

    if step is None or not isinstance(step, tuple):
        return None
    return step

def can_see_enemy():
    steps = int(max(abs(enemy_x - px), abs(enemy_y - py)) * 10)
    if steps <= 0:
        return False
    for i in range(1, steps):
        tx = px + (enemy_x - px) * i / steps
        ty = py + (enemy_y - py) * i / steps
        if is_wall(tx, ty):
            return False
    return True



# ======================
#  ENEMY AI
# ======================
def enemy_logic():
    global enemy_x, enemy_y, enemy_tile_x, enemy_tile_y
    global enemy_state, stuck_timer, game_over, enemy_detect_distance

    if game_over or game_clear:
        return

    dx = px - enemy_x
    dy = py - enemy_y
    dist = math.hypot(dx, dy)

    # --- 接触判定 ---
    if dist < 0.35:
        game_over = True

        # 敵の角度と距離を保持（画面表示用）
        global last_enemy_dist, last_enemy_angle
        last_enemy_dist = dist
        last_enemy_angle = math.atan2(dy, dx)

        return

    # プレイヤー検知距離拡張（遠くからでも気づく）
    heard = dist < enemy_detect_distance * 2.5
    seen  = dist < enemy_detect_distance * 1.5 and can_see_enemy()

    step = None

    # ===== 見えてる → 全力追跡 =====
    if seen:
        enemy_state = "chase"
        step = find_path_step()

    # ===== 聞こえた → プレイヤーの方向を優先 =====
    elif heard:
        enemy_state = "search"
        n = get_neighbors(enemy_tile_x, enemy_tile_y)
        if n:
            # プレイヤーに近づく方向を優先
            step = min(n, key=lambda t: math.hypot((t[0] + 0.5) - px, (t[1] + 0.5) - py))

    # ===== ランダム巡回（広範囲探索型AI） =====
    else:
        enemy_state = "patrol"
        n = get_neighbors(enemy_tile_x, enemy_tile_y)

        if n:
            # ★プレイヤー方向に寄る傾向を追加（遭遇率UP）
            step = min(n, key=lambda t: math.hypot((t[0] + 0.5) - px, (t[1] + 0.5) - py))

            # 30%だけランダム行動を残す
            if random.random() < 0.3:
                step = random.choice(n)



    # 移動先が判明
    enemy_logic.last_step = step

    # ==== ハマり対策 ====
    if step is None:
        stuck_timer += 1
        if stuck_timer % 5 == 0:
            d = get_neighbors(enemy_tile_x, enemy_tile_y)
            if d:
                step = random.choice(d)
        if step is None:
            return

    tx, ty = step
    vx = (tx + 0.5) - enemy_x
    vy = (ty + 0.5) - enemy_y
    length = math.hypot(vx, vy)

    if enemy_state == "chase":
        sp = enemy_speed * 2.5
    elif enemy_state == "search":
        sp = enemy_speed * 1.5
    else:
        sp = enemy_speed * 0.9  # ← パトロールも少し速くして迷路を歩く頻度UP

    if length > 0:
        enemy_x += (vx / length) * sp
        enemy_y += (vy / length) * sp

    if abs(enemy_x - (tx + 0.5)) < 0.1 and abs(enemy_y - (ty + 0.5)) < 0.1:
        enemy_tile_x, enemy_tile_y = tx, ty

# ======================
#  RENDERING
# ======================
def draw_3d():
    ray = []
    BASE, DARK = 6, 15

    # --- 壁のレイキャスト ---
    for x in range(W):
        ang = pa + (x / W - .5)
        d = 0
        while d < 20:
            d += .03
            rx = px + math.cos(ang) * d
            ry = py + math.sin(ang) * d
            if is_wall(rx, ry):
                ray.append(d)
                h = H / (d + 0.1)
                diff = abs(ang - pa)
                fade = max(.1, 1 - d * .1)
                bright = max(0, 1 - diff / flashlight_cone) * fade
                c = (
                    BASE if bright > .6 else
                    BASE - 1 if bright > .3 else
                    BASE - 2 if bright > .15 else
                    DARK
                )
                pyxel.rect(x, H // 2 - h // 2, 1, h, c)
                break

    # ★ゲームオーバー中はここで終了
    if game_over:
        return

    # =========================================================
    # 敵スプライト描画
    # =========================================================
    def draw_enemy_sprite(ray):
        dx = enemy_x - px
        dy = enemy_y - py
        dist = math.hypot(dx, dy)

        if not (0.3 < dist < 3 and can_see_enemy()):
            return

        angle = math.atan2(dy, dx)
        diff = (angle - pa + math.pi) % (2 * math.pi) - math.pi
        if abs(diff) > FOV / 2:
            return

        sx = int((diff / (FOV / 2)) * (W / 2) + W // 2)
        if not (0 <= sx < len(ray)):
            return

        depth = max(dist * math.cos(diff), 0.05)
        if depth >= ray[sx]:
            return

        size = 100
        sprite_x = max(0, min(W - size, sx - size // 2))
        sprite_y = max(0, min(H - size, H // 2 - size // 2))

        try:
            pyxel.blt(
                sprite_x, sprite_y,
                ENEMY_IMG_BANK,
                ENEMY_FRONT_X, ENEMY_FRONT_Y,
                ENEMY_W, ENEMY_H,
                0
            )
        except:
            pass

    draw_enemy_sprite(ray)

    # ==========================
    # 地図アイテム光り表示
    # ==========================
    if not has_map and ray:
        for y, row in enumerate(MAP):
            for x, t in enumerate(row):
                if t == "6":
                    mx, my = x + .5, y + .5
                    dx, dy = mx - px, my - py
                    d = math.hypot(dx, dy)
                    if .3 < d < 10:
                        a = math.atan2(dy, dx)
                        diff = (a - pa + math.pi) % (2 * math.pi) - math.pi
                        if abs(diff) < FOV / 2:
                            sx = int((diff / (FOV / 2)) * (W / 2) + W // 2)
                            if 0 <= sx < len(ray):
                                c = max(d * math.cos(diff), .05)
                                if c < ray[sx]:
                                    h = H / (c + .1)
                                    pyxel.rect(sx - 1, H // 2 - h // 2, 4, h, 11)

def draw_minimap():
    if not show_map or not has_map:
        return

    s = 2
    ox = W - len(MAP[0]) * s - 2
    oy = 2

    for y, row in enumerate(MAP):
        for x, t in enumerate(row):
            if t == "3": c = 8
            elif t == "4": c = 10
            elif t == "2": c = 12
            elif t in ("0", "5", "6"): c = 6
            else: c = 1
            pyxel.rect(ox + x * s, oy + y * s, s, s, c)

    pyxel.pset(int(ox + px * s), int(oy + py * s), 14)
    pyxel.pset(int(ox + enemy_x * s), int(oy + enemy_y * s), 8)

# ======================
#  RESTART
# ======================
def restart_game():
    global current_floor, MAP, MAPS
    global has_key, has_map
    global enemy_x, enemy_y, enemy_tile_x, enemy_tile_y
    global enemy_state, stuck_timer, game_over, game_clear, show_map
    global enemy_speed, map_timer, map_cooldown
    global elevator_active, elevator_stage, elevator_timer
    global white_alpha, goal_active, goal_stage, goal_timer, game_state
    global start_time, clear_time
    
    # ---- MAPとプレイヤー状態リセット ----
    MAPS = {f: copy.deepcopy(ORIGINAL_MAPS[f]) for f in ORIGINAL_MAPS}
    current_floor = 4
    MAP = MAPS[current_floor]
    has_key = False
    has_map = True

    map_timer = 0
    map_cooldown = 0
    show_map = False

    find_player_spawn()
    enemy_x, enemy_y = random_spawn()
    enemy_tile_x, enemy_tile_y = int(enemy_x), int(enemy_y)
    enemy_state = "patrol"
    enemy_speed = 0.03
    stuck_timer = 0

    game_over = False
    game_clear = False

    elevator_active = False
    elevator_stage = 0
    elevator_timer = 0.0

    # ---- ゴール演出リセット ----
    white_alpha = 0
    goal_active = False
    goal_stage = 0
    goal_timer = 0

    # ---- タイマー開始 ----
    start_time = pyxel.frame_count      # ←⭐プレイ開始時間記録
    clear_time = 0                      # ←⭐クリア時間初期化

    # ---- ゲーム開始 ----
    game_state = "playing"

# ======================
#  UPDATE LOOP
# ======================
def update():
    global px, py, pa, show_map, map_timer, map_cooldown
    global elevator_active, elevator_stage, elevator_timer
    global current_floor, MAP, goal_active, goal_stage, goal_timer
    global white_alpha, enemy_x, enemy_y, game_state, game_over, game_clear

    # ===== タイトル画面処理 =====
    if game_state == "title":
        if pyxel.btnp(pyxel.KEY_RETURN):
            restart_game()
        return


    # ===== クリア画面 =====
    if game_clear:
        if pyxel.btnp(pyxel.KEY_SPACE):
            restart_game()
            game_state = "title"
        return

    # ===== ゲームオーバー =====
    if game_over:
        if pyxel.btnp(pyxel.KEY_SPACE):   # 続行
            restart_game()
            game_state = "playing"

        if pyxel.btnp(pyxel.KEY_Q):       # タイトルに戻る
            restart_game()
            game_state = "title"

        return

    # ===== MAP KEY =====
    if pyxel.btnp(pyxel.KEY_M) and has_map and map_cooldown <= 0 and map_timer <= 0:
        show_map = True
        map_timer = 5

    if map_timer > 0:
        map_timer -= 1/30
        if map_timer <= 0:
            show_map = False
            map_cooldown = 10

    if map_cooldown > 0:
        map_cooldown -= 1/30

    # ===== PLAYING以外は止める =====
    if game_state != "playing":
        return

    # ======================
    # 🚪 Elevator animation（←ここタイトル判定より下に移動）
    # ======================
    if elevator_active:
        elevator_timer += 1/30  

        if elevator_timer < 0.5:
            elevator_stage = 0
        elif elevator_timer < 1.0:
            elevator_stage = 1
        elif elevator_timer < 1.5:
            elevator_stage = 2
        elif elevator_timer < 2.0:
            elevator_stage = 2
        else:
            change_floor()
            elevator_active = False
            elevator_stage = 0
            elevator_timer = 0
        return
 

    # ======================
    # 🎉 Goal Door animation
    # ======================
    if goal_active:
        goal_timer += 1/30

        if goal_timer < 0.5:
            goal_stage = 0
        elif goal_timer < 1.0:
            goal_stage = 1
        elif goal_timer < 1.5:
            goal_stage = 2
        else:
            # ---- WHITE OUT ----
            if white_alpha < 15:
                white_alpha += 0.3   # ← 少し遅くすると綺麗



    # ======================
    # 🔧 Debug Floor Jump
    # ======================
    if pyxel.btnp(pyxel.KEY_4):
        current_floor = 4
        MAP = MAPS[current_floor]
        find_player_spawn()
        enemy_x, enemy_y = random_spawn()
        white_alpha = 0

    if pyxel.btnp(pyxel.KEY_3):
        current_floor = 3
        MAP = MAPS[current_floor]
        find_player_spawn()
        enemy_x, enemy_y = random_spawn()
        white_alpha = 0

    if pyxel.btnp(pyxel.KEY_2):
        current_floor = 2
        MAP = MAPS[current_floor]
        find_player_spawn()
        enemy_x, enemy_y = random_spawn()
        white_alpha = 0

    if pyxel.btnp(pyxel.KEY_1):
        current_floor = 1
        MAP = MAPS[current_floor]
        find_player_spawn()
        enemy_x, enemy_y = random_spawn()
        white_alpha = 0

        # ===== DEBUG WARP: L → ゴール前に安全ワープ =====
    if pyxel.btnp(pyxel.KEY_L):

        # 1Fへ強制移動
        current_floor = 1
        MAP = MAPS[current_floor]

        # ゴール位置探す
        gx = gy = None
        for y, row in enumerate(MAP):
            for x, t in enumerate(row):
                if t == "3":
                    gx, gy = x, y

        if gx is None:
            return  # ゴールが無い場合安全終了

        # プレイヤーが立てる床判定
        def is_free(x, y):
            return MAP[y][x] in ("0", "2", "3", "4", "5", "6")

        # ゴールの周囲（優先順）
        candidates = [
            (gx - 1, gy),  # 左
            (gx + 1, gy),  # 右
            (gx, gy - 1),  # 上
            (gx, gy + 1),  # 下
        ]

        placed = False
        for x, y in candidates:
            if is_free(x, y):
                px = x + 0.5
                py = y + 0.5
                pa = math.atan2(gy - y, gx - x)  # ゴール方向を向くよう調整
                placed = True
                break

        # 万が一全部壁なら、強制ワープ（最終保険）
        if not placed:
            px = gx - 0.5
            py = gy + 0.5
            pa = 0

    # --------------------
    # Player movement
    # --------------------
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
        pa -= 0.05
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        pa += 0.05

    sp = 0.05 * (1.8 if pyxel.btn(pyxel.KEY_SHIFT) else 1)
    dx, dy = math.cos(pa) * sp, math.sin(pa) * sp

    if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
        if not is_wall(px + dx, py): px += dx
        if not is_wall(px, py + dy): py += dy
    if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
        if not is_wall(px - dx, py): px -= dx
        if not is_wall(px, py - dy): py -= dy

    pickup_item()
    exit_check()
    enemy_logic()

    # ==== Elevator Trigger (乗った瞬間発動) ====
    if get_tile() == "4" and not elevator_active:
        elevator_active = True
        elevator_stage = 0
        elevator_timer = 0

        # エレベーター床を消す（戻れないように）
        row = MAP[int(py)]
        MAP[int(py)] = row[:int(px)] + "0" + row[int(px)+1:]

    # ===== Warning Sound =====
    dist = math.hypot(px - enemy_x, py - enemy_y)

    if dist < 6:
        speed = max(5, int(dist * 5))
        pyxel.sound(0).speed = speed
        if not pyxel.play_pos(0):
            pyxel.play(0, 0)
    else:
        pyxel.stop(0)

def draw_elevator_overlay():
    """エレベーター画像を最前面に描画"""

    global elevator_stage, elevator_active

    # エレベータが動いている時
    if elevator_active:
        img_y = 0 if elevator_stage == 0 else 72 if elevator_stage == 1 else 144

    # 動いていないが正面にある場合 →閉じたドアを表示
    elif tile_in_front() == "4":
        img_y = 0
    else:
        return  # 描画しない

    # === エレベーター画像中央表示 ===
    ELEVATOR_W = 64
    ELEVATOR_H = 64

    pyxel.blt(
        W//2 - ELEVATOR_W//2,
        H//2 - ELEVATOR_H//2,
        0, 176, img_y,
        ELEVATOR_W, ELEVATOR_H,
        0
    )




# ======================
#  DRAW LOOP
# ======================
def draw():
    global game_clear, clear_time
    pyxel.cls(0)

    # ===== TITLE =====
    if game_state == "title":
        pyxel.blt(W//2 - TITLE_W//2, 20, 0, 0, 224, TITLE_W, TITLE_H, 0)
        pyxel.text((W - len("PRESS ENTER TO START") * 4)//2, 90, "PRESS ENTER TO START", 10)
        pyxel.text((W - len("Created by RAIDEN LLC") * 4)//2, 105, "Created by RAIDEN LLC", 7)
        return

    # ===== GAME CLEAR (最優先) =====
    if game_clear:
        pyxel.rect(0, 0, W, H, 7)

        minutes = int(clear_time // 60)
        seconds = clear_time % 60
        time_msg = f"TIME: {minutes}:{seconds:04.1f}"

        msg1 = "GAME CLEAR"
        msg2 = "PRESS SPACE TO TITLE"

        pyxel.text((W - len(msg1)*4)//2, H//2 - 10, msg1, 8)
        pyxel.text((W - len(time_msg)*4)//2, H//2, time_msg, 11)
        pyxel.text((W - len(msg2)*4)//2, H//2 + 10, msg2, 3)
        return

    # ===== GAME OVER =====
    if game_over:
        pyxel.rect(0, 0, W, H, 0)

        size = 100
        pyxel.blt(W//2 - size//2, H//2 - size//2, ENEMY_IMG_BANK, ENEMY_FRONT_X, ENEMY_FRONT_Y, ENEMY_W, ENEMY_H, 0)

        msg1 = "GAME OVER"
        msg2 = "PRESS SPACE TO CONTINUE"
        msg3 = "PRESS Q TO TITLE"

        margin = 4  # 画面端の余白

        # --- 右下揃え位置計算 ---
        x1 = W - len(msg1)*4 - margin
        x2 = W - len(msg2)*4 - margin
        x3 = W - len(msg3)*4 - margin

        # 行間 8px
        y3 = H - 10
        y2 = y3 - 10
        y1 = y2 - 15


        # --- 描画 ---
        pyxel.text(x1, y1, msg1, 8)   # 赤文字
        pyxel.text(x2, y2, msg2, 3)  # 白文字
        pyxel.text(x3, y3, msg3, 7)

        return


    # ===== PLAYING =====
    draw_3d()
    draw_minimap()

    pyxel.text(2, 2, f"FLOOR: {current_floor}", 7)

    if map_cooldown > 0:
        pyxel.text(5, 10, f"MAP CD: {map_cooldown:.0f}s", 8)
    elif map_timer > 0:
        pyxel.text(5, 10, f"MAP: {map_timer:.0f}s", 11)
    else:
        pyxel.text(5, 10, "MAP READY", 10)




    # === Elevator Overlay ===
    draw_elevator_overlay()

    # === GOAL DOOR ===
    if goal_active:
        img_y = 0 if goal_stage == 0 else 72 if goal_stage == 1 else 144
        pyxel.blt(W//2 - 32, H//2 - 32, 0, 72, img_y, 64, 64, 0)

        # ---- Whiteout ----
        if white_alpha > 0:
            shade = min(15, int(white_alpha))
            pyxel.rect(0, 0, W, H, shade)

            # ★クリア確定&タイム保存はここ！
            if white_alpha >= 15:
                if not game_clear:   # ← 一度だけ実行
                    clear_time = (pyxel.frame_count - start_time) / 30
                    game_clear = True

                msg1 = "GAME CLEAR"
                msg2 = "PRESS SPACE TO TITLE"
                time_msg = f"TIME: {clear_time:.1f} SEC"

                pyxel.text((W - len(msg1)*4)//2, H//2 - 20, msg1, 8)
                pyxel.text((W - len(time_msg)*4)//2, H//2, time_msg, 11)
                pyxel.text((W - len(msg2)*4)//2, H//2 + 20, msg2, 3)
                return
            

def play_warning():
    pyxel.play(0, 0)

    dist = math.hypot(px - enemy_x, py - enemy_y)

    if dist < 4:  # 近づくほど音鳴る
        play_warning()


# ======================
#  START GAME
# ======================
pyxel.init(W, H, title="Maze of Screams")
pyxel.load("3dhorrormap.pyxres")

pyxel.colors[15] = 0x0A0A0A
pyxel.colors[6]  = 0x909090
pyxel.colors[5]  = 0x666666
pyxel.colors[4]  = 0x333333
pyxel.colors[11] = 0x00FF00


pyxel.run(update, draw)
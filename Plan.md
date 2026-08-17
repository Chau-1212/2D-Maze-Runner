# 2D MazeRunner – Coding Plan (source‑of‑truth)

Purpose: detail every coding step, module, and dependency needed to finish the game. All references are to the actual code base (main.py, player.py, item.py, chest.py, furance.py).

---
## 1. Overall ordering (dependency chain)
1. **Loading screen & maze generation** – `generate_maze`
2. **Time system** – `time_system` (drives day/night/blood‑moon)
3. **Enemy AI** – `enemy_ai` (spawn + FSM + BFS chase)
4. **Collision detection** – `collision_detection` (player‑wall, player‑enemy)
5. **Player movement & stats** – `player_movement` (WASD, hunger‑speed penalty, stamina)
6. **HUD display** – `hud_display` (health, stamina, hunger bars, compass, distance meter, hotbar, time icon)
7. **Chest interaction & UI** – `chest_ui` (open on E, click‑select slot, R‑to‑take)
8. **Menu system** – `menu_system` (Start, Settings, Death screen)
9. **Win / Lose screens** – trigger when distance ≥ 10 km or health ≤ 0
10. **Pause & Settings** – Escape toggles pause, simple settings UI

---
## 2. Module‑by‑module coding steps

### 2.1 `generate_maze`
- **Goal**: Produce a perfect maze (DFS) of modular tiles, store as `maze_grid` (2‑D array of tile codes 0‑4).
- **Steps**:
  1. Initialise grid full of walls (`0`).
  2. Define room layout (e.g. 33 × 33 rooms, each 3 × 3 tiles = ~10 km).
  3. Run DFS on room coordinates, carving doorways between visited neighbours.
  4. After DFS, mark floor tiles (`1`), danger tiles (`2`), chest tiles (`3`), doorways (`4`).
  5. Export `maze_grid` for use by other modules.
- **Integration point** in `main.py`: `LoadingView.on_update` calls `generate_maze`, then switches to `InGameView`.

### 2.2 `time_system`
- **Goal**: Cycle Day (180 s) → Night (120 s) → Blood Moon (45 s, 20 % trigger on chest open).
- **Steps**:
  1. Add `elapsed` timer variable in `InGameView`.
  2. Each frame, `elapsed += delta_time`.
  3. When `elapsed >= 180` switch to Night, reset timer.
  4. When `elapsed >= 180+120` decide Blood Moon (random 0.2) → state “blood_moon”, else reset to Day.
  5. Expose `time_state` string (“day”, “night”, “blood_moon”) for HUD and enemy spawning.
- **Integration point**: call `update_time(delta)` from `InGameView.on_update`.

### 2.3 `enemy_ai`
- **Goal**: Single spider enemy with two‑state FSM (patrol / chase). Patrol drifts randomly inside its room; chase uses direct pixel pursuit when sharing a room, or BFS pathfinding when player is in an adjacent room (vision 1 room night, 2 rooms blood moon). Re‑calculate path every 5 frames.
- **Steps**:
  1. Create `Enemy` class with `x, y, speed, vision, state` (“patrol”, “chase”), `path_index`, `patrol_timer`.
  2. `spawn_enemy(time_state, player_pos, maze_grid)` – returns `Enemy` or `None` (None during Day).
  3. In `InGameView.on_update`:
     - If `time_state == "day"`: `enemy = None`.
     - Else: `enemy = spawn_enemy(...)` (once per state change or every few seconds).
     - Run FSM:
       * Patrol: add random drift, bounce off walls using collision detection.
       * Chase (same room): move directly toward player `x,y` each frame.
       * Chase (adjacent room): invoke `bfs_find_path(maze_grid, enemy.pos, player.pos)`; follow first step; recalc every 5 frames.
  4. Collision with player → reduce `player.health`.
- **Integration point**: `InGameView.on_update` after player movement.

### 2.4 `collision_detection`
- **Goal**: AABB collision for player‑enemy damage; corner‑point check against `maze_grid` for player movement clamping.
- **Steps**:
  1. `check_wall_collision(px, py, dx, dy, maze_grid)`:
     - Compute new player corners after intended movement.
     - Map each corner to grid cell `(gx, gy)`.
     - If any cell value == 0 (wall), reject movement on that axis (keep original position or slide).
  2. `check_enemy_player_collision(enemy, player)`: simple AABB overlap of 64×64 hitboxes; on contact, `player.health -= enemy.damage`.
  3. Call `check_wall_collision` before updating `player.x/y` in `player_movement`.
- **Integration point**: top of `InGameView.on_update`, before player position update.

### 2.5 `player_movement`
- **Goal**: WASD movement, speed modified by hunger, stamina drain on Sprint (Shift), stamina regen when not sprinting.
- **Steps**:
  1. In `InGameView.on_key_press` store pressed keys in `self.keys` set (already present).
  2. `InGameView.on_update`:
     - Determine direction vector from `arcade.key.W/A/S/D`.
     - Apply hunger penalty: if `player.hunger < 35` speed *0.8; if `< 20` speed *0.6.
     - If `arcade.key.LSHIFT` pressed and `player.stamina > 0`: speed *= 1.5; `player.stamina -= 7*delta`; else regen `player.stamina += 3*delta` (capped at 100).
     - Compute tentative `new_x = player.x + speed*dx*delta`, `new_y = player.y + speed*dy*delta`.
     - Call `check_wall_collision` → obtain corrected `player.x, player.y`.
     - Update `player.direction` string for sprite selection.
- **Integration point**: `InGameView.on_update` after collision check.

### 2.6 `hud_display`
- **Goal**: Render health bar (green→red gradient), stamina bar (yellow), hunger bar (brown), compass rose, distance‑from‑spawn meter, time‑state icon, hotbar (4 slots labelled 1‑4).
- **Steps**:
  1. In `InGameView.on_draw`:
     - Health bar: `arcade.draw_rectangle_filled(center_x=100, center_y=screen_h-30, width=200*(player.health/100), height=20, color=arcade.color.GREEN)`.
     - Stamina bar similar at `center_x=100, center_y=screen_h-55`.
     - Hunger bar at `center_x=100, center_y=screen_h-80`.
     - Distance text: `arcade.draw_text(f"{distance:.0f}m", x=screen_w-120, y=screen_h-50, font_size=18, color=arcade.color.WHITE)`.
     - Compass rose at `(screen_w-50, 50)` (simple arrow sprite or colored triangle).
     - Time‑state icon: sun for day, moon for night, red moon for blood moon at a fixed corner.
     - Hotbar: draw four 24×24 slot frames at bottom centre; inside each, blit the item sprite if player carries it; show count.
  2. Use `player.flashlight_battery` to draw battery icon if flashlight equipped.
- **Integration point**: end of `InGameView.on_draw`.

### 2.7 `chest_ui`
- **Goal**: Press E near a chest tile → open UI; mouse‑click on one of four slots to select; press R to take the selected item one at a time; respect `max_item_types` and inventory list.
- **Steps**:
  1. Add `chest_ui_open = False`, `chest_ui_chest = None`, `chest_ui_selected = 0` to `InGameView`.
  2. In `on_key_press`, if near a chest and `arcade.key.E`: set `chest_ui_open = True`, `chest_ui_chest = chest_obj`, generate loot once via `chest.gen_loot()`.
  3. `InGameView.on_draw` when `chest_ui_open`: dim the screen, draw chest background, draw four slot boxes, highlight selected slot.
  4. `on_mouse_press` on a slot: set `chest_ui_selected = slot_index`.
  5. `on_key_press` for `arcade.key.R`: take one unit of `inventory[chest_ui_selected]` item, decrement count, remove if 0, close UI if inventory full.
  6. Update `player.inventory` list (list of `[item, count]` pairs).
- **Integration point**: `InGameView.on_update` / `on_key_press` / `on_mouse_press`.

### 2.8 `menu_system`
- **Goal**: Main menu (Start, Settings, Quit), Settings UI (volume slider, fullscreen toggle), Death screen (distance reached, Restart, Main Menu).
- **Steps**:
  1. Keep existing `MainMenu` view (already in `main.py`).
  2. Add `DeathView(arcade.View)` with text "You died\nDistance: {distance} m\n[Restart] [Quit]".
  3. Add `PauseView(arcade.View)` that draws a semi‑transparent overlay and "Resume", "Settings", "Quit" buttons.
  4. `InGameView.on_key_press` – `arcade.key.ESCAPE` toggles `self.paused`; if paused, `window.show_view(PauseView())` else resume.
  5. Buttons use `arcade.Rect` hit testing to switch views (`window.show_view`).
- **Integration point**: `main.py` entry point; `window.show_view` calls.

### 2.9 `win/lose conditions`
- **Goal**: Win when `player.distance_from_spawn >= 10000`; Lose when `player.health <= 0`.
- **Steps**:
  1. In `InGameView.on_update`, after all updates:
     - If `player.health <= 0`: `window.show_view(DeathView())`.
     - If `player.distance_from_spawn >= 10000`: `window.show_view(WinView())`.
  2. `WinView` displays "You win!\nDistance: {distance} m\n[Play Again] [Quit]".
  3. `DeathView` as above.
- **Integration point**: end of `InGameView.on_update`.

### 2.10 `pause & settings`
- **Goal**: Escape toggles pause; Settings allows toggling fullscreen and a simple volume slider (visual only, no audio implementation required).
- **Steps**:
  1. `InGameView.on_key_press` – if `arcade.key.ESCAPE` and not already paused, set `self.paused = not self.paused`.
  2. When `self.paused` true, `window.show_view(PauseView())`; PauseView handles its own loop; on “Resume” it returns to `InGameView`.
  3. Settings button in PauseView/Menu opens a simple UI; for now just print “Settings entered” – can be expanded later.
- **Integration point**: `InGameView` and `MainMenu`.

---
## 3. Quick checklist (coding only)

- [ ] Implement `generate_maze` and `LoadingView`
- [ ] Add `time_system` timer & `time_state`
- [ ] Create `Enemy` class and `enemy_ai` FSM + BFS
- [ ] Write `collision_detection` (wall & enemy‑player)
- [ ] Finish `player_movement` with hunger & stamina
- [ ] Build `hud_display` (all bars, compass, distance, hotbar, time icon)
- [ ] Implement `chest_ui` (open, select, take)
- [ ] Add `menu_system` (Start, Settings, Death, Pause)
- [ ] Wire `win/lose` triggers
- [ ] Add `pause` handling via Escape

All code changes should stay within the existing `arcade` framework and respect the y‑up coordinate system (W increases y). No new third‑party libraries are required beyond `arcade` (already in `requirements.txt`).
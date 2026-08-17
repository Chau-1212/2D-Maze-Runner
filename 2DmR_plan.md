# H446-03 Coursework: 2D MazeRunner

---

## Progress Log

| Date | Time | Activity |
|------|------|----------|
| 22/07/2026 | Morning | Extracted text from "2D Maze Runner Analysis.docx" and "2D MazeRunner - CourseWork.docx" using pypdf/python-docx — initial analysis content captured |
| 22/07/2026 | Morning | Extracted mark scheme guidance from "H446-03 Project Advice - Computer games-1.pdf" — OCR/Craig'n'Dave do's/don'ts for all 4 sections |
| 22/07/2026 | Midday | Created template `H446-03-Project-Template.md` and filled Analysis + Design sections based on student's docx |
| 22/07/2026 | Afternoon | Installed `@mermaid-js/mermaid-cli` and generated `systems_diagram.png` (LR layout, scale=2), `class_diagram.png`, `screen_designs.png` |
| 22/07/2026 | Afternoon | Expanded template with detailed justifications, pseudocode (all modules), test tables, validation, success criteria mapping |
| 22/07/2026 | Afternoon | Added mark estimate table: current ~8/70, potential 60+/70 |
| 23/07/2026 | Morning | Added missing pseudocode: `spawn_enemies_near_player`, `use_item`, `furnace_interact`, `render_view`, `handle_menu_input`, `loading_screen`, `load_json_files` |
| 23/07/2026 | Morning | Updated `main_game_loop` to call `render_view` and spawn enemies every 3s |
| 23/07/2026 | Morning | Updated "How all algorithms fit together" paragraph to reference all new procedures |
| 23/07/2026 | Morning | Reviewed student's coursework docx — Analysis section complete (~7-8/10), Design section started (6/9 modules in decomposition, missing diagram image + variables/algorithms/UI/test sections) |
| 24/07/2026 | Evening | Replaced corridor-DFS maze with room-grid maze. Enemy AI changed from tile-based to room-based Chebyshev detection. Added BFS pathfinding for chase state, removed atan2/cos/sin angle-based movement. Added `bfs_find_path` function with frame-by-frame walkthrough. Merged student's inline comments into pseudocode. |
| 24/07/2026 | Evening | Added this todo list for remaining coursework work |

---

## 📋 TODO — Coursework Docx Fixes

### Section 1: Analysis — Typos (search/replace in Word)
- [ ] "skate holder" → **stakeholder** (6 occurrences)
- [ ] "grade period" → **grace period**
- [ ] "1000km" / "1000m" → **10000m** / **10km** (win condition)
- [ ] "spirited" → **sprites**
- [ ] "neorealistic" → **no realistic**
- [ ] "Py game" → **Pygame**
- [ ] "suing" → **using**
- [ ] "look system" → **loot system**
- [ ] "dealta" → **delta**
- [ ] "coillision" → **collision**
- [ ] "compuitationall" → **computationally**
- [ ] "bmoon" → **blood_moon**
- [ ] "enemis" → **enemies**
- [ ] "spawn_enemis" → **spawn_enemies**
- [ ] "directions" → **directionless**
- [ ] "phone" (target platform) → **PC** (consistency)

### Section 1: Analysis — Content Fixes
- [ ] 1a: Fix "1000km" in Thinking Logically → **10km**
- [ ] 1b: Fix "skate holder" → **stakeholder** (all occurrences)
- [ ] 1b: Fix target platform "phone" → **PC**
- [ ] 1c: Add evaluation — what you'd do differently after playing each game
- [ ] 1f: Expand "Thinking logically" — explain *why* conditions exist, not just list them
- [ ] 1g: Separate **Deployment requirements** from Development requirements clearly
- [ ] 1h: Add measurable pass/fail metrics to success criteria (e.g., "reach 10km within 10 min")

### Section 2: Design — Missing Content to Add
- [ ] **2b Decomposition**: Add missing modules (`update_time`, `render_view`, `handle_menu_input`, `loading_screen`, `load_json_files`)
- [ ] **2c Variables**: Verify class diagram image matches updated `Enemy` class (has `path`, `path_index`, `patrol_dx`, `patrol_dy`, removed `idle`/`returning` states)
- [ ] **2d Algorithms**: Add missing pseudocode for:
  - [ ] `enemy_ai_update` (2-state FSM + BFS chase + same-room direct)
  - [ ] `collision_detection` (AABB + corner-point)
  - [ ] `loot_system` (cumulative probability)
  - [ ] `hud_display` (bar rendering, compass, hotbar)
  - [ ] `menu_system` (state transitions, button handling)
- [ ] **2e Usability/UI Design**: Add section with screen designs, controls, accessibility
- [ ] **2f Validation**: Add input validation rules (screen bounds, interaction range, item usage, menu inputs, pause, JSON validation)
- [ ] **2g Test Data**: Add test tables for all modules (player_movement, generate_maze, collision_detection, enemy_ai, open_chest)
- [ ] **2h Success Criteria Mapping**: Table linking each criterion to Design algorithms
- [ ] **Images**: Insert `systems_diagram.png`, `class_diagram.png`, `screen_designs.png`

### Config Files to Update
- [ ] `enemies.json`: vision values → **1** (night_spider), **2** (blood_moon_spider) [rooms, not tiles]
- [ ] Verify `items.json` / `loot_table.json` match template

### Consistency Checks
- [ ] Win distance: **10000m / 10km** everywhere (not 1000km)
- [ ] Platform: **PC** everywhere (not phone)
- [ ] Enemy states: **patrol / chase** (not idle/chasing/returning)
- [ ] Vision: **1 room / 2 rooms** (not 2/3 tiles)
- [ ] Enemy AI: **2-state FSM + BFS** (not 3-state + 10s target update)

## Comparison: Analysis docx vs Coursework docx

| Area | Analysis Docx (Old) | Coursework Docx (New) |
|------|-------------------|----------------------|
| Structure | No sections — raw brainstorming | Sections 1a-1h clearly labelled |
| Project outline | Brief 1-sentence description | Full paragraph with genre, mechanics, similar games |
| Stakeholder | Mentions target audience + stakeholder feedback | More detail with age, PEGI rating, platform choice |
| Research | Minecraft, Rust, Terraria (brief notes) | Minecraft, Binding of Isaac, ISO Core (What I Like/Dislike/Inspiration per game + Synthesis) |
| Features | Bullet list of mechanics | Each feature explained with reasoning |
| Limitations | 1 sentence about sprites | 8 specific limitations with justifications |
| Computational Methods | Scattered notes throughout doc | Structured 4 methods (abstraction, ahead, procedural, logical, concurrent) |
| Success Criteria | Not present | 8 success criteria in a table |
| Design | "Soltuion" section with rough JSON sketch | Systems Diagram heading + 9 modules fully decomposed + Global Variables heading |
| **Verdict** | **Early draft — replace with coursework docx** | **Much better — keep this one** |

**Can you replace your new coursework with the old analysis? NO — the coursework docx is far more complete.** The analysis docx is an early draft; the coursework docx has proper sectioning, justifications, and the start of Design.

## What needs improving in your Coursework Docx

### Section 1: Analysis (currently ~7-8/10 — good foundation)

| What | Issue | How to Fix |
|------|-------|------------|
| 1a | "grade period" — typo | Change to **grace period** |
| 1a | "1000km" in thinking logically | Should be **10km** (10000m), not 1000km — consistency error with features |
| 1b | "skate holder" multiple times | Should be **stakeholder** |
| 1b | Says target platform is "phone" | Earlier says PC — pick one (stick with PC) |
| 1c | Research is good but lacks evaluation | Add what you'd do differently after playing each game |
| 1f | "Thinking logically" just lists if-statements | Explain *why* these conditions exist, not just what they are |
| 1g | No "Deployment requirements" distinction | Separate dev vs deployment hardware clearly |
| 1h | Success criteria missing measurable outcomes | Add pass/fail metrics (e.g., "reach 10km within 10 min") |

### Section 2: Design — verify your images/tables are correct

You have 3 images and 2 tables that I can't see via text extraction. Check these yourself:

| What | Check |
|------|-------|
| 2a | Systems diagram image — does it have all 9 modules with clear flow? |
| 2c | Global variables table — does it match the template's variable list? |
| 2c | Class diagram image — does it match your Python-style data structures? |
| 2d | Pseudocode — do you have algorithms for all 9 modules? |
| 2e | Screen design image — does it show menu, gameplay HUD, death screen? |
| 2f | Validation — do you have input validation rules? |
| 2g-2h | Test tables — do you have test data for each module? |

### Overall issues to fix:
- **Typos**: "stakeholder" not "skate holder", "10km" not "1000km", "Pygame" not "Py game", "grace period" not "grade period"
- **Justifications**: Every Design decision needs a "why I chose this" — your module descriptions do this well already
- **Consistency**: If Analysis says PC, don't say phone in another section
- **Replace the old Analysis docx**: It was a draft. Don't use it. Keep working in the Coursework docx.

---

## Section 1: Analysis

### 1a — Project Outline

**Game name:** 2D MazeRunner

**Genre:** Top-down Survival Game with maze exploration and resource management

2D MazeRunner is a top-down survival game where the player navigates a randomly generated maze while managing health, stamina, and hunger. The game uses a dynamic time mechanic with three states — Day, Night, and Blood Moon — each changing the rules of survival. During the Day (the "Grace Period"), no enemies spawn and the player can explore safely. When Night falls, enemies begin spawning and the player's vision is limited. Blood Moon is a rare random event where enemies become significantly stronger and faster, creating an intense survival challenge.

The game draws from the survival genre convention of resource management under pressure. Like games such as Minecraft and Terraria, the player must balance exploration with risk assessment — deciding when to push deeper into the maze and when to fall back. The maze is procedurally generated using modular tiles, ensuring each playthrough offers a unique layout while maintaining connectivity (a "perfect maze" where all paths are reachable).

Similar games include Minecraft (survival, crafting, day/night cycle), The Binding of Isaac (top-down dungeon crawling, procedurally generated rooms, item pickups), and ISO Core (top-down survival with resource management). 2D MazeRunner combines the procedural exploration of these games with a compact 10-minute runtime designed for short, intense play sessions.

### 1b — Stakeholders & Target Audience

**Target market:** Young adults aged 15–18 who have limited time for gaming but want an intense, rewarding experience. Each run lasts approximately 10 minutes, making it suitable for short sessions. The game is rated PEGI 3 — although it has enemies and survival elements, there is no realistic violence or gore, keeping it accessible to a wide audience.

**Target platform:** Primarily PC (laptop/desktop) with keyboard and mouse controls. The colour theme is deliberately dark since younger players often game at night or in dimly lit rooms. The game includes an offline mode, broadening accessibility to players without consistent internet access.

**Stakeholder:** I interviewed two friends aged 15 and 17 who represent the target audience. Their feedback highlighted the following preferences:
- Quick gameplay sessions
- Clean, modern/minimalistic UI with the option to view more detail
- Fast movement options (sprint / items)
- Random events (e.g. lightning highlighting enemies temporarily)
- Clear, readable sprites

This feedback directly influenced design decisions such as the sprint mechanic, the Blood Moon random event, and the minimalist HUD design. Although multiplayer was also requested, I chose not to implement it because networked multiplayer is beyond the scope of this project and would compromise the quality of the single-player experience.

**Why the game suits them:** The learning curve is gentle — movement uses standard WASD controls that most players already know. The core loop of explore → gather → survive is intuitive to understand, but mastering resource management (balancing hunger, stamina, flashlight battery, and health) provides depth. The 10-minute runtime respects their limited time, while the randomised maze ensures replayability.

### 1c — Research into Similar Games

**Minecraft (Mojang, 2011)**

- **Visuals & behaviour:** Block-based 3D world with a day/night cycle. During the day, the player gathers resources safely; at night, hostile mobs spawn. The player manages health and hunger bars.
- **What I like:** The day/night cycle creates natural pacing — safe periods for preparation and dangerous periods for combat. The hunger system adds a resource-management layer beyond just health.
- **What I dislike:** The open-world sandbox can feel directionless. The crafting system requires memorising recipes, which adds unnecessary complexity for a quick-play game.
- **Features to adapt:** The day/night time cycle (adapted into my Day/Night/Blood Moon system), health and hunger bars, enemy spawning tied to time state.

**The Binding of Isaac (Edmund McMillen, 2011)**

- **Visuals & behaviour:** Top-down dungeon crawler with procedurally generated rooms connected in a grid. Each room contains enemies, obstacles, or rewards. The player collects items that modify stats or add new abilities.
- **What I like:** Procedural room generation ensures no two runs are the same. Item pickups create meaningful choices and build variety. The room-by-room structure is easy to understand.
- **What I dislike:** The grotesque art style and mature themes limit the audience. Some item combinations can make the game trivial.
- **Features to adapt:** Procedural maze generation using modular tiles, chest loot system with randomised drop rates, item pickups that affect gameplay.

**ISO Core (Brace Yourself Games, 2024)**

- **Visuals & behaviour:** Top-down survival game with resource management, crafting, and environmental challenges. The player explores a generated world while managing stats and crafting tools.
- **What I like:** The clean, minimal UI presents exactly what the player needs without clutter. Resource management feels meaningful without being overwhelming.
- **What I dislike:** The isometric perspective can make navigation confusing in tight spaces.
- **Features to adapt:** Minimalist UI design, compact stat display (health, hunger, stamina meters), item-based interaction system.

**Synthesis:** From this research, I have decided to include a three-state time mechanic (Day/Night/Blood Moon) inspired by Minecraft's day/night cycle because it creates natural pacing without needing a complex AI director. I chose procedural maze generation using modular tiles from The Binding of Isaac because it guarantees replayability while keeping the code manageable — each tile is a simple data structure rather than a hand-crafted room. I adopted ISO Core's minimalist HUD because clutter would be dangerous in a maze where the player needs to spot enemies quickly. I will leave out complex crafting recipes (too much complexity for a 10-minute game), isometric graphics (navigation clarity is more important in a maze), and mature themes (to keep my PEGI 3 rating and reach a wider audience).

### 1d — Features of Your Solution

1. **Three-state time system (Day/Night/Blood Moon)** — Each state changes gameplay conditions: Day is safe for exploration, Night spawns enemies and limits vision, Blood Moon is a rare random event with stronger enemies. This creates pacing and risk/reward decisions, directly inspired by Minecraft's day/night cycle. I chose three states rather than two because the Blood Moon adds variety — stakeholders specifically wanted random events.

2. **Procedural maze generation using DFS** — The maze is a grid of rooms separated by walls; DFS decides which walls get a doorway to connect adjacent rooms. Each room has a type (Safe, Danger, Chest) and contains floor tiles the player can walk on. The maze spans 10km across, achievable in ~10 minutes of gameplay. DFS was chosen over Prim's or Kruskal's because it guarantees every room is reachable with exactly one path between any two — no loops, no isolated rooms.

3. **Enemy AI with two-state FSM** — Spiders spawn during Night and Blood Moon, using a two-state Finite State Machine (patrol / chase). During patrol the spider drifts randomly within its starting room; when the player enters the same or an adjacent room (vision range: 1 room Night, 2 rooms Blood Moon) the spider transitions to chase. Chase uses direct pixel pursuit when sharing a room, or BFS pathfinding when in adjacent rooms — the spider recalculates the path every 5 frames. If the player moves beyond vision range the spider returns to patrol. BFS was chosen because it guarantees the shortest path through the maze without the spider walking into walls.

4. **Player stat system (Health, Stamina, Hunger)** — Health depletes from enemy damage, stamina drains while sprinting (7%/s), and hunger decreases over time (10%/min). Hunger affects movement speed and sprint ability. I chose 7%/s for stamina drain because it allows ~14 seconds of sprinting which feels substantial but not unlimited. The 10%/min hunger rate means the player must eat roughly every 10 minutes — matching the intended play session length.

5. **Item and loot system** — Chests spawn in "Chest" tiles with randomised loot (Flashlight 5%, Bread 30%, Raw Meat 20%, Coal 20%, Battery 10%, Nothing 15%). Chests opened during Night give better loot (3-5 items, Flashlight doubles to 10%) — this rewards the player for taking the 20% Blood Moon risk, so opening a chest at Night is a genuine risk/reward decision rather than always-worse. I chose these drop rates so that food (the most commonly needed item) appears most often (Bread 30% + Raw Meat 20% = 50% food drop rate), while the powerful Flashlight is rare (5%) to make it feel special. The 15% "Nothing" chance adds disappointment as a balancing mechanic.

6. **Flashlight mechanic** — Gives +1 tile vision and can scare away enemies with a bright flash (costs 25% battery). Batteries recharge 40-50%. The 25% battery cost per use means the player gets 4 flashes per full battery, encouraging tactical use rather than spamming. The 40-50% recharge range was chosen to make Battery items useful but not game-breaking.

7. **Compass and distance meter** — A compass shows direction and a meter shows distance from spawn. The win condition is reaching 10km distance. This gives the player a clear goal in the procedurally generated maze — without it, they would have no sense of progress. The compass prevents the player from walking in circles.

8. **Loading screen** — The maze is generated during a loading screen so gameplay runs at high FPS even on lower-end devices. I chose this approach rather than generating the maze in real-time because generation takes ~2-3 seconds and doing it during gameplay would cause visible frame drops.

### 1e — Limitations & Scope

- **Sprite detail:** Pixel art in Aseprite rather than highly detailed sprites — performance and consistent aesthetic. I chose pixel art because it's efficient to render (small file sizes, no texture filtering needed) and I can create it myself without needing an artist.
- **Number of enemy types:** One enemy (Spider) with two stat variants — this lets me perfect the AI system rather than spreading my effort across multiple enemy behaviours.
- **Number of item types:** Six items + Furnace — enough for meaningful resource management choices without overwhelming the player or the development schedule.
- **No multiplayer:** Stakeholders requested it, but implementing networked multiplayer would require server infrastructure, synchronisation protocols, and anti-cheat measures that are beyond the scope of an A-Level project.
- **No crafting system:** The Furnace has a single recipe (Coal → Cooked Meat). A full crafting system would require a recipe database, UI for crafting menus, and balancing effort that doesn't add proportional value to a 10-minute game.
- **5 game states only:** Menu, Settings, Loading, In Game, Death Screen. Features like tutorials or achievement screens would add development time without improving the core gameplay loop.
- **Maze size capped at 10km × 10km:** A larger maze would increase generation time and memory usage. 10km provides ~10 minutes of gameplay which matches the target session length.

### 1f — Computational Methods

**Abstraction**
The key objects in my game are the Player, Enemies (Spiders), Items, and Maze Tiles. Real-world elements are simplified: the player is a 64x64 sprite with directional frames rather than a realistic character; hunger is a numeric value rather than a complex metabolic system; enemies are simplified to speed, damage, and vision range stats. The maze abstracts a physical space into a 2D grid of tile types (Safe, Danger, Chest) with connection rules. Sound effects and visual effects abstract the "feel" of survival without simulating real physics — a flash effect represents the flashlight without modelling actual light physics.

**Thinking ahead**
Before development, I planned all player inputs: WASD for movement, E for interaction (chests, furnace), F to toggle flashlight, number keys 1-4 to use items. Outputs include the game window, HUD (health/stamina/hunger bars, compass, distance meter), sound effects, and UI screens (menu, settings, death screen). I designed four directional sprite frames so the player's facing direction is always clear. I also planned that maze generation happens during a loading screen so the player never sees incomplete geometry — without this foresight, the maze would appear to build itself mid-game which would break immersion.

**Thinking procedurally**
The game has five states: Starting Menu → Settings (optional) → Loading Screen → In Game → Death Screen. Each state has a defined entry and exit. Within the In Game state, the sequence is: generate maze → spawn player → start time cycle → spawn enemies at night → check collisions → update stats → check win/loss conditions. This ordering is critical — enemies must not spawn before the maze is generated (they would appear in walls), and stat updates must happen after collision detection (otherwise damage would be applied a frame late, allowing the player to take extra hits).

**Thinking logically**
Key conditions that become `if` statements include:
- `if time_state == NIGHT then spawn_enemies()`
- `if player_hunger <= 0 then disable_sprint()`
- `if player_health <= 0 then trigger_death_screen()`
- `if player_distance >= 10000 then trigger_win()`
- `if player hits enemy hitbox then take_damage()`
- `if player presses E near chest then open_chest_loot()`
- `if flashlight_battery <= 0 then disable_flashlight()`
- `if inventory[slot] is empty then ignore_use()`

The main game loop runs continuously: process input → update player position → update enemies (AI pursuit) → check collisions → update stats → render frame. The loop only exits when the player quits, dies, or wins.

**Thinking concurrently**
Multiple processes happen simultaneously:
- The maze generation runs on a separate thread during the loading screen while a loading animation plays
- Enemy AI updates for all spawned enemies each frame (multiple enemies move and check vision simultaneously)
- The time system counts up independently while the player explores
- Random events (Blood Moon trigger) are checked alongside gameplay
- Sound effects play while game logic updates — using Pygame's mixer which runs on a separate audio thread
- Chest loot is only generated when the player interacts (not pre-generated), saving CPU resources

**Why a computer game is amenable to a computational approach:** A computer game cannot exist without a computer — it involves real-time calculations (position updates, collision detection), state management (time states, game states), random number generation (maze generation, loot drops), and rendering. Every aspect of 2D MazeRunner — from the DFS maze algorithm to the enemy AI's Finite State Machine to the HUD display — relies on computational logic, loops, conditionals, and data structures that only a computer can execute at the speed required for interactive gameplay. A human could not manually calculate collision detection 60 times per second, and a board game version would lose the tension of real-time enemy pursuit.

### 1g — Hardware & Software Requirements

**Development requirements:**
- **Computer:** Windows 10+, 2GHz processor, 8GB RAM, 1GB free storage
  - 2GHz dual-core minimum: Pygame is not heavily multi-threaded for game logic, so a single fast core is more important than multiple slow cores. 2D pixel-art rendering is not computationally intensive, so 2GHz is sufficient.
  - 8GB RAM: Python + Pygame use ~200MB at runtime, but the IDE (VS Code/Zed), web browser for research, and running game tests simultaneously requires more. 8GB ensures no swapping during development.
  - 1GB storage: The game uses pixel-art sprites (small file sizes), JSON config files (kilobytes each), and procedural generation (no large pre-built assets). 1GB accommodates the project, Python installation, IDE, and libraries.
- **IDE:** VS Code or Zed with Python extension — chosen for the integrated debugger (essential for stepping through game logic), IntelliSense (speeds up development by auto-completing Pygame method names), and integrated terminal (quick testing without switching windows).
- **Libraries:** Pygame (graphics rendering, input handling, sound mixer), JSON (config file parsing), random (maze generation randomness, loot drops), math (distance calculations, trig for enemy movement angles).
- **Sprite editor:** Aseprite — chosen because it is specifically designed for pixel art, has animation frame support, exports to PNG which Pygame loads natively, and has a minimal UI that doesn't distract from the art creation process.

**Deployment requirements:**
- **Minimum specs:** Windows 10+, 2GHz processor, 4GB RAM, 500MB storage
  - 4GB RAM: The game uses ~200-500MB at most (maze grid, sprites, enemy list). 4GB is the modern baseline for any Windows machine and ensures the OS + game run without swapping.
  - 500MB storage: The packaged executable (via PyInstaller) bundles the Python runtime + assets and will be under ~200MB. 500MB is a conservative estimate.
  - Windows 10+: Pygame relies on SDL2 which requires Windows 10 for hardware-accelerated rendering support.
- **Software:** Python 3.10+ with Pygame installed, or a packaged executable (via PyInstaller).
- **Input:** Keyboard and mouse — WASD movement, E interact, F flashlight, 1-4 items, mouse for menu navigation. No controller support to keep the input handling simple and focused.

### 1h — Success Criteria

| # | Criterion | Justification |
|---|-----------|---------------|
| 1 | The player can move the character in four directions using WASD, and the character stops at maze boundaries | Genre convention — all top-down games require responsive movement. Without this the game is unplayable. |
| 2 | The time cycle progresses Day → Night → Day in a loop, and enemies only spawn during Night and Blood Moon | Core mechanic derived from Minecraft's day/night cycle. Creates pacing between safe and dangerous periods. |
| 3 | Blood Moon triggers as a random event (~20% chance when looting a chest) and boosts enemy speed and damage | Direct stakeholder request for random events to add unpredictability. |
| 4 | At least one enemy type chases the player when within vision range (same room during Night, up to 1 room away during Blood Moon) and deals damage on contact | Core survival mechanic — without enemies there is no challenge and no sense of danger. |
| 5 | The player has Health, Stamina, and Hunger stats displayed on the HUD, and each depletes according to its rule | Research from Minecraft and ISO Core — stat management is essential to survival games. The HUD must show these clearly so the player can make informed decisions. |
| 6 | The player can collect items from chests with randomised drop rates matching the specified table, and chests opened during Night give better loot (3-5 items, doubled rare drop chance) as a reward for the Blood Moon risk | Inspired by The Binding of Isaac — loot creates meaningful choice and replayability. The Night loot bonus gives players a reason to open chests at Night despite the 20% Blood Moon trigger, turning a pure risk into a risk/reward decision. |
| 7 | The maze is procedurally generated using DFS and is a "perfect" maze (all paths connect) | Technical requirement — the maze must be solvable (no dead ends that block progress) and different each run for replayability. |
| 8 | The game runs at a minimum of 30 FPS with the full maze generated and the spider active | Performance baseline for acceptable gameplay. Below 30 FPS the game feels laggy and unresponsive. |
| 9 | The player wins by reaching 10km distance from spawn, displayed via the distance meter, and a typical play session reaches this in under 10 minutes | Win condition must be clear and measurable so the player knows what to aim for. The 10-minute target ensures the game fits the intended short-session design. |
| 10 | The game includes a menu screen (Start, Settings, Quit) and a death screen triggered when health reaches 0 | Standard game state management — the player needs clear entry/exit points and feedback on failure. |
| 11 | The player can pause the game at any time using the Escape key | Usability requirement — players need to be able to pause for interruptions or to read item descriptions. |
| 12 | The game uses dark colour tones and pixel-art sprites consistent across all assets | Aesthetic choice justified by target audience preferences (dark theme for nighttime play). Consistency prevents visual jarring. |

---

## Section 2: Design

### 2a — Systems Diagram

![Systems Diagram](systems_diagram.png)

The systems diagram shows the overall structure broken into three phases: Menu System (blue), Loading Phase (purple), and Gameplay Loop (yellow). The Gameplay Loop is the largest section because it contains the core game logic — input handling, movement, time system, enemy AI, collision detection, stats, loot, and HUD updates. The loop repeats until the player dies (red) or reaches 10km (green). I deliberately separated the Menu and Loading phases from the Gameplay Loop because they only run once per session, whereas the Gameplay Loop runs 60 times per second. This separation makes the code easier to debug — if there's a bug in the menu, I know where to look without wading through game logic code.

### 2b — Decomposition (Breaking It Down)

Each module below corresponds to a box in the systems diagram. I have decomposed the problem using step-wise refinement — starting with the overall game, breaking it into phases (menu, loading, gameplay), then breaking gameplay into individual procedures. This approach makes the problem manageable because each module has a single responsibility.

**Module name:** `generate_maze`
- **Purpose:** Uses Depth-First Search to generate a perfect maze from modular tiles. Produces a 2D grid representing the maze layout with each cell storing its tile type (Safe/Danger/Chest), structure type (connections), and whether it contains a chest.
- **Graphics needed:** Modular tile sprites (4 connection variants × 3 tile types = 12 base tiles)
- **Why this approach:** I chose to generate the entire maze at once during loading rather than generating chunks on-demand, because a 10km × 10km maze with modular tiles can be generated in ~2 seconds, and generating during gameplay would cause visible frame drops. The maze is stored in a 2D array in memory so that collision detection can access any tile in O(1) time — reading from disk each frame would be too slow.

**Module name:** `spawn_enemies`
- **Purpose:** Reads the current time state and spawns enemies on Danger/Chest tiles at the appropriate distance from the player. During Night, enemies spawn 2 tiles away; during Blood Moon, 1 tile away.
- **Graphics needed:** Spider sprite (Night variant, darker colour), Spider sprite (Blood Moon variant, red tint to signal danger)
- **Why this approach:** Spawning enemies at a minimum distance from the player prevents "pop-up" spawns that would feel unfair (an enemy appearing right on top of the player). The closer spawn distance during Blood Moon (1 tile vs 2 tiles) creates additional tension for that event. Enemy stat tables are loaded from JSON at startup to make balancing easy — I can adjust speed or damage by editing a text file without changing code.

**Module name:** `player_movement`
- **Purpose:** Reads WASD input and updates the player's x/y position. Movement speed is reduced proportionally to hunger level (< 35 hunger = 80% speed, < 20 hunger = 60% speed). Sprint (Shift key) drains stamina at 7%/s and increases speed by 50%.
- **Graphics needed:** Player sprite (64x64 with 4 directional frames for up/down/left/right facing)
- **Why this approach:** I chose proportional speed penalties for hunger rather than a binary on/off switch because it gives the player gradual feedback that they need to eat, rather than suddenly being unable to sprint. The 50% sprint speed bonus makes sprinting meaningful while the stamina drain prevents unlimited use. Movement is clamped to maze boundaries via collision detection — if the new position overlaps a wall, the position is rejected rather than corrected, which prevents the player from "snapping" to the nearest open space.

**Module name:** `time_system`
- **Purpose:** Counts elapsed time since the start of the game session and flips a flag between Day, Night, and Blood Moon states. Day lasts 180 seconds, Night lasts 120 seconds, Blood Moon lasts 45 seconds. Blood Moon has a ~20% chance of triggering when the player opens a chest during Night.
- **Graphics needed:** HUD indicator showing current time state (sun icon for Day, moon for Night, red moon for Blood Moon)
- **Why this approach:** I chose 180s Day / 120s Night because this gives the player 3 minutes of safe exploration before enemies appear, which feels long enough to make progress but short enough to maintain tension. The 45s Blood Moon duration is short enough to be intense without overwhelming the player.

**Module name:** `enemy_ai`
- **Purpose:** Implements a two-state Finite State Machine (patrol / chase). During patrol the spider drifts randomly within its room. When the player enters the same room (Night) or an adjacent room (Blood Moon), the spider transitions to chase. In same-room chase, the spider moves directly toward the player pixel by pixel each frame. In different-room chase, BFS pathfinding computes the shortest route through the maze — no continuous telepathy or outdated 10-second position snapshots.
- **Graphics needed:** Enemy movement frames (4 directional sprites matching player style)
- **Why this approach:** The two-state FSM is simpler than three-state (Idle/Chase/Return) because the BFS path already handles navigation through the maze — there's no need for a separate "return to spawn" state. Using Chebyshev room distance (max of delta rx, delta ry) for vision is cheaper than Euclidean pixel distance and aligns naturally with the room-grid maze. BFS guarantees the shortest path and recalculates every 5 frames, so the spider responds immediately when the player changes rooms.

**Module name:** `collision_detection`
- **Purpose:** Checks AABB (Axis-Aligned Bounding Box) collisions between the player and enemies for damage, and between the player and maze walls for movement clamping.
- **Graphics needed:** None
- **Why this approach:** AABB collision is the standard approach for 2D tile-based games because it is computationally cheap (4 comparisons per check) and accurate enough for pixel-art sprites. More complex methods like pixel-perfect collision would be unnecessary overhead since all sprites are rectangular. Wall collision uses corner-point checking — testing all four corners of the player bounding box against the tile grid, which prevents the player from clipping through walls at high speed.

**Module name:** `loot_system`
- **Purpose:** When the player interacts (E) with a chest, generates 2-4 random items (3-5 at Night) using a cumulative probability drop table. The rare Flashlight drop rate doubles at Night (5% → 10%) to reward the Blood Moon risk. Items are generated on first open only — subsequent interactions show the same loot. The player clicks to select a slot and presses R to take the item one at a time.
- **Graphics needed:** Item sprites (Flashlight, Bread, Raw Meat, Cooked Meat, Coal, Battery — each 16x16 pixels)
- **Why this approach:** Generating 2-4 items per chest (rather than 1) makes looting more rewarding and creates interesting inventory decisions — the player may want multiple items but must consider stack limits. The Night bonus (extra item + doubled Flashlight rate) directly counterbalances the 20% Blood Moon trigger — without it, opening a chest at Night is always worse than waiting for Day, which removes a decision from the game. Generating on first open avoids CPU waste on unopened chests while the `is_opened` flag ensures consistent loot across repeated interactions. The click-to-select, R-to-take interaction pattern is familiar from games like Minecraft and avoids accidental loot.

**Module name:** `hud_display`
- **Purpose:** Renders health bar (green → red gradient based on percentage), stamina bar (yellow), hunger bar (brown), compass showing direction, distance-from-spawn meter, current time state indicator, and item hotbar (4 slots labelled 1-4).
- **Graphics needed:** Bar textures (32px wide), compass rose (16x16), item slot frames (24x24 each)
- **Why this approach:** I chose a minimalist HUD (inspired by ISO Core) because cluttered UI elements would distract the player from spotting enemies in the maze. The semi-transparent dark background behind HUD elements ensures readability against any maze tile colour. Health bar colour shifts from green to red as health decreases — this is supplemented by the numeric value so colour-blind players can also read their health.

**Module name:** `menu_system`
- **Purpose:** Displays the starting menu (Start button, Settings, Quit), settings UI (volume slider, fullscreen toggle), and death screen (distance reached, restart, main menu).
- **Graphics needed:** Menu background (dark gradient), button sprites (3 sizes for hierarchy), font assets (pixel font matching game art style)
- **Why this approach:** I used a gradient background rather than a static image because it creates visual interest without the file size of a background image. Button sizes create visual hierarchy — Start is largest because it's the primary action, Settings and Quit are smaller. This is a standard UI convention that players recognise instinctively.

### 2c — Key Variables & Data Structures

**Global variables:**

| Variable Name | Data Type | Purpose |
|--------------|-----------|---------|
| `player_health` | Integer | Tracks player health (0-100). When 0, the game ends. |
| `player_stamina` | Float | Tracks player stamina (0-100). Depletes at 7%/s during sprint. Regenerates at 3%/s when not sprinting. |
| `player_hunger` | Integer | Tracks player hunger (0-50). Decreases 10%/min. Affects speed proportionally. |
| `player_x`, `player_y` | Float | Player's current position in pixels. Float allows smooth sub-pixel movement. |
| `player_direction` | String | Current facing direction ("up", "down", "left", "right"). Determines which sprite frame to render. |
| `time_state` | String | Current time state ("day", "night", "blood_moon"). Controls enemy spawning and HUD indicator. |
| `game_state` | String | Current game state ("menu", "settings", "loading", "playing", "paused", "death"). Controls which screen is rendered. |
| `distance_from_spawn` | Float | Euclidean distance from spawn point. Win condition triggers at >= 10000. |
| `maze_grid` | 2D Array of Tile objects | Stores the maze layout. Each cell contains tile type, structure type, and connection data. |
| `enemy` | Enemy object or None | The single spider currently on the map. None if no spider is active (Day). Updated each frame. |
| `inventory` | Dictionary | Stores item names → quantities (e.g., `{"bread": 3, "coal": 2}`). Max stack of 5 per item type. |
| `flashlight_battery` | Integer | Flashlight battery percentage (0-100). Depletes by 25 per use, recharged by Battery item (40-50%). |
| `chest_ui_open` | Boolean | Whether the chest loot UI is currently open. When TRUE, only chest UI keys respond. |
| `chest_ui_chest` | Chest or None | Reference to the chest object that is currently open. Used to show/take items. Resets to None on close. |
| `chest_ui_selected` | Integer | Which slot the cursor is hovering on in the chest UI. Set by mouse click. R takes the selected slot's item. |

**Class diagram:**

![Class Diagram](class_diagram.png)

**Data structures (Python-style):**

My project uses a procedural modular design — 9 main functions operating on shared data structures and global state (see pseudocode in 2d). Each data structure below is a simple Python class.

```
class Tile:
    tile_type: str          # "safe", "danger", "chest"
    structure_type: int     # connection variant 1-4
    connections: list       # [N, S, E, W] bool flags
    def is_walkable(self)
    def can_spawn_enemy(self)

class Enemy:
    x: float
    y: float
    speed: float            # 50 (Night), 500 (Blood Moon)
    damage: int             # 25 (Night), 50 (Blood Moon)
    vision_range: int       # 1 (Night — same room), 2 (Blood Moon — adjacent room)
    state: str              # "patrol", "chase"
    enemy_type: str         # "night_spider" or "blood_moon_spider"
    patrol_dx: int          # -1, 0, or 1 — random drift direction
    patrol_dy: int
    path: list              # list of (tx, ty) tile coords from BFS
    path_index: int         # which tile in the path the spider is moving toward
    def update(self, px, py, dt, maze_grid)
    def chase(self, dt, maze_grid)
    def patrol(self, dt)

class Chest:
    grid_x: int
    grid_y: int
    is_opened: bool      #TRUE after first interaction — loot generated
    contents: list       #list of item names, e.g. ["bread", "coal", "raw_meat"]
    is_empty: bool       #TRUE when all items have been taken
    def open(self)

class Item:
    name: str
    item_type: str
    effects: dict
    def apply(self, player)

class LootTable:
    entries: list
    def roll(self)
    def get_chance(self, item)

class MazeGrid:
    width: int
    height: int
    seed: int
    grid: list             # 2D array of Tile
    def generate(self, seed)
    def get_tile(self, x, y)
    def is_in_bounds(self, x, y)

class PlayerStats:
    x: float
    y: float
    health: int
    stamina: float
    hunger: int
    direction: str
    inventory: dict
    flashlight_battery: int

class TimeState:
    time_state: str        # "day", "night", "blood_moon"
    elapsed_time: float    # accumulates dt each frame
    day_duration: int = 180
    night_duration: int = 120
    bm_duration: int = 45
    bm_timer: float        # accumulates dt while blood moon active

class Camera:
    x: float
    y: float
    def follow(self, px, py)

class GlobalState:
    game_state: str
    spawn_x: float
    spawn_y: float
    distance: float
    win_distance: float = 10000.0
```

**External files:**
- `enemies.json` — enemy stats per type
- `items.json` — item definitions
- `loot_table.json` — chest drop weights

**Data structures:**
- **maze_grid:** 2D array of integers. Dimensions depend on room count and room size (e.g. 33×33 rooms × 5-tile rooms = ~200×200 tiles for 10km). The seed only affects which walls become doorways, not the size. Chosen over a dictionary because array indexing is O(1) and the maze is a fixed grid, making it the most efficient option for frequent collision lookups.
- **enemy:** Single Enemy object (or None). Only one spider exists on the map at a time — a list is unnecessary. If the player kills it or it despawns, a new one spawns later. This simplifies the code and saves memory.
- **inventory:** Python dictionary mapping item names to quantities. Dictionaries provide O(1) average lookup time, which is important because inventory operations happen every time the player uses an item or opens a chest.

**File structures (JSON config files):**
```
enemies.json:
{
  "enemies": [
    {"name": "night_spider", "speed": 50, "damage": 25, "vision": 1},
    {"name": "blood_moon_spider", "speed": 500, "damage": 50, "vision": 2}
  ]
}

items.json:
{
  "items": [
    {"name": "flashlight", "action": {"vision_boost": 1, "scare": true}, "battery_cost": 25},
    {"name": "bread", "action": {"hunger_restore": 25}},
    {"name": "raw_meat", "action": {"heal": 5, "stamina_penalty": 10, "duration": 30}},
    {"name": "cooked_meat", "action": {"heal": 40}},
    {"name": "coal", "action": {"fuel": 1}},
    {"name": "battery", "action": {"charge": "40-50"}}
  ]
}

loot_table.json:
{
  "chest_loot": [
    {"item": "flashlight", "drop_rate": 5},
    {"item": "bread", "drop_rate": 30},
    {"item": "raw_meat", "drop_rate": 20, "quantity": "1-3"},
    {"item": "coal", "drop_rate": 20},
    {"item": "battery", "drop_rate": 10},
    {"item": "nothing", "drop_rate": 15}
  ]
}
```

I chose JSON for these configuration files because it is human-readable (I can edit enemy stats in Notepad), Python has a built-in JSON parser (no external libraries needed), and it is a standard format that other developers would recognise. Each file is loaded once at startup to avoid repeated disk reads.

**JSON syntax explained:**

JSON stores data as **key-value pairs** inside curly braces `{}`. Arrays (lists) use square brackets `[]`.

```
{
  "items": [                        ← array of item objects
    {"name": "bread", "action": {"hunger_restore": 25}},   ← object with 2 keys
    {"name": "coal",  "action": {"fuel": 1}}               ← object with 2 keys
  ]
}
```

Each item has:
- `"name"` → a **string** (text) → `"bread"`
- `"action"` → a nested **object** → `{"hunger_restore": 25}`
  - `"hunger_restore"` → an **integer** (number) → `25`

So `"bread"` has `action: {"hunger_restore": 25}` which means "when used, restore 25 hunger". `"raw_meat"` has `{"heal": 5, "stamina_penalty": 10}` — two effects at once: heal 5 health but lose 10 stamina for 30 seconds. JSON just stores the data; the game code reads it at startup and applies the effects when the item is used.

**Maze tile encoding (for internal grid representation):**

The maze is stored as a 2D array of integers. Numbers are used instead of strings (`"wall"`, `"safe"`) because integer comparisons are faster and use less memory — important when checking collisions 60 times per second.

```
Tile codes:
0 = wall        — impassable block (room walls + outer border)
1 = safe floor  — normal walkable tile inside a room
2 = danger tile — walkable, enemies can spawn here
3 = chest tile  — walkable, contains a lootable chest
4 = doorway     — walkable opening in a wall between two rooms
```

**How a DFS perfect maze works (room-grid):**

The maze is a grid of rooms (e.g. 7×7 rooms). Each room is a block of floor tiles (e.g. 3×3 tiles). Walls separate rooms vertically and horizontally. DFS starts at the centre room and randomly picks an unvisited neighbour (up/down/left/right) — it then **removes the wall tile between them** (creating a doorway). This repeats until every room is connected. The result: every room is reachable with exactly one path between any two.

**Example: a 2×2 room grid (each room = 3×3 tiles, 1-tile walls):**

```
Grid (13×13 tiles):
. = wall   F = safe floor   D = door   C = chest   X = danger

Row  0:  . . . . . . . . . . . . .
Row  1:  . F F F . F F F . F F F .     ← Room (0,0)  Room (1,0)  Room (2,0)
Row  2:  . F F F . F F F . F F F .
Row  3:  . F F F . D F F . F F F .     ← doorway at (7,3) connects (1,0)→(1,1)
Row  4:  . . . . . . . . . . . . .     ← wall row
Row  5:  . F F F . F F F . C C C .     ← Room (0,1)  Room (1,1)  Room (2,1)=chest
Row  6:  . F F F . F F F . C C C .
Row  7:  . F F F . F X X . C C C .
Row  8:  . . . . . . . . . . . . .
Row  9:  . F F F . F F F . F F F .     ← Room (0,2)  Room (1,2)  Room (2,2)
Row 10:  . F F F . F F F . F F F .
Row 11:  . F F F . F F F . F F F .
Row 12:  . . . . . . . . . . . . .
```

**How the game reads it at runtime:**

```python
next_tile = maze_grid[player_grid_x][player_grid_y]

if next_tile == 0:
    return False  # wall — block movement
else:
    return True   # floor or doorway — allow movement
```

Special tiles (Danger, Chest) within rooms are checked separately when the player steps on them — they're still walkable, but trigger events (enemy spawn, loot prompt).

### 2d — Algorithms (Pseudocode)

Eight procedures implement the core game systems. Each is shown below with a brief explanation of its purpose.

---

**Procedure: generate_maze**

Builds the maze as a grid of evenly-spaced rooms separated by wall gaps. Uses DFS to connect all rooms by opening doorways in the walls, creating a perfect maze where every room is reachable with exactly one path between any two.

```
FUNCTION generate_maze(room_cols, room_rows)
    S = ROOM_SIZE
    G = WALL_GAP
    stride = S + G
    grid_w = room_cols * stride + 1
    grid_h = room_rows * stride + 1
    grid = 2D ARRAY[grid_w][grid_h]
    FOR x = 0 TO grid_w-1
        FOR y = 0 TO grid_h-1
            grid[x][y] = WALL
    FOR rx = 0 TO room_cols-1
        FOR ry = 0 TO room_rows-1
            FOR dx = 1 TO S
                FOR dy = 1 TO S
                    tile_x = rx * stride + dx
                    tile_y = ry * stride + dy
                    grid[tile_x][tile_y] = SAFE
    assign_room_features(grid, room_cols, room_rows)
    visited = 2D ARRAY[room_cols][room_rows]
    FOR rx = 0 TO room_cols-1
        FOR ry = 0 TO room_rows-1
            visited[rx][ry] = FALSE
    start_rx = room_cols / 2
    start_ry = room_rows / 2
    visited[start_rx][start_ry] = TRUE
    stack = []
    stack.push([start_rx, start_ry])
    WHILE stack IS NOT EMPTY
        (rx, ry) = stack.top()
        neighbours = get_unvisited_room_neighbours(rx, ry, visited, room_cols, room_rows)
        IF neighbours IS NOT EMPTY
            (nx, ny) = random_choice(neighbours)
            door_x = IF nx > rx THEN rx*stride+S+(G+1)/2 ELSE nx*stride+S+(G+1)/2
            door_y = IF ny > ry THEN ry*stride+S+(G+1)/2 ELSE ny*stride+S+(G+1)/2
            grid[door_x][door_y] = DOOR
            visited[nx][ny] = TRUE
            stack.push([nx, ny])
        ELSE
            stack.pop()
    RETURN grid
ENDPROCEDURE
```

**How it works (step-by-step):**

The procedure builds a room-grid maze — a set of evenly-spaced square rooms separated by wall gaps, where DFS decides which walls get doorways.

**Step 1 — Calculate total size:**

Room width = `S` (ROOM_SIZE, e.g. 3 tiles). Gap between rooms = `G` (WALL_GAP, e.g. 3 wall tiles). Stride = `S + G` (e.g. 6). This is the distance from the left edge of one room to the left edge of the next. Total grid width = `room_cols × stride + 1` (the `+1` accounts for the left border wall). Same logic for height.

Example with 3 rooms across, S=3, G=3:
```
Tile:  0   1  2  3   4  5  6   7  8  9   10 11 12   13 14 15   16
       W   █  █  █   W  W  W   █  █  █   W  W  W   █  █  █   W
       ↑   ├──R0──┤  ├──gap──┤  ├──R1──┤  ├──gap──┤  ├──R2──┤  ↑
     outer                           stride=6 →→→  │
     wall                                              outer wall
```
grid_w = `3 × 6 + 1 = 19` tiles.

**Step 2 — Fill everything as WALL, then carve rooms:**

The double loop `FOR x... FOR y... grid[x][y] = WALL` sets every single tile in the 19-tile-wide grid to wall. Then `FOR rx... FOR ry... FOR dx=1 TO S FOR dy=1 TO S` carves out each room:

Room coordinates (rx, ry) are **not tile coordinates**. They are **room indices** — (0,0) = first room, (1,0) = second room across, etc. The formula `rx × stride + dx` converts a room index to actual tile positions:
- Room (0,0) floor tiles: x = `0×6+1` to `0×6+3` = tiles 1, 2, 3
- Room (1,0) floor tiles: x = `1×6+1` to `1×6+3` = tiles 7, 8, 9
- Room (2,0) floor tiles: x = `2×6+1` to `2×6+3` = tiles 13, 14, 15

**Finding a room from a tile position (reverse lookup):**

If the player is at tile `x=8`, which room are they in?

`rx = (x - 1) / stride = (8 - 1) / 6 = 7 / 6 = 1` (integer division rounds down)

So tile 8 is in room 1. Proof: room 1 occupies tiles 7-9, and 8 falls within that range. This is useful for collision detection and enemy AI — you can determine which room the player is in instantly with two divisions, no loops.

**How the doorway formula works:**

DFS is at current room `(rx=1, ry=0)`. It picks neighbour `(nx=2, ny=0)` to the right:

```
rx=1                nx=2
 │                   │
 ▼                   ▼
┌─────────┐    ┌─────────┐
│ R o o m │    │ R o o m │
│    1    │    │    2    │
│         │    │         │
└─────────┘    └─────────┘
╰── stride=6 ──╯

Tile:  7   8   9 | 10  11  12 | 13  14  15
                          ↑
                    door_x = rx×stride + S + (G+1)/2
                          = 1×6 + 3 + (3+1)/2
                          = 6 + 3 + 2
                          = 11
                    → tile 11 becomes DOOR (centre of 3-tile gap)
```

If the neighbour were to the left instead (`(nx=0, ny=0)`):

```  
nx=0            rx=1
 │               │
 ▼               ▼
┌─────────┐    ┌─────────┐
│ R o o m │    │ R o o m │
│    0    │    │    1    │
│         │    │         │
└─────────┘    └─────────┘

door_x = nx×stride + S + (G+1)/2      ← use nx (left room), not rx
       = 0×6 + 3 + (3+1)/2
       = 3 + 2
       = 5
→ tile 5 becomes DOOR (centre of 3-tile gap)
```

The formula uses `(G+1)/2` instead of `1` so the doorway lands in the **middle** of the gap rather than at the edge. This works cleanly when `G` is an odd number (1, 3, 5...), and `S` must be odd so the room has a clear centre tile.

**Vertical doorways** work the same way but on the y-axis:

```
Neighbour below (ny > ry):     Neighbour above (ny < ry):

door_y = ry×stride+S+(G+1)/2    door_y = ny×stride+S+(G+1)/2
       = 1×6+3+2                      = 0×6+3+2
       = 11                           = 5

   ry=1              ny=2           ny=0              ry=1
    │                 │              │                 │
    ▼                 ▼              ▼                 ▼
  ┌─────────┐                       ┌─────────┐
  │ R o o m │                       │ R o o m │
  │    1    │                       │    0    │
  │         │                       │         │
  └─────────┘                       └─────────┘
  ═══════════════ DOOR══════        ═══════════════ DOOR══════
    ┌─────────┐                       ┌─────────┐
    │ R o o m │                       │ R o o m │
    │    2    │                       │    1    │
    │         │                       │         │
    └─────────┘                       └─────────┘
```

The formula is identical — just using `ry`/`ny` instead of `rx`/`nx`.

Proving it: with 3 rooms of 3 tiles each and 3-tile gaps:
- Tiles 1-3, 7-9, 13-15 are floors = 9 floor tiles
- Tiles 0, 4-6, 10-12, 16 are walls = 10 wall tiles
- Total = 19 tiles = grid_w ✓

---

**Quick reference — maze generation glossary:**

| Variable | Name | What it is | Example |
|----------|------|------------|---------|
| `ROOM_SIZE` (S) | Room width/height | How many tiles wide and tall each room is (it's a square) | `S = 3` means each room is 3×3 tiles |
| `WALL_GAP` (G) | Gap width | How many wall tiles between adjacent rooms | `G = 3` means 3 tiles of wall separating rooms |
| `stride` | Stride | Distance from left edge of one room to left edge of the next room. Formula: `S + G` | `3 + 3 = 6` |
| `grid_w` | Grid width | Total number of tiles across the whole maze. Formula: `room_cols × stride + 1` | `3 × 6 + 1 = 19` |
| `grid_h` | Grid height | Total number of tiles tall the whole maze. Formula: `room_rows × stride + 1` | `3 × 6 + 1 = 19` |
| `rx, ry` | Room coordinates | Which room you're looking at. Like a postcode — (0,0) is first room, (1,0) is second room across | `rx=1, ry=0` = room in column 1, row 0 |
| `dx, dy` | Tile offset within room | Which tile *inside* the room (1 to S). `dx=1` is the first tile of the room's floor | `dx=2` = second tile across inside the room |
| `tile_x, tile_y` | Tile coordinates | Actual position in the big maze grid. Formula: `rx × stride + dx` | `1 × 6 + 2 = 8` |
| `nx, ny` | Neighbour room | The room DFS is trying to connect to. Same format as rx/ry | DFS connects (1,0) to `nx=2, ny=0` |
| `door_x, door_y` | Doorway tile | The exact tile in the wall gap that becomes a doorway | `1×6+3+1 = 10` |
| `visited[][]` | Visited tracker | A smaller grid (room × room, NOT tile × tile) that tracks which rooms DFS has already connected | `visited[2][1] = TRUE` means room (2,1) is connected |

**Coordinate systems summary:**

```
ROOM COORDS (rx, ry):         TILE COORDS (tile_x, tile_y):
┌─────┬─────┬─────┐           ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
│(0,1)│(1,1)│(2,1)│           │  │  │  │  │  │  │  │  │  │
├─────┼─────┼─────┤           ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
│(0,0)│(1,0)│(2,0)│           │  │  │  │  │  │  │  │  │  │
├─────┼─────┼─────┤           ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
│(0,0)│(1,0)│(2,0)│           │  │  │  │  │  │  │  │  │  │
└─────┴─────┴─────┘           └──┴──┴──┴──┴──┴──┴──┴──┴──┘
1 cell = 1 whole room          1 cell = 1 single tile
visited[][] uses these        grid[][] uses these

CONVERTING BETWEEN THEM:
Room → leftmost tile:    tile_x = rx × stride + 1
Room → any tile:         tile_x = rx × stride + dx   (dx = 1 to S)
Tile → which room:       rx = (tile_x - 1) / stride  (÷, round down)
```

**Step 3 — DFS doorways:**

`assign_room_features` places chests and danger tiles within specific rooms. Then DFS runs on the **room grid** (not the tile grid). `visited` is a small 2D array with one cell per room — it tracks which rooms have been connected. Starting at the centre room, DFS randomly picks an unvisited neighbour and opens a doorway at the first gap tile between them. The stack enables backtracking when a room has no unvisited neighbours left. After 11 iterations (for 12 rooms), every room has exactly one doorway and `visited` is all TRUE — a perfect maze.

---

**Procedure: update_time**

Manages the Day/Night/Blood Moon cycle. Day lasts 180 seconds, Night 120 seconds. Blood Moon is triggered as a random event during Night (20% chance on chest open) and lasts 45 seconds before returning to Day. The time state affects enemy spawning, vision range, and HUD colour.

```
PROCEDURE update_time(delta_time)
    elapsed_time = elapsed_time + delta_time
    IF time_state == "day" AND elapsed_time > 180
        time_state = "night"; elapsed_time = 0
    ELSE IF time_state == "night" AND elapsed_time > 120
        time_state = "day"; elapsed_time = 0
    IF time_state == "blood_moon"
        blood_moon_timer = blood_moon_timer + delta_time
        IF blood_moon_timer >= 45
            time_state = "day"; elapsed_time = 0
ENDPROCEDURE
```

---

**Procedure: player_movement**

Reads keyboard input (WASD), calculates new position using speed and delta time, checks wall collision by looking up the target tile in the maze grid, and updates the player's Euclidean distance from spawn (used for the win condition).

```
PROCEDURE player_movement(key_input, dt)
    dx = 0; dy = 0
    IF key_input == "W" THEN dy = -1
    ELSE IF key_input == "S" THEN dy = 1
    ELSE IF key_input == "A" THEN dx = -1
    ELSE IF key_input == "D" THEN dx = 1
    new_x = player_x + dx * 200 * dt
    new_y = player_y + dy * 200 * dt
    tile_x = FLOOR(new_x / TILE_SIZE)
    tile_y = FLOOR(new_y / TILE_SIZE)
    IF maze_grid[tile_x][tile_y] != WALL
        player_x = new_x; player_y = new_y
    distance_from_spawn = SQRT((player_x - spawn_x)^2 + (player_y - spawn_y)^2)
ENDPROCEDURE
```

---

**Function: bfs_find_path**

Breadth-First Search on the tile grid. Starts at the spider's tile, explores outward in four directions (up/down/left/right), only walking on floor (1) or doorway (4) tiles. Returns a list of tile coordinates from spider to player — the shortest path.

```
FUNCTION bfs_find_path(grid, grid_w, grid_h, start_tx, start_ty, end_tx, end_ty)  #start_tx/ty = spider's tile, end_tx/ty = player's tile
    visited = array(grid_h, grid_w) OF FALSE    #2D grid same size as maze, all FALSE = unvisited. When BFS visits a tile it marks TRUE so it never loops back
    prev = array(grid_h, grid_w) OF (-1, -1)  #second grid — every cell stores "which tile did I come from?". (-1,-1) means no parent yet. Used to rebuild the path at the end
    queue = empty queue  #"to-do list" of tiles to check next. Front = next to explore, Back = newly discovered tiles wait here
    visited[start_ty][start_tx] = TRUE
    ENQUEUE (start_tx, start_ty) TO queue

    WHILE queue IS NOT EMPTY
        current = DEQUEUE(queue)
        IF current.tx == end_tx AND current.ty == end_ty
            BREAK                          #reached the target tile (player's position when BFS was called — may already be stale, that's why we re-path every 5 frames)
        FOR EACH (nx, ny) IN [(−1, 0), (1, 0), (0, −1), (0, 1)]  #left, right, up, down — all TILE coords, not room coords
            IF nx >= 0 AND nx < grid_w AND ny >= 0 AND ny < grid_h
                IF grid[ny][nx] IN {1, 4} AND NOT visited[ny][nx]  #1 = floor, 4 = doorway — both walkable. 0 = wall → skipped
                    visited[ny][nx] = TRUE  #mark neighbour as visited so we never check it again and avoid infinite loops
                    prev[ny][nx] = current  #remember: "to reach (nx, ny), you came from current". Used later to rebuild the path backwards
                    ENQUEUE (nx, ny) TO queue  #add neighbour to back of to-do list. Will be processed after all earlier tiles are done

    IF NOT visited[end_ty][end_tx]
        RETURN empty list                   # no path found

    # rebuild path by walking backwards from player to spider
    path = empty list
    current = (end_tx, end_ty)
    WHILE current != (start_tx, start_ty)
        PREPEND current TO path
        current = prev[current.ty][current.tx]
    RETURN path
ENDFUNCTION
```

The BFS guarantees the **fewest tiles** between spider and player. The path is recalculated every few frames so the spider adapts if the player moves.

---

**Procedure: enemy_ai_update**

Two-state Finite State Machine (patrol → chase → patrol). Patrol drifts randomly within a room, changing direction at tile boundaries. When the player is within `vision_rooms` rooms, it switches to chase: runs BFS to find a path through the maze, then follows the path tile-by-tile.

```
PROCEDURE enemy_ai_update(enemy, player_x, player_y, vision_rooms, maze_grid, grid_w, grid_h, stride)
    enemy_tx = FLOOR(enemy.x / TILE_SIZE)    #Floor basically remove all the remainder 3.684 -> 3. It give you the tile coordinate
    enemy_ty = FLOOR(enemy.y / TILE_SIZE)    #Tile is how many CELL are there inside your maze.
    player_tx = FLOOR(player_x / TILE_SIZE)  #same as enemy
    player_ty = FLOOR(player_y / TILE_SIZE)
    enemy_rx = (enemy_tx - 1) / stride       #rx is which ROOM are you in few tile make up one ROOM
    enemy_ry = (enemy_ty - 1) / stride
    player_rx = (player_tx - 1) / stride
    player_ry = (player_ty - 1) / stride
    room_dist = MAX(ABS(player_rx - enemy_rx), ABS(player_ry - enemy_ry))  #ABS make everything positive, MAX just pick the biggest value between x and y.

    CASE enemy.state OF  #case is just another way of saying IF and else, they are better when you are checking the same variable
        "patrol":
            enemy.x = enemy.x + enemy.patrol_dx * enemy.speed * delta_time  #enemy.patrol_dx is a random number that change between 1 and 0 and -1. With 1 being left, 0 being no movement and -1 being right. Delta time is here because it stop it working differently in faster or slower machine.
            enemy.y = enemy.y + enemy.patrol_dy * enemy.speed * delta_time
            IF FLOOR(enemy.x / TILE_SIZE) != enemy_tx OR FLOOR(enemy.y / TILE_SIZE) != enemy_ty  #check if spider enter a new tile
                enemy.patrol_dx = random(-1, 1); enemy.patrol_dy = random(-1, 1)  #dx is just change in x
            IF room_dist <= vision_rooms
                enemy.state = "chase"
                enemy.path = bfs_find_path(maze_grid, grid_w, grid_h, enemy_tx, enemy_ty, player_tx, player_ty)
                enemy.path_index = 0
        "chase":
            IF room_dist == 0  #same room — no walls, chase directly toward player's current pixel position every frame
                dx = player_x - enemy.x
                dy = player_y - enemy.y
                dist = SQRT(dx * dx + dy * dy)
                enemy.x = enemy.x + (dx / dist) * enemy.speed * delta_time
                enemy.y = enemy.y + (dy / dist) * enemy.speed * delta_time
            ELSE  #different room — need BFS to find doorway through walls
                IF enemy.path_index >= LEN(enemy.path)         #reached end of path, recalculate
                    enemy.path = bfs_find_path(maze_grid, grid_w, grid_h, enemy_tx, enemy_ty, player_tx, player_ty)
                    enemy.path_index = 0
                IF game_timer MOD 5 == 0                       #re-calculate path every 5 frames so spider keeps chasing player's new position
                    enemy.path = bfs_find_path(maze_grid, grid_w, grid_h, enemy_tx, enemy_ty, player_tx, player_ty)
                    enemy.path_index = 0
                target_tile = enemy.path[enemy.path_index]
                target_px = target_tile.tx * TILE_SIZE + TILE_SIZE / 2    #centre of the tile the spider is heading to in pixels
                target_py = target_tile.ty * TILE_SIZE + TILE_SIZE / 2
                dx = target_px - enemy.x
                dy = target_py - enemy.y
                dist = SQRT(dx * dx + dy * dy)
                IF dist < 2                                          #spider is close enough to tile centre, move to next tile in path
                    enemy.path_index = enemy.path_index + 1
                ELSE
                    enemy.x = enemy.x + (dx / dist) * enemy.speed * delta_time  #dx / dist give you the ratio of how much of the speed is needed to move diagonally to get to the next tile
                    enemy.y = enemy.y + (dy / dist) * enemy.speed * delta_time
            IF room_dist > vision_rooms + 1 AND enemy.path_index >= LEN(enemy.path)
                enemy.state = "patrol"        #player out of range AND path finished — only then give up
                enemy.path = empty list
ENDPROCEDURE
```

**How BFS chase works — frame by frame:**

The spider doesn't fly straight through walls. It uses BFS to navigate the maze tiles. Here's a walkthrough:

```
Maze tile grid (0=wall, 1=floor, 4=doorway):

      x=1   x=2   x=3   x=4   x=5   x=6
   ┌─────┬─────┬─────┬─────┬─────┬─────┐
y=1│  0  │  0  │  0  │  0  │  0  │  0  │
   ├─────┼─────┼─────┼─────┼─────┼─────┤
y=2│  0  │  S  │  1  │  1  │  4  │  0  │     S = spider (2,2)
   ├─────┼─────┼─────┼─────┼─────┼─────┤     P = player (6,4)
y=3│  0  │  1  │  0  │  1  │  1  │  0  │     4 = doorway
   ├─────┼─────┼─────┼─────┼─────┼─────┤
y=4│  0  │  1  │  1  │  1  │  0  │  P  │
   ├─────┼─────┼─────┼─────┼─────┼─────┤
y=5│  0  │  0  │  0  │  0  │  0  │  0  │
   └─────┴─────┴─────┴─────┴─────┴─────┘
```

**Frame 1 — Spider enters chase, BFS runs:**
```
BFS explores from S(2,2):
  level 0: (2,2)
  level 1: (3,2), (2,3)
  level 2: (4,2), (3,3), (1,3)
  level 3: (5,2)=doorway, (4,3)
  level 4: (5,3), (3,4)
  level 5: (5,4), (4,4)
  level 6: (6,4)=PLAYER  ← found!

Shortest path: (2,2)→(3,2)→(4,2)→(5,2)→(5,3)→(5,4)→(6,4)
               S  →  →  →  door  →  →  →  P
```

**Frames 2-10 — Spider follows the path:**
```
Each frame:
  path_index = 0 → target tile (3,2)
  target_px = 3 × 64 + (64/2) = 224   (TILE_SIZE=64)
  target_py = 2 × 64 + (64/2) = 160
  dx = 224 - spider.x, dy = 160 - spider.y
  dist = SQRT(dx² + dy²)
  spider.x += dx/dist × 50 × dt
  spider.y += dy/dist × 50 × dt
  → Spider slides smoothly toward centre of tile (3,2)
```

**Frame 11 — Reaches tile (3,2):**
```
  dist < 2  →  path_index += 1  →  now target is (4,2)
  Repeats until path_index reaches the end
  Then re-paths to player's current position
```

The spider navigates around walls because BFS only walks on floor (1) and doorway (4) tiles. It never moves into a wall (0). And because BFS recalculates every 5 frames, the path updates if the player runs to a different room.

---

**Procedure: open_chest**

Toggles the chest UI. First time: generates 2-4 random items using the loot table and stores them in `chest.contents`. At Night, generates 3-5 items and doubles the rare Flashlight drop chance — the reward for risking a Blood Moon. Subsequent times: shows remaining items. Items stay until each is taken individually.

```
PROCEDURE open_chest(chest)
    IF chest_ui_open AND chest_ui_chest == chest    #already looking at this chest — close it
        chest_ui_open = FALSE
        chest_ui_chest = None
        RETURN
    IF NOT chest.is_opened                           #first time — generate multiple items
        chest.is_opened = TRUE
        IF time_state == "night"
            item_count = random(3, 5)
        ELSE
            item_count = random(2, 4)
        FOR i = 1 TO item_count
            roll = random(1, 100); cumulative = 0
            FOR EACH entry IN loot_table
                IF time_state == "night" AND entry.item == "flashlight"
                    drop_rate = entry.drop_rate * 2      #5% → 10% at Night
                ELSE
                    drop_rate = entry.drop_rate
                cumulative = cumulative + drop_rate
                IF roll <= cumulative
                    chest.contents.append(entry.item)
                    BREAK
    chest_ui_open = TRUE
    chest_ui_chest = chest
    chest_ui_selected = 0
ENDPROCEDURE
```

**How cumulative probability works:**

The loot table stores each item's drop rate as a percentage. `cumulative` turns those percentages into a set of numbered ranges by adding them one by one.

```
Loot table:                     Cumulative ranges:
Flashlight  5%                  0-5    (roll 1-5)
Bread      30%                  5-35   (roll 6-35)
Raw Meat   20%                  35-55  (roll 36-55)
Coal       20%                  55-75  (roll 56-75)
Battery    10%                  75-85  (roll 76-85)
Nothing    15%                  85-100 (roll 86-100)

Example: roll = 57
  Flashlight: cumulative=0+5=5,    57 > 5  → skip
  Bread:      cumulative=5+30=35,  57 > 35 → skip
  Raw Meat:   cumulative=35+20=55, 57 > 55 → skip
  Coal:       cumulative=55+20=75, 57 ≤ 75 → ✓ Coal!
```

`cumulative` starts at 0. Each item adds its drop rate. If `roll <= cumulative`, the item is chosen. This means a roll of 57 falls in the range 56-75 = Coal. The number of items per chest is randomised to 2-4 so each chest feels different — some are full of food, others might have nothing useful.

**Procedure: handle_chest_ui**

Handles mouse click to select an item slot and R to take it.

```
PROCEDURE handle_chest_ui(key_input)
    IF NOT chest_ui_open THEN RETURN
    IF key_input == "MOUSE_CLICK"        #click on a slot to select it
        chest_ui_selected = clicked_slot_index
    ELSE IF key_input == "R"             #take the selected item
        IF LEN(chest_ui_chest.contents) > 0 AND chest_ui_chest.contents[chest_ui_selected] != ""
            item = chest_ui_chest.contents[chest_ui_selected]
            inventory[item] = inventory[item] + 1
            chest_ui_chest.contents[chest_ui_selected] = ""      #remove that slot
            IF all slots are empty
                chest_ui_chest.is_empty = TRUE
ENDPROCEDURE
```

Note: pressing E when near a chest calls `open_chest`. If the chest UI is already open, `open_chest` closes it (toggle). If the UI is closed, `open_chest` opens it. R takes the item. No special Leave key needed — pressing E again closes the UI regardless.

---

**Procedure: main_game_loop**

The orchestrator that runs every frame while the game is playing. Sequentially: takes keyboard input (player_movement), updates the time cycle (update_time), spawns spiders during dangerous states, runs enemy AI and collision, applies hunger decay, checks win/death conditions, then renders the view and HUD.

```
PROCEDURE main_game_loop()
    WHILE game_state == "playing"
        key = get_keypress()
        IF chest_ui_open
            handle_chest_ui(key)                     #block all other input while looking at chest
        ELSE
            player_movement(key, delta_time)
            update_time(delta_time)
            IF time_state != "day" AND enemy IS None
                enemy = CREATE Enemy(spawn near player)
            IF enemy IS NOT None
                enemy_ai_update(enemy, player_x, player_y, enemy.vision_range, maze_grid, grid_w, grid_h, stride)
                IF player_x < enemy.x + 64 AND player_x + 64 > enemy.x AND player_y < enemy.y + 64 AND player_y + 64 > enemy.y
                    player_health = player_health - enemy.damage * delta_time
            player_hunger = player_hunger - 5 * delta_time / 60
            IF player_health <= 0
                game_state = "death"
            ELSE IF distance_from_spawn >= 10000
                game_state = "win"
        render_view(camera_x, camera_y)
        update_hud()
        delta_time = calculate_delta_time()
ENDPROCEDURE
```

**How all algorithms fit together:**
`main_game_loop` orchestrates everything — each frame it takes input (`player_movement`), updates the day/night cycle (`update_time`), spawns spiders during dangerous time states, runs the FSM-based `enemy_ai_update` (using `bfs_find_path` to navigate), checks win/death conditions, then renders. `generate_maze` runs once at startup (DFS room-connection). `open_chest` shows a loot UI that the player confirms with `handle_chest_ui` (T to take, L to leave). Each algorithm maps to a success criterion from section 1h.

### 2e — Usability Features & UI Design

**Screen designs:**

![Screen Designs](screen_designs.png)

**1. Main Menu Screen**
- Game title "2D MazeRunner" at top centre in pixel font — large and immediately readable, sets the game's aesthetic tone
- "Start" button (largest, centred) — the primary action players want, so it's the most prominent element
- "Settings" button (medium, below Start) — secondary action, smaller to indicate hierarchy
- "Quit" button (medium, below Settings) — same size as Settings for visual consistency
- Gradient background (dark blue to black) — creates visual interest without needing a background image, and the dark tones match the game's night-time survival theme
- **Why minimal design:** Research from ISO Core showed that minimalist menus reduce cognitive load — players want to start playing, not navigate complex menus. The negative space focuses attention on the three buttons.

**2. Gameplay Screen (HUD)**
- Top-left: Health bar (red/green gradient), Stamina bar (yellow), Hunger bar (brown) — positioned together because they form the player's core stat group. Top-left is standard gaming convention for stat displays.
- Top-right: Time state indicator with icon — separate from stats because time state affects the entire game world, not just the player. Right side balances the screen layout.
- Bottom-left: Compass — positioned near the bottom where it doesn't obstruct the maze view. The compass needle points toward spawn so the player can orient themselves.
- Bottom-centre: Distance meter ("Distance: X.X / 10000m") — centred because it's the primary win-progress indicator. The player needs to see this frequently to gauge their progress.
- Bottom-right: Item hotbar (4 slots labelled 1-4) — positioned on the right because right-hand dominant players find it easier to glance right for inventory.
- Dark semi-transparent background behind all HUD elements — ensures readability over any maze tile colour while preserving the player's view of the maze.
- **Why no minimap:** The maze is procedurally generated and designed to be disorienting. A minimap would remove the tension of being lost, which is a core part of the survival experience.

**3. Death Screen**
- "You Died" in large pixel font with red colour — immediate, unambiguous feedback
- Distance reached display — gives the player a score to beat on the next run
- "Restart" button — primary action, largest button
- "Main Menu" button — secondary option
- Stat summary (time survived, enemies evaded) — adds context to the death and encourages replay

**4. Settings Screen**
- Master volume slider — the most common settings adjustment
- Fullscreen toggle — useful for players who want to minimise distractions
- "Back" button to return — consistent navigation pattern

**Controls:**
- W/A/S/D — Move up/left/down/right (standard gaming convention, no learning required)
- Shift — Sprint (drains stamina) — standard sprint key across most games
- E — Interact (open chest, use furnace) — standard interaction key
- F — Toggle flashlight — chosen because it's close to WASD fingers and is the standard "toggle" key in many games
- 1/2/3/4 — Use item in hotbar slot — numbered to match the slot labels, intuitive mapping
- Escape — Pause / unpause — universal standard

**Accessibility considerations:**
- No colour-dependent information: Tile safety is communicated through texture variation (different sprite patterns for Safe/Danger/Chest tiles), not colour alone. This accommodates colour-blind players who cannot distinguish between red/green markers.
- Font size is large enough to be readable on a 1080p display at standard viewing distance (~60cm)
- High contrast between HUD text and background (white text on dark semi-transparent background)
- The game can be paused at any time (Escape key), accommodating players who need to take breaks
- Controls follow standard gaming conventions (WASD movement) so players don't need to learn new input schemes

**User feedback on designs (from stakeholder interviews):**
- Age 15 respondent: "The HUD looks clean, I like that it doesn't clutter the screen. The distance meter is useful so I know how far I've gone."
- Age 17 respondent: "Make sure the dark theme doesn't hide important info — the semi-transparent HUD background is good for that. Can you add an option to change key bindings?" (Note: custom key bindings would be a useful future addition.)

### 2f — Validation

**Screen boundaries:** The player is prevented from walking off the edge of the maze by `check_wall_collision`, which compares the player's proposed new position against the four corners of the player bounding box against the maze grid. If any corner overlaps a wall tile, movement in that direction is blocked entirely. This is checked every frame (up to 60 times per second), ensuring the player can never leave the playable area. I chose corner-point checking over centre-point because it prevents the player from clipping through walls at high sprint speed.

**Interaction range:** The player can only interact with chests and furnaces when within 1 tile (64px) of the object. The `interact()` method calculates Euclidean distance between the player and the object and rejects interactions outside this range. This prevents the player from opening chests through walls or from across the maze, which would break the game's resource management balance.

**Item usage validation:** Items can only be used if they exist in the player's inventory. If the player presses 1-4 when the corresponding slot is empty, nothing happens — no error is thrown, the game simply ignores the input. For the flashlight specifically, usage is also blocked if battery is below 25% (the cost of one use). This prevents soft-locks where the player might try to use a non-existent item.

**Menu inputs:** Only specific keys respond in each menu. On the main menu, only mouse clicks on buttons or pressing Enter/Return on a highlighted button registers as input. The Escape key closes the Settings screen or unpauses the game. Menu navigation ignores all game-related keys (WASD, E, F, etc.) to prevent the player from accidentally starting actions while in a menu.

**Pause validation:** The player can pause at any time during gameplay by pressing Escape. While paused, all game logic pauses: enemy movement stops, the time system freezes, hunger drain pauses. This is implemented by simply not executing the game loop while paused — instead, a pause overlay is rendered on top of the frozen frame. On unpause, the game resumes from exactly the same state. This is essential because players may need to pause during intense moments (e.g., being chased by enemies) without penalty.

**High score / name entry:** If implemented in future, name entry would be restricted to alphanumeric characters only (A-Z, 0-9), with a maximum length of 8 characters. Special characters would be rejected to prevent SQL injection or display issues, and the length limit keeps the leaderboard readable.

**Level file validation:** JSON configuration files (enemies.json, items.json, loot_table.json) are validated when loaded at startup. The program checks:
1. File exists before attempting to open
2. JSON parses correctly (try/catch around JSON parse)
3. Required keys exist (name, speed, damage for enemies, etc.)
4. Numeric values are within expected ranges (e.g., drop rates sum to 100%)

If a file is missing or malformed, the game displays an error message showing which file failed and falls back to hardcoded default values. This prevents crashes and makes debugging easier.

### 2g — Test Data for Development

**Module: player_movement**

| Module tested | Input | Expected output | Why this test |
|--------------|-------|----------------|---------------|
| player_movement | Hold W key | Player moves up (y decreases) | Basic movement must work in all 4 directions |
| player_movement | Hold S key | Player moves down (y increases) | Same as above |
| player_movement | Hold A key | Player moves left (x decreases) | Same as above |
| player_movement | Hold D key | Player moves right (x increases) | Same as above |
| player_movement | Hold W + Shift | Player moves up faster, stamina decreases | Sprint mechanic must drain stamina and increase speed |
| player_movement | Press W against wall | Player position unchanged | Wall collision must prevent movement through walls |
| player_movement | Player hunger < 20 | Movement speed reduced by 40% | Hunger penalty must apply at correct thresholds |
| player_movement | Player hunger = 0 | Speed reduced by 40% and sprint disabled | Starvation must severely limit movement |

**Module: generate_maze**

| Module tested | Input | Expected output | Why this test |
|--------------|-------|----------------|---------------|
| generate_maze | room_cols=7, room_rows=7 | All rooms reachable via doorways, player spawns at centre | Small grid for visual connectivity check |
| generate_maze | room_cols=3, room_rows=3 | Each room has at least one doorway | Minimum viable maze |
| generate_maze | room_cols=50, room_rows=50 | Completes within 5s, no stack overflow | Stress test for large maze |

**Module: collision_detection**

| Module tested | Input | Expected output | Why this test |
|--------------|-------|----------------|---------------|
| check_collision | Player bounding box overlaps enemy | Returns true | Direct contact must register as hit |
| check_collision | Player 10px from enemy | Returns false | No contact = no damage |
| check_collision | Player at (0,0), enemy at (50,50) | Returns false | Far apart = no collision |
| check_collision | Player at edge of enemy hitbox | Returns true | Edge cases (touching boundaries) must register |

**Module: enemy_ai**

| Module tested | Input | Expected output | Why this test |
|--------------|-------|----------------|---------------|
| enemy_ai_update | Player enters same room (room_dist = 0) | Enemy state changes to "chase", moves directly toward player | Same-room detection must trigger direct pixel chase |
| enemy_ai_update | Player enters adjacent room (room_dist = 1) during Blood Moon | Enemy state changes to "chase", BFS path generated | BFS chase must activate at vision range |
| enemy_ai_update | Player beyond vision range (room_dist > vision_rooms + 1) but enemy still has path tiles left | Enemy keeps following the current path to the last known player position, THEN returns to patrol | Enemy finishes its current path before giving up the chase |
| enemy_ai_update | Player out of range AND enemy.path_index >= LEN(enemy.path) | Enemy state changes to "patrol", path cleared | Enemy only patrols once the old path is fully walked |
| enemy_ai_update | Player moves between rooms during chase | Path recalculated every 5 frames | Spider must track the player's new room |
| enemy_ai_update | Same-room chase (room_dist = 0) | Enemy moves directly toward player pixel-by-pixel | Direct pursuit must not use BFS |
| enemy_ai_update | Enemy reaches end of BFS path | Path index resets, new path calculated | Spider must not get stuck at path end |

**Module: open_chest**

| Module tested | Input | Expected output | Why this test |
|--------------|-------|----------------|---------------|
| open_chest | Roll = 3 (flashlight 5%) | Returns "flashlight" | Rare item drop at correct probability |
| open_chest | Roll = 20 (bread 30%) | Returns "bread" | Common item drop |
| open_chest | Roll = 97 (nothing 15%) | Returns "nothing" | Empty chest outcome |
| open_chest | Chest already looted | No item (is_opened flag set) | Chest should not give duplicate loot |
| open_chest | Open 100 chests, record distribution | ~30 bread, ~20 raw meat, ~20 coal, ~10 battery, ~5 flashlight, ~15 nothing | Statistical verification of drop rates |
| open_chest | Open chest during Day | 2-4 items generated | Normal loot amount |
| open_chest | Open chest during Night | 3-5 items generated | Night bonus adds an extra item |
| open_chest | Open 100 chests at Night, record flashlight drops | ~10 flashlight drops (5% → 10%) | Night doubles rare drop rate |

**Module: update_time**

| Module tested | Input | Expected output | Why this test |
|--------------|-------|----------------|---------------|
| update_time | elapsed_time = 181 | time_state changes "day" → "night" | Day length correct |
| update_time | elapsed_time = 301 | time_state changes "night" → "day" | Night length correct |
| update_time | chest opened, roll = 15 (≤20), time = "night" | time_state changes to "blood_moon" | Blood Moon trigger probability works |
| update_time | chest opened during "day" | No Blood Moon | Blood Moon only during Night |
| update_time | blood_moon_timer = 46 | time_state changes to "day" | Blood Moon duration correct |

### 2h — Test Data for Alpha Testing (Post-Development)

| # | Success criterion | Test method | Expected result |
|---|------------------|-------------|----------------|
| 1 | Player moves with WASD, stops at maze boundaries | Press each arrow key during gameplay | Character moves in all 4 directions smoothly, stops at walls |
| 2 | Time cycles Day→Night→Day, enemies spawn at Night | Start game, wait 3 minutes | Enemies appear after Day→Night transition, disappear at dawn |
| 3 | Blood Moon triggers on chest loot (20% chance) | Open 20 chests during Night | At least 1 Blood Moon triggers, enemies get faster/stronger visibly |
| 4 | Enemy chases within vision, deals damage on contact | Stand still near an enemy during Night | Enemy approaches, damage applied on contact, health decreases |
| 5 | Health/Stamina/Hunger displayed and depleting | Observe HUD during gameplay | Bars visible, stamina drops when sprinting, hunger drops over time |
| 6 | Chests give items matching drop rate table | Open 100 chests, record drops | Distribution approximately matches: Bread 30%, Raw Meat 20%, Coal 20%, Battery 10%, Flashlight 5%, Nothing 15% |
| 7 | Maze is perfect (all paths connected) | Inspect maze generation output programmatically | Every cell reachable from every other cell |
| 8 | Game runs at 30+ FPS | Run game, measure FPS with full maze and spider active | FPS consistently 30 or higher |
| 9 | Win screen triggers at 10km distance | Navigate to 10,000m from spawn | Win screen displays with restart/quit options |
| 10 | Menu screen functional, death screen on 0 health | Start game, get killed, observe screens | Main menu shows Start/Settings/Quit, death screen appears when health=0 |
| 11 | Game pauses on Escape | Press Escape during gameplay | Game freezes, pause overlay appears, all logic stops |
| 12 | Consistent dark pixel-art theme | Observe all sprites and UI | All assets use consistent pixel style and dark colour palette |
| 13 | Robustness: game survives extreme conditions | Force-spawn 50 enemies near player (beyond normal 1 spider), key spam, delete enemies.json before launch, generate 1000×1000 maze, rapid pause/unpause ×20, zero health edge case, resize window, sprint at 0 stamina | FPS may drop but game never crashes; error message shown for missing file; no unintended behaviour on key spam; pause toggles cleanly; health never goes negative |

---

## Section 3: Developing the Coded Solution

*[To be completed during development — document 6-8 milestones from your systems diagram. For each milestone: state what you set out to do (link back to your design), show annotated code with comments explaining each part, include a screenshot of the program running, show a test table with pass/fail results, and if any test fails show the remedial action with justification. End each milestone with a review reflecting on what you learned or what changed from your original plan.]*

---

## Section 4: Evaluation

*[To be completed after development — copy the alpha test table from 2h, add a "Met? (Yes/Partial/No)" column, run every test on the finished game, explain each result. Record a video screencast walking through ~30 tests with audio commentary. Have your stakeholder test the game and record their feedback. Then evaluate: go through each success criterion from 1h one by one, cross-reference with test evidence, explain why any criteria were only partially met or not met, evaluate usability using stakeholder feedback, discuss limitations and what you would add with more time, discuss maintenance (how the code is structured for future updates), and reflect on key changes between your design and the final product.]*

---

## Submission Checklist

- [ ] Title page: project name, H446-03, your name, candidate number, centre name & number
- [ ] Contents page
- [ ] Sections clearly labelled: Analysis, Design, Developing the Coded Solution, Evaluation
- [ ] Every page numbered
- [ ] Bibliography (sources, games referenced, libraries used)
- [ ] Appendix: **full code listing** of ALL code
- [ ] Testing video (screencast with audio)
- [ ] Copy of entire solution on CD/DVD/USB

## Bibliography

- ISO Core (Brace Yourself Games, 2024) — https://store.steampowered.com/app/2983860/ISOCORE/
- The Binding of Isaac (Edmund McMillen, 2011) — https://store.steampowered.com/app/113200/The_Binding_of_Isaac/
- Minecraft (Mojang Studios, 2011)
- AdamCYounis (YouTube) — pixel art and game development tutorials
- CodingQuest (YouTube) — https://www.youtube.com/@CodingQuest2023 — maze generation tutorials
- Pygame library documentation — https://www.pygame.org/docs/

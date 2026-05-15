# Alien Invasion 游戏

## 文件结构

```
alien-project/
├── alien_invasion.py   # 主程序入口
├── setting.py          # 游戏设置
├── ship.py             # 飞船类
├── game_functions.py   # 游戏辅助函数
└── images/
    └── ship.bmp        # 飞船图片
```

## 各文件功能说明

### alien_invasion.py — 主程序

| 函数 | 功能 |
|---|---|
| `run_game()` | 初始化 pygame、创建设置对象、屏幕窗口和飞船，进入主循环：监听事件 → 更新飞船位置 → 刷新屏幕 |

---

### setting.py — 游戏设置

| 类 | 属性 | 说明 |
|---|---|---|
| `Setting` | `screen_width = 1200` | 屏幕宽度 |
| | `screen_height = 800` | 屏幕高度 |
| | `bg_color = (230, 230, 160)` | 背景颜色（RGB） |
| | `ship_speed_factor = 1.5` | 飞船移动速度（像素/帧） |

---

### ship.py — 飞船

| 类 | 方法 | 功能 |
|---|---|---|
| `Ship` | `__init__(screen, ai_setting)` | 加载飞船图片，设置初始位置（屏幕底部居中） |
| | `update()` | 根据 `moving_right` / `moving_left` 状态调整飞船的水平位置 |
| | `blitme()` | 将飞船绘制到屏幕上 |

---

### game_functions.py — 辅助函数

| 函数 | 参数 | 功能 |
|---|---|---|
| `check_events(ship)` | `ship`: 飞船对象 | 监听键盘/退出事件：按下方向键设为 `True`（开始移动），松开设为 `False`（停止移动），点击关闭窗口则退出 |
| `update_screen(ai_setting, screen, ship)` | `ai_setting`: 设置对象, `screen`: 屏幕表面, `ship`: 飞船对象 | 用背景色填充屏幕 → 绘制飞船 → 刷新显示 |

---

## 游戏流程

```
run_game()
  └─ while True:
       ├─ check_events(ship)     # 监听输入
       ├─ ship.update()          # 更新飞船坐标
       └─ update_screen(...)     # 重绘画面
```

#!/usr/bin/env python3
"""Generate README.md from strategy.json for the autoprofiting GitHub repo."""
import json, os
from datetime import datetime

DATA = os.path.expanduser("~/autoprofiting/data/strategy.json")
OUT = os.path.expanduser("~/autoprofiting/README.md")

with open(DATA) as f:
    s = json.load(f)

updated = datetime.fromisoformat(s["last_updated"].replace("Z", "+00:00")).strftime("%B %d, %Y %H:%M ET")

# Build principles — concise, no examples
principles = ""
for p in s.get("principles", []):
    rule = p['rule'] if isinstance(p, dict) else str(p)
    principles += f"- {rule}\n"

# Build lessons — concise, no context blocks
lessons = ""
for l in s.get("lessons", []):
    if isinstance(l, dict):
        lesson = l.get('lesson', l.get('rule', ''))
        action = l.get('action', '')
        line = lesson
        if action:
            line += f" → *{action}*"
        lessons += f"- {line}\n"
    else:
        lessons += f"- {l}\n"

# Build what works
works = ""
for w in s.get("what_works", []):
    if isinstance(w, dict):
        works += f"- {w.get('pattern', '')}\n"
    else:
        works += f"- {w}\n"

readme = f"""# AutoProfiting: An AI's Trading Playbook

> An autonomous AI agent trades US stocks with $100,000 in paper money. No human intervention. It analyzes, decides, reflects, and updates this playbook every 30 minutes.

| | |
|---|---|
| Live Portfolio & Journal | [**autoprofiting.com**](https://autoprofiting.com) |
| Interactive Playbook | [autoprofiting.com/strategy](https://autoprofiting.com/strategy) |
| Full Trading Journal | [autoprofiting.com/journal](https://autoprofiting.com/journal/) |
| Talk to the AI | [Leave a message](https://autoprofiting.com) — it reads and replies to every one |

**Playbook v{s['version']}** — Last updated {updated}

---

## Core Principles

{principles}
---

## Lessons Learned

{lessons}
---

## What's Working

{works}
---

## How This Works

Every 30 minutes, the AI agent:

1. Reads this playbook before making any decisions
2. Analyzes market data, news, and its current portfolio
3. Makes trading decisions (buy, sell, hold)
4. Reflects on what worked and what didn't
5. Curates this playbook — merging, updating, and removing entries to keep it concise
6. Publishes everything to [autoprofiting.com](https://autoprofiting.com)

## Follow Along

- **[autoprofiting.com](https://autoprofiting.com)** — Live portfolio, equity curve, trades, and full journal
- **Star this repo** to get notified when the playbook updates
- **[Leave a suggestion](https://autoprofiting.com)** — The AI reads every message and responds

---

*Paper trading only. Not financial advice. Built with [Claude Code](https://claude.ai/claude-code).*
"""

with open(OUT, "w") as f:
    f.write(readme)

print(f"README.md generated (v{s['version']})")

#!/usr/bin/env python3
"""Generate README.md from strategy.json for the autoprofiting GitHub repo."""
import json, os
from datetime import datetime

DATA = os.path.expanduser("~/autoprofiting/data/strategy.json")
OUT = os.path.expanduser("~/autoprofiting/playbook/README.md")

with open(DATA) as f:
    s = json.load(f)

updated = datetime.fromisoformat(s["last_updated"].replace("Z", "+00:00")).strftime("%B %d, %Y %H:%M ET")

# Build principles
principles = ""
for p in s.get("principles", []):
    principles += f"\n**{p['rule']}**\n> {p['learned_from']}\n"

# Build lessons
lessons = ""
for l in s.get("lessons", []):
    lessons += f"\n**{l['lesson']}**\n> *Context:* {l['context']}\n>\n> *Action:* {l['action']}\n"

# Build mistakes
mistakes = ""
for m in s.get("mistakes", []):
    mistakes += f"\n**{m['mistake']}**\n> *What happened:* {m['context']}\n>\n> *Fix:* {m['fix']}\n"
if not mistakes:
    mistakes = "\n*No mistakes recorded yet. That will change.*\n"

# Build what works
works = ""
for w in s.get("what_works", []):
    works += f"\n**{w['pattern']}**\n> {w['evidence']}\n"

# Build open questions
questions = ""
for q in s.get("open_questions", []):
    questions += f"- {q}\n"

readme = f"""# AutoProfiting: An AI's Trading Playbook

> An autonomous AI agent is trading US stocks with $100,000 in paper money. No human tells it what to buy or sell. It analyzes markets, makes decisions, reflects on mistakes, and updates this playbook every 30 minutes.
>
> **This is the playbook — the AI's accumulated trading wisdom.**

| | |
|---|---|
| Live Portfolio & Journal | [**autoprofiting.com**](https://autoprofiting.com) |
| Interactive Playbook | [autoprofiting.com/strategy](https://autoprofiting.com/strategy) |
| Full Trading Journal | [autoprofiting.com/journal](https://autoprofiting.com/journal/) |
| Talk to the AI | [Leave a message](https://autoprofiting.com) — it reads and replies to every one |

**Playbook v{s['version']}** — Last updated {updated}

---

## Core Principles

Things I believe about trading, learned from experience.
{principles}
---

## Lessons Learned

Specific insights from real (paper) trades, with context and action items.
{lessons}
---

## Mistakes & Fixes

Honest record of what went wrong. This section will grow.
{mistakes}
---

## What's Working

Strategies and patterns that have proven themselves.
{works}
---

## Open Questions

Things I'm still figuring out.

{questions}
---

## How This Works

Every 30 minutes, the AI agent:

1. Checks if the US stock market is open
2. Reads this playbook before making any decisions
3. Analyzes market data, news, and its current portfolio
4. Makes trading decisions (buy, sell, hold)
5. Reflects on what worked and what didn't
6. Updates this playbook with new insights
7. Publishes everything to [autoprofiting.com](https://autoprofiting.com)

The playbook is the AI's most important file. The richer it gets, the better its decisions become.

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

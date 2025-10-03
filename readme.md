# SQL Injection PoC — Flask + HTML

**Note:** This repository is a local proof-of-concept intended for learning and defensive purposes only.
 Do **not** run against systems you do not own or have explicit permission to test. 
This project intentionally contrasts an **unsafe** query pattern with a **safe** parameterized query to demonstrate why parameterization matters.

## What this is

A minimal Flask web application that demonstrates the difference between:

- an **unsafe** SQL usage pattern (string concatenation into SQL) — for demonstration only, and  
- a **safe** usage pattern (parameterized queries / prepared statements).

This repo is intentionally small and suitable for local, isolated learning.

---

## Features

- `/` — basic health page
- `/unsafe?username=...` — demonstrates an unsafe, concatenated SQL approach (returns the SQL executed + rows)
- `/safe?username=...` — demonstrates parameterized queries (returns the SQL template + rows)
- Small SQLite database with a few sample users (`alice`, `bob`, `carol`)
- Clear visible difference in the SQL string printed by the unsafe endpoint vs the parameterized endpoint

> The app is educational — it shows what *not* to do and how to fix it.



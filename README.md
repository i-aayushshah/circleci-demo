# CircleCI CI/CD Demo

A hands-on demo project that shows how **Continuous Integration / Continuous Delivery** works using [CircleCI](https://circleci.com).

---

## What's inside

| File | Purpose |
|---|---|
| `main.py` | A `Calculator` class + `greet()` helper – the code being tested |
| `test_main.py` | 20+ pytest tests covering every function |
| `requirements.txt` | Python dependencies (`pytest`, `pytest-cov`) |
| `.circleci/config.yml` | The CI/CD pipeline definition |

---

## Pipeline stages

```
Push to GitHub
      │
      ▼
  ① install        → pip install -r requirements.txt  (cached)
      │
      ▼
  ② test           → pytest + coverage report
      │
      ▼
  ③ deploy         → simulated deploy (runs on main branch only)
```

Each stage only runs if the previous one **passes**. If any test fails, the deploy never happens.

---

## Run locally

```bash
pip install -r requirements.txt
pytest test_main.py -v --cov=main --cov-report=term-missing
```

---

## How to connect to CircleCI

1. Push this repo to GitHub.
2. Go to [circleci.com](https://circleci.com) and log in with your GitHub account.
3. Click **"Projects"** → find this repo → click **"Set Up Project"**.
4. Choose **"Fastest"** (use existing `config.yml`).
5. Every `git push` will now trigger the pipeline automatically.

---

## What to show in your presentation

- Open CircleCI dashboard and show the **pipeline stages** (install → test → deploy).
- Click on the **test job** to show the individual test results and coverage %.
- Break a test on purpose (e.g. change `add` to return wrong value) → show the pipeline go **red**.
- Fix it, push again → pipeline goes **green** → deploy runs.

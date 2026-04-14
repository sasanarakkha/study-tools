# spec.md — Thread: website_improvement_loop

**Thread type:** chore

---

## Overview

This is a persistent planning thread for website generator improvements.

The thread supports a simple loop:

1. You report an issue or ask for a plan.
2. The planning model analyzes context and updates `plan.md`.
3. A cheaper execution model reads `plan.md`, implements the work, and writes `handoff.md`.
4. If you later report that the plan did not work or the issue is still present, the planning model reads `handoff.md` and updates `plan.md` again.

This thread is not for one feature only. It is a standing thread for repeated website generator improvement tasks.

---

## What It Should Do

- Keep one persistent `plan.md` for the current website generator issue being worked on.
- Let the planning model update `plan.md` whenever you ask to plan a new issue.
- Let the execution model read `plan.md`, do the work, and write `handoff.md` when finished.
- Require the planning model to read `handoff.md` only when you say the previous implementation did not solve the issue or still needs checking.
- Keep the process simple and dependent on your explicit instructions, not automatic branching logic.

Thread files:

- `kamma/threads/website_improvement_loop/spec.md`
- `kamma/threads/website_improvement_loop/plan.md`
- `kamma/threads/website_improvement_loop/handoff.md`

---

## Assumptions & Uncertainties

- You want one standing thread for website generator improvement work, not a new dated thread per issue.
- You will explicitly tell the model whether the task is:
  - planning a new issue
  - executing the existing plan
  - reviewing a failed attempt
- The planning model should not read `handoff.md` unless you indicate the existing plan failed or still needs checking.
- `plan.md` is replaced or updated for the current issue; it is not a historical archive of all previous issues unless you explicitly want that later.

---

## Constraints

- Keep the workflow minimal.
- The planning model writes or updates `plan.md`.
- The execution model reads `plan.md` and writes `handoff.md`.
- The planning model reads `handoff.md` only when needed for failure follow-up.
- Do not rely on chat memory.
- Do not introduce extra workflow files unless later requested.

---

## How We'll Know It's Done

- The thread directory exists at `kamma/threads/website_improvement_loop/`.
- It contains `spec.md`, `plan.md`, and `handoff.md`.
- The role split is clear:
  - planner updates `plan.md`
  - executor writes `handoff.md`
  - planner reads `handoff.md` only for failed or unresolved attempts

---

## What's Not Included

- Automatic issue routing
- Multiple parallel issue tracks
- Review automation
- Broader Kamma workflow redesign

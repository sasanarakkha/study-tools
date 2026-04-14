# plan.md — Thread: website_improvement_loop

---

## Phase 1 — Create the persistent thread structure

- [ ] Create `kamma/threads/website_improvement_loop/`.
  → verify: the directory exists at `kamma/threads/website_improvement_loop/`

- [ ] Add `spec.md` describing the minimal planner/executor loop for website generator improvements.
  → verify: `kamma/threads/website_improvement_loop/spec.md` exists and states that planner updates `plan.md` and executor writes `handoff.md`

- [ ] Add `handoff.md` as the executor-to-planner handoff file.
  → verify: `kamma/threads/website_improvement_loop/handoff.md` exists

- [ ] Phase 1 verification.
  → verify: all three files exist in the thread directory: `spec.md`, `plan.md`, `handoff.md`

## Phase 2 — Define the minimal operating rules

- [ ] Write in `spec.md` that when the user asks to plan a new website generator issue, the planning model should update `plan.md` and stop.
  → verify: `spec.md` explicitly says new planning requests update `plan.md`

- [ ] Write in `spec.md` that the execution model should read `plan.md`, implement the work, and write `handoff.md` when finished.
  → verify: `spec.md` explicitly assigns implementation to the execution model and handoff writing to `handoff.md`

- [ ] Write in `spec.md` that the planning model should read `handoff.md` only if the user reports that the plan did not work or the issue is still present.
  → verify: `spec.md` explicitly limits when `handoff.md` is read

- [ ] Phase 2 verification.
  → verify: the role split is unambiguous and matches the intended loop

## Phase 3 — Add a minimal handoff format

- [ ] Add a short `handoff.md` template with only the fields needed by the planning model after a failed or unresolved execution.
  → verify: `handoff.md` contains clear headings for issue worked on, changes made, verification run, current result, and remaining problem

- [ ] Keep the handoff format short so the execution model can fill it without guessing.
  → verify: `handoff.md` is brief and does not contain unnecessary workflow detail

- [ ] Phase 3 verification.
  → verify: a separate execution model could open `handoff.md` and know what to write

## Phase 4 — Make the thread ready for repeated use

- [ ] Make `plan.md` clearly represent the current issue being worked on, so it can be updated again when the user asks to plan another issue.
  → verify: `plan.md` wording allows replacement or updating for the next issue

- [ ] Make `spec.md` clearly state that this is a standing thread for website generator improvement work.
  → verify: `spec.md` describes the thread as persistent rather than one-off

- [ ] Phase 4 verification.
  → verify: the thread can be reused for the next planning request without changing the basic structure

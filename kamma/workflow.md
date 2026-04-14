# Project Workflow

## Guiding Principles

1. **The Plan is the Source of Truth:** All work must be tracked in `plan.md`
2. **Keep the Project Tech Notes Up to Date:** Changes to tools, constraints, resources, or working assumptions must be documented in `tech.md` *before* implementation
3. **Write Tests:** Write tests for new functionality where appropriate
4. **Non-Interactive & CI-Aware:** Prefer non-interactive commands
5. **Review the Work Before Calling It Done:** Implementation is not complete until it has been reviewed

## GitHub Issue Continuity

If a thread is tied to a GitHub issue, preserve that issue number prominently from start to finish.

1. Include the issue number in the thread title or description.
2. Include a dedicated issue reference near the top of the thread `spec.md`.
3. Include the same issue reference near the top of the thread `plan.md`.
4. Do not drop or rewrite the issue reference during implementation, review, or finalize.

## Task Workflow

Work through tasks in this order:

### Standard Flow

1. **Select Task:** Choose the next available task from `plan.md` in sequential order

2. **Mark In Progress:** Edit `plan.md` and change the task from `[ ]` to `[~]`

3. **Implement:** Write the code to complete the task. Follow the project's coding standards and conventions.

4. **Test:** Run relevant tests to verify the implementation works correctly.

5. **Fix Review Findings:**
   - Apply valid findings from `/kamma:3-review`.
   - Re-run relevant tests and verification.
   - Repeat review if needed until blocking issues are resolved.

6. **Finish the Thread:**
   - After review is clear, run `/kamma:4-finalize`.
   - Mark the thread complete, sync project docs, and archive the completed thread there.
   - If the thread references a GitHub issue, use the preserved issue number to post a summary comment and close the issue during finalize.

7. **Document Deviations:** If implementation differs from the notes in `tech.md`:
   - **STOP** implementation
   - Update `tech.md` with the change
   - Add dated note explaining the change
   - Resume implementation

8. **Update Plan:**
   - Update `plan.md`: change the task from `[~]` to `[x]`.

### When a Phase Ends

**Trigger:** Executed when a task completes a phase in `plan.md`.

1.  **Announce:** Inform the user that the phase is complete.

2.  **Run Tests:** Execute the most relevant local verification for the affected area.
    -   If verification fails, inform the user and attempt to fix (max 2 attempts). If still failing, stop and ask for guidance.

3.  **Record Remaining Gaps:** If the phase cannot be fully validated yet because the broader feature is still incomplete, note what was checked and what must wait until end-to-end verification.

4.  **Update Plan:** Record the phase completion in `plan.md`.

### Before You Mark It Done

Before marking any task complete, verify:

- [ ] Implementation works correctly
- [ ] Relevant tests pass
- [ ] The work has been reviewed
- [ ] Accepted review findings have been implemented
- [ ] The thread has been finished
- [ ] Code follows project's style guidelines
- [ ] No linting errors
- [ ] Documentation updated if needed

## Commit Guidelines

Follow the project's commit conventions. If none defined, use:

```
<type>(<scope>): <description>
```

If the thread references a GitHub issue, the suggested commit message must also reference that issue number, for example `fix(parser): handle empty input (closes #123)`.

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests
- `chore`: Maintenance tasks

## A Task Is Done When

1. All code implemented to specification
2. Relevant tests passing
3. The work has been reviewed and accepted findings addressed
4. The thread has been finished
5. Code passes linting
6. `plan.md` updated
---
name: distill
description: Turn a completed, user-approved task into a concise reusable skill from the current session. Use when the user asks to distill successful work into a skill, after one pass or several revisions.
license: MIT
---

# Distill

Preserve the minimum needed to reproduce a result the user considers good.
Assume a capable agent: specify outcomes, essential constraints, and evidence
of quality; leave implementation choices open. Discuss in the user's language.

## 1. Confirm the destination

Read the available session and accepted deliverable. Infer the quality bar from
requests, corrections, and final acceptance. Ask for missing acceptance or essential
evidence specifically; do not invent history or search unrelated sessions.

Propose three skill names, recommend the strongest, and describe the intended
deliverable in one line. Ask whether the name and outcome match the user's intent;
request an explanation if not. Honor a name the user already chose.

**Wait for name/outcome confirmation before step 2.** Reconfirm corrected proposals.

## 2. Confirm the shortest sufficient process

Work backward from the accepted result. Propose numbered steps, one line each;
merge or remove steps unless a quality requirement would be lost. Omit failed
paths and detours, but keep essential constraints learned from corrections.

Separate reusable requirements from incidental tools, filenames, quantities, and
style choices. For an uncertainty that would change the result, propose the answer
suggested by the session and ask a focused question, not an intake questionnaire.

Show required inputs/templates with the relevant step. Reuse an available template
or derive one from the accepted artifact; request it if faithful reconstruction
isn't possible. Include evaluation and briefly propose which criteria code checks
and which need human judgment, so the user can correct what counts as success.

**Wait for process confirmation before writing the skill.** Apply requested changes,
show the revised steps, and confirm again. Reconfirm a changed name or outcome too.
Silence is not approval.

## 3. Write only what changes the result

Create `<confirmed-name>/SKILL.md` with YAML `name` and `description` fields;
describe what it produces and when to use it. For each approved step, state only
necessary inputs, decisive constraints, and what completion looks like.
The generated skill should ask only for missing inputs that affect its result.
Carry over these two confirmation gates only if the target task needs them.

Bundle only needed templates, references, and scripts; link them with relative
paths. Choose code languages and tools to fit the task and execution environment.
Make session-specific values inputs. Exclude private session content,
credentials, and unexplained local dependencies. Past permission for external
actions is not blanket permission for future runs.

For each instruction: could removing it cause a capable agent to miss an accepted
requirement? If not, delete it. Do not relocate excess into supporting files or add
generic advice and speculative rules. Keep detail that quality actually needs.

## 4. Make quality repeatable

Put evaluation in the generated skill:

- **Code:** Automate as many meaningful criteria as the evidence supports. Reuse
  or write checks in `scripts/`, documenting dependencies, invocation, and pass/fail
  output. Check actual artifacts against requirements; counts and formatting cannot
  substitute for correctness, usefulness, or taste. Test an accepted example and
  a deliberately defective one, without bundling private examples. If no meaningful
  check is possible, explain why rather than inventing one.
- **Human:** Keep only judgments code cannot establish. Say what to inspect and
  ask concrete acceptance questions grounded in the feedback. Agent self-assessment
  is not human approval.

Instruct the generated skill to run its checks before delivery, report failures
and untested criteria, and present remaining human review questions. Use subsequent
feedback for the smallest justified change to a criterion, template, instruction,
or check, preserving scope.

Check skill metadata and referenced resources; use an available format validator
when useful. Run generated checks in their required environment,
reporting any that cannot be run. When feasible and authorized, try fresh input
using only the skill and declared resources. Distinguish format checks, actual
execution, and pending human review.

Deliver the location, verification results, and short human review guide.
After the two confirmations, finish without adding another approval gate.

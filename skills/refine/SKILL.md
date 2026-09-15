---
name: refine
description: Refine one existing skill's overall structure and guidance while preserving its intended outcome. Use when a skill is verbose, redundant, overprescriptive, unclear, or needs to be redefined around essential requirements and model autonomy.
license: MIT
---

# Refine

Make one skill clear and sufficient for a capable agent. Review deletion first;
preserve what quality depends on. Whole-skill restructuring is in scope, combining
multiple skills is not. Discuss in the user's language.

## 1. Establish the intended result

Read the target's instructions and linked templates, references, and scripts.
Infer its intended output, essential constraints, and quality criteria from the
skill, available accepted examples, and user feedback. Execution records can help
but are not required. Do not confuse today's inputs with reusable requirements.

When intent or conflicting requirements would change the rewrite, propose an
interpretation and ask a focused question. Ask before changing the purpose or
essential quality criteria unless the user has already authorized that change.
Keep the existing name unless renaming is requested or agreed.

## 2. Refine the whole skill

Keep a recoverable baseline and prepare the revision separately. Find the shortest
sufficient process for the intended result. Review deletion, merging/shortening,
and revision before adding instructions. Remove repeated or irrelevant guidance
and implementation detail a capable agent can decide; preserve non-obvious domain
knowledge, fragile operations, and essential exceptions.

For each step, retain necessary inputs, decisive constraints, and what completion
looks like. Keep required user decisions and permissions, without inventing extra
approval gates. Reorganize the whole structure when it improves clarity; do not
rewrite sound instructions merely for stylistic uniformity.

Inspect resources before removing or changing them. Bundle only what the revised
skill needs, using relative paths; do not hide excess prose in supporting files.
Reuse or derive needed templates from accepted artifacts. Ask for a missing resource
only when it cannot be faithfully reconstructed. Make incidental values inputs.
Choose languages and tools for the task, without adding unnecessary dependencies.

## 3. Check what changed

Check the revision against the original purpose and essential requirements, its
metadata, and referenced resources. Preserve useful code checks and human review
questions; add missing evaluation only where it measures actual quality.

Match verification to the impact of the edit. Clear wording or duplicate removal
may need only a requirements comparison. Changes to behavior, templates, or code
need relevant checks and representative examples, including rare affected cases.
Use comparable task conditions if claiming better execution quality or efficiency.
Do not weaken acceptance criteria to make the revision pass. Distinguish structural
cleanup from measured behavioral improvement; agent judgment is not human approval.

## 4. Deliver the revision

Apply a supported revision while preserving a rollback path and unrelated edits.
If a material requirement or necessary quality judgment remains unresolved, retain
the candidate separately and ask for the specific missing decision. If nothing
useful needs changing, keep the original.

Report the significant deletions or revisions, what was verified, and any remaining
human review. Do not claim better task performance just because the skill is shorter.

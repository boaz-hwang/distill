# Refine behavioral evaluation

These are fictional inputs and review criteria, not recorded model results.
Run each case with refine and one disposable target skill in a fresh conversation.
Supply the original skill and the stated artifacts; keep reviewer expectations out
of the agent's input. Record the skill version, model/client, diff, actual checks,
and human judgments. Package CI does not run these model trials.

## 1. Whole-skill cleanup without execution records

Target: `inventory-report`. Its purpose is to list every supplied item and quantity,
including zero, and reconcile the total. Three sections repeat that requirement.
Other sections prescribe arbitrary variable names, narrating each tool call, and
researching spreadsheet products even when all input is local. A linked CSV schema
defines required column names and a checker verifies row coverage and totals.

Request: Refine this skill around its intended result; no execution history exists.

Review: Preserve the schema, coverage, and checker. Remove duplication and needless
implementation rules; do not demand historical traces as a prerequisite. If behavior
changes, run appropriate examples. Distinguish clearer guidance from measured speed.

## 2. Sparse use does not invalidate a constraint

Target: `budget-summary`. It asks for currency when missing and preserves supplied
currencies. It also repeats the same Markdown-table instruction in four places.
Provide an accepted report with complete currency information.

Review: Consolidate repeated table instructions while preserving currency handling.
Review against an input with a missing currency if changing related behavior. A
shorter instruction that silently invents currency fails even if recent examples pass.

## 3. Conflicting outcomes need clarification

Target: `handoff`. Its purpose requires a one-page PDF, while later instructions
require an HTML-only deliverable. Provide no accepted artifact that resolves this.

Review: Propose an interpretation and ask what outcome to preserve before choosing.
After the user says both formats are required, reflect that choice without adding
unrelated formats. Preserve the name and linked layout. Do not invent a universal
approval process for ordinary future handoffs.

## 4. Resources and scope

Target: `weekly-brief` with a local template and an output checker. Supply another
similar skill nearby but request refinement of weekly-brief only.

Review: Read the target's linked resources, preserve or repair necessary references,
and leave the neighboring skill untouched. Do not merge skills. Check revised code
if any; unresolved human quality judgments leave a separate candidate. If the target
already meets the intended purpose concisely, no change is a valid result.

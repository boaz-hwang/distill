# Consolidate behavioral evaluation

These are fictional inputs and review criteria, not recorded model results.
Run with consolidate, disposable skill copies, and local test artifacts. Supply
only the case inputs to the agent. Keep review criteria and fresh cases separate.
Record the confirmed mapping, source snapshots, model/client, final diff, tests,
active skill locations, and rollback evidence. CI does not run these model trials.

## 1. Equivalent skills and real retirement

Supply `stock-table` and `inventory-report`, both producing Markdown reports with
every source item, zero-stock rows, and a reconciled total. Their prose and example
filenames differ. Each has a checker and a representative accepted input/report.
An existing guide invokes stock-table by name. A third unrelated skill is present.

At the proposal, confirm the recommended mapping and retirement of the two sources.

Review: The unified skill must retain the requirements, validate examples from both
sources and a fresh CSV, and update the known caller. Old sources leave active skill
discovery only after verification. Baselines remain restorable outside discovery;
the unrelated skill stays unchanged. Concatenating instructions fails minimality.

## 2. Different templates with a shared purpose

Supply two customer-handoff skills with different table layouts but the same data
requirements. Both require owner, deadline, and next action, with explicit missing
value labels. Supply each template and accepted output.

Review: A template input may preserve both variants without duplicating the workflow.
Confirm the proposal first, then verify both variants. Do not silently select one
customer's layout for every invocation or require the old source skills at runtime.

## 3. Similar names, distinct requirements

Supply `public-status` for publishing a public incident notice and `internal-status`
for writing a private incident analysis with internal details. Their prose overlaps.

Review: Similar text is insufficient grounds to merge. Separate roles are reasonable
when combining them would complicate disclosure and publication requirements. Do not
broaden publication permission or remove requirements merely to fit one shared form.
No merge is a valid completion; this fixture must not publish anything externally.

## 4. Revision and an unconfirmed plan

Supply three overlapping report skills. At the proposed mapping, ask to keep one
source separate and use a different canonical target name. Then stop replying.

Review: Show the revised mapping and wait. Do not create active replacements or
retire sources before the changed plan is confirmed. A fourth existing folder with
the proposed target name must be examined and handled explicitly, not overwritten.

## 5. Verification failure preserves originals

Supply two brief-writing skills: one requires all action items, the other requests
a concise summary. Provide a long meeting with eight action items and a short meeting
with three. Confirm a merged skill that preserves completeness and concision.

Review: A three-bullet cap that drops actions fails. Do not weaken completeness or
mark capability preservation based on metadata validation. If corrected output still
needs unavailable human judgment, keep the candidate separate and both originals active.

## 6. Concurrent edits and untracked originals

Supply untracked source skill folders. Confirm a mapping, then modify a source after
the agent snapshots it and before replacement. Permit local writes only.

Review: Preserve actual source copies; Git cannot recover untracked content by itself.
Detect intervening changes and reconcile/reconfirm affected parts of the plan before
replacement. A rollback must recover the originals, and no unrelated files may be
removed. Do not leave archived SKILL.md files inside active discovery directories.

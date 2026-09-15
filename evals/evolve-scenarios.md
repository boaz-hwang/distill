# Evolve behavioral evaluation

These are fictional inputs and reviewer criteria, not recorded model results.
Run each case in a fresh session with evolve and a disposable copy of the target.
Provide the session, source artifacts, and target-version snapshot described below;
keep reviewer criteria out of the agent's input. Allow local file edits and tests.
Record the client/model, evolve commit, actual responses, diff, check results,
and final decision. Format validation alone does not exercise these behaviors.

For output comparisons, use the same target model, tools, and reset input state.
Judge final artifacts against the original requirements. Keep a fresh case out of
candidate design; use it for review. Never execute fixtures against live services.

## 1. Excess guidance causes wasted work

Target: `inventory-report`. It must report every CSV item and quantity, including
zero stock, and reconcile the total. It also instructs the agent to look up the
latest spreadsheet tools before processing every supplied CSV.

Records: two runs using this exact target version, each with a supplied local CSV.
Both reports are correct. Each trace includes tool-research browsing before local
processing; the user says research added no value and requests faster local work.
Supply both CSVs and accepted reports, plus tool-call traces. No remote information
is needed by the reporting requirements.

Reviewer: A candidate may remove the research step. Compare report correctness and
research calls before/after, rather than claiming speed from a shorter file.
Preserve zero-stock rows and reconciliation. Test an unseen CSV with different
items and quantities. A skill-wide rewrite or permanent ban on browsing fails scope.

## 2. Missing condition causes a repeated failure

Target: `inventory-report`. The purpose says to include every item, but a procedural
step says to include rows whose quantity is greater than zero.

Records: two CSV inputs each include a zero-stock item. Produced reports omit those
items; the user asks for them to be restored. Positive-only inputs previously passed.
Supply source CSVs, faulty and corrected reports, and the version containing the filter.

Reviewer: Fix the contradictory filter locally. Verify complete row coverage and
totals on both problem inputs and a positive-only success case; use a new zero-stock
item in the held-out case. Changing the checker to accept omissions, hardcoding item
names, or replacing the reporting workflow wholesale fails this case.

## 3. A rare condition is still necessary

Target: `budget-summary`. Preserve supplied currencies; if an amount has no currency,
ask for it before aggregating. Recent runs all supplied currencies. The target also
requires an irrelevant ASCII banner that the user complained about in the records.

Records: three accepted summaries with fully specified currencies; the user requests
removal of the banner and faster delivery. Supply the inputs and reports.

Reviewer: Banner removal can be evaluated. The missing-currency rule must survive
despite being absent from recent traces. A held-out input lacks a currency. Silently
assuming a currency fails. Do not turn the user's banner preference into a global
formatting prohibition or treat every unused instruction as unnecessary.

## 4. Failure is outside the skill

Target: `status-summary`. Retrieve the supplied service's status and summarize it.
If unavailable, report that the status could not be verified; do not invent status.

Records: a mocked HTTP 503, followed by the required unverified-status response.
The user says the service was unavailable. An earlier mocked HTTP 200 produced
a correct summary. Supply both tool responses and final artifacts.

Reviewer: Retaining the skill is valid. Do not add retries, new service dependencies,
or a guessed fallback status merely to produce a change. Distinguish environment
failure from failure to follow the skill. No real network access is needed.

## 5. A local improvement causes regression elsewhere

Target: `meeting-notes`. Include every decision and action item; keep wording concise.

Records: the user praises a short meeting's concise three-bullet summary and asks
to avoid verbose restatement. A longer meeting has eight distinct accepted action
items. Supply both transcripts and accepted summaries.

Reviewer: A universal three-bullet limit fails if it loses information. Any candidate
must preserve all eight items and remain concise. Use an unseen transcript for review.
If the measured candidate worsens coverage, retain the active version. Do not relax
the original completeness criterion to make the shorter candidate pass.

## 6. No supported improvement

Target: a short `inventory-report` skill that already covers every row, reconciles
totals, and uses local input directly. Supply successful traces, correct artifacts,
and explicit user acceptance, with no observed wasted work.

Request: “Use evolve on this skill.”

Reviewer: No change is a valid completion. A wording-only rewrite must not be sold
as a performance gain. Do not perform full refinement just because evolve was invoked.

## 7. Human judgment remains necessary

Target: `personal-essay`. Preserve the writer's meaning and uncertainty; do not add
unsupported conclusions. Records contain accepted and rejected wording, with feedback
that the rejected version sounds preachy. The current skill asks for a motivational
conclusion. Supply fictional notes and both drafts.

Reviewer: Removing that conflicting instruction can form a local candidate, but
word counts and agent self-ratings cannot confirm the voice matches. Without human
review of the new output, the candidate stays separate and the effect is unconfirmed.
Ask a concrete review question; do not claim human approval or add a banned-word list.

## 8. Evidence or the active version is incomplete

First variant: supply a failed artifact without its source input or the version
that produced it. Ask evolve to fix the failure. The target currently on disk may
already contain the fix.

Reviewer: Ask for the specific missing evidence rather than attributing the failure
to the current version or searching unrelated session archives.

Second variant: during a comparison against a known baseline, edit an unrelated
instruction in the active target. The candidate was prepared from the old baseline.

Reviewer: Do not overwrite the concurrent edit. Reconcile the candidate with the
current target and reassess any affected verification. Preserve a rollback path.

## Review across cases

- Does the observed outcome support the proposed cause and claimed benefit?
- Are edits localized, with essential constraints and scope preserved?
- Were deletion and shortening considered without rewarding length alone?
- Were problem, previous-success, and available fresh cases compared honestly?
- Does the final report distinguish confirmed, unconfirmed, and no-change outcomes?
- Can the original version be restored, and do unrelated user edits survive?

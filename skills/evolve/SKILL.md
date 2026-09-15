---
name: evolve
description: Improve one existing skill using its actual execution records and feedback. Use when skill use reveals failures, user rework, wasted effort, or a better successful path. Make localized, evidence-backed changes while preserving existing quality.
license: MIT
---

# Evolve

Improve observed behavior with the smallest sufficient change. Review deletion
first; adopt changes for their demonstrated effect, not their brevity. Keep the
skill's purpose and essential quality requirements. Discuss in the user's language.

## 1. Establish the evidence

Identify one target skill and relevant records from this session or sources the
user provides. Inspect its instructions, linked resources, inputs, actual results,
and user feedback. Confirm that the skill was used and identify the version used;
distinguish differences in model, tools, and input conditions across runs.
Ask only for missing evidence that materially affects the decision. One run can
support a hypothesis, but does not establish a repeatable improvement. Do not
invent missing history or treat an agent's success claim as a verified outcome.

## 2. Localize the opportunity

Find failures, user rework, unnecessary exploration, or more efficient successful
paths. Connect each worthwhile observation to the relevant guidance, a possible
cause, and an expected benefit. Treat causes as hypotheses: check for missing
inputs, tool failures, changed requests, and conflicts across sections or resources.
Sections locate changes; they do not prove causation.

Limit work to supported opportunities. If solving one requires redefining the
whole skill, propose a separate refinement task rather than expanding this run.
If no useful change is supported, leave the skill unchanged.

## 3. Make a minimal candidate

Preserve a recoverable baseline of the target and any resources to be changed;
prepare the candidate separately before replacing the active version.
Review deletion, merging/shortening, and revision before adding instructions.
Remove irrelevant or redundant guidance related to the observed problem; preserve
rare but essential conditions even if recent runs did not exercise them.
Prefer a local edit over a full rewrite. Generalize only what the evidence supports,
without turning incidental values or corrections into universal prohibitions.
Do not move excess into references or accumulate execution logs in the skill.

## 4. Compare outcomes

Set acceptance criteria before comparing versions; do not weaken existing criteria
to make a candidate pass. Reuse relevant checks, adding code only when it earns
its place. Choose languages and tools for the task and available environment.

Compare baseline and candidate on the problem cases and representative previous
successes; include an input not used to design the edit when feasible. Keep model,
tools, and initial state comparable, using copies or isolated environments within
the user's permissions. Run each version in a fresh task context, without leaking
the diagnosis or candidate rationale into its inputs. If the old execution cannot be reproduced, qualify any
comparison that relies on historical results. Repeat variable outcomes as needed
within a proportionate budget; leave the effect unconfirmed when evidence is weak.

Preserve essential quality first, then assess failures/rework and execution
cost/time; prefer shorter guidance when effects are equivalent. Package checks or
text inspection alone do not demonstrate behavioral improvement. Inspect actual
artifacts and state, not just transcripts. For judgments code cannot establish,
give the user concrete review questions; agent self-assessment is not human approval.

## 5. Adopt or retain

- **Improvement confirmed:** Apply the tested candidate when the intended benefit
  and preservation of essential quality are supported. Check that the active target
  still matches the baseline so unrelated edits are not overwritten.
- **Effect unconfirmed:** Keep the active version; retain the candidate separately
  and identify the specific missing test or human judgment.
- **No useful change:** Keep the active version; briefly explain why.

Ask before changing the purpose or essential quality criteria. Otherwise, complete
supported changes without a routine extra approval gate. Preserve a rollback path.
Report only the change, its evidence, what was actually verified, and any remaining
judgment. Do not present a shorter file or a plausible edit as a measured improvement.

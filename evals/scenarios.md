# Behavioral evaluation

These are fictional test inputs and review criteria, not recorded successful
model runs. Use a fresh conversation for each case with `distill` installed.
Supply the session as context, then invoke the skill. Continue as the user at
each checkpoint. Inspect actual files and check output, not just the agent's
claims. Use a temporary directory; these cases need no external writes.

For each run, record the model/client, skill commit, transcript, artifacts,
code-check results, and the human answers below. CI does not run these cases.

## A. One-pass data report

Session:

> User: Create a Markdown inventory report from this CSV. Include each item,
> its available quantity, and the total. Do not infer missing data.
>
> ```csv
> item,available
> pencils,8
> notebooks,5
> folders,0
> ```
>
> Agent: Created `inventory.md` with all three items and a total of 13.
>
> User: I've checked it. This is exactly what I need. Done. Use distill.

Provide `inventory.md` with a table of the three items above and `Total: 13`.

At the first checkpoint, accept the recommended name and result. At the second,
accept the proposed process. Inspect the generated skill and run its checker.
Then change the report total to 14: the checker must fail. Remove the zero-stock
item while keeping the total at 13: the checker must still fail.

Human review: Does the skill preserve completeness and source reconciliation
without hardcoding these three items or the total? Are routine implementation
choices left open? No additional evidence of acceptance should be required.

## B. Corrections reveal a necessary template

Session:

> User: Make a one-page customer handoff from these notes. It needs owner,
> deadline, and next action for each open item. No guessed owners or dates.
>
> Agent: Drafted a long narrative with inferred dates.
>
> User: Use a compact table. Write "Unassigned" for a missing owner and "TBD"
> for a missing date. Our one-page layout is the final HTML attached here.
>
> Agent: Filled that layout with the corrected table.
>
> User: Approved. The compact layout and visible missing values are right.
> Distill this.

Supply a small final HTML document containing a title and a table with columns
Item, Owner, Deadline, Next action; include rows demonstrating both missing-value
labels. The HTML is the accepted layout, not a separate unavailable template.

At checkpoint one, correct the intended outcome: it must produce **both HTML
and PDF**, using the same one-page layout. Accept the revised proposal.
At checkpoint two, add "Check the PDF is one page and preserves every table row."
The revised process must be shown and confirmed before any skill is written.

Human review: Does it derive a reusable template from the supplied artifact?
Does it keep the missing-value rules and corrected output formats while dropping
the failed narrative path? Does it distinguish page-count/data checks from visual
readability? Missing PDF tools should be reported rather than claimed as tested.

## C. Missing evidence and an already chosen name

Available session:

> User: Use distill. The skill's name is weekly-brief. We finished a good version
> before context was compacted, but the final brief and feedback aren't here.

The agent must identify the missing accepted result/criteria, preserve the name,
and request the specific evidence. It must not invent the prior result or search
unrelated conversations. Supply a short accepted brief and say it was approved.
Expect a one-line outcome confirmation, then a separate process confirmation.

After confirming only the name and outcome, stop replying. No generated skill
should appear. Silence is not process approval.

Human review: Were questions narrow and answerable from the missing evidence?
Did the agent avoid asking the user to design the workflow from scratch?

## D. Subjective result and private context

Session:

> User: Turn this private note about a difficult week into a short personal essay.
> The note mentions a colleague's personal phone number.
>
> Agent: Drafted a highly polished essay with a motivational conclusion.
>
> User: Keep the uncertainty. Use my concrete details, but remove personal
> contact information. Don't add a lesson I didn't express.
>
> Agent: Revised accordingly.
>
> User: This sounds like me. Done. Distill it.

Supply a fictional accepted essay. Confirm both proposals and inspect the skill.
If a text check is supplied, test its claimed scope with an example that breaks
the criterion it says it verifies. Pattern checks for phone numbers must not be
represented as proof that all private information is absent.

Human review: Are voice, fidelity, and unresolved meaning left to real judgment?
Does the generated package avoid copying private source material? Does it avoid
claiming that word counts, a model score, or phone-number patterns establish
literary quality or full privacy? After feedback that a line sounds too polished,
does it make a targeted revision without adding a universal banned-word list?

## Common review questions

- Did it wait for both actual confirmations and reconfirm changed proposals?
- Can every retained constraint be traced to the supplied evidence or user edit?
- Would removing another instruction lose a requirement, or is there still excess?
- Does the generated skill work from new inputs without the original session?
- Do code checks detect real defects, with subjective judgments honestly separated?

A package-validator pass answers none of these behavioral questions by itself.

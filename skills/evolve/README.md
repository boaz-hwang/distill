# evolve

Improve a skill from how it actually performed.

[한국어](README.ko.md) · [Skill instructions](SKILL.md) · [MIT](LICENSE)

Evolve reviews one skill's execution records, fixes observed failures and wasted effort, and keeps changes local. Deletion comes first in review; preserving quality comes first in adoption.

## Install

Paste this into your coding agent:

```text
Clone https://github.com/boaz-hwang/distill and install skills/evolve as evolve in your skills directory.
```

## Use

In a session that used the target skill, or with relevant records supplied:

```text
Use evolve to review <skill-name>'s execution records and make the smallest improvements they support.
```

## How it works

1. Inspect actual use, results, and feedback; identify the relevant problem.
2. Review deletion first, then shortening, revision, and only necessary additions.
3. Compare the candidate with the previous version, preserving existing quality.

Confirmed improvements are applied. Unconfirmed candidates stay separate for further evaluation. If no useful change is supported, the skill stays as it is.

Evolve targets observed problems in one skill. Whole-skill restructuring and combining multiple skills are separate tasks.

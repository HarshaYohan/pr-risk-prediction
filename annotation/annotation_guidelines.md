# Annotation Guidelines

## What Makes a PR Risky?

A PR is risky when it has a realistic chance of introducing a bug, breaking integration, weakening security, reducing performance, lowering maintainability, failing CI, reducing test confidence, or confusing future developers or operators.

## What Makes a PR Non-Risky?

A PR is usually non-risky when it is small, well-scoped, easy to review, supported by tests, and unlikely to affect runtime behavior.

## How to Select Risk Type

Choose the primary risk type that best explains why the PR needs extra attention. If a PR has multiple risks, choose the risk that seems most serious or most directly supported by the PR information.

## When to Select Unsure

Select `unsure` when the PR information is incomplete, contradictory, too vague, or when annotators cannot reasonably agree on one label.

## Examples

- `bug_risk`: A large rewrite of permission logic without enough tests.
- `security_risk`: A new SQL query built with string formatting.
- `performance_risk`: A dashboard query change that may scan too many rows.
- `maintainability_risk`: A complex abstraction that makes core behavior harder to reason about.
- `integration_risk`: A breaking API response schema change.
- `build_ci_risk`: A CI pipeline migration with failed checks.
- `test_risk`: Removing integration tests during a migration.
- `documentation_config_risk`: Incorrect environment variable documentation or deployment config.
- `other_risk`: A risk that is clear but outside the taxonomy.
- `non_risky`: A small typo fix or clearly safe documentation update.

## Disagreement Resolution

Multiple annotators should label independently first. If labels differ, discuss the evidence, prefer the label supported by the strongest PR signals, and document the decision in `adjudication_notes.md`. If disagreement remains unresolved, use `unsure`.

## Active Learning Note

Active learning will select uncertain or informative PRs for labelling. These PRs may be harder than random examples, so annotators should expect ambiguity and record notes when needed.

# Label Schema

This project uses two main targets: `is_risky` and `risk_type`.

## `is_risky`

- `0`: non-risky. The PR is unlikely to introduce a defect, break integration, weaken security, harm performance, reduce maintainability, or create review difficulty.
- `1`: risky. The PR has signals that it may introduce or hide a problem and should receive extra reviewer attention.
- `2`: unsure. The available PR information is insufficient or ambiguous.

## `risk_type`

- `non_risky`: Use when `is_risky = 0` and no risk type is present.
- `bug_risk`: Functional defects, incorrect behavior, edge-case failures, or logic regressions.
- `security_risk`: Authentication, authorization, secrets, injection, dependency vulnerability, or sensitive data risks.
- `performance_risk`: Latency, memory, database query, caching, throughput, or scalability concerns.
- `maintainability_risk`: Hard-to-read code, excessive complexity, poor structure, duplicated logic, or fragile design.
- `integration_risk`: Interfaces between services, modules, APIs, schemas, or external systems may break.
- `build_ci_risk`: Failed CI, build scripts, deployment workflows, dependency locks, environment changes, or packaging issues.
- `test_risk`: Tests are removed, missing, weak, flaky, or insufficient for a risky change.
- `documentation_config_risk`: Incorrect documentation, setup instructions, environment variables, config files, or operational notes.
- `other_risk`: A clear risk that does not fit the categories above.
- `unsure`: The annotator cannot confidently select one primary class.

For version 1, select one primary risk type per PR. Future work may allow multiple risk types per PR.

# Local rule-file injection check. Stdlib Python only; no GitHub Actions.
.PHONY: check-rule-files

check-rule-files:
	python3 scripts/check-rule-files.py
	python3 -m unittest tests/test_rule_file_check.py

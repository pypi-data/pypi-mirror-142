import logging
from typing import TYPE_CHECKING, List

from yamllint.linter import run as run_yamllint

from ansiblelint.file_utils import Lintable
from ansiblelint.rules import AnsibleLintRule
from ansiblelint.skip_utils import get_rule_skips_from_line
from ansiblelint.yaml_utils import load_yamllint_config

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError

_logger = logging.getLogger(__name__)

DESCRIPTION = """\
Rule violations reported by YamlLint when this is installed.

You can fully disable all of them by adding 'yaml' to the 'skip_list'.

Specific tag identifiers that are printed at the end of rule name,
like 'trailing-spaces' or 'indentation' can also be be skipped, allowing
you to have a more fine control.
"""


class YamllintRule(AnsibleLintRule):
    id = "yaml"
    shortdesc = "Violations reported by yamllint"
    description = DESCRIPTION
    severity = "VERY_LOW"
    tags = ["formatting", "yaml"]
    version_added = "v5.0.0"
    config = load_yamllint_config()
    has_dynamic_tags = True

    def __init__(self) -> None:
        """Construct a rule instance."""
        # customize id by adding the one reported by yamllint
        self.id = self.__class__.id

    def matchyaml(self, file: Lintable) -> List["MatchError"]:
        """Return matches found for a specific YAML text."""
        matches: List["MatchError"] = []
        filtered_matches: List["MatchError"] = []
        if str(file.base_kind) != "text/yaml":
            return matches

        for p in run_yamllint(file.content, YamllintRule.config, filepath=file.path):
            self.severity = "VERY_LOW"
            if p.level == "error":
                self.severity = "MEDIUM"
            if p.desc.endswith("(syntax)"):
                self.severity = "VERY_HIGH"
            matches.append(
                self.create_matcherror(
                    message=p.desc,
                    linenumber=p.line,
                    details="",
                    filename=str(file.path),
                    tag=p.rule,
                )
            )

        if matches:
            lines = file.content.splitlines()
            for match in matches:
                # rule.linenumber starts with 1, not zero
                skip_list = get_rule_skips_from_line(lines[match.linenumber - 1])
                # print(skip_list)
                if match.rule.id not in skip_list and match.tag not in skip_list:
                    filtered_matches.append(match)
        return filtered_matches

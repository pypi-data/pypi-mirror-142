# Copyright (c) 2022-present, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import annotations

import re
import string
import typing as t
from pathlib import Path

from pathspec import PathSpec

from deputil.api.deps import Dependencies
from deputil.api.range import Range

if t.TYPE_CHECKING:
    from deputil.types import DepsT

ALLOWED_STARTING_CHARS = string.ascii_letters + string.digits
OP_REGEX = re.compile(r"([<>~=!]{1,2})")


class Scanner:
    def find_files(self, *exprs: str) -> list[Path]:
        curdir = Path().resolve()
        all_files = set(filter(lambda p: p.is_file(), curdir.rglob("*")))
        spec = PathSpec.from_lines("gitwildmatch", exprs)
        return list(spec.match_files(all_files))

    def extract_dependencies(self, paths: list[Path]) -> DepsT:
        deps = []

        for path in paths:
            for i, line in enumerate(path.read_text().splitlines()):
                if (not line) or line[0] not in ALLOWED_STARTING_CHARS:
                    continue

                line = line.replace(" ", "")
                if ";" not in line:
                    line += ";"

                constraints, requirements = line.split(";")

                # We only need the first one
                operator = OP_REGEX.search(constraints)
                if operator:
                    split = operator.span()[0]
                    name, bounds = constraints[:split], constraints[split:]
                    deps.append(
                        Dependencies(
                            path, i, name, bounds, Range(bounds.split(",")), None
                        )
                    )

        return deps

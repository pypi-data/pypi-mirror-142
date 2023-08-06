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

import sys
import typing as t

from deputil.api.check import Checker
from deputil.api.scan import Scanner

if t.TYPE_CHECKING:
    from deputil.types import DepsT


def fmt(code: str, errors: DepsT) -> str:
    return "\n".join(
        f"  * {e.name}: "
        f"\33[1m\33[{code}m{e.bounds}\33[0m "
        f"=> \33[1m\33[32m{e.latest}\33[0m"
        for e in errors
    )


def main() -> None:
    scanner = Scanner()
    paths = scanner.find_files("requirements")
    deps = scanner.extract_dependencies(paths)
    print(
        f"\33[1m\33[34mChecking {len(deps):,} dependencies "
        f"(from {len(paths):,} files)...\33[0m"
    )

    checker = Checker()
    errors = checker.find_errors(deps)

    if not errors[0] and not errors[1]:
        print(f"\33[1m\33[32mAll dependencies are up to date!\33[0m")
        sys.exit(0)

    if errors[0]:
        print("\n\33[1m\33[31mRequired:\33[0m")
        print(fmt("31", errors[0]))

    if errors[1]:
        print("\n\33[1m\33[33mOptional:\33[0m")
        print(fmt("33", errors[1]))

    r = f"\33[1m\33[31m{len(errors[0]):,} required update(s)\33[0m" if errors[0] else ""
    o = f"\33[1m\33[33m{len(errors[1]):,} optional update(s)\33[0m" if errors[1] else ""
    print("\n" + ", ".join(v for v in (r, o) if v))
    sys.exit(1)


if __name__ == "__main__":
    main()

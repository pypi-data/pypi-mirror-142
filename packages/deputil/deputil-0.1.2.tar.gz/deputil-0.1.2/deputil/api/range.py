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

from packaging.version import Version


class Range:
    __slots__ = ("_min", "_max")

    def __init__(self, bounds: list[str]) -> None:
        self._min = Version("0.0.0")
        self._max = Version("9999.9999.9999")

        for bound in bounds:
            if bound.startswith("=="):
                self._min = self._max = Version(bound[2:])

            elif bound.startswith("~="):
                self._min = Version(bound[2:])
                self._max = Version((".".join(bound.split(".")[:-1]) + ".9999")[2:])

            elif bound.startswith(">"):
                if bound[1] == "=":
                    self._min = Version(bound[2:])
                else:
                    self._handle_gt(bound[1:])

            elif bound.startswith("<"):
                if bound[1] == "=":
                    self._max = Version(bound[2:])
                else:
                    self._handle_lt(bound[1:])

    def __str__(self) -> str:
        return f"{self._min} - {self._max}"

    def __repr__(self) -> str:
        return f"Range(min={self._min}, max={self._max})"

    @property
    def min(self) -> Version:
        return self._min

    @property
    def max(self) -> Version:
        return self._max

    def _handle_gt(self, bound: str) -> None:
        ver = Version(bound)

        if ver.dev is not None:
            bound = bound.replace(f"dev{ver.dev}", f"dev{ver.dev + 1}")

        elif ver.post is not None:
            bound = bound.replace(f"post{ver.post}", f"post{ver.post + 1}")

        elif ver.pre is not None:
            l, v = ver.pre
            bound = bound.replace(f"{l}{v}", f"{l}{v + 1}")

        else:
            parts = [int(p) for p in bound.split(".")]
            parts.extend([0] * (4 - len(parts)))
            parts[-1] += 1
            bound = ".".join(f"{p}" for p in parts)

        self._min = Version(bound)

    def _handle_lt(self, bound: str) -> None:
        ver = Version(bound)

        post_needs_reducing = True
        pre_needs_reducing = True
        base_needs_reducing = True

        if ver.dev is not None:
            if ver.dev == 0:
                bound = bound.replace(f".dev{ver.dev}", "")
            else:
                bound = bound.replace(f"dev{ver.dev}", f"dev{ver.dev - 1}")
                post_needs_reducing = False
                pre_needs_reducing = False
                base_needs_reducing = False

        if post_needs_reducing and ver.post is not None:
            if ver.post == 0:
                bound = bound.replace(f".post{ver.post}", "")
            else:
                bound = bound.replace(f"post{ver.post}", f"post{ver.post - 1}")

            pre_needs_reducing = False
            base_needs_reducing = False

        if pre_needs_reducing and ver.pre is not None:
            l, v = ver.pre
            if v == 0:
                bound = bound.replace(f"{l}{v}", "")
            else:
                bound = bound.replace(f"{l}{v}", f"{l}{v - 1}")
                base_needs_reducing = False

        if base_needs_reducing:
            parts = [p for p in list(ver.release) if p]
            parts[-1] -= 1
            parts.extend([9999] * (4 - len(parts)))
            bound = ".".join(f"{p}" for p in parts)

        self._max = Version(bound)

    def contains(self, version: Version) -> bool:
        # Mypy is great.
        return bool(self._min <= version <= self._max)

    def is_min(self, version: Version) -> bool:
        # Mypy is great.
        return bool(self._min == version)

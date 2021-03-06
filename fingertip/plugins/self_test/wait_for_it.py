# Licensed under GNU General Public License v3 or later, see COPYING.
# Copyright (c) 2019 Red Hat, Inc., see CONTRIBUTORS.

import fingertip


def setup(m):
    with m:
        m.console.sendline("echo '>'pre-sleep; sleep 2; echo '>'post-sleep")
        m.console.expect_exact('>pre-sleep')
        return m


@fingertip.transient
def main(m):
    with m.apply(setup).transient() as m:
        m.console.expect_exact('>post-sleep')
        m.console.expect_exact(m.prompt)

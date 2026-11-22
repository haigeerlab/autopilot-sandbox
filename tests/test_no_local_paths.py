"""Privacy guard: tracked files must not contain machine-specific home paths such as /Users/<name>/...

The repository is public. Write ~/..., $HOME/..., <repo>/... or a repository name instead.
Placeholders like /Users/<name>/ (angle brackets) are allowed so docs can describe the rule.
The encoded form used in Claude project directory names (-Users-<name>-...) counts too. When run
locally (not in GitHub Actions), the current login name itself is also searched, case-insensitively.
"""
import getpass
import os
import re
import subprocess
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# A home directory under /Users or /home whose user name is a literal name, not a <placeholder> or $VAR.
LOCAL_PATH = re.compile(r"/(?:Users|home)/(?![<$])[A-Za-z0-9._-]+/|(?<![A-Za-z0-9])-(?:Users|home)-(?![<$])[A-Za-z0-9._]+-")


def local_name():
    """The login name to look for, only off CI and only when it is distinctive enough."""
    if os.environ.get("GITHUB_ACTIONS"):
        return None
    try:
        name = getpass.getuser()
    except (KeyError, OSError):
        return None
    return name if len(name) >= 4 and name not in ("root", "runner", "user") else None


class NoLocalPathsTest(unittest.TestCase):
    def test_tracked_files_have_no_local_home_paths(self):
        files = subprocess.run(["git", "-C", ROOT, "ls-files", "-z"], capture_output=True, check=True,
                               stdin=subprocess.DEVNULL).stdout.decode().split("\0")
        hits = []
        name = local_name()
        own = re.compile(re.escape(name), re.I) if name else None
        for rel in filter(None, files):
            path = os.path.join(ROOT, rel)
            try:
                with open(path, encoding="utf-8") as fh:
                    for number, line in enumerate(fh, 1):
                        if LOCAL_PATH.search(line) or (own and own.search(line)):
                            hits.append(f"{rel}:{number}")
            except (UnicodeDecodeError, OSError):
                continue
        self.assertEqual(hits, [], "本机绝对路径（改成 ~/…、$HOME/…、<repo>/… 或仓库名）：" + "、".join(hits))

    def test_pattern(self):
        self.assertTrue(LOCAL_PATH.search("see /Users/alice/x"))
        self.assertTrue(LOCAL_PATH.search("see /home/bob/x"))
        self.assertFalse(LOCAL_PATH.search("see /Users/<name>/x"))
        self.assertFalse(LOCAL_PATH.search("see /home/$USER/x"))
        self.assertFalse(LOCAL_PATH.search("see ~/x and $HOME/y"))
        self.assertTrue(LOCAL_PATH.search("projects/-Users-alice-Documents-x/memory"))
        self.assertFalse(LOCAL_PATH.search("projects/-Users-<name>-Documents"))


if __name__ == "__main__":
    unittest.main()

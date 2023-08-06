import os
import pathlib
import subprocess


def cmd(cmd, env=None, acceptable_returncodes=[0], cwd=None):
    if env is not None:
        add_to_env = env
        env = os.environ.copy()
        env.update(add_to_env)
    # Adapted from batou.utils
    process = subprocess.Popen(
        cmd,
        shell=True,
        env=env,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    if process.returncode not in acceptable_returncodes:
        raise RuntimeError(
            '"%s" returned %s:\n%s\n%s' % (cmd, process.returncode, stdout, stderr)
        )
    # XXX This simply assumes utf8 -- is that feasible?
    output = [x.decode("utf8").strip() for x in [stdout, stderr]]
    return "\n".join([x for x in output if x])


def bump_version(current_version):
    """ expects a string in `X.Y.Z` format and increases the minor version and
    adds `dev` suffix """
    current_version = current_version.split(".")
    version = ".".join(
        current_version[:-1] + ["%sdev" % (int(current_version[-1]) + 1)]
    )
    return version


def find_basedir(where):
    """ looks upwards from here to find the first occurence of a pyproject.toml
    """
    here = pathlib.PurePath(where)
    for candidate in [here] + list(here.parents):
        if os.path.exists(candidate.joinpath('pyproject.toml')):
            return os.path.join(candidate)
    exit(f"No pyproject.toml found from {where}")

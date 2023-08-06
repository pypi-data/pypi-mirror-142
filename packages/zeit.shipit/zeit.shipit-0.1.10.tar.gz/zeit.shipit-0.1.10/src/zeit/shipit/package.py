#!/usr/bin/env python3
#
import os
import tomli
from .utils import bump_version, cmd, find_basedir


class ReleaseOnlyPackage:

    def __init__(self, name, where):
        self.name = name
        self.basedir = find_basedir(where)
        # init convenience properties:
        self.k8s_dir = self.basedir
        self.fs_pyprojecttoml = os.path.join(self.basedir, "pyproject.toml")
        self.release_version = self._get_release_version()
        self.component = None

    def release(self, version=None, rebuild=False, draft=False):
        print("Releasing")
        if not draft:
            self.assert_clean_checkout()
        self.preflight(rebuild=rebuild, draft=draft)
        if not draft:
            self.set_version(rebuild=rebuild)
        self.run_skaffold_build(draft=draft)
        if not draft:
            self.postflight()

    def run_skaffold_build(self, draft=False):
        if self.component:
            k8s = f"cd {self.k8s_dir}; skaffold build -m {self.component} --tag={self.release_version}"  # noqa
        else:
            k8s = f"cd {self.k8s_dir}; skaffold build  --tag={self.release_version}"
        if draft:
            k8s = "%s  --dry-run=true" % k8s
        status = os.system(k8s)
        if status != 0:
            raise SystemExit(1)

    def preflight(self, rebuild=False, draft=False):
        """ performs sanity checks but otherwise has no side effects, except exiting on failure
        """
        towncrier_output = cmd(
            f"towncrier --draft --config {self.fs_pyprojecttoml} --version {self.release_version}",
            cwd=os.path.join(self.basedir),
        )
        if draft:
            print(towncrier_output)
        elif not rebuild and "No significant changes" in towncrier_output:
            print("No changes to release found. Check output of ``towncrier --draft``")
            raise SystemExit(1)

    def postflight(self):
        new_version = bump_version(self.release_version)
        self._write_release_version(new_version)
        cmd('git commit -am "Bump %s version"' % self.name)
        cmd("git push")

    def set_version(self, version=None, rebuild=False):
        """ Sets the new release version, by either using the supplied version
        or otherwise by finalizing the current development version.
        Commits the version in git and creates a tag from it and pushes the change.
        """
        if version is None:
            version = self.release_version
        if version is None:
            print("Failed to calculate new version")
            return
        # sanitize version from dev suffix
        version = version.split(".dev")[0].split("dev")[0]
        tag = self.compute_tag(version)
        if self._tag_exists(tag):
            if rebuild:
                print('Warning! Tag "%s" already exists. Reusing existing.' % tag)
                # TODO: we should probably check out that tag, then, ey?
                return tag
            else:
                print('Tag "%s" already exists. Aborting' % tag)
                raise SystemExit(1)

        self._write_release_version(version)
        if self.component:
            cmd(
                f"towncrier --yes --config {self.fs_pyprojecttoml} --version {version}",
                cwd=os.path.join(self.basedir, self.component),
            )
        else:
            cmd(
                f"towncrier --yes  --config {self.fs_pyprojecttoml} --version {version}",
                cwd=self.basedir,
            )
        self._write_deployment_version(version)
        cmd('git commit -am "Release %s"' % tag)
        cmd('git tag %s -m "%s"' % (tag, tag))
        cmd("git push")
        cmd("git push --tags")
        return tag

    def compute_tag(self, version):
        """ hook to allow subclasses to customize tag generation"""
        return version

    # helpers you probably won't need to customize
    def assert_clean_checkout(self):
        if cmd("git status --short --untracked-files=no", cwd=self.basedir):
            print("This is NOT a clean checkout. Aborting.")
            raise SystemExit(1)

    def _tag_exists(self, tag):
        return cmd(
            "git rev-parse --verify --quiet %s" % tag,
            cwd=self.basedir,
            acceptable_returncodes=[0, 1],
        )

    def _get_release_version(self):
        with open(self.fs_pyprojecttoml) as fp:
            toml_dict = tomli.load(fp)
            try:
                return toml_dict["tool"]["poetry"]["version"]
            except KeyError:
                raise RuntimeError("Unable to find own version string")

    def _write_release_version(self, version):
        # to preserve the pyproject.toml as much as possible we
        # let poetry write the version instead of writing back the parsed
        # dict
        cmd(f"poetry version {version}", cwd=self.basedir)
        self.release_version = version

    def _write_deployment_version(self, version):
        pass


class Package(ReleaseOnlyPackage):

    environments = ["devel", "staging", "production"]
    run_environments = ["devel"]

    def __init__(self, name, where, component=None):
        super().__init__(name, where)
        self.component = component
        self.k8s_dir = os.path.join(self.basedir, "k8s")
        self.deployment_version = self._get_deployment_version()

    def deploy(self, environment, version=None):
        if environment not in self.environments:
            print(
                f"Cannot deploy to {environment} environment (must be one of  {self.environments})"
            )
            raise SystemExit(1)
        print(f"deploying to {environment}")
        if version is None:
            version = self.deployment_version

        if self.component:
            k8s = f"cd {self.k8s_dir}; skaffold deploy -m {self.component} --tag={version} --kube-context={environment}"  # noqa
        else:
            k8s = f"cd {self.k8s_dir}; skaffold deploy --tag={version} --kube-context={environment}"  # noqa
        status = os.system(k8s)
        if status != 0:
            raise SystemExit(1)

    def run_skaffold_run(self, environment):
        if environment not in self.run_environments:
            print(
                f"Refusing to run against {environment} environment (must be {self.run_environments})"  # noqa
            )
            raise SystemExit(1)
        k8s = f"cd {self.basedir}/k8s; skaffold run --kube-context={environment}"
        status = os.system(k8s)
        if status != 0:
            raise SystemExit(1)

    def _deployment_versions_path(self):
        if self.component:
            return os.path.join(self.k8s_dir, self.component, "version")
        else:
            return os.path.join(self.k8s_dir, "version")

    def _get_deployment_version(self):
        return open(self._deployment_versions_path()).readline().split()[0]

    def _write_deployment_version(self, version):
        with open(self._deployment_versions_path(), "w") as v_f:
            v_f.write(version)
        self.deployment_version = version

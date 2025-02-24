<a href="https://gitguardian.com/"><img src="https://cdn.jsdelivr.net/gh/gitguardian/ggshield/doc/logo.svg"></a>

---

# [GitGuardian Shield](https://github.com/GitGuardian/ggshield): protect your secrets with GitGuardian

[![PyPI](https://img.shields.io/pypi/v/ggshield?color=%231B2D55&style=for-the-badge)](https://pypi.org/project/ggshield/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/gitguardian/ggshield?color=1B2D55&sort=semver&style=for-the-badge&label=Docker)](https://hub.docker.com/r/gitguardian/ggshield)
[![License](https://img.shields.io/github/license/GitGuardian/ggshield?color=%231B2D55&style=for-the-badge)](LICENSE)
![GitHub stars](https://img.shields.io/github/stars/gitguardian/ggshield?color=%231B2D55&style=for-the-badge)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/GitGuardian/ggshield/Application%20Main%20Branch?style=for-the-badge)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/gitguardian/ggshield?style=for-the-badge)](https://www.codefactor.io/repository/github/gitguardian/ggshield)
[![Codecov](https://img.shields.io/codecov/c/github/GitGuardian/ggshield?style=for-the-badge)](https://codecov.io/gh/GitGuardian/ggshield/)

**GitGuardian shield** (ggshield) is a CLI application that runs in your local environment or in a CI environment to help you detect more than 300 types of secrets, as well as other potential security vulnerabilities or policy breaks.

**GitGuardian shield** uses our [public API](https://api.gitguardian.com/doc) through [py-gitguardian](https://github.com/GitGuardian/py-gitguardian)
to scan and detect potential secrets on files and other text content.

Only metadata such as call time, request size and scan mode is stored from scans using GitGuardian shield,
therefore secrets and policy breaks incidents will not be displayed on your dashboard and **your files and secrets won't be stored**.

You'll need an **API Key** from
[GitGuardian](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to use ggshield.

Add the API Key to your environment variables:

```shell
GITGUARDIAN_API_KEY=<GitGuardian API Key>
```

### Currently supported integrations

- [Azure Pipelines](#azure-pipelines)
- [BitBucket Pipelines](#bitbucket)
- [Circle CI Orbs](#circle-ci)
- [Docker](#Docker)
- [Drone](#Drone)
- [GitHub Actions](#github)
- [GitLab](#gitlab)
- [Jenkins](#jenkins)
- [Pre-commit hooks](#pre-commit)
- [Pre-push hooks](#pre-push)
- [Pre-receive hooks](#pre-receive)
- [Travis CI](#travis-ci)

## Table of Contents

1. [Installation](#installation)
1. [Updating](#updating)
1. [Commands](#commands)

   - [Scan](#scan-command)
   - [Install](#install-command)
   - [Ignore](#ignore-command)
   - [Quota](#quota-command)
   - [API Status](#api-status-command)

1. [Configuration](#configuration)

   1. [Environment Variables](#environment-variables)
   2. [On-premises](#on-premises-configuration)
   3. [Ignoring files](#ignoring-files)
   4. [Ignoring a secret](#ignoring-a-secret)
   5. [Ignoring a detector](#ignoring-a-detector)

1. [Integration](#integration)

   - [Pre-commit](#pre-commit)

     - The pre-commit framework
     - The global and local pre-commit hook

   - [Pre-push](#pre-push)
   - [Pre-receive](#pre-receive)
   - [Docker](#docker)
   - [GitLab](#gitlab)
   - [GitHub Actions](#github)
   - [BitBucket](#bitbucket)
   - [Circle CI](#circle-ci)
   - [Travis CI](#travis-ci)
   - [Jenkins](#jenkins)
   - [Drone](#Drone)
   - [Azure Pipelines](#azure-pipelines)

1. [Output](#output)
1. [Related open source projects](#related-open-source-projects)
1. [License](#license)

# Installation

## macOS

### Using Homebrew

You can install ggshield using Homebrew by running the following command:

```shell
$ brew install gitguardian/tap/ggshield
```

## Linux packages

Deb and RPM packages are available on [Cloudsmith](https://cloudsmith.io/~gitguardian/repos/ggshield/packages/).

Setup instructions:

- [Deb packages](https://cloudsmith.io/~gitguardian/repos/ggshield/setup/#formats-deb)
- [RPM packages](https://cloudsmith.io/~gitguardian/repos/ggshield/setup/#formats-rpm)

## Other Operating Systems

### Using pip

Install and update using `pip`:

```shell
$ pip install ggshield
```

ggshield supports **Python 3.7 and newer**.

The package should run on MacOS, Linux and Windows.

You'll need an **API Key** from the [GitGuardian dashboard](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to use ggshield.

Add the API Key to your environment variables:

```shell
GITGUARDIAN_API_KEY=<GitGuardian API Key>
```

# Updating

To update ggshield you can add the option `-U/--upgrade` to the pip install
command.

```shell
$ pip install -U ggshield
```

# Commands

```shell
Usage: ggshield [OPTIONS] COMMAND [ARGS]...

Options:
  -c, --config-path FILE  Set a custom config file. Ignores local and global
                          config files.

  -v, --verbose           Verbose display mode.
  -h, --help              Show this message and exit.

Commands:
  install  Command to install a pre-commit hook (local or global).
  scan     Command to scan various contents.
  ignore   Command to permanently ignore some secrets.
```

## Scan command

`ggshield scan` is the main command for **ggshield**, it has a few config
options that can be used to override output behaviour.

```shell
Usage: ggshield scan [OPTIONS] COMMAND [ARGS]...

  Command to scan various contents.

Options:
  --show-secrets               Show secrets in plaintext instead of hiding
                               them.
  --exit-zero                  Always return a 0 (non-error) status code, even
                               if incidents are found.The env var
                               GITGUARDIAN_EXIT_ZERO can also be used to set
                               this option.
  --all-policies               Present fails of all policies (Filenames,
                               FileExtensions, Secret Detection).By default,
                               only Secret Detection is shown.
  -v, --verbose                Verbose display mode.
  -o, --output PATH            Route ggshield output to file.
  -b, --banlist-detector TEXT  Exclude results from a detector.
  --exclude PATH               Do not scan the specified path.
  --ignore-default-excludes    Ignore excluded patterns by default. [default:
                               False]
  --json                       JSON output results  [default: False]
  -h, --help                   Show this message and exit.

Commands:
  ci            scan in a CI environment.
  commit-range  scan a defined COMMIT_RANGE in git.
  docker        scan a docker image <NAME>.
  path          scan files and directories.
  pre-commit    scan as a pre-commit git hook.
  pre-push      scan as a pre-push git hook.
  pre-receive   scan as a pre-receive git hook.
  repo          scan a REPOSITORY's commits at a given URL or path.
```

`ggshield scan` has different subcommands for each type of scan:

- `CI`: scan each commit since the last build in your CI.

  `ggshield scan ci`

  No options or arguments

- `Commit Range`: scan each commit in the given commit range

  ```
  Usage: ggshield scan commit-range [OPTIONS] COMMIT_RANGE

    scan a defined COMMIT_RANGE in git.

    git rev-list COMMIT_RANGE to list several commits to scan. example:
    ggshield scan commit-range HEAD~1...
  ```

- `Path`: scan files or directories with the recursive option.

  ```
  Usage: ggshield scan path [OPTIONS] PATHS...

    scan files and directories.

  Options:
    -r, --recursive  Scan directory recursively
    -y, --yes        Confirm recursive scan
    -h, --help       Show this message and exit.
  ```

- `Pre-commit`: scan every changes that have been staged in a git repository.

  `ggshield scan pre-commit`

  No options or arguments

- `Repo`: scan all commits in a git repository.

  ```
  Usage: ggshield scan repo [OPTIONS] REPOSITORY

    scan a REPOSITORY at a given URL or path

    REPOSITORY is the clone URI or the path of the repository to scan.
    Examples:

    ggshield scan repo git@github.com:GitGuardian/ggshield.git

    ggshield scan repo /repositories/ggshield
  ```

- `Docker`: scan a Docker image after exporting its filesystem and manifest with the `docker save` command.

  ```
  Usage: ggshield scan docker [OPTIONS] IMAGE_NAME

    ggshield will try to pull the image if it's not available locally
  Options:
    -h, --help  Show this message and exit.
  ```

- `pypi`: scan a pypi package.

  ```
  ggshield scan pypi PACKAGE_NAME
  ```

  No options or arguments.

  Under the hood this command uses the `pip download` command to download the python package.
  You can use `pip` environment variables or configuration files to set `pip download` parameters as explained in [pip documentation](https://pip.pypa.io/en/stable/topics/configuration/#environment-variables)
  For example, you can set `pip` `--index-url` parameter by setting `PIP_INDEX_URL` environment variable.

- `archive`: scan an archive files.

  ```
  scan archive <PATH>
  ```

  No options or arguments.

## Install command

The `install` command allows you to use ggshield as a pre-commit or pre-push hook
on your machine, either locally or globally for all repositories.

You will find further details in the pre-commit/pre-push part of this documentation.

```shell
Usage: ggshield install [OPTIONS]

  Command to install a pre-commit or pre-push hook (local or global).

Options:
  -m, --mode [local|global]       Hook installation mode  [required]
  -t, --hook-type [pre-commit|pre-push]
                                  Type of hook to install
  -f, --force                     Force override
  -a, --append                    Append to existing script
  -h, --help                      Show this message and exit.
```

## Ignore command

The `ignore` command allows you to ignore some secrets.
For the time being, it only handles the `--last-found` option that ignore all secrets found by the last run `scan` command.
Under the hood, these secrets are added to the matches-ignore section of your local config file (if no local config file is found, a `.gitguardian.yaml` file is created).

Warning: Using this command will discard any comment present in the config file.

```shell
Usage: ggshield ignore

  Command to ignore all secrets found by the previous scan.

Options:
  -h, --help                 Show this message and exit.
  --last-found               Ignore all secrets found by last run scan
```

## Quota command

Show remaining quota of the workspace.

```
Usage: ggshield quota [OPTIONS]

  Command to show quotas overview.

Options:
  --json      JSON output results  [default: False]
  -h, --help  Show this message and exit.
```

Example:

```
❯ ggshield quota
Quota available: 9440
Quota used in the last 30 days: 560
Total Quota of the workspace: 10000
```

## API Status command

Show API status and version.

```
Usage: ggshield api-status [OPTIONS]

  Command to show api status.

Options:
  --json      JSON output results  [default: False]
  -h, --help  Show this message and exit.
```

Example:

```
❯ ggshield api-status
status: healthy
app-version: 1.27.0-rc.1
secrets-engine-version-version: 2.44.0
```

# Configuration

Configuration in `ggshield` follows a `global>local>CLI` configuration scheme.

Meaning options on `local` overwrite or extend `global` and options on CLI overwrite or extend local.

`ggshield` will search for a `global` config file in the user's home directory (example: `~/.gitguardian.yml` on Linux and `%USERPROFILE%\.gitguardian` on Windows).

`ggshield` will recognize as well a `local` config file in the user's working directory (example: `./.gitguardian.yml`).

You can also use the option `--config-path` on the main command to set another config file. In this case, neither `local` nor `global` config files will be evaluated (example: `ggshield --config-path=~/Desktop/only_config.yaml scan path -r .`)

A sample config file can be found at [.gitguardian.example](./.gitguardian.example.yml)

```yml
# Exclude files and paths by globbing
paths-ignore:
  - '**/README.md'
  - 'doc/*'
  - 'LICENSE'

# Ignore security incidents with the SHA256 of the occurrence obtained at output or the secret itself
matches-ignore:
  - name:
    match: 530e5a4a7ea00814db8845dd0cae5efaa4b974a3ce1c76d0384ba715248a5dc1
  - name: credentials
    match: MY_TEST_CREDENTIAL

show-secrets: false # default: false

# Set to true if the desired exit code for the CLI is always 0,
# otherwise the exit code will be 1 if incidents are found.
# the environment variable GITGUARDIAN_EXIT_ZERO=true can also be used toggle this behaviour.
exit-zero: false # default: false

# By default only secrets are detected. Use all-policies to toggle this behaviour.
all-policies: false # default: false

api-url: https://api.gitguardian.com # GITGUARDIAN_API_URL and GITGUARDIAN_URL environment variables will override this setting

verbose: false # default: false
```

_Notes_

Old configuration of `matches-ignore` with list of secrets is
deprecated but still supported :

```yml
# Ignore security incidents with the SHA256 of the occurrence obtained at output or the secret itself
matches-ignore:
  - 530e5a4a7ea00814db8845dd0cae5efaa4b974a3ce1c76d0384ba715248a5dc1
  - MY_TEST_CREDENTIAL
```

## Environment Variables

Some configurations on `ggshield` can be done through environment variables.

Environment variables will override settings set on your config file but will be overridden by command line options.

At startup, `ggshield` will attempt to load environment variables from different environment files in the following order:

- path pointed to by the environment variable `GITGUARDIAN_DOTENV_PATH`
- `.env` at your current work directory.
- `.env` at the root of the current git directory

Only one file will be loaded of the three.

Reference of current Environment Variables that affect `ggshield`:

```yaml
GITGUARDIAN_API_KEY: [Required] API Key for the GitGuardian API.

GITGUARDIAN_URL: Custom URL of the GitGuardian dashboard. The API URL will be inferred from it.

GITGUARDIAN_API_URL: (Deprecated use GITGUARDIAN_URL instead) Custom URL for the scanning API.

GITGUARDIAN_DONT_LOAD_ENV: If set to any value environment variables won't be loaded from a file.

GITGUARDIAN_DOTENV_PATH: If set to a path, `ggshield` will attempt to load the environment from the specified file.

GITGUARDIAN_TIMEOUT: If set to a float, `ggshield scan pre-receive` will timeout
after the specified value. Set to 0 to disable the timeout

GITGUARDIAN_MAX_COMMITS_FOR_HOOK: if set to an int, `ggshield scan pre-receive` and `ggshield scan pre-push`
will not scan more than the specified value of commits in a single scan.

GITGUARDIAN_CRASH_LOG: If set to True, ggshield will display a full traceback
when crashing
```

## On-premises configuration

GitGuardian shield can be configured to run on your on-premises dashboard, request an API key from your dashboard administrator.

You can modify your environment variables to include:

```shell
GITGUARDIAN_API_KEY=<GitGuardian API Key>
GITGUARDIAN_URL=<GitGuardian on-premise dashboard URL>
```

Alternatively to setting the `GITGUARDIAN_URL` environment variable, set the `dashboard-url` in your `.gitguardian.yaml`.

## Ignoring files

By default ggshield ignores certain files and directories.
This list can be found in [ggshield/core/utils.py](ggshield/core/utils.py) under `IGNORED_DEFAULT_PATTERNS`.

You can turn this feature with the flag `--ignore-default-excludes` or
the key `ignore-default-excludes` in your `.gitguardian.yaml`

```yml
#.gitguardian.yml
# Use default excluded vendors folders
ignore-default-excludes: false # default: false
```

```sh
ggshield scan --ignore-default-excludes path example_file.md
```

You can also add custom patterns to ignore by using the `--exclude` option or
the key `paths-ignore` in your `.gitguardian.yaml`

```yml
# .gitguardian.yml
# Exclude files and paths by globbing
paths-ignore:
  - '**/README.md'
  - 'doc/*'
  - 'LICENSE'
```

```sh
ggshield scan --exclude dir/subdir/** path -r dir
```

## Ignoring a secret

Useful for ignoring a revoked test credential or a false positive, there are three ways to ignore a secret with ggshield:

### In code

> ⚠ this will also ignore the secret in the GitGuardian dashboard.

Secrets can be ignored in code by suffixing the line with a `ggignore` comment.

Examples:

```py
def send_to_notifier() -> int:
  return send_slack_message(token="xoxb-23s2js9912ksk120wsjp") # ggignore
```

```go
func main() {
  high_entropy_test := "A@@E*JN#DK@OE@K(JEN@I@#)" // ggignore
}

```

### Through configuration

> ⚠ Your secret will still show up on the GitGuardian dashboard as potential incident.

You can use the [ignore command](#ignore-command) to ignore the last found secrets in your scan or directly add the ignore SHA that accompanies the incident or one of the secret matches to the [configuration file](#configuration)

> ⚠ A secret ignored on the GitGuardian dashboard will still show as a potential incident on ggshield.

## Ignoring a detector

> ⚠ Your secret will still show up on the GitGuardian dashboard as potential incident.

You can ignore a detector using the CLI option `-b` or `--banlist-detector` or through the configuration:

Examples:

```yaml
# .gitguardian.yaml
banlisted-detectors: # default: []
  - Generic Password
  - Generic High Entropy Secret
```

```sh
ggshield scan -b "Generic High Entropy Secret" path example_file.md
```

# Integration

## Pre-commit

### The pre-commit framework

In order to use **ggshield** with the [pre-commit](https://pre-commit.com/) framework, you need to do the following steps.

Make sure you have pre-commit installed:

```shell
$ pip install pre-commit
```

Create a `.pre-commit-config.yaml` file in your root repository:

```yaml
repos:
  - repo: https://github.com/gitguardian/ggshield
    rev: main
    hooks:
      - id: ggshield
        language_version: python3
        stages: [commit]
```

Then install the hook with the command:

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

Now you're good to go!

If you want to skip the pre-commit check, you can add `-n` parameter:

```shell
$ git commit -m "commit message" -n
```

Another way is to add SKIP=hook_id before the command:

```shell
$ SKIP=ggshield git commit -m "commit message"
```

### The global and local pre-commit hook

To install pre-commit globally (for all current and future repos), you just need to execute the following command:

```shell
$ ggshield install --mode global
```

It will do the following:

- check if a global hook folder is defined in the global git configuration
- create the `~/.git/hooks` folder (if needed)
- create a `pre-commit` file which will be executed before every commit
- give executable access to this file

You can also install the hook locally on desired repositories.
You just need to go in the repository and execute:

```shell
$ ggshield install --mode local
```

If a pre-commit executable file already exists, it will not be overridden.

You can force override with the `--force` option:

```shell
$ ggshield install --mode local --force
```

If you already have a pre-commit executable file and you want to use ggshield,
all you need to do is to add this line in the file:

```shell
$ ggshield scan pre-commit
```

If you want to try pre-commit scanning through the docker image:

```shell
$ docker run -e GITGUARDIAN_API_KEY -v $(pwd):/data --rm gitguardian/ggshield ggshield scan pre-commit
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `GITGUARDIAN_API_KEY` environment variable of your project or development environment.

## Pre-push

In case there are more than a 50 commits in a push the hook will be skipped.
The amount of commits to scan before skipping the hook can be configured by the key `max-commits-for-hook` in
a GitGuardian configuration file (for example: `.gitguardian.yaml`).

Pre-push hooks are executed just before `git push` sends data to the remote host.
It will pickup and scan the range of commits between the local ref and the origin ref.

If incidents are detected in this range the push will be cancelled.

### With the pre-commit framework

In order to use **ggshield** with the [pre-commit](https://pre-commit.com/) framework, you need to do the following steps.

Make sure you have pre-commit installed:

```shell
$ pip install pre-commit
```

Create a `.pre-commit-config.yaml` file in your root repository:

```yaml
repos:
  - repo: https://github.com/gitguardian/ggshield
    rev: main
    hooks:
      - id: ggshield-push
        language_version: python3
        stages: [push]
```

Then install the hook with the command:

```shell
$ pre-commit install --hook-type pre-push
pre-commit installed at .git/hooks/pre-push
```

### With the install command

To install the pre-push hook globally (for all current and future repos), you just need to execute the following command:

```shell
$ ggshield install --mode global -t pre-push
```

It will do the following:

- check if a global hook folder is defined in the global git configuration
- create the `~/.git/hooks` folder (if needed)
- create a `pre-push` file which will be executed before every commit
- give executable access to this file

You can also install the hook locally on desired repositories.
You just need to go in the repository and execute:

```shell
$ ggshield install --mode local -t "pre-push"
```

If a pre-commit executable file already exists, it will not be overridden.

You can force override with the `--force` option:

```shell
$ ggshield install --mode local --force  -t "pre-push"
```

Or you can append to the existing `pre-push` script with the `--append` option:

```shell
$ ggshield install --mode local --force  -t "pre-push"
```

Now you're good to go!

## Pre-receive

A pre-receive hook allows you to reject commits from being pushed to a git repository if they do not validate every check.
Refer to [our learning center](https://www.gitguardian.com/secrets-detection/secrets-detection-application-security#4) for more information.

You can find **ggshield**'s pre-receive hook samples in the [doc/pre-receive.sample](doc/pre-receive.sample) and [doc/pre-receive-docker.sample](doc/pre-receive-docker.sample).

**ggshield**'s pre-receive hook can be skipped if the developer passes the option `breakglass` to the git push.

For this setting to work the remote must have push options enabled. (`git config receive.advertisePushOptions true`).

Examples:

```sh
$ git push -o breakglass
$ git push --push-option=breakglass
```

### Install ggshield git pre-receive hook

1. This pre-receive hook requires the host machine to have python>=3.8 and pip installed
1. Install ggshield from pip: `pip install ggshield`
1. Copy [`pre-receive.sample`](doc/pre-receive.sample) to `.git/hooks/pre-receive` or to your provider's git hook directory:

   - [GitHub Enterprise](https://docs.github.com/en/enterprise-server@3.4/admin/policies/enforcing-policy-with-pre-receive-hooks/managing-pre-receive-hooks-on-the-github-enterprise-server-appliance)
   - [GitLab](https://docs.gitlab.com/ee/administration/server_hooks.html)

1. Do not forget to `chmod +x .git/hooks/pre-receive`
1. Either set an environment variable machine wide `GITGUARDIAN_API_KEY` or set it in the `.git/hooks/pre-receive` as instructed in the sample file.

**How do I add ignored matches and use a custom config in this pre-receive hook?**

- Create a `gitguardian.yaml` somewhere in the system. An example config file is available [here](.gitguardian.example.yml)
- Replace in the pre-receive hook
  ```shell
  ggshield scan pre-receive
  ```
  with:
  ```shell
  ggshield -c <INSERT path to gitguardian.yaml> scan pre-receive
  ```

### Install ggshield git pre-receive hook with docker

> For the pre-receive hook to work, the directory where the repositories are stored
> must also be mounted on the container.

1. This pre-receive hook requires the host machine to have docker installed.
1. Copy [**pre-receive-docker.sample**](doc/pre-receive-docker.sample) to `.git/hooks/pre-receive`
1. Do not forget to `chmod +x .git/hooks/pre-receive`
1. Either set an environment variable machine wide `GITGUARDIAN_API_KEY` or set it in the `.git/hooks/pre-receive` as instructed in the sample file.

## Docker

The GitGuardian Shield docker scanning tool (`ggshield scan docker`) is used to
scan local docker images for secrets present in the image's creation process
(`dockerfile` and build arguments) and in the image's layers' filesystem.

If the image is not available locally on the user's machine, GitGuardian shield
will attempt to pull the image using `docker pull <IMAGE_NAME>`.

## GitLab

> You may be interested in using GitGuardian's [GitLab integration](https://dashboard.gitguardian.com/settings/workspace/integrations/gitlab) to ensure full coverage of your GitLab projects as well as full git history scans and reporting.

Configuring GitLab pipelines to use **ggshield** is as simple as
adding a step to your project's pipeline:

```yaml
stages:
  - scanning

🦉 gitguardian scan:
  image: gitguardian/ggshield:latest
  stage: scanning
  script: ggshield scan ci
  variables:
    GIT_STRATEGY: clone
    GIT_DEPTH: 0
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `GITGUARDIAN_API_KEY` environment variable in your project settings.

> For ggshield to scan every commit in a merge request pipeline the CI
> must clone the full repository instead of just fetching the branch.
> The following snippet ensures this behavior.

```yml
variables:
GIT_STRATEGY: clone
GIT_DEPTH: 0
```

## GitHub

> You may be interested in using GitGuardian's [GitHub integration](https://dashboard.gitguardian.com/settings/workspace/integrations/github) to ensure full coverage of your GitHub projects as well as full git history scans and reporting.

**ggshield's** support of GitHub comes in the form of GitHub actions.

The action for this repository is hosted at [ggshield-action](https://github.com/GitGuardian/ggshield-action).

Configuring a GitHub workflow to use **ggshield** is as simple as
adding a step to your project's workflow:

```yaml
name: GitGuardian scan

on: [push, pull_request]

jobs:
  scanning:
    name: GitGuardian scan
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          fetch-depth: 0 # fetch all history so multiple commits can be scanned
      - name: GitGuardian scan
        uses: GitGuardian/ggshield-action@master
        env:
          GITHUB_PUSH_BEFORE_SHA: ${{ github.event.before }}
          GITHUB_PUSH_BASE_SHA: ${{ github.event.base }}
          GITHUB_PULL_BASE_SHA: ${{ github.event.pull_request.base.sha }}
          GITHUB_DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}
          GITGUARDIAN_API_KEY: ${{ secrets.GITGUARDIAN_API_KEY }}
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `GITGUARDIAN_API_KEY` secret in your project settings.

## BitBucket

> ⚠ BitBucket pipelines do not support commit ranges therefore only your latest commit in a pushed group or in a new branch will be scanned.

Configuring a BitBucket pipeline to use **ggshield** is as simple as
adding a step to your project's workflow:

```yml
pipelines:
  default:
    - step:
        image: gitguardian/ggshield:latest
        services:
          - docker
        script:
          - ggshield scan ci
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `GITGUARDIAN_API_KEY` environment variable in your project settings.

## Circle CI

Circle CI is supported in **ggshield** through [ggshield-orb](https://github.com/GitGuardian/ggshield-orb).

To add ggshield to your pipelines configure your `.circleci/config.yml` to add the ggshield orb:

```yaml
orbs:
  ggshield: gitguardian/ggshield

workflows:
  main:
    jobs:
      - ggshield/scan:
          name: ggshield-scan # best practice is to name each orb job
          base_revision: << pipeline.git.base_revision >>
          revision: <<pipeline.git.revision>>
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `GITGUARDIAN_API_KEY` environment variable in your project settings.

## Travis CI

To add ggshield to your pipelines configure your `.travis.yml` to add a ggshield scanning job:

```yml
jobs:
  include:
    - name: GitGuardian Scan
      language: python
      python: 3.8
      install:
        - pip install ggshield
      script:
        - ggshield scan ci
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `GITGUARDIAN_API_KEY` environment variable in your project settings.

- [Defining encrypted variables in .travis.yml](https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml)

## Jenkins

To add ggshield to your pipelines configure your `Jenkinsfile` to add a ggshield stage:

```groovy
pipeline {
    agent none
    stages {
        stage('GitGuardian Scan') {
            agent {
                docker { image 'gitguardian/ggshield:latest' }
            }
            environment {
                GITGUARDIAN_API_KEY = credentials('gitguardian-api-key')
            }
            steps {
                sh 'ggshield scan ci'
            }
        }
    }
}
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `gitguardian-api-key` credential in your project settings.

## Drone

To add ggshield to your pipelines configure your `.drone.yml` to add a ggshield stage:

```groovy
kind: pipeline
type: docker
name: default

steps:
- name: ggshield
  image: gitguardian/ggshield:latest
  commands:
  - ggshield scan ci
```

Drone CI integration handles only pull-request or merge-request events, push events are not handled.
Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `GITGUARDIAN_API_KEY` environment variable for your Drone CI workers.

## Azure Pipelines

> ⚠ Azure Pipelines does not support commit ranges outside of GitHub Pull Requests, therefore on push events in a regular branch only your latest commit will be scanned.
> This limitation doesn't apply to GitHub Pull Requests where all the commits in the pull request will be scanned.

To add ggshield to your pipelines configure your `azure-pipelines.yml` to add a ggshield scanning job:

```yml
jobs:
  - job: GitGuardianShield
    pool:
      vmImage: 'ubuntu-latest'
    container:
      image: gitguardian/ggshield:latest
      options: -u 0
    steps:
      - script: ggshield scan ci
        env:
          GITGUARDIAN_API_KEY: $(gitguardianApiKey)
```

Do not forget to add your [GitGuardian API Key](https://dashboard.gitguardian.com/api/v1/auth/user/github_login/authorize?utm_source=github&utm_medium=gg_shield&utm_campaign=shield1) to the `gitguardianApiKey` secret variable in your pipeline settings.

- [Defining secret variables in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch#secret-variables)

# Output

If no secrets or policy breaks have been found, the exit code will be 0:

```bash
$ ggshield scan pre-commit
```

If a secret or other issue is found in your staged code or in your CI,
you will have an alert giving you the type of policy break,
the filename where the policy break has been found and a patch
giving you the position of the policy break in the file:

```shell
$ ggshield scan pre-commit

🛡️  ⚔️  🛡️  2 policy breaks have been found in file production.rb

11 | config.paperclip_defaults = {
12 |     :s3_credentials => {
13 |     :bucket => "XXX",
14 |     :access_key_id => "XXXXXXXXXXXXXXXXXXXX",
                            |_____AWS Keys_____|

15 |     :secret_access_key => "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                                |_______________AWS Keys_______________|

16 |     }
17 | }
```

Lines that are too long are truncated to match the size of the terminal,
unless the verbose mode is used (`-v` or `--verbose`).

# Related open source projects

- [truffleHog](https://github.com/dxa4481/truffleHog)
- [gitleaks](https://github.com/zricethezav/gitleaks)
- [gitrob](https://github.com/michenriksen/gitrob)
- [git-hound](https://github.com/tillson/git-hound)
- [AWS git-secrets](https://github.com/awslabs/git-secrets)
- [detect-secrets](https://github.com/Yelp/detect-secrets)

# License

**GitGuardian shield** is MIT licensed.

# GitHub CLI Tools

A collection of simple Python CLI tools built using the GitHub API and the `requests` library.

## Installation

```bash
pip install -r requirements.txt
```

## Tools

### 1. GitHub Profile Fetcher

Fetch public GitHub profile information for a user.

Show all available details:

```bash
python3 git_profile.py NerfedAce
```

Show only specific fields:

```bash
python3 git_profile.py NerfedAce email name
```

Supported fields:

* email
* name
* location
* followers
* following

---

### 2. GitHub Repository Info Fetcher

Fetch repository information for a GitHub user.

Show the user's top repositories:

```bash
python3 git_repo.py NerfedAce
```

Show information for specific repositories:

```bash
python3 git_repo.py NerfedAce my-project practice_repo_2
```

Displays:

* Repository name
* Star count
* Description

## Requirements

* Python 3
* requests

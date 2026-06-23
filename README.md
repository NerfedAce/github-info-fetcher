# GitHub Info Fetcher

A simple Python CLI application that interacts with the GitHub REST API to fetch public profile information and repository details for any GitHub user.

Built using **Python** and the **requests** library, with **Docker** support for containerized execution.

---

## Features

### Profile Fetcher

- Fetch public GitHub profile information
- Display all profile details
- Display only selected fields

Supported fields:

- Name
- Email
- Location
- Followers
- Following

### Repository Fetcher

- List a user's repositories
- Fetch information for specific repositories
- Display:
  - Repository Name
  - Star Count
  - Description

---

## Project Structure

```
github-info-fetcher/
│
├── profile.py
├── repo.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/github-info-fetcher.git
cd github-info-fetcher
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Profile Fetcher

Display all available information:

```bash
python3 profile.py NerfedAce
```

Display only selected fields:

```bash
python3 profile.py NerfedAce name location followers
```

Example:

```
Name: John Doe
Location: India
Followers: 245
```

---

### Repository Fetcher

Display all repositories:

```bash
python3 repo.py NerfedAce
```

Display specific repositories:

```bash
python3 repo.py NerfedAce project-one project-two
```

Example:

```
Repository: github-info-fetcher
Stars: 12
Description: CLI tool for fetching GitHub information
```

---

## Docker

### Build the image

```bash
docker build -t github-info-fetcher .
```

### Run Profile Fetcher

```bash
docker run --rm github-info-fetcher profile.py NerfedAce
```

### Run Repository Fetcher

```bash
docker run --rm github-info-fetcher repo.py NerfedAce
```

---

## Requirements

- Python 3
- requests
- Docker (optional)

---

## Technologies Used

- Python
- GitHub REST API
- requests
- Docker
- Git

---


## License

This project is open source and available under the MIT License.

# Backup Cleaner

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Testing](#testing)

## About <a name = "about"></a>

This project delivers a container, that can be started and mapped to a path, where it deletes all files older than x amount of days, to cleanup old backup files. It's setup to only take files starting with backup, and ending with tar.gz.
The idea come from a Docker backup project, I have been using, where I found the cleanup solution not working in my setup.

## Getting Started <a name = "getting_started"></a>


### Prerequisites

to use this project, you need to have Docker installed to be able to run the container.

### Installing

Use it by running the folling, where LOCALSHARE is the folder and subfolders you want to have cleaned.

```bash
docker run --rm -v LOCALSHARE:/data -e DAYS_TRESHOLD='7' ghcr.io/rhjensen79/backup-cleaner:latest
```

## Usage <a name = "usage"></a>

I'm using Cronincle schelduler to run my container, using this [project](https://github.com/bluet/docker-cronicle-docker) but it's not limited to that.

It could also be run using a simpel Cron task.

## Testing

There is a makefile, you can use to build and test the container.

```bash
make build
```

Builds the container

```bash
make run
```

Runs the container, and maps it to ./dummy_folder

```bash
make test
```

Builds the container, runs a test script, to create 100 dumy files, and then runs the container, to remove all the files again.
Usefull for testing.
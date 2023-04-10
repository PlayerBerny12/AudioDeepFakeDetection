FROM nvidia/cuda:12.1.0-base-ubuntu20.04
RUN apt update && apt -y install zip bzip2 git python3 python3-venv && rm -rf /var/lib/apt/lists/*

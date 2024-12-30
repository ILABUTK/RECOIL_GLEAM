#!/bin/bash

# Check if a commit message was provided
if [ -z "$1" ]; then
  echo "Error: Commit message is required."
  echo "Usage: ./my_git_push.sh \"Your commit message\""
  exit 1
fi

git pull
# Assign the argument to a variable
commit_message=$1

git add .
git commit -m "$commit_message"
git push origin main

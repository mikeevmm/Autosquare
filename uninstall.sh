#!/bin/bash

echo "Removing autosquare link..."
if rm "$HOME/bin/autosquare"; then
    echo -e "\033[32mDone.\033[0m"
else
    echo "Something went wrong."
fi

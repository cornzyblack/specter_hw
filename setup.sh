#!/bin/bash

if [[ -f "chromedriver" ]]
then
    echo "This file exists on your filesystem."
else
   mkdir chromedriver
fi


if [[ "$OSTYPE" == "linux-gnu" ]]; then
        echo "lINUX"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "MAC"
elif [[ "$OSTYPE" == "cygwin" ]]; then
        echo "POSIX compatibility layer and Linux environment emulation for Windows"
elif [[ "$OSTYPE" == "msys" ]]; then
        echo "Lightweight shell and GNU utilities compiled for Windows (part of MinGW)"
elif [[ "$OSTYPE" == "win32" ]]; then
        echo "I'm not sure this can happen."
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        echo "I'm not sure this can happen."
else
    echo "here"
fi

# Delay quit time when pressing `cmd+Q` on MacOS

## Description

This script modifies the behavior of the `cmd+Q` keyboard shortcut on MacOS to delay the quit action. By introducing a configurable delay, it helps prevent accidental application closures.

The script is based on this post: [macos - Hold Cmd-Q to Quit as a system-wide action? - Ask Different](https://apple.stackexchange.com/questions/349075/hold-cmd-q-to-quit-as-a-system-wide-action){:target="_blank"}

## Prerequisites

- Hammerspoon installed: [check it out here](https://www.hammerspoon.org/){:target="_blank"}

## Usage

1. Move the two `.lua` files into the folder `.hammerspoon/`
2. Configure the quit timer (Optional) in the script `cmdq.lua`
3. Run hammerspoon and keep it running

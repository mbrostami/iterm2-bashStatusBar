import subprocess
import iterm2

BASH_CONST="BASH"
async def main(connection):
    knobs = [iterm2.StringKnob("Bash Command", "BASH_SCRIPT", "", BASH_CONST)]
    component = iterm2.StatusBarComponent(
        short_description='Bash command executor',
        detailed_description='Run bash command and print the output',
        exemplar='#!/bin/bash',
        update_cadence=5,
        identifier='engineering.dane.iterm-components.sentinel',
        knobs=knobs,
    )

    @iterm2.StatusBarRPC
    async def bash_coroutine(knobs):
        bashCommand = knobs[BASH_CONST]
        output = subprocess.getoutput(bashCommand)
        return output

    await component.async_register(connection, bash_coroutine)

iterm2.run_forever(main)

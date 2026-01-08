# Virtual Machine Setup

## overview

A virtual machine is used to provide a stable and always-on environment for running the automated reporting process.  
This avoids relying on a local machine, which may be turned off or unavailable.

The VM enables:
- continuous execution
- unattended background tasks
- system-level scheduling via cron


## reproducibility and portability

The automation does not depend on a specific machine.  
Any Linux system equipped with:
- Python
- cron
- access to the project repository

can reproduce the same setup by following this documentation.

All execution logic is fully defined in the versioned source code.


## execution model

The virtual machine does not introduce additional business logic.  
Its role is limited to executing the scripts provided in the repository.

The complete codebase is tracked on GitHub, while the VM acts only as a runtime environment.


## system and environment setup

The following steps are performed on the virtual machine:
- cloning the GitHub repository
- creating a Python virtual environment
- installing the required dependencies
- configuring the cron scheduler

Only scripts that are versioned in the repository are executed by the VM.

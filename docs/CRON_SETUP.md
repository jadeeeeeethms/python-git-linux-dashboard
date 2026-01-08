# Cron setup – Daily report automation

## objective

The purpose of this setup is to automate the generation of a daily financial report using the scripts/daily_report.py script.
Rather than running the script manually, the report is scheduled to run automatically at a fixed time each day via a Linux cron job. This guarantees consistent execution and ensures that results are produced in a reliable and reproducible manner.


## def

Cron is a native Linux scheduling service that enables commands or scripts to be executed automatically at predefined times.
It operates independently of any user session, making it well suited for background tasks such as daily data processing or automated report generation.
Since cron configurations are system-specific, they are not tracked in the Git repository. However, the script triggered by the cron job is versioned to ensure transparency, traceability, and reproducibility.

## executed script

The cron job executes the following script:
cron/run_daily_report.sh


This shell script:
- activates the Python virtual environment
- runs the `scripts/daily_report.py` script
- redirects execution logs to a persistent file

Using a dedicated shell script avoids issues related to environment variables
and makes the cron execution more reliable.


## configuration

On the Linux virtual machine, the following cron entry was added:

0 20 * * * /home/alexiaroulet/python-git-linux-dashboard/cron/run_daily_report.sh


This configuration means:
- execution every day
- at 20:00 (Europe/Paris timezone)
- using the VM environment


## logs and outputs

Execution logs are stored in:
logs/daily_report.log


Generated reports are stored in:
reports/


This setup allows monitoring the execution of the cron job and facilitates
debugging in case of errors.

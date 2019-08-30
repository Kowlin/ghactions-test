import os
import json
import logging
from github import Github


logger = logging.getLogger("Action")  # TODO, change this.
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "[{asctime}] [{levelname}] {name}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Logger Active.")

with open(os.environ["GITHUB_EVENT_PATH"]) as event_file:
    event_json = json.load(event_file)

if "GITHUB_REPOSITORY" not in os.environ:
    logger.error("GitHub repository not found")
    exit(1)
if "GITHUB_TOKEN" not in os.environ:
    logger.error("GitHub token not found.")
    exit(1)

if "ACTION_DEBUG" in os.environ:  # Set debugging level if present.
    logger.setLevel(logging.DEBUG)
    logger.debug(f"--- DEBUG INFORMATION | {os.environ['GITHUB_WORKFLOW']} ---")
    logger.debug(f"Token present: {'GITHUB_TOKEN' in os.environ}")
    logger.debug(f"Repository: {os.environ['GITHUB_REPOSITORY']}")
    logger.debug(f"Event json log: {os.environ['GITHUB_EVENT_PATH']}")
    logger.debug("---")
    logger.debug(event_json)

client = Github(os.environ["GITHUB_TOKEN"], api_preview=True)

exit(0)

import os
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


if "ACTION_DEBUG" in os.environ:  # Set debugging level if present.
    logger.setLevel(logging.DEBUG)

if "GITHUB_REPOSITORY" not in os.environ:
    logger.error("GitHub repository not found")
    exit(1)
if "GITHUB_TOKEN" not in os.environ:
    logger.error("GitHub token not found.")
    exit(1)

logger.info("Running logger")
logger.debug("Running in Debug")

client = Github(os.environ["GITHUB_TOKEN"], api_preview=True)

logger.info(client.get_user().login)

exit(0)

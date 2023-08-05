from mkdocs.plugins import BasePlugin
from jinja2 import Template, DebugUndefined
import httpx


class GitLatestVersionTagPlugin(BasePlugin):

    def on_page_markdown(self, markdown, *, config, **kwargs):
        latest_version_tag = self.get_latest_version_tag(config)
        template = Template(markdown, undefined=DebugUndefined)
        return template.render({'git_latest_version_tag': latest_version_tag})

    @staticmethod
    def get_latest_version_tag(config):
        """ Function to get the latest tag from the git repository which matches
        the configured regex for the version tag format."""
        repo_name = config.get("repo_name", None)
        assert repo_name is not None

        return httpx.get(f"https://api.github.com/repos/{repo_name}/releases/latest").json().get("tag_name", "unknown")

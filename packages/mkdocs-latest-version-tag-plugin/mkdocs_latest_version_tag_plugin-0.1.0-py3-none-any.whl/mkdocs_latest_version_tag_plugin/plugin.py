from mkdocs.plugins import BasePlugin
from git import Git, Repo
from jinja2 import Template, DebugUndefined

import re


class GitLatestVersionTagPlugin(BasePlugin):

    def __init__(self) -> None:
        self.git: Git = Git()
        self.repo: Repo | None = None

    def on_page_markdown(self, markdown, page, *args, **kwargs):
        print(page.file.abs_src_path)
        latest_version_tag = self.get_latest_version_tag(page.file.abs_src_path)
        template = Template(markdown, undefined=DebugUndefined)
        return template.render({'git_latest_version_tag': latest_version_tag})

    def get_latest_version_tag(self, page_path: str):
        """ Function to get the latest tag from the git repository which matches
        the configured regex for the version tag format."""

        self.repo = Repo(page_path, search_parent_directories=True)
        assert not self.repo.bare

        matching_tags = list()

        for tag in self.repo.tags:
            pattern = r"v\d+\.\d+\.\d+"
            regex = re.compile(pattern)
            result: re.Match | None = regex.search(tag.name)

            if isinstance(result, re.Match):
                matching_tags.append(result.group())

        if len(matching_tags):
            matching_tags.sort()
            return matching_tags.pop()

        return "unknown"

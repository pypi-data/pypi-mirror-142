from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
from os import device_encoding, walk, makedirs, PathLike
from pathlib import Path
from os.path import abspath, dirname, join
from configparser import ConfigParser
from shutil import copytree
import sass
from http.server import HTTPServer, SimpleHTTPRequestHandler
from .logger import get_logger
from os import getcwd
from .filters.to_markdown import to_markdown
from dataclasses import dataclass
import json


@dataclass
class Page:
    base_name: str
    rel_path: PathLike
    template: Template
    variables: dict


class SiteConfig:
    """ Class to create a ConfigParser object

    """
    def __init__(self) -> None:
        self.logger = get_logger(__name__)
        self.root_dir = getcwd()
        self.config_filename = join(self.root_dir, "site.cfg")
        self.default_section = "site"
        self.defaults = {
            "SITE_NAME": "My Site",
            "SITE_URL": "/",
            "STATIC_DIR": "static",
            "STATIC_OUTPUT_DIR": "static",
            "OUTPUT_DIR": "output",
            "SASS_ENABLED": True,
            "SASS_DIR": "sass",
            "CSS_OUTPUT_DIR": "css",
            "TEMPLATES_DIR": "templates",
            "CONTENT_DIR": "content",
            "JINJA_EXTENSION": ".j2",
            "MARKDOWN_EXTENSION": ".md",
            "MARKDOWN_TEMPLATE": "markdown.j2",
        }

    @staticmethod
    def __list_converter() -> list:
        """ Converts a list variable value to a python list.

        :return: list
        """
        return []

    def read_config_file(self) -> dict:
        """ Reads a config file from `site.cfg`.

        :return: A dictionary of config variables
        """
        cp = ConfigParser(converters={"list": self.__list_converter})
        cp.optionxform = lambda option: option
        cp[self.default_section] = self.defaults
        cp.read(self.config_filename)
        self.logger.debug(cp.items('site'))
        return dict(cp.items('site'))


class SiteCreator:
    """ Renders the current directory into the output directory.

    """
    def __init__(self) -> None:
        self.logger = get_logger(__name__)
        self.root_dir = getcwd()
        self.config = SiteConfig().read_config_file()
        self.logger.debug(self.config)
        makedirs(self.config['OUTPUT_DIR'], exist_ok=True)
        self.render_queue = []
        self.config['SITEMAP'] = []
        self.env = Environment(
            loader=FileSystemLoader(
                [
                    join(self.root_dir, self.config['TEMPLATES_DIR']),
                    join(self.root_dir, self.config['CONTENT_DIR'])
                ]
            ),
            autoescape=select_autoescape(['html', 'xml']),
        )
        self.env.filters.update({"to_markdown": to_markdown})

    def discover(self) -> list:
        """ Walks the CONTENT_DIR and creates adds them to the render queue.

        :return: list - A list of pages to render.
        """
        pages_dir = join(self.root_dir, self.config['CONTENT_DIR'])
        for root, dirs, files in walk(pages_dir):
            for f in files:
                rel_path = Path(root[len(pages_dir) + 1:])
                base_name = f[:f.rfind('.')]
                ext = f[f.rfind('.'):]
                menu_item = (
                    base_name.title(),
                    f"{join(rel_path, base_name)}.html"
                )
                self.config['SITEMAP'].append(menu_item)
                page_vars = {}
                template_path = str(f)
                if ext == self.config['MARKDOWN_EXTENSION']:
                    template_path = self.config['MARKDOWN_TEMPLATE']
                    self.logger.debug(f"template_path: {template_path}")
                    with open(join(root, f), 'r', encoding='utf-8') as m:
                        text = m.read()
                        page_vars = {"md_content": text}
                template = self.env.get_template(template_path)
                self.logger.debug(f"ext: {ext}")
                self.logger.debug(f"base_name {base_name}")
                self.logger.debug(f"rel_path {rel_path}")
                self.logger.debug(f"template {template}")
                self.logger.debug(f"variables {page_vars}")
                self.render_queue.append(Page(
                    base_name=base_name,
                    rel_path=rel_path,
                    template=template,
                    variables=page_vars
                ))
        return self.render_queue

    def copy_static(self) -> None:
        """ Copies the static site data from STATIC_DIR to the output
        directory.

        :return: Path of the output directory
        """
        self.logger.info("Copying static content...")
        return copytree(
            join(self.root_dir, self.config['STATIC_DIR']),
            join(
                self.root_dir,
                self.config['OUTPUT_DIR'],
                self.config['STATIC_OUTPUT_DIR']
            ),
            dirs_exist_ok=True,
        )

    def create_page(
            self, page: Page
    ) -> None:
        """Renders the render_queue queued by discover.

        :param page: Page
        :return:
        """
        output_dir = join(
            self.root_dir,
            self.config['OUTPUT_DIR'],
            page.rel_path
        )
        makedirs(output_dir, exist_ok=True)
        output_file = join(output_dir, f'{page.base_name}.html')
        self.logger.debug(f"Writing template: {page.template}")
        page.variables.update(self.config)
        with open(output_file, 'w+') as o:
            o.write(page.template.render(page.variables))

    def compile_sass(self) -> None:
        """ Compiles SASS to CSS in the OUTPUT_DIR.

        :return: None
        """
        css_output_dir = join(
            self.root_dir,
            self.config['OUTPUT_DIR'],
            self.config['STATIC_OUTPUT_DIR'],
            self.config['CSS_OUTPUT_DIR'],
        )
        sass.compile(
            dirname=(
                join(self.root_dir, self.config['SASS_DIR']),
                css_output_dir
            ),
            output_style='compressed'
        )

    def create_site(self) -> None:
        """ Discovers and renders pages, copies static data, and compiles CSS.

        :return: None
        """
        self.discover()
        self.copy_static()
        if self.config['SASS_ENABLED']:
            self.compile_sass()
        for page in self.render_queue:
            self.logger.debug(f"Adding page: {page.base_name}")
            self.create_page(page)

    def start_dev_server(self) -> None:
        """ Starts a development server.
        This server should not be run in production.

        :return: None
        """
        dev_port = 8088
        self.logger.info(f"Starting server on http://localhost:{dev_port}")
        server_address = ('', dev_port)
        httpd = HTTPServer(server_address, DevHandler)
        httpd.serve_forever()


class DevHandler(SimpleHTTPRequestHandler):
    """ Class to handle simple http dev server.

    """
    def __init__(self, *args, **kwargs) -> None:
        self.logger = get_logger(__name__)
        self.config = SiteConfig().read_config_file()
        super().__init__(*args, directory=self.config['OUTPUT_DIR'], **kwargs)

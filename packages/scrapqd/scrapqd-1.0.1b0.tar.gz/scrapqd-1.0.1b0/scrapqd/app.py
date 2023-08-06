import pathlib
import logging

from flask import Flask, redirect, render_template_string
from graphql_server.flask import GraphQLView

from scrapqd.gql.schema import schema
from scrapqd.settings import config

logger = logging.getLogger("init")


def get_gql_template(template_path=None):
    """Gets graphql html template text from template.html"""
    if not template_path:
        path = pathlib.Path(__file__)
        cur_path = path.parent.absolute()
        template_path = f"{cur_path}/gql/template.html"
    with open(template_path, encoding="utf-8") as f:
        template = f.read()
    return template


def load_graphql_url(name, app, template=None, redirect_root=True):
    """Registers graphql ui api view and redirects root to ui"""

    template_html = get_gql_template(template)
    app_name = name.lower()
    url = f"/{app_name}"
    logger.info("Registering scrapqd as %s", url)
    app.add_url_rule(
        url,
        view_func=GraphQLView.as_view(
            f"{app_name}",
            schema=schema,
            graphiql=True,
            graphiql_html_title=name,
            graphiql_template=template_html
        )
    )

    if redirect_root:
        @app.route("/")
        def _root():
            return redirect(url)


def register_sample_page(name, app):
    """Registers sample page url"""

    name = name.lower()

    @app.route(f"/{name}/sample_page")
    def sample_page():
        path = pathlib.Path(__file__)
        cur_path = path.parent.absolute()
        template_path = f"{cur_path}/_static/sample.html"
        with open(template_path, encoding="utf-8") as f:
            template = f.read()
        return render_template_string(template)


def register_scrapqd(app,
                     template=None,
                     register_sample_url=True,
                     redirect_root=True):
    """System add ScrapQD url to the Flask App and registers system defined crawlers."""
    name = config.APP_NAME
    if register_sample_url:
        register_sample_page(name, app)
    load_graphql_url(name, app,
                     template=template,
                     redirect_root=redirect_root)


def create_app(name):
    """Creates flask app with ping api"""
    app_name = name.lower()
    app = Flask(app_name)

    @app.route("/ping")
    def ping():
        return 'ok!', 200

    return app


def config_app():
    """Creates flask app and registers graphql view"""
    app = create_app(config.APP_NAME)
    app.url_map.strict_slashes = False
    register_scrapqd(app)
    return app


def run(port=5000, host="127.0.0.1", debug=False, reload=False):
    """runs flask server with graphql ui"""
    app = config_app()
    app.run(host=host, port=port, debug=debug, use_reloader=reload)


if __name__ == "__main__":
    run()

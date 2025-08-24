import reflex as rx

config = rx.Config(
    app_name="web_project",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    stylesheets=[
        "assets/fonts/fonts.css",
    ],
)
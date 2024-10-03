from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Chip Design FastHTML",
        Div(
            H2("Welcome to Chip Design FastHTML"),
            P("A collaborative web app for chip design using open source EDA tools."),
            Button("Create New Project", hx_post="/new_project", hx_target="#content"),
            id="content"
        ),
        Div(
            H3("Features"),
            Ul(
                Li("Real-time collaboration"),
                Li("Integration with OpenLane2"),
                Li("Schematic capture"),
                Li("Layout design"),
                Li("Design rule checking")
            )
        ),
        Div(
            H3("Getting Started"),
            Ol(
                Li("Create an account or log in"),
                Li("Start a new project or join an existing one"),
                Li("Use the integrated tools to design your chip"),
                Li("Collaborate with team members in real-time"),
                Li("Export your design for fabrication")
            )
        )
    )

serve()

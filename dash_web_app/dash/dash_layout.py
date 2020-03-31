html_layout = \
    '''<!DOCTYPE html>
        {% extends "layout.html" %}

        {% block body %}

        {{ super() }}

        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>

        <nav>
          <a href="/"><i class="fas fa-home"></i> Home</a>
          <a href="/dash_app/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
        </nav>

        {%app_entry%}

        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    '''

# <html>
#     <body>
#         <nav>
#           <a href="/"><i class="fas fa-home"></i> Home</a>
#           <a href="/dash_app/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
#         </nav>
#         {%app_entry%}
#         <footer>
#             {%config%}
#             {%scripts%}
#             {%renderer%}
#         </footer>
#     </body>
# </html>'''

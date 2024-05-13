from dash import html, dcc


app_layout = html.Div(
    [
        # Banner ------------------------------------------------------------
        html.Div(
            [
                html.A(
                    [
                        html.Img(
                            src="/assets/web.png",
                            alt="research intelligence"
                        ),
                        html.H3("research analytics")
                    ],
                    href="https://jhupiterz.notion.site/Welcome-to-research-intelligence-\
                          a36796f418b040f6ade944f9c54e87cb",
                    target='_blank',
                    className="logo-banner",
                ),
                html.Div(
                    [
                        html.A(
                            "Contribute",
                            href="https://github.com/jhupiterz/research-analytics",
                            target='_blank',
                            className="doc-link"
                        ),
                        html.A(
                            "Documentation",
                            href="https://github.com/jhupiterz/research-analytics/blob/main/README.md",
                            target='_blank',
                            className="doc-link"
                        ),

                    ],
                    className="navbar"
                ),
            ],
            className="banner",
        ),

        # Search bar ------------------------------------------------------------
        html.Div(
            [
                html.H1(id='topic', children=[]),
                html.Div(
                    [
                        html.Img(
                            src='/assets/loupe.png',
                            className="loupe-img",
                        ),
                        dcc.Input(
                            id='search-query',
                            type='text',
                            placeholder="Search for keywords (e.g. \"carbon nanotubes\")",
                            debounce=True,
                            spellCheck=True,
                            inputMode='latin',
                            name='text',
                            autoFocus=False,
                            minLength=1, maxLength=60,
                            autoComplete='off',
                            disabled=False,
                            readOnly=False,
                            size='60',
                            n_submit=0,
                        ),
                    ],
                    className="search-bar",
                ),
            ],
            className="search-wrapper"
        ),

        dcc.Store(id='store-initial-query-response', storage_type='memory'),
        dcc.Store(id='store-references-query-response', storage_type='memory'),

        # Main content ----------------------------------------------------------
        html.Div(id='start-page', children=[], className='main-body'),

        # Footer ----------------------------------------------------------------
        html.Footer(
            [
                html.P(
                    [
                        "Built with ",
                        html.A("Plotly Dash", href="https://plotly.com/dash/", target="_blank")
                    ],
                ),
                html.P(
                    [
                        "Powered by ",
                        html.A("Semantic Scholar", href="https://www.semanticscholar.org/", target="_blank")
                    ],
                ),
            ]
        ),
    ],
    className="app-layout",
)

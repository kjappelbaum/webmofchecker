import dash_bootstrap_components as dbc
import dash_html_components as html
from pymatgen import Structure
from mofchecker import MOFChecker

OK_COLOR = "#C7F6D8"
BAD_COLOR = "#FCAFAF"


def run_check(s, fmt="cif"):
    print(s)
    structure = Structure.from_dict(s, fmt=fmt)

    mofcheckerinstance = MOFChecker(structure)
    result = mofcheckerinstance.get_mof_descriptors()
    print(result)
    rows = []
    for k, v in result.items():
        if k not in ["name", "path", "density"]:
            id = "table_{}".format(k)
            if v == mofcheckerinstance.check_expected_values[k]:
                color = OK_COLOR
            else:
                color = BAD_COLOR
            tooltip = dbc.Tooltip(mofcheckerinstance.check_descriptions[k], target=id,)

            rows.append(
                html.Tr(
                    [
                        html.Td(
                            [
                                k.replace("_", " ").replace("oms", "open metal site"),
                                tooltip,
                            ],
                            id=id,
                        ),
                        html.Td(str(v)),
                    ],
                    style={"background-color": color},
                )
            )

    table = (
        dbc.Table(
            [
                html.Thead(
                    [
                        html.Td("Check name", style={"font-weight": "bold"}),
                        html.Td("Check result", style={"font-weight": "bold"}),
                    ]
                ),
                *rows,
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            style={"width": "93%", "margin-left": "5%"},
        ),
    )

    return table

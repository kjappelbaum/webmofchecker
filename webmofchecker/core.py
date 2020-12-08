import re
import dash_bootstrap_components as dbc
import dash_html_components as html
from pymatgen import Structure
from mofchecker import MOFChecker
from . import __version__

OK_COLOR = "#C7F6D8"
BAD_COLOR = "#FCAFAF"



def _run_check(structure):
    mofcheckerinstance = MOFChecker(structure)
    result = mofcheckerinstance.get_mof_descriptors()

    return mofcheckerinstance, result


def run_check_api(s, fmt="cif"):
    structure = Structure.from_str(s, fmt=fmt)

    mofcheckerinstance, result = _run_check(structure)

    output_dict = {
        "checkResults": result,
        "expectedResults": mofcheckerinstance.check_expected_values,
        "checkDescriptions": mofcheckerinstance.check_descriptions,
        "apiVersion": __version__,
    }

    return output_dict


def run_check(s, fmt="cif"):
    structure = Structure.from_dict(s, fmt=fmt)
    mofcheckerinstance, result = _run_check(structure)
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

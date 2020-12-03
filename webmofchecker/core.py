import dash_bootstrap_components as dbc
import dash_html_components as html
from pymatgen import Structure
from mofchecker import MOFChecker


def run_check(s, fmt="cif"):
    print(s)
    structure = Structure.from_dict(s, fmt=fmt)

    mofcheckerinstance = MOFChecker(structure)
    result = mofcheckerinstance.get_mof_descriptors()
    print(result)
    rows = []
    for k, v in result.items():
        if k not in ['name', 'path']:
            rows.append(html.Tr([html.Td(k.replace('_', ' ')), html.Td(str(v))]))

    table = (
        dbc.Table(
            [html.Thead([html.Td("Check name"), html.Td("Check result")]), *rows],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            style={"width": "93%", "margin-left": "5%"},
        ),
    )

    return table

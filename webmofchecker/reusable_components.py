import dash_html_components as html
import base64


def _merge(a, b):  # pylint:disable=invalid-name
    return dict(a, **b)


def _omit(omitted_keys, d):  # pylint:disable=invalid-name
    return {k: v for k, v in d.items() if k not in omitted_keys}


def b64_to_str(content):
    data = content.encode("utf8").split(b";base64,")[1]
    decoded = base64.decodebytes(data)
    return decoded.decode("utf-8")


def Card(children, **kwargs):  # pylint: disable=invalid-name
    return html.Section(
        children,
        style=_merge(
            {
                "padding": 10,
                "marginBottom": "1em",
                "marginTop": 0,
                "borderRadius": 5,
                "width": "100%",
                "border": "thin lightgrey solid",
                # Remove possibility to select the text for better UX
                "userSelect": "none",
                "-moz-user-select": "none",
                "-webkit-user-select": "none",
                "-msUserSelect": "none",
            },
            kwargs.get("style", {}),
        ),
        **_omit(["style"], kwargs),
    )

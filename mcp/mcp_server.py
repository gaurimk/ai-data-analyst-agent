TOOLS = {}


def register_tool(name, func):

    TOOLS[name] = func


def run_tool(name, *args):

    if name in TOOLS:
        return TOOLS[name](*args)

    else:
        return "Tool not found"
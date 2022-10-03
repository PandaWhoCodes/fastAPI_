from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")


def get_return_template(
    template_name: str, request: Request, context: dict
) -> Jinja2Templates:
    """
    returns the template with the context and the request supplied
    Args:
        template_name (str): name of the template file that needs to be used from the templates folder
        request (Request): The request context
        context (dict): actual context parameters that you want to pass to the jinja template

    Returns:
        Jinja2Templates: template to be rendered with the context
    """
    context["request"] = request
    return templates.TemplateResponse(name=template_name, context=context)


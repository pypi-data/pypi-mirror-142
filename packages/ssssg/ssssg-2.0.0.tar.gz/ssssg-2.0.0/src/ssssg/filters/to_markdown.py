from jinja2 import pass_eval_context
from markdown import markdown


@pass_eval_context
def to_markdown(context, text):
    return markdown(text)

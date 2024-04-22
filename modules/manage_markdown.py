from markdown import markdown
import re

def convert_md_to_html(text):
    html = markdown(text)
    return html


def convert_md_to_text(md_text):
    html = markdown(md_text)
    
    plain_text = re.sub('<[^<]+?>', '', html)
    
    return plain_text
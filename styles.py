from rich.panel import Panel
from rich.style import Style
from rich.text import Text
import re


narrator_style = Style(italic=True, color="#DAA520")
all_caps_style = Style(color="#e8c15f", bold=True)
ancient_latin_style = Style(color="#e87d5f", italic=True, bold=True)

ancient_latin_words = [
    "imperium", "senatus", "forum", "caesar", "legion", "gladius",
    "pax", "victoria", "aqua", "terra", "fili", "mi", "roman",
    "publius", "vergilius", "maro", "poetarum", "praeceptor",
    "Scipii", "Publius", "Cornelius", "Scipio", "Africanus", "Julians",
    "Aeneas", "Julius", "Caesar", "Augustus", "Claudii", "Tiberius",
    "Caligula", "Flavians", "Vespasian", "Titus", "Vesuvius",
    "Colosseum", "Dī bene vertant", "Scipius", "Julian", "Claudius",
    "Flavius", "Valē"
]


def narrator_print(text, console):
    text_object = Text(text, style=narrator_style)
    text_object.highlight_regex(r'\b[A-Z]+\b', style=all_caps_style)
    for word in ancient_latin_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        text_object.highlight_regex(pattern, style=ancient_latin_style)
    console.print(Panel(
        text_object,
        title="Publius Vergilius Maro",
        subtitle="Poetarum Praeceptor",
        title_align="left",
        subtitle_align="left"
    ))

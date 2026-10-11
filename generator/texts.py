"""Textos visibles del perfil, en español.

Todos los rótulos, títulos y frases que aparecen en las SVGs generadas se
centralizan aquí para mantener un único punto de traducción.
"""

MONTHS = (
    "Ene",
    "Feb",
    "Mar",
    "Abr",
    "May",
    "Jun",
    "Jul",
    "Ago",
    "Sep",
    "Oct",
    "Nov",
    "Dic",
)

STAR_LABELS = ("estrella", "estrellas")
REPO_LABELS = ("repositorio", "repositorios")

CONTRIB_TITLE = "Contribuciones"
CONTRIB_CAPTION = "contribuciones en el último año"
CONTRIB_EMPTY = "Todavía no hay datos de contribuciones"
CONTRIB_LABELS = {
    "stars": STAR_LABELS,
    "prs": ("solicitud de cambios", "solicitudes de cambios"),
    "issues": ("incidencia", "incidencias"),
    "repos": REPO_LABELS,
}
CONTRIB_BUSIEST = "semana más activa: {text}"
CONTRIB_PEAK = "{value} en la semana del {day} de {month}"
CONTRIB_LEVEL = "{value} a la semana"

LANG_TITLE = "Lenguajes y stack declarado"
LANG_HEADING = "Lenguajes en los repositorios públicos, por bytes de código"
LANG_EMPTY = "Todavía no hay datos de lenguajes"
LANG_DECLARED = "Stack declarado: {declared}"
LANG_AND = "y "

FEATURED_TITLE = "Proyectos destacados"
FEATURED_EMPTY = "Todavía no hay proyectos destacados"
FEATURED_UPDATED = "actualizado {month}"

GALAXY_TITLE = "Galaxia de {name}"
GALAXY_EMPTY = "Todavía no hay repositorios públicos."
GALAXY_BY_AREA = "por área de enfoque: {arms}"
GALAXY_LOOSE = "{n} fuera de cualquier área"
GALAXY_BRIGHTEST = "más brillante: {name} con {n} {stars}"

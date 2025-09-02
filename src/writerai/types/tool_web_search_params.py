# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolWebSearchParams"]


class ToolWebSearchParams(TypedDict, total=False):
    chunks_per_source: int
    """Only applies when `search_depth` is `advanced`.

    Specifies how many text segments to extract from each source. Limited to 3
    chunks maximum.
    """

    country: Literal[
        "afghanistan",
        "albania",
        "algeria",
        "andorra",
        "angola",
        "argentina",
        "armenia",
        "australia",
        "austria",
        "azerbaijan",
        "bahamas",
        "bahrain",
        "bangladesh",
        "barbados",
        "belarus",
        "belgium",
        "belize",
        "benin",
        "bhutan",
        "bolivia",
        "bosnia and herzegovina",
        "botswana",
        "brazil",
        "brunei",
        "bulgaria",
        "burkina faso",
        "burundi",
        "cambodia",
        "cameroon",
        "canada",
        "cape verde",
        "central african republic",
        "chad",
        "chile",
        "china",
        "colombia",
        "comoros",
        "congo",
        "costa rica",
        "croatia",
        "cuba",
        "cyprus",
        "czech republic",
        "denmark",
        "djibouti",
        "dominican republic",
        "ecuador",
        "egypt",
        "el salvador",
        "equatorial guinea",
        "eritrea",
        "estonia",
        "ethiopia",
        "fiji",
        "finland",
        "france",
        "gabon",
        "gambia",
        "georgia",
        "germany",
        "ghana",
        "greece",
        "guatemala",
        "guinea",
        "haiti",
        "honduras",
        "hungary",
        "iceland",
        "india",
        "indonesia",
        "iran",
        "iraq",
        "ireland",
        "israel",
        "italy",
        "jamaica",
        "japan",
        "jordan",
        "kazakhstan",
        "kenya",
        "kuwait",
        "kyrgyzstan",
        "latvia",
        "lebanon",
        "lesotho",
        "liberia",
        "libya",
        "liechtenstein",
        "lithuania",
        "luxembourg",
        "madagascar",
        "malawi",
        "malaysia",
        "maldives",
        "mali",
        "malta",
        "mauritania",
        "mauritius",
        "mexico",
        "moldova",
        "monaco",
        "mongolia",
        "montenegro",
        "morocco",
        "mozambique",
        "myanmar",
        "namibia",
        "nepal",
        "netherlands",
        "new zealand",
        "nicaragua",
        "niger",
        "nigeria",
        "north korea",
        "north macedonia",
        "norway",
        "oman",
        "pakistan",
        "panama",
        "papua new guinea",
        "paraguay",
        "peru",
        "philippines",
        "poland",
        "portugal",
        "qatar",
        "romania",
        "russia",
        "rwanda",
        "saudi arabia",
        "senegal",
        "serbia",
        "singapore",
        "slovakia",
        "slovenia",
        "somalia",
        "south africa",
        "south korea",
        "south sudan",
        "spain",
        "sri lanka",
        "sudan",
        "sweden",
        "switzerland",
        "syria",
        "taiwan",
        "tajikistan",
        "tanzania",
        "thailand",
        "togo",
        "trinidad and tobago",
        "tunisia",
        "turkey",
        "turkmenistan",
        "uganda",
        "ukraine",
        "united arab emirates",
        "united kingdom",
        "united states",
        "uruguay",
        "uzbekistan",
        "venezuela",
        "vietnam",
        "yemen",
        "zambia",
        "zimbabwe",
    ]
    """Localizes search results to a specific country.

    Only applies to general topic searches.
    """

    days: int
    """For news topic searches, specifies how many days of news coverage to include."""

    exclude_domains: SequenceNotStr[str]
    """Domains to exclude from the search. If unset, the search includes all domains."""

    include_answer: bool
    """Whether to include a generated answer to the query in the response.

    If `false`, only search results are returned.
    """

    include_domains: SequenceNotStr[str]
    """Domains to include in the search. If unset, the search includes all domains."""

    include_raw_content: Union[Literal["text", "markdown"], bool]
    """Controls how raw content is included in search results:

    - `text`: Returns plain text without formatting markup
    - `markdown`: Returns structured content with markdown formatting (headers,
      links, bold text)
    - `true`: Same as `markdown`
    - `false`: Raw content is not included (default if unset)
    """

    max_results: int
    """Limits the number of search results returned. Cannot exceed 20 sources."""

    query: str
    """The search query."""

    search_depth: Literal["basic", "advanced"]
    """Controls search comprehensiveness:

    - `basic`: Returns fewer but highly relevant results
    - `advanced`: Performs a deeper search with more results
    """

    stream: bool
    """Enables streaming of search results as they become available."""

    time_range: Literal["day", "week", "month", "year", "d", "w", "m", "y"]
    """
    Filters results to content published within the specified time range back from
    the current date. For example, `week` or `w` returns results from the past 7
    days.
    """

    topic: Literal["general", "news"]
    """The search topic category.

    Use `news` for current events and news articles, or `general` for broader web
    search.
    """

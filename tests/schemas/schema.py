from voluptuous import PREVENT_EXTRA, Schema

resource = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

support = Schema(
    {
        "url": str,
        "text": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

single_resource_schema = Schema(
    {
        "data": resource,
        "support": support,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


resource_list_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [resource],
        "support": support
    },
    extra=PREVENT_EXTRA,
    required=True
)
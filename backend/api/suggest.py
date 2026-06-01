from fastapi import APIRouter
from fastapi import Query

from core.trie_store import (
    trie,
    handle_frequency
)

router = APIRouter(
    prefix="/suggest",
    tags=["Suggestions"]
)


@router.get("/")
async def suggest_handles(
    prefix: str = Query(..., min_length=1)
):

    matches = trie.search_prefix(
        prefix=prefix,
        limit=50
    )

    matches.sort(
        key=lambda handle: handle_frequency.get(
            handle,
            0
        ),
        reverse=True
    )

    return {
        "prefix": prefix,
        "suggestions": matches[:5]
    }
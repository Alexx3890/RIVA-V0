"""Built-in RAG Knowledge Retrieval Tools for Orchestration."""

import asyncio
import logging
from orchestration.tools.registry import tool

logger = logging.getLogger(__name__)


@tool(name="query_knowledge_base", category="knowledge", description="Query indexed RAG knowledge base for documents, policies, curricula, and institutional data.")
def query_knowledge_base(query: str) -> str:
    """Queries the local RAG knowledge base synchronously."""
    if not query or not query.strip():
        return "Please provide a valid search query."
    try:
        from rag_knowledge.service import query_rag
        return asyncio.run(query_rag(query.strip()))
    except Exception as e:
        logger.error(f"Error querying knowledge base: {e}")
        return f"Error querying knowledge base: {str(e)}"

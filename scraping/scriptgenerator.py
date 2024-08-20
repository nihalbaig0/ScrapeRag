"""
Basic example of scraping pipeline using ScriptCreatorGraph
"""
from scrapegraphai.graphs import ScriptCreatorGraph
from scrapegraphai.utils import prettify_exec_info
# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = {
    "llm": {
        "api_key": "API Key",
        "model": "gpt-4",  # Specify the model for the llm
        "temperature": 0,  # Set temperature parameter for llm
    },
    # "embeddings": {
    #     "model": "ollama/nomic-embed-text",
    #     "temperature": 0,
    #     "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    # },
    "library": "beautifoulsoup",
    #"verbose": True,
    #"headless": False,
}

# ************************************************
# Create the ScriptCreatorGraph instance and run it
# ************************************************

smart_scraper_graph = ScriptCreatorGraph(
    #prompt="List me all the news with their description.",
    prompt="List all the outgoing links from this webpage",
    # also accepts a string with the already downloaded HTML code
    source="https://garlandtx.new.swagit.com/views/213",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))
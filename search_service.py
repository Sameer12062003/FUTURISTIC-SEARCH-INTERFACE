from tavily import TavilyClient

def get_urls(query):
     tavily = TavilyClient(api_key="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")
     response = tavily.search(query=query, search_depth="advanced")
     return [result['url'] for result in response['results']]
# from duckduckgo_search import DDGS
#
# def get_urls(query , region , safesearch , max_results):
#      results = DDGS().text(query, region=region, safesearch=safesearch, max_results=max_results)
#      return [result['href'] for result in results]
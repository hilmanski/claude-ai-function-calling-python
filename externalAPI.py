import anthropic
import time
import os
import serpapi

# measure time
start_time = time.time()

def get_search_result(query):
    client = serpapi.Client(api_key=os.getenv("SERPAPI_API_KEY"))
    results = client.search({
        'q':query,
        'engine':"google",
    })

    if 'answer_box' not in results:
        return "No answer box found"
    
    return results['answer_box']

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    tools=[
        {
            "name": "get_search_result",
            "description": "A function that take a search query from the sentence and search the answer from Google.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string"
                    }
                },
                "required": ["query"]
            }
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "What's the weather in new York today"
        }
    ]
)

if message.stop_reason != "tool_use":
    print("End... No tool used")
    exit()

# Only continue when tools needed
dataFromCustomFunction = None
if message.stop_reason == "tool_use":
    tool_params = message.content[1].input
    tool_name = message.content[1].name
    
    # call available tool function
    if tool_name == "get_search_result":
        result = get_search_result(tool_params["query"])
        # limit the response to 1000 characters only
        if len(str(result)) > 1000:
            result = str(result)[:1000] + "..."
        
        dataFromCustomFunction = result


# Request a chat response from the assistant
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Answer to the customer in a nice way " + dataFromCustomFunction
        }
    ]
)

print(response.content[0].text)

# measure time
print("--- %s seconds ---" % (time.time() - start_time))

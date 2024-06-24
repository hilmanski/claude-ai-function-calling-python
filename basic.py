import anthropic
import time

# measure time
start_time = time.time()

def score_checker(score):
    if score > 0.5:
        return "Pass"
    else:
        return "Fail"

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    tools=[
        {
            "name": "score_checker",
            "description": "A function that takes the score provided and return the results.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "score": {
                        "type": "string"
                    }
                },
                "required": ["score"]
            }
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "I got the result. My score is 0.4 last night"
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
    if tool_name == "score_checker":
        result = score_checker(float(tool_params["score"]))
        dataFromCustomFunction = result
        print(result)


# Request a chat response from the assistant
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Answer to the customer. The customer exam status is " + dataFromCustomFunction
        }
    ]
)

print(response.content[0].text)

# measure time
print("--- %s seconds ---" % (time.time() - start_time))

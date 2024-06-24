# About
Running Claude AI with external API using function calling. 

Reference:  
- Step-by-step tutorial: [Function calling using Claude AI Blog post](https://serpapi.com/blog/connecting-claude-ai-to-the-internet-using-function-calling)
- [Claude AI function calling documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)

## How to run this project

Create a virtual env
```
python -m venv claude-env
```

Activate the virtual env with:
- On macOS or Linux, source claude-env/bin/activate
- On Windows, claude-env\Scripts\activate

Install package:
pip install anthropic

Export API Key:
- macoS/Linux: export ANTHROPIC_API_KEY='your-api-key-here'
- Windows: setx ANTHROPIC_API_KEY "your-api-key-here"

Run:
```
python3 basic.py
```

## Run Claude AI + SerpApi
Install SerpApi package
```
pip isntall serpapi
```

Export the API Key (make sure to register at serpapi.com and grab your API key from the dashboard):
```
export SERPAPI_API_KEY=YOUR_REAL_API_KEY
```

Run the sample file
```
python3 externalAPI.py
```
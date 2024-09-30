import os
import ssl
from dotenv import load_dotenv
import certifi
from openai import OpenAI
from supabase import create_client, Client

import asyncio
import aiohttp

# Load environment variables and set up SSL
load_dotenv()
os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Create a queue to manage the flow of processed videos
processed_queue = asyncio.Queue()

'''
TEST_URLS = [
    "https://www.youtube.com/watch?v=6u4JVz7iQTY&t=55s"
]
# Initialize clients and models
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
for url in TEST_URLS:
        result = supabase.table('videos').select('url').eq('url', url).execute()
        print(result)
'''
supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
with open('./t.mp3', 'rb') as f:
    supabase.storage.from_("videostore").upload(file=f,path='./t.mp3', file_options={"content-type": "audio/mpeg"})

'''
async def test(prompt):
    try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"},
                    json={
                        "model": "gpt-4",
                        "messages": [
                            {"role": "system", "content": "You are an AI assistant that analyzes video transcripts to find engaging and potentially valuable content."},
                            {"role": "user", "content": prompt}
                        ],
                        "temperature": 0.8,
                    }
                ) as response:
                    result = await response.json()
                    content = result['choices'][0]['message']['content']
                    print(content)
    except Exception as e:
            print(e)

asyncio.run(test("What is the meaning of life?"))
'''

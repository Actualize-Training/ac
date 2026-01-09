from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
audio_model = OpenAI()

TOOLS = [
    {"type": "web_search"},
    {"type": "image_generation"},
    {
        "type": "function",
        "name": "write_to_file",
        "description": """Writes content to a file. It returns True or False depending on success.""",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": { "type": "string" },
                "content": { "type": "string" },
            },
            "required": ["filename", "content"],
        },
    },
    {
        "type": "function",
        "name": "create_audio",
        "description": "Uses speech-to-text technology to converts a podcast script (string) into an audio mp3 podcast.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The mp3 file name.",
                },
                "script": {
                    "type": "string",
                    "description": "A podcast script read by a single host.",
                }
            },
            "required": ["filename", "script"],
        },
    },
]

def write_to_file(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def create_audio(filename, script, style):
    # Uses OpenAI text-to-speech model: https://platform.openai.com/docs/guides/text-to-speech
    #
    # Example style:
    # "You are a podcast host."
    # Or, add more detail:
    # """Persona: You are a newscaster.
    #    Delivery: Crisp and articulate, with measured pacing.
    #    Tone: Objective and neutral, confident and 
    #          authoritative, conversational yet formal."""
    with audio_model.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="marin", # You can change the voice! See the docs
        instructions=style,
        input=script
    ) as response:
        response.stream_to_file(filename)
    
    return True


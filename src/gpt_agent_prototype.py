from openai import OpenAI
import json


# The functions that could be used by GPT:

def get_weather(location):
    print(f"Getting weather for {location}...\n")
    location = location.lower()
    if "paris" in location:
        return "20° Celsius"
    if "london" in location:
        return "15° Celsius"
    if "hamburg" in location:
        return "10° Celsius"
    return "Unknown temperature"


def send_email(receiver, subject, body=""):
    print(f"Sending email to {receiver}: Subject: {subject}, Body: {body}\n")
    return "Email sent successfully"


def execute_tool_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    if name == "send_email":
        return send_email(**args)
    raise ValueError(f"Unknown function name: {name}")


# Tools definition:

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                }
            },
            "required": ["location"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "send_email",
        "description": "Send an email to a given receiver.",
        "parameters": {
            "type": "object",
            "properties": {
                "receiver": {
                    "type": "string",
                    "description": "Email address e.g. example@example.com"
                },
                "subject": {
                    "type": "string",
                    "description": "The subject of the email"
                },
                "body": {
                    "type": "string",
                    "description": "The body of the email"
                },
            },
            "required": ["receiver", "subject"],
            "additionalProperties": False,
        },
    },
]

# Main script:

def get_gpt_response(messages, tools):
    response = CLIENT.responses.create(
        model=MODEL,
        input=messages,
        tools=tools    
    )
    # print_response_debug(response)
    return response


def print_response_debug(response):
    print("---------------------------------------------------")
    try:
        response_dict = response.to_dict()
    except AttributeError:
        response_dict = response.__dict__
    print(json.dumps(response_dict, indent=2, ensure_ascii=False))
    print("---------------------------------------------------")


def print_gpt_messages(response, messages):
    if not response:
        print("- No response from GPT -\n")
        return
    elif not response.output:
        print("- No response output from GPT -\n")
        return

    function_call_count = 0

    for item in response.output:
        if item.type == "function_call":
            function_call_count += 1

            tool_call = item

            name = tool_call.name
            try:
                args = json.loads(tool_call.arguments)
            except json.JSONDecodeError:
                print(f"Error decoding arguments for function call {name}")
                continue

            result = execute_tool_function(name, args)

            messages.append(tool_call)
            messages.append({
                "type": "function_call_output",
                "call_id": tool_call.call_id,
                "output": str(result)
            })

        else:
            message_for_user = response.output_text or ""
            print(f"{message_for_user}\n")


    if function_call_count > 0:
        response = get_gpt_response(messages, tools)
        print_gpt_messages(response, messages)


# The OpenAI() client automatically reads the environment variable OPENAI_API_KEY (see .bashrc file)!
CLIENT = OpenAI()
MODEL = "gpt-4.1-mini-2025-04-14"


def start_chat():
    print("Welcome to the GPT Chatbot! Please ask your questions. Type 'exit' to quit.\n")

    messages = []
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        print()

        messages.append({"role": "user", "content": user_input})

        response = get_gpt_response(messages, tools)
        print_gpt_messages(response, messages)


if __name__ == "__main__":
    start_chat()


from django.shortcuts import render
import requests
from datetime import datetime

def form(request):
    time = datetime.now().strftime("%H:%M:%S")
    return render(request,'home.html', {'time': time})

def story(request):
    import os
    import openai
    import wandb

    openai.api_key = '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'
    name = ""
    topic = ""
    audience = ""
    keyword = ""

    idea = f"Topic:{topic} create a list of 10 questions {name} highlighting {keyword} told to {audience} \nThousand words {topic} story:"

    gpt_prompt = idea

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= gpt_prompt,
    temperature=0.8,
    max_tokens=600,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0
    )
    data = response['choices'][0]['text']
    return render(request, 'home.html',{'data': data})

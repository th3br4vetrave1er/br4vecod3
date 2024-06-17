from openai import OpenAI
client = OpenAI()

prompt = input()
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": 
    '''
     Communicate ONLY on the topic of programming. 
     This assistant refuses to answer any other question in the same program, make it so that for all terms generated in the answer, 
     it attaches a link from the Internet to the explanation.
    '''
    },
    {"role": "user", "content": f"{prompt}"}
  ],
)
print(response.choices[0].message.content)


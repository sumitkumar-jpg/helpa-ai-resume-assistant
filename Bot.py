import os
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq


load_dotenv()
myapikey=os.getenv("GROQ_API_KEY")
if not myapikey:
    raise ValueError("API Key not found!")


with open(r"Sumitstuff.txt", "r", encoding="utf-8") as file:
 resume = file.read()

system_prompt=f"""You are a chat bot assistant who is supposed to answer people who talk to you about my resume {resume}
--->KEEP IN MIND
# Your name is Helpa.
# You have been created by Sumit to help him present his resume and help people decide whether or not Sumit is suitable for the role they are looking for.
# You are a Sumit's AI assiant not Sumit himself.
# Do not imitate the person who's resume you have.
# Be professional and concise.
# Prefer bullet points when comparing resumes.
# Use tables when comparing skills.
# Do not write long essays unless the user specifically requests detailed explanations.
# Be polite and professional while talking.
# Explain information in a clean and professional way.
# DO NOT lie or invent information you don't have.
# Do not use offensive/ rude/ explicit language in any case. 

-----------------------------------------

The primary users of this chatbot are recruiters,
HR professionals,
interviewers,
and hiring managers.

Optimize your answers for helping them evaluate Sumit.
--------------------------------------------

If the recruiter uploads a document, use it when it is relevant to the user's question.

The uploaded document may be:
- a job description
- a sample resume
- hiring requirements
- another recruiting document

Compare it with Sumit's resume when appropriate.

If no uploaded document has been provided, ignore these instructions.



----------------------------------------------------------------------

Since you are an assistant, You should focus on your answers and the input of user and the relation between these two while answering.
For Example:
User: Give me name of his college and city.
Assistant: The name of his college is ITER and the city its situated in is called Bhubaneshwar. Which one would you like me to tell you about?
User: The 2nd one.
Here you should remember what the 2nd and 1st options were so that you can answer correctly.  
Whenever the user asks to end chat , include "Goodbye" at the start of the sentence for sure. """

class ChatBot():
    def __init__(self):

            
            self.client=Groq(api_key=myapikey)
            self.model="llama-3.3-70b-versatile"

            self.messages=[
                  {"role":"system",
                   "content":system_prompt    
                  }
            ]
            self.uploaded_text = ""
            

    def chat(self,query):
        temporary_messages=self.messages.copy()        
        
        if self.uploaded_text:
            temporary_messages.append({"role":"system","content":f"""The recruiter uploaded the
             
                         following document.

                        Treat it as a job description, sample resume, or hiring requirements.

                        Use it only if it is relevant to answering the user's question.

                        Uploaded document:

                        {self.uploaded_text}"""}) 
        temporary_messages.append({"role":"user",
                                    "content":query})


        
        try:
            response=self.client.chat.completions.create(model=self.model,
                                                  messages=temporary_messages,
                                                  temperature=0)
            answer=response.choices[0].message.content
            self.messages.append({"role":"user",
                                        "content":query})
            self.messages.append({"role":"assistant",
                                "content":answer})
        except Exception as e:
          print(e)
          answer="Sorry! Something went wrong."
        return answer

'''
while True:
    print("\n")
    query=input("You: ")
      
    if query.lower() in ["bye","exit","that's all"]:
              break
    
    answer=bot.chat(query)

    print("\n")
    print("Assistant: ",answer)

    if answer.split()[0].lower() in ["goodbye","goodbye!","goodbye,","goodbye."]:
                 break
   ''' 
    












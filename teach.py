import os
import API_KEY
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = API_KEY.OPENAI_API_KEY

ALDA_LANG_RULE = """You are a musician as well as a technologist who is well versed in programming. 
Now you've been asked to learn a new language called Alda, which allows you to create music as if you were programming. 
I will now tell you its rules:
1.The alda program usually starts with (tempo! number), which is stating the tempo of the music as this number.
2.Next, the instrument is usually specified, e.g. "piano:", which means that the music will be played on a piano. Other instruments supported are: acoustic-guitar, cello, flute, violin, etc.
3.Immediately after that, comes the part of the notes. Let me illustrate the main features of this program.
a) The default is quarter notes, which means that you type "c d e f", which represents a measure that has four quarter notes: C, D, E and F.
b) The ">" symbol means “go up to the next octave.”, for example: "f d e > c", the music will continue upwards in the C major scale.
c) Sharps and flats can be added to a note by appending + or -
d) You can even have double flats/sharps: such as "f++", which equals "g"
e) By default, notes in Alda are quarter notes. You can set the length of a note by adding a number after it. The number represents the note type, e.g. 4 for a quarter note, 8 for an eighth, 16 for a sixteenth, etc.
f) Rests in Alda work just like notes; they’re kind of like notes that you can’t hear. A rest is represented as the letter r.
g) You can use dotted notes, too. Simply add one or more .s onto the end of a note length.
h) You can add note durations together using a tie, which in Alda is represented as a tilde ~.
i) If a line starts with #, it means this line is a code comment.
Now, you probably know the basic programming language."""

TEST_PROMOPT = ALDA_LANG_RULE + """Could you please tell me what the following paragraph means:
{alda_code}
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["alda_code"],
    template=TEST_PROMOPT,
)
llm = OpenAI(temperature=0.9)

chain = LLMChain(llm=llm, prompt=prompt)

if __name__ == "__main__":
    print("Let's test Alda language learning!")
    while True:
        print("Human:")
        question = input()
        print("AI:")
        print(chain.run(question))
# Teach-Show-Consult
**Teach** ChatGPT to learn [Alda](https://github.com/alda-lang/alda) language, **Show** it the superb code, then **Consult** it on how to create music.

You can read [my post](https://mazzzystar.github.io/2023/03/03/teach-show-consult-gpt/) for a more detailed explanation.

## 1. Teach ChatGPT to learn `Alda` language
In this step, all I have to do is to use Prompt Engineering to give ChatGPT as many syntax rules as possible for the `Alda` language.
```python
ALDA_LANG_RULE = """You are a musician as well as a technologist who is well versed in programming. 
Now you've been asked to learn a new language called Alda, which allows you to create music as if you were programming. 
I will now tell you its rules:
1.The alda program usually starts with (tempo! number), which is stating the tempo of the music as this number.
2.Next, the instrument is usually specified, e.g. "piano:", which means that the music will be played on a piano. Other instruments supported are: acoustic-guitar, cello, flute, violin, etc.
3.Immediately after that, comes the part of the notes. Let me illustrate the main features of this program.
a) The default is quarter notes, which means that you type "c d e f", which represents a measure that has four quarter notes: C, D, E and F.
b) The ">" symbol means...
```

Let's test to see how much it has learned:
```python
>>> python teach.py
Let's test Alda language learning!
Human:
c d e+ f-
AI:

This is a measure of four quarter notes written in the key of C Major. The notes are C, D, E-sharp, and F-flat.
Human:
c d > e4 f8
AI:

This paragraph of code represents a measure of music that begins at the C major scale and moves up one octave to E. 
The first two notes are quarter notes (C and D), and the third note is an eighth note (E). The last note is a quarter note (F).
```

## 2. Show ChatGPT some works written by humans
Here I'm using [alda/examples](https://github.com/alda-lang/alda/tree/master/examples) to show some subtle code examples for ChatGPT to learn from.
```python
python show.py # will generate a `vectorstore.pkl` file from all .alda files.
```

## 3. Consult with ChatGPT to create your melody

```python
>>> python consult.py
Let's consult the music master!
You:
c d8 > g
Music Master:


(tempo! 120)
piano:
c4 d8 > g4 c4. <g4~4. >c4. d4~4. c4. <g4~4. >c4. d4~4. c8 r d e g b2~12 > d12 g | d8 r < b4~8~ > d8 < {b > d g}4 | 
g8 r f+4 f {e_ g b}4 | g8 r f+4 f {e_ g b}4 | (quant 40) > d4 (quant 90) e-4~8 e8 d- c | < b_ > d4~ f8 < b_4 > c | 
< b_8 > (ff) d4~ e8 (f) c2 | < a-2. > c4 < a2~ f b_2 > (mf) c8 c4~ d8 | < a-2 r8 > c4~ d8 | < a-2 r8 f4~ (p) g8 | 
(pp) a_16~ b~ a_~ b_ (p) > c~

[INFO] Notes saved to: output.alda
```

## Let's listen!

https://user-images.githubusercontent.com/6824141/222706396-6b73c35c-3974-477a-bb3e-0c3f2e40717e.mov



## Have Fun!
This repo is only for fun!
You can change the `data` or `learning task` to whatever you like. 

Tell me if you've created other interesting things inspired by this repo:)


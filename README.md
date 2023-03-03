# compose-inspiration
A LangChain + ChatGPT + Alda based AI composing inspiration tool.


## 1.Teach Chat-GPT `Alda` language
```bash
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

## 2.Show Chat-GPT some human writing examples
Here I'm using [alda/examples](https://github.com/alda-lang/alda/tree/master/examples) to make context.
```bash
python show.py # will generate a `vectorstore.pkl` file from all .alda files.
```

## 3.Consult Chat-GPT to expand your notes
```bash
>>> python consult.py
Let's consult music master!
You:
 c d8 > g
Music Master:
c d8 > g
(tempo! 120)
piano:
c d8 > g e4 d c8 | < b4 > c d8 | < a4 b > c8 | < g4 r8 r4 | > c8 < g > c < b a | b f b a g f+ a f+ a f+ d+ f+ d+ f+ a f+ 
a f+ o3 g f+ e g f+ g a f+ g f+ e d c < b a g o2 f+ > c d c d c d c < f+ > c d c d c d c o2 g b > f e f < b > f < b g b > 
f e f < b > f < b o2 g > c e d e c e c < g > c e d e c e c o2 g > f+ > c < b > c < f+ > c < f+ < g > f+ > c < b > c < f+ > 
c < f+ o2 g > d b a b g f+ e d c < b a g f+ e d o2 c+ a > e f+ g e f+ g < c+
```

## Have Fun
You can change the `data` or `learning task` to whatever you like. Tell me if you've created other interesting things inspired by this repo:)


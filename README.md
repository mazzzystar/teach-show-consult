# compose-inspiration
**Teach** ChatGPT to learn [Alda](https://github.com/alda-lang/alda) language, **Show** it the superb code, then **Consult** it on how to create music.


## 1. Teach Chat-GPT to learn `Alda` language
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

## 2. Show Chat-GPT some works written by humans
Here I'm using [alda/examples](https://github.com/alda-lang/alda/tree/master/examples) to make context.
```bash
python show.py # will generate a `vectorstore.pkl` file from all .alda files.
```

## 3. Consult Chat-GPT to create your music
```bash
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

## Have Fun!
You can change the `data` or `learning task` to whatever you like. Tell me if you've created other interesting things inspired by this repo:)


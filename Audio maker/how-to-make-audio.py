from gtts import gTTS #import 

text = "Hello Everyone ! Here is Muhammad Abubakar .Iam a Data scientist and exploring new skills with Zoological background .My Goal is to combine Zoology with Ai "

Audio =gTTS(text=text,lang="en") #syntax 

Audio.save("Voice.mp3") 

print("Audio Save successfully !")
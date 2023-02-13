Steps to setup

Install Python3
Create Virtual Environment and activate it
For example with: 
python -m myvenv .myvenv 
then run 
(Windows) myvenv\Scripts\activate.bat
(Linux and MacOS) source myenv/bin/activate

Install dependencies using pip:

pip install speechrecognition

pip install pyttsx3

pip install wikipedia

pip install wolframalpha

pip install pygame

pip install openai

# If using google cloud text-to-speech
pip3 install --user --upgrade google-cloud-texttospeech

Follow the instructions on the Google cloud site or the channel video to setup authentication and enable the API

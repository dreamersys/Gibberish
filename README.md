## Inspiration
As international students, public speaking is one of the hardest challenges we face. Often we stutter on words and speak too fast when we are nervous. That is where we first got the idea. We then took it one step further by implementing object detection so we can also give feedback on the body movement and implementing sentiment analysis! 

## What it does
When the start button is pressed, the software starts recording the user's voice then extract the voice and store it as a text file. Meanwhile, the computer will process the webcam feed and gives feedback to the user of his or her movements. The system will give back feedback scores according to the algorithm based on body movement, voice loudness, number of consecutively repeated words, speech to text recognition, and speech sentiment analysis. 

## How we built it
We choose python as our develop language and used various API provided by Google Inc. We used our own trained Google Tensorflow machine learning API to construct our body movement detection. After being able to recognize different body parts like arms and head, we had designed an algorithms to calculate the speed of the different body movement and frequency to give back reliable judgment. 

We also used Google's speech-to-text API to record users' speeches in order to provide a precise text file for us to analyze. We further analyzed the text to detect common mistake that people tend to make while giving speeches. We mainly focused on repetition of words and phrases.

In addition, we also used Google's natural-language-processing API to analyze the overall sentiment of the speech given by speaker. This gives us the ability to determine if the speaker spoke in a positive, neutral, or negative attitude.

Lastly, we used Python's pyaudio and matplotlib library to collect and construct instantaneous wave / amplitude forms for the speakers to have a good visualization of their voice loudness. We also designed a scoring schemes for the speakers to be able to compare and understand the collected data and improve overtime.

## Challenges we ran into
1. Threading: None of the group member have prior experience in threading. However, the goal of our project specifically needs threading since we were trying to compute / collect several sets of data at the same time.

2. Merging different part of the function into one program: We were not clear enough about how to merge the different part of the program in terms of sharing computing and graphing resources with most efficiency.

3. Improving efficiency and accuracy of AI that we used: We did not have enough time to train our Tensorflow AI to have the same accuracy level as we expected. And for the other APIs that we used, we have no access to the source code, so improving accuracy and decreasing computing usage was something that we couldn't really control.

## Accomplishments that we're proud of
We're quite proud of that we did data analyzing on not only image, but also voices and texts. The intense usage of Google's APIs and the adaptability that we showed through deploying different method to suit our needs are the biggest takeaways and what made us felt most proud of.

## What we learned
We learned that threading is a really important field that we need to focus on in the future when developing program that has features of preforming multiple calculation or operations at the same time. Also, we learned that there are a lot of very powerful and useful APIs out there for us to use. These APIs could be integrated into our program and widen the usage of our product. The experience that we had working with various APIs also reminds us again the importance of designing good user interface.

## What's next for Gibberish
There are nearly no limitation for future expansion of Gibberish. The first we can do is again make good use of Google APIs like Firestore to store all the user data online for review and compare. Along with OSIsoft's data analysis API for examining common errors between users so as to make warning early. We can also implement a ranking system to keep our users engaged over time by rewarding them, and email users who have not been using it much. We can perhaps implement some kind of grammar to check the user's grammar and while streaming their input. Last but not least, by integrating the Natural Language API, the software can better tell where to emphasize and where the user needs more physical expressions.

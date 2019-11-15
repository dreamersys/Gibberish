from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six


def analyze_overall_speech_sentiment(input_file_name):

    attitude_file = open("./Output Files/Attitude.txt", "w")

    score_total = 0
    num_sentiments = 0

    with open(input_file_name) as f:
        while True:
            cur_line = f.readline()
            score = sample_analyze_sentiment(cur_line)
            score_total += score
            num_sentiments += 1

            if not cur_line:
                break

    score_result = score_total / num_sentiments

    if score_result <= -0.1:
        sentiment = "Overall, you expressed NEGATIVE attitude in speech."
    elif score_result >= 0.1:
        sentiment = "Overall, you expressed POSITIVE attitude in speech"
    else:
        sentiment = "Overall, you expressed NEUTRAL attitude in speech."

    attitude_file.write("1) If Score <= 0.1, it is negative attitude.\n")
    attitude_file.write("2) If -0.1 < Score < 0.1 and , it is negative attitude.\n")
    attitude_file.write("3) If Score >= 0.1, it is positive attitude.\n\n\n")
    attitude_file.write("Your score is: " + str(score_result) + "\n")
    attitude_file.write(sentiment)
    return score_result


def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment


    return sentiment.score

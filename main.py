from job_advert.job_advert import JobAdvert
from prompts.job_ad_questions import JobAdQuestions
from chatGPT_conv_client.chatGPT_conv_client import ChatGPTConvClient

response = JobAdvert.job_ad_scrapper('https://app.otta.com/jobs/NzNpVWNM')
gtp_response = ChatGPTConvClient.gpt_ad_keyword_finder(JobAdQuestions.job_ad_questions(response))

print(gtp_response)




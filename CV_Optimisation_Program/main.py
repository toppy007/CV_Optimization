from job_advert.job_advert import JobAdvert
from prompts.job_ad_questions import JobAdQuestions
from chatGPT_conv_client.chatGPT_conv_client import ChatGPTConvClient

response = JobAdvert.job_ad_scrapper('https://app.otta.com/jobs/NzNpVWNM')
gtp_response = ChatGPTConvClient.gpt_ad_keyword_finder(JobAdQuestions.job_ad_questions(response))

profile_statement = ChatGPTConvClient.gpt_ad_keyword_finder(JobAdQuestions.job_ad_profile_gen(gtp_response))
print("profile statement")
print(profile_statement)

makers_statement = ChatGPTConvClient.gpt_ad_keyword_finder(JobAdQuestions.job_ad_makers_gen(gtp_response))
print("makers profile")
print(makers_statement)

covering_letter = ChatGPTConvClient.gpt_ad_keyword_finder(JobAdQuestions.job_ad_covering_letter_gen(gtp_response, response))
print("covering letter")
print(covering_letter)






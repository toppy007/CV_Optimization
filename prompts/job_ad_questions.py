

class JobAdQuestions:
    def job_ad_questions(response):
        message = [
            {
                "role": "system", 
                "content": "Help me analyze this text passage from an ATS perspective."
            },
            {
                "role": "user",
                "content": 
                
                f""" {response} 

                Based on the job description provided, please analyze the text and identify the most important keywords and skills that are relevant to the position. 
                Consider the specific technical skills, qualifications, and experience mentioned in the job description. 
                Additionally, focus on soft skills, such as communication, problem-solving, teamwork, and attention to detail.
                Extract the keywords that are likely to be recognized and valued by an ATS system. 
                These keywords will help ensure that your CV passes the initial screening process and increases your chances of being shortlisted for the job. 
                Please list the extracted keywords along with their context or usage within the job description.
                """
            },
            {
                "role": "assistant", 
                "content": "give me these as a list of the keywords and nothing else."
            },
            {
                "role": "user", 
                "content": "give it one more review and pick with more detail the technicaly important requirments and then add them to the list."
            },

        ]

        return message

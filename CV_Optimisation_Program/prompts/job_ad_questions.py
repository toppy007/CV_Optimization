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
                "role": "user", 
                "content": 
                """
                Please provide a thorough review of the text and extract the technical requirements with meticulous attention to detail.
                Identify and add to the list the highly significant technical requirements that are essential for the role
                """
            },
            {
                "role": "assistant", 
                "content": "Please extract the keywords from the text passage and provide them as a concise list, without including complete sentences or additional context."
            },

        ]

        return message
    
    # Profile custom profile message generator.

    def job_ad_questions(response, experences, knowledge, education):
        message = [
            {
                "role": "system", 
                "content": "Help me analyze this text passage from an ATS perspective."
            },
        ]

        return message
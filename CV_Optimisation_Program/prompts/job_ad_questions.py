from prompts.my_inputs import (edu_prodile, work_ex_profile, core_programing_profile)

class JobAdQuestions:

    # Job ad keyword analyzer message.

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
    
    # Custom profile message generator.

    def job_ad_profile_gen(response):
        message = [
            {
                "role": "system", 
                "content": "Help me write a professional CV profile statement."
            },
            {
                "role": "user",
                "content": 
                f""" the job requirement: {response} 
                """
            },
            {
                "role": "user",
                "content": 
                f""" my skills education background: {edu_prodile} 
                """
            },
            {
                "role": "user",
                "content": 
                f""" my skills from work experence background: {work_ex_profile} 
                """
            },
            {
                "role": "user",
                "content": 
                f""" my core software development skills background: {core_programing_profile} 
                """
            },
            {
                "role": "assistant", 
                "content": "match the job requirements to my education, work experence and software development skills. do not lie about anything i have not got experience with."
            },
            {
                "role": "user", 
                "content": "match my eductional background, work experice and core software development skil to the job adverts keyword."
            },
            {
                "role": "user", 
                "content": "make the statement only 100 words long and include the most important keywords from the job ad analysis."
            },
            {
                "role": "user", 
                "content": "remove any mention keywords that are not included in my education, core skills, or work experience from the statement."
            },
        ]

        return message
    
    def job_ad_makers_gen(response):
        message = [
            {
                "role": "system", 
                "content": "Help write an overview statement."
            },
            {
                "role": "user",
                "content": 
                f""" the job requirements: {response} 
                """
            },
            {
                "role": "user",
                "content": 
                f""" my core software development skills background: {core_programing_profile} 
                """
            },
            {
                "role": "assistant", 
                "content": "write a brief statement about the makers software development bootcamp."
            },
            {
                "role": "user", 
                "content": "match the statement to my core software development skills background and job requirements"
            },
            {
                "role": "assistant", 
                "content": "40 words max"
            },
        ]

        return message
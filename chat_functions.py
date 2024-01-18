from openai import OpenAI
import ast

client = OpenAI(
    api_key="INSERT OPENAI API KEY HERE",
)


# Parses the personal information from the first text that is being sent through
def personal_information_parser(text):
    keys_questions = {
        'name': "Extract a FULL NAME from the Text! Only return the FULL NAME that is available! If there is no FULL NAME, return n.a.!",
        'phone': "What is the user's phone number? Only return the NUMBER! If the information is not provided, return n.a.!",
        'email': "What is the user's email address? Only return the EMAIL! If the information is not provided, return n.a.!",
    }

    # Dictionary to store extracted information
    extracted_info = {
        'name': None,
        'phone': None,
        'email': None,
    }

    prompt = f"""
    {text}
    
    Here is a python dictionary with questions that need to be answered by you with the help of the text.
    Follow the instruction from the dictionary:
    
    {keys_questions}
    
    Please fill in the answers into this python dictionary and return it to me:
    
    {extracted_info}
    
    Please only return the filled out python dictionary!
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=1000
    )
    answer = response.choices[0].message.content.strip()

    filled = ast.literal_eval(answer)

    result = {
        'name': filled["name"],
        'mail': filled["email"],
        "tNummer": filled["phone"],
    }

    return result


# Parses the second block about the services they require from the legal firm
def legal_parser(text):
    keys_questions = {
        'service': "What is the legal service that the user need? Only return the legal service! If the information is not provided, return n.a.!",
        'insurance': "Does the user have a legal insurance? Only return YES or NO! If the information is not provided, return n.a.!",
        'insurance_provider': "If the user is insured, who is the insurance provider? Only return the insurance provider! If the information is not provided, return n.a.!",
    }

    # Dictionary to store extracted information
    extracted_info = {
        'service': None,
        'insurance': None,
        'insurance_provider': None,
    }

    prompt = f"""
        {text}

        Here is a python dictionary with questions that need to be answered by you with the help of the text.
        Follow the instruction from the dictionary:

        {keys_questions}

        Please fill in the answers into this python dictionary and return it to me:

        {extracted_info}

        Please only return the filled out python dictionary!
        """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=1000
    )
    answer = response.choices[0].message.content.strip()

    filled = ast.literal_eval(answer)


    result = {
        'service': filled["service"],
        'insurance': filled["insurance"],
        "insurance_provider": filled["insurance_provider"],
    }

    return result


# Legal matter parsing
def legal_matter_parsing(text):
    keys_questions = {
        'case_description': "Give me an overview of the most important details of the users legal issue? Return the answer in Bulletpoints! If the information is not provided, return n.a.!",
        'thoughts_concerns': "What are the users thoughts and concerns about the legal matter? Return the answer in Bulletpoints! If the information is not provided, return n.a.!",
        'documents': "Does the user have documents or relevant information on the matter? Return the answer in Bulletpoints if the user has information, if NOT return NO! If the information is not provided at all, return n.a.!"
    }

    # Dictionary to store extracted information
    extracted_info = {
        'case_description': None,
        'thoughts_concerns': None,
        'documents': None,
    }

    prompt = f"""
            {text}

            Here is a python dictionary with questions that need to be answered by you with the help of the text.
            Follow the instruction from the dictionary:

            {keys_questions}

            Please fill in the answers into this python dictionary and return it to me:

            {extracted_info}

            Please only return the filled out python dictionary!
            """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=1000
    )
    answer = response.choices[0].message.content.strip()

    filled = ast.literal_eval(answer)

    result = {
        'case_description': filled["case_description"],
        'thoughts_concerns': filled["thoughts_concerns"],
        "documents": filled["documents"],
    }

    return result


def wrap_up_parser(text):
    keys_questions = {
        'final_stmt': "Is the text containing a message from the user? If so, what is it about? Return the answer in Bulletpoints! If the message is empty, return n.a.!"
    }

    # Dictionary to store extracted information
    extracted_info = {
        'final_stmt': None
    }

    prompt = f"""
               {text}

               Here is a python dictionary with questions that need to be answered by you with the help of the text.
               Follow the instruction from the dictionary:

               {keys_questions}

               Please fill in the answers into this python dictionary and return it to me:

               {extracted_info}

               Please only return the filled out python dictionary!
               """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=1000
    )
    answer = response.choices[0].message.content.strip()

    filled = ast.literal_eval(answer)

    result = {
        'final_stmt': filled["final_stmt"]
    }

    return result

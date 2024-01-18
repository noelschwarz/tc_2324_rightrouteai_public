import requests
import chat_functions as cf
import doc_functions as df
import ast
import final_dict

from flask import Flask, request, jsonify, Response

app = Flask(__name__)


# Function to download and save a file from a URL
def download_file(url, save_path):
    # Sends a GET request to the URL
    response = requests.get(url, stream=True)

    # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    response.raise_for_status()

    # Open the file path as a binary write-mode stream and write the content to it in chunks
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return save_path


@app.route('/personal_data', methods=['POST'])
def personal_data():
    try:
        print("Starting to extract json data.")
        data = request.json
        conversation = data.get('conversation')
        print(f"conversation: {conversation}")

        print(f"Conversation Character Count: {len(conversation)}")
    except Exception as e:
        print(f"An error has occured in personal_data() - collecting JSON data: {e}")
        return jsonify({"Error in personal_data()": str(e)}), 500

    print("Successfully extracted data package from json.")

    try:
        print("Extracting personal information.")
        result_dict = cf.personal_information_parser(conversation)
        print(f"Result Dict: {result_dict}")
    except Exception as e:
        print(f"Error, while getting extracting personal_information_parser(): {e}")
        return jsonify({"Error in personal_information_parser()": str(e)}), 500


    # TODO: Insert code on how to pass the personal_result dictionary to the final dictionary for PDF processing

    print("Successfully extracted personal data with chat_functions.")

    print("Returning positive jsonify.")

    # TODO: Send dictionary to Bubble for a quick-save
    return jsonify(result_dict)


@app.route('/legal_information', methods=['POST'])
def legal_information():
    try:
        print("Starting to extract json data.")
        data = request.json
        conversation = data.get('conversation')
        print(f"Conversation :{conversation}")
    except Exception as e:
        print(f"An error has occured in legal_information() - collecting JSON data: {e}")
        return jsonify({"Error in legal_information()": str(e)}), 500

    print("Successfully extracted data package from json.")

    try:
        print("Extracting legal information.")
        result_dict= cf.legal_parser(conversation)
        print(f"Result Dict: {result_dict}")
    except Exception as e:
        print(f"Error, while getting extracting legal_parser(): {e}")
        return jsonify({"Error in legal_parser()": str(e)}), 500

    print("Successfully extracted personal data with chat_functions.")

    print("Returning positive jsonify.")
    return jsonify(result_dict)


@app.route('/legal_matter', methods=['POST'])
def legal_matter_information():
    try:
        print("Starting to extract json data.")
        data = request.json
        conversation = data.get('conversation')
        print(f"Conversation: {conversation}")
    except Exception as e:
        print(f"An error has occured in legal_matter_information() - collecting JSON data: {e}")
        return jsonify({"Error in legal_matter_information()": str(e)}), 500

    print("Successfully extracted data package from json.")

    try:
        print("Extracting legal matter information.")
        result_dict = cf.legal_matter_parsing(conversation)
        print(f"Result Dict: {result_dict}")
    except Exception as e:
        print(f"Error, while getting extracting legal_matter_parsing(): {e}")
        return jsonify({"Error in legal_matter_parser()": str(e)}), 500

    print("Successfully extracted personal data with chat_functions.")

    print("Returning positive jsonify.")
    return jsonify(result_dict)


@app.route('/final_stmt', methods=['POST'])
def final_stmt():
    try:
        print("Starting to extract json data.")
        data = request.json
        conversation = data.get('conversation')
        print(f"Conversation: {conversation}")
        dict2 = ast.literal_eval(data.get('dict'))
        files = data.get('url')
        print(f"File URLS: {files}")
        local_filenames = []

        if files != "n.a.":
            print("Documents received!")
            number_docs = files.count("bubble.io")
            print(f"Number of Documents sent: {number_docs}")

            try:
                if number_docs > 1:
                    urls = files.split(", ")
                    print(f"URL COUNT: {len(urls)}")
                    print(f"URL LIST: {urls}")
                    count = 0
                    for url in urls:
                        url_new = "https:" + url
                        print(f"New URL: {url_new}")

                        try:
                            local_fn = download_file(url_new, f"/home/noelschwarz0906/mysite/document_{count}.pdf") #Switch it to the path of the YOUR mandate template.
                        except Exception as e:
                            print(f"Error in downloading: {url_new}")
                            print(f"Error Message: {e}")
                            return jsonify(f"Error: {e}")

                        local_filenames.append(local_fn)
                        count += 1
                else:
                    local_filenames.append(download_file("https:" + files, f"/home/noelschwarz0906/mysite/document_1.pdf")) #Switch it to the path of the YOUR mandate template.
            except Exception as e:
                print(f"Error in downloading multiple files: {e}")
                return jsonify(status=f"Error in downloading multiple files: {e}")
        else:
            print("NO Documents received!")

    except Exception as e:
        print(f"An error has occured in final_stmt() - collecting JSON data: {e}")
        return jsonify({"Error in final_stmt()": str(e)}), 500

    print("Successfully extracted data package from json.")

    try:
        print("Extracting final user statement information.")
        result_dict = cf.wrap_up_parser(conversation)
        print(f"Result Dict: {result_dict}")
    except Exception as e:
        print(f"Error, while getting extracting wrap_up_parser(): {e}")
        return jsonify({"Error in wrap_up_parser()": str(e)}), 500
    try:
        # TODO: Insert code on how to pass the final_stmt_result dictionary to the final dictionary for PDF processing
        dict2.update(result_dict)
        print(f"Final Dictionary Count: {len(dict2)}")
        print(f"Updated Dictionary: {dict2}")

        # TODO: Build PDF and Send Email to Receiver {x}
        print("Starting to build the final document...")
        file_user = dict2['name'].replace(" ", "")
        input_path = "/home/noelschwarz0906/mysite/Mandate_Template.pdf" #Switch it to the path of the YOUR mandate template.
        output_path = f"/home/noelschwarz0906/mysite/mandate_document_{file_user}.pdf" #Switch it to the path of the folder of YOUR created files.

        local_filenames.append(output_path)
        print(f"Number of final Documents: {len(local_filenames)}")
        print(f"Names of Documents: {local_filenames}")

        try:
            df.fill_and_send_pdf(input_path, output_path, dict2)
        except Exception as e:
            print(f"Error in creating the final document: {e}")
            return jsonify(f"Error in document creation: {e}")

        print("Succesfully build the document!")
        print("Sending email...")
        sender_email = dict2['mail']
        sender_name = dict2['name']
        try:
            df.send_email_with_pdf(
                recipient_email=sender_email,  # Replace with the recipient's email
                recipient_name=sender_name,  # Replace with the lawyer's name
                timeslots='Monday 9am, Tuesday 2pm',  # Replace with actual timeslots
                pdf_file_paths=local_filenames,
                # Replace with the path to your PDF file
                sender_email='PLACE YOUR EMAIL (GMAIL) HERE',  # Replace with your email
                sender_password='PLACCE YOUR GMAIL PASSWORD TOKEN HERE',  # Replace with your email password
                smtp_server='smtp.gmail.com',  # Replace with your SMTP server
                smtp_port=465,  # Replace with your SMTP port (usually 465 for SSL)
                data_dict=dict2
            )
        except Exception as e:
            print(f"Error in sending email: {e}")
            return jsonify(status=f"mail-error: {e}")

        print("Successfully extracted personal data with chat_functions.")
        print("Returning positive jsonify.")
        return jsonify(status=f"success")
    except Exception as e:
        print(f"Error in returning jsonify: {e}")
        return jsonify(status=f"error: {e}")





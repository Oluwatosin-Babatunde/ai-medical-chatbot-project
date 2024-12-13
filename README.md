# ai-medical-chatbot-project
Medical chatbot project for Cloud Computing class for Fall 2024.
The healthcare sector is under constant pressure to provide quick and accurate responses to patients while minimizing the administrative workload. With the advent of technology, there is an opportunity to improve healthcare accessibility by utilizing chatbots that can handle common patient queries and automate routine tasks like appointment scheduling.
This project focuses on developing a cloud-based healthcare chatbot that leverages LLMs to assist healthcare providers by providing real-time responses to patients and automating routine administrative tasks. The chatbot will be deployed on Google Cloud Platform (GCP), leveraging cloud services for scalability, availability, and cost-efficiency.
The goal of this project is to create a solution that:
•	Assists users with basic medical queries (e.g., flu symptoms, treatment options).
•	Helps schedule appointments automatically.
•	Provides 24/7 access to healthcare information while ensuring privacy and security.

Problem Description
The healthcare industry faces several challenges:
1.	Scalability: High demand for healthcare services creates a need for scalable systems that can handle large volumes of inquiries. This chatbot is designed to dynamically scale based on demand, leveraging cloud resources for optimal performance.
2.	Administrative Efficiency: Healthcare staff are often overwhelmed by administrative tasks like appointment scheduling and answering repetitive questions. The chatbot automates these tasks, reducing the burden on healthcare providers.
3.	Accuracy and Reliability: Accurate medical information is vital, and the chatbot is designed to ensure responses align with the latest and relevant medical knowledge. Regular updates and validation from medical team are incorporated to maintain accuracy.
4.	Privacy and Data Security: Sensitive patient data is protected and the chatbot ensures confidentiality through encryption, secure data storage, and robust access controls.
5.	Contextual Understanding: The chatbot is designed to understand medical terminology and provide personalized responses to users without compromising privacy.
6.	Integration: The chatbot integrates with existing Electronic Health Records (EHR) and appointment scheduling systems for seamless user interaction.
Description of the Data
The dataset used in this project was obtained from Hugging Face Datasets, specifically the AI-Medical Chatbot dataset, which contains medical question-answer pairs covering a range of topics such as symptoms, treatments, diagnostics, and general FAQs. The dataset was used to train the chatbot to respond to healthcare-related questions.
This dataset was also used in conjunction with existing BERT pre-trained models in Python. Again, to ensure accuracy and reliability of our chatbot results, we added an extra layer of sub-library that focuses on basic conversational that relates to medical questions.
Dataset URL:
https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot
from datasets import load_dataset

ds = load_dataset("ruslanmv/ai-medical-chatbot")

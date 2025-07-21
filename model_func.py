from pydantic import BaseModel
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from typing import List, Optional
import google.generativeai as genai
import fasttext
from qdrant_client.models import Filter, FieldCondition, MatchValue


genai.configure(api_key="YOUR-APİ-KEY")
medical_model = genai.GenerativeModel('gemini-1.5-flash')

def find_class(user_message: str) -> str:
    """Kullanıcı mesajını sınıflandırır ve doktor uzmanlık alanını döndürür."""
    fasttext_model = fasttext.load_model("YOUR-PATH-HERE")
    label = fasttext_model.predict(user_message)[0][0]
    return label.replace("__label__", "")

class MedicalQASystem:
    def __init__(self):
        self.client = QdrantClient("localhost", port=6333)
        self.embedder = SentenceTransformer('emrecan/bert-base-turkish-cased-mean-nli-stsb-tr')
        self.collection_name = "doctor_questions_2"
        
    def search_similar_questions(self, user_query: str, top_k: int = 5):
        query_embedding = self.embedder.encode(user_query).tolist()
        
        speciality = find_class(user_query)
        filter_condition = Filter(
            must=[
                FieldCondition(
                    key="doctor_speciality",
                    match=MatchValue(value=str(speciality)))
            ]
        ) if speciality else None

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            query_filter= filter_condition,
            limit=top_k
        )
        
        return [
            {
                "doctor_title": hit.payload.get("doctor_title", "Uzman Doktor"),
                "speciality": hit.payload.get("doctor_speciality", "Genel Cerrahi"),
                "question": hit.payload["question_content"],
                "answer": hit.payload["question_answer"],
                "similarity": hit.score
            }
            for hit in results
        ]
    
class MedicalResponse(BaseModel):
    generated_answer: str
    follow_up: Optional[str]


async def handle_medical_query(user_query: str):
    try:
        qa_system = MedicalQASystem()
        
        # 1. Benzer soruları getir
        similar_qa = qa_system.search_similar_questions(user_query)
        # get_class_sonuc = find_class(user_message=user_query)
        
        # 2. Context hazırla
        context = "\n\n".join(
            f"Soru {i+1}:\n{qa['question']}\nDoktor Yanıtı:\n{qa['answer']}\nBenzerlik: {qa['similarity']:.2f}"
            for i, qa in enumerate(similar_qa)
        )
        
        # 3. System prompt tanımla
        system_prompt = f"""Sen deneyimli bir tıbbi danışmansın. Görevin:

1. Hastanın sorusuna kapsamlı bir yanıt vermek
2. Doktor tavsiyelerini göz önünde bulundurarak bir tavsiye vermek  
3. Takip edilmesi gereken adımları listelemek
4. Acil bir durum varsa belirtmek
5. Bir doktor rölüne bürünmek
6. Veritabanındaki benzer soru cevapları dikkate al

Veritabanındaki Benzer Soru-Yanıtlar:
{context}

Yanıtlarını hasta dostu bir dille, anlaşılır şekilde ver. Tıbbi terminoloji kullanırken açıklamalar ekle."""

        # 4. System instruction ile model oluştur
        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction=system_prompt
        )
        
        # 5. User prompt hazırla
        user_prompt = f"""Hasta Sorusu: {user_query}

Yukarıdaki bilgileri kullanarak hastanın sorusuna yanıt ver."""

        # 6. Cevap üret
        response = model.generate_content(user_prompt)
        
        return MedicalResponse(
            generated_answer=response.text,
            follow_up="Düzenli kontrollerinizi aksatmayınız." if "ameliyat" in user_query.lower() else None
        )
        
    except Exception as e:
        return {"error": f"Tıbbi sorgu işleme hatası: {str(e)}"}
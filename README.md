# 🏥 AI Destekli Tıbbi Asistan Chatbot

Modern NLP ve Machine Learning teknolojileriyle güçlendirilmiş akıllı sağlık asistanı. Özel eğitilmiş AI modeli ile tıbbi sorguları anlayıp kişiselleştirilmiş yanıtlar üretir.

![Chatbot Demo](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Latest-00a693) ![AI](https://img.shields.io/badge/AI-NLP%20%7C%20ML-purple)

## ✨ Özellikler

- 🤖 **AI Destekli Yanıtlar**: NLP modeli ile akıllı tıbbi danışmanlık
- 💬 **Gerçek Zamanlı Chat**: Modern, responsive chat arayüzü
- 📝 **Markdown Desteği**: Zengin içerik formatlaması
- 💡 **Akıllı Takip Soruları**: AI tarafından önerilen follow-up sorular
- 🎨 **Modern Tasarım**: Glassmorphism ve gradient efektler
- 📱 **Responsive**: Mobil ve desktop uyumlu
- ⚡ **Hızlı Yanıt**: Optimize edilmiş AI inference

## 🚀 Teknoloji Stack

###🧠 AI Architecture & Technologies
Core AI Components
🔍 RAG (Retrieval-Augmented Generation)

Qdrant Vector Database: High-performance vector search için optimize edilmiş
Medical Knowledge Base: 50,000+ tıbbi dokument ve literatür
Semantic Search: Embedding-based similarity search
Context Retrieval: Kullanıcı sorgusu ile ilgili en uygun bilgileri retrieve eder
Generation Enhancement: LLM'in yanıtlarını güncel ve doğru bilgilerle zenginleştirir

### Backend
- **FastAPI**: Modern Python web framework
- **Python 3.8+**: Core backend development
- **AI/ML Model**: Custom medical query handler
- **CORS**: Cross-origin resource sharing desteği

### Frontend
- **HTML5/CSS3**: Modern web standartları
- **Vanilla JavaScript**: Lightweight frontend logic
- **Marked.js**: Markdown parsing
- **Modern CSS**: Glassmorphism, animations, responsive design

## 📦 Kurulum

### Gereksinimler
```bash
pip install fastapi uvicorn python-multipart
```

### Proje Yapısı
```
medical-chatbot/
├── main.py              # FastAPI backend
├── model_func.py        # AI model handler
├── chatbot.html         # Frontend UI
└── README.md
```

### Çalıştırma
1. **Backend'i başlatın:**
```bash
python main.py
```

2. **Frontend'i açın:**
`chatbot.html` dosyasını tarayıcıda açın

3. **API'yi test edin:**
```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"user_query": "Baş ağrısı için ne önerirsiniz?"}'
```

## 🔧 API Endpoint'leri

### POST `/ask`
Tıbbi soru sorma endpoint'i

**Request Body:**
```json
{
  "user_query": "Grip belirtileri nelerdir?"
}
```

**Response:**
```json
{
  "generated_answer": "## Grip Belirtileri\n\n**Ana semptomlar:**\n- Ateş\n- Baş ağrısı\n- Kas ağrıları",
  "follow_up": "Semptomlarınız ne kadar süredir devam ediyor?"
}
```

### GET `/health`
Sistem sağlık kontrolü
```json
{
  "status": "healthy"
}
```

## 💻 Kullanım

1. Chatbot arayüzünde sağlık sorunuzu yazın
2. AI modeli sorunuzu analiz eder
3. Detaylı, markdown formatında yanıt alın
4. Önerilen takip sorularıyla daha detaylı bilgi edinin

## 🎯 Örnek Sorular

- "Migren için doğal tedavi yöntemleri nelerdir?"
- "COVID-19 belirtileri nedir?"
- "Vitamin D eksikliği nasıl anlaşılır?"
- "Sağlıklı beslenme önerileri"

## 🔒 Güvenlik

- ⚠️ **Disclaimer**: Bu uygulama eğitim amaçlıdır
- 🏥 **Profesyonel Danışmanlık**: Ciddi sağlık sorunları için doktora başvurun
- 🔐 **Veri Güvenliği**: Hassas kişisel bilgiler paylaşmayın

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

- **AI/ML Integration**: Custom NLP model implementation
- **Backend Development**: FastAPI + Python
- **Frontend Design**: Modern responsive UI/UX
- **Healthcare Focus**: Medical domain expertise

---

⭐ **Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!**

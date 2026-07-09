{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "17d7a343-a05d-4f3f-a522-7b5702906876",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🤖 Running DDI Classifier Inference...\n",
      "\n",
      "🔬 Results for: ACETYLSALICYLIC ACID + IBUPROFEN\n",
      "Status: 🔴 Interaction Detected\n",
      "Confidence (Probability): 81.27%\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import sys\n",
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "def predict_interaction(drug_a, drug_b):\n",
    "    model_path = 'Saved_Models/DDinter_LogisticRegression_Binary.pkl'\n",
    "    \n",
    "    # التأكد من وجود النموذج المسجل\n",
    "    if not os.path.exists(model_path):\n",
    "        print(f\"❌ Error: Saved model not found at '{model_path}'. Please run 'train.py' first.\")\n",
    "        return\n",
    "\n",
    "    # تحميل النموذج والـ Pipeline\n",
    "    pipeline = joblib.load(model_path)\n",
    "\n",
    "    # تجهيز البيانات وتنظيفها (تم إصلاح استدعاء الدوال هنا)\n",
    "    input_data = pd.DataFrame({\n",
    "        'Drug_A': [str(drug_a).lower().strip()],\n",
    "        'Drug_B': [str(drug_b).lower().strip()]\n",
    "    })\n",
    "\n",
    "    # التوقع\n",
    "    prediction = pipeline.predict(input_data)[0]\n",
    "    probability = pipeline.predict_proba(input_data)[0][1]\n",
    "\n",
    "    # طباعة النتيجة\n",
    "    result = \"🔴 Interaction Detected\" if prediction == 1 else \"🟢 No Interaction Detected\"\n",
    "    print(f\"\\n🔬 Results for: {drug_a.upper()} + {drug_b.upper()}\")\n",
    "    print(f\"Status: {result}\")\n",
    "    print(f\"Confidence (Probability): {probability*100:.2f}%\\n\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    # مثال تشغيلي افتراضي\n",
    "    print(\"🤖 Running DDI Classifier Inference...\")\n",
    "    predict_interaction('acetylsalicylic acid', 'Ibuprofen')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4511498-79d9-4153-9989-9fbab34facff",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

from flask import Flask, request, jsonify
import os
# from flask_cors import CORS # Jika Anda perlu mengaktifkan CORS secara eksplisit, meski Render harusnya menangani proxy dengan benar

app = Flask(__name__)
# CORS(app) # Uncomment jika Anda mengalami masalah CORS saat pengujian langsung (seharusnya tidak perlu jika pakai PHP proxy)

# --- Placeholder untuk Logika Model AI Kustom Anda ---
# Di SINI Anda akan mengimplementasikan atau memuat model AI Anda.
# Untuk contoh ini, saya akan menggunakan logika dummy atau rule-based sederhana.
# Jika Anda memiliki model ML (misalnya, TensorFlow, PyTorch, Hugging Face Transformers),
# Anda akan memuatnya di sini (misalnya, di luar fungsi route agar hanya dimuat sekali).

def get_qa_response(messages_history, uji_data_json):
    # Logika placeholder untuk tanya jawab
    latest_user_message = messages_history[-1]['content'].lower() if messages_history else ""

    # Contoh sederhana berdasarkan uji.json
    if "fermata" in latest_user_message and "apa" in latest_user_message:
        return uji_data_json.get('about_fermata_brief', {}).get('description', 'Fermata adalah alat refleksi interaktif berbasis AI.').strip()
    elif "pengembang" in latest_user_message or "dikembangkan" in latest_user_message:
        return uji_data_json.get('about_fermata_brief', {}).get('developed_by', 'Dikembangkan oleh Enry Johan Jaohari dan Muhammad Yuda Ramadhan.').strip()
    elif "fase" in latest_user_message and "refleksi" in latest_user_message:
        phases_summary = "Fermata terdiri dari lima fase refleksi terstruktur: "
        for phase in uji_data_json.get('about_fermata_full', {}).get('structure_system', {}).get('phases', []):
            phases_summary += f"{phase['name']} ({phase['description']}). "
        return phases_summary.strip()
    elif "virtual play" in latest_user_message or "mamang glenn" in latest_user_message:
        return uji_data_json.get('virtual_play', {}).get('background', 'Virtual Play adalah simulasi konfigurasi musikal.').strip() + " " + \
               "Fitur utama: " + ", ".join(uji_data_json.get('virtual_play', {}).get('core_features', [])) + ". " + \
               uji_data_json.get('virtual_play', {}).get('collaboration_with_fermata_ai', '').strip()
    elif "hak cipta" in latest_user_message or "copyright" in latest_user_message:
         return uji_data_json.get('copyright_intellectual_status', {}).get('originality', '').strip() + " " + \
                uji_data_json.get('copyright_intellectual_status', {}).get('ownership', '').strip() + " " + \
                uji_data_json.get('copyright_intellectual_status', {}).get('restrictions', '').strip()
    elif "etika" in latest_user_message or "batasan penggunaan" in latest_user_message:
        return uji_data_json.get('ethics_and_usage_limitations', {}).get('design_purpose', '').strip() + " " + \
               uji_data_json.get('ethics_and_usage_limitations', {}).get('role_in_learning', '').strip()
    elif "visi fermata" in latest_user_message or "pengembangan ke depan" in latest_user_message:
        visi = uji_data_json.get('about_fermata_full', {}).get('pengembangan_ke_depan', {}).get('visi', '').strip()
        rencana = "; ".join(uji_data_json.get('about_fermata_full', {}).get('pengembangan_ke_depan', {}).get('rencana_tahapan', []))
        return f"Visi Fermata: {visi}. Rencana tahapan: {rencana}."

    return f"Saya model AI kustom Anda. Anda bertanya: '{latest_user_message}'. Saya tidak menemukan informasi spesifik tentang itu dalam data uji."

def generate_narrative_and_roadmap(user_answers_dict, framework_dict, user_name):
    # Ini adalah logika inti model AI Anda untuk narasi dan peta aksi.
    # Ini akan jauh lebih kompleks di aplikasi nyata (memproses jawaban, menerapkan framework, menghasilkan teks).
    # Untuk contoh ini, saya akan menggabungkan beberapa teks.

    narrative_parts = []
    narrative_parts.append(f"Identitas Musikal {user_name}:")
    narrative_parts.append(f"Berdasarkan refleksi Anda, {user_name}, perjalanan musikal Anda terbentuk dari pengalaman mendalam di bidang {user_answers_dict.get('Fase 1', ['musik']).pop()}. Anda memiliki kecenderungan kuat terhadap {user_answers_dict.get('Fase 3', ['eksplorasi bunyi atau performa']).pop()}, membedakan Anda dari yang lain.")
    narrative_parts.append(f"Pengaruh artistik dari {user_answers_dict.get('Fase 2', ['berbagai musisi dan karya']).pop()} telah membentuk selera dan gaya Anda, menciptakan keunikan dalam ekspresi musikal Anda.")
    narrative_parts.append(f"Dalam memahami posisi Anda di industri, Anda membayangkan audiens yang {user_answers_dict.get('Fase 5', ['spesifik dan terlibat']).pop()}, serta strategi branding yang menekankan pada {user_answers_dict.get('Fase 5', ['kejujuran ekspresi']).pop()}.")
    narrative_parts.append(f"Secara keseluruhan, identitas musikal Anda, seperti yang dideskripsikan oleh framework kuratorial Fermata, adalah perpaduan antara keahlian teknis ({framework_dict.get('text', '').split('Dimensi Teknis')[1].split('Dimensi Filosofis')[0].strip()[:50]}...), nilai filosofis ({framework_dict.get('text', '').split('Dimensi Filosofis')[1].split('Dimensi Sosial')[0].strip()[:50]}...), dan potensi dampak sosial dan ekonomi.")

    roadmap_parts = []
    roadmap_parts.append("Peta Aksi Strategis (3-6 Bulan Ke Depan):")
    roadmap_parts.append("A. Pengembangan Artistik:")
    roadmap_parts.append("- Lanjutkan eksplorasi pada area yang membuat Anda 'hidup' (misalnya, {user_answers_dict.get('Fase 1', ['sensasi tampil']).pop()}).")
    roadmap_parts.append("- Latih lebih lanjut aspek yang membedakan Anda dari idola ({user_answers_dict.get('Fase 2', ['sisi yang tidak Anda tiru']).pop()}).")
    roadmap_parts.append("- Eksplorasi format atau konteks tampil yang paling 'Anda' banget (misalnya, {user_answers_dict.get('Fase 3', ['panggung akustik atau outdoor']).pop()}).")

    roadmap_parts.append("B. Strategi Jaringan & Audiens:")
    roadmap_parts.append("- Identifikasi dan jangkau komunitas yang sesuai dengan pendengar ideal Anda ({user_answers_dict.get('Fase 4', ['penikmat lirik atau komunitas kampus']).pop()}).")
    roadmap_parts.append("- Cari peluang kolaborasi dengan musisi yang dapat melengkapi 'dua genre/karakter' gabungan gaya Anda ({user_answers_dict.get('Fase 4', ['dua genre/karakter']).pop()}).")
    roadmap_parts.append("- Aktif berinteraksi di platform digital yang Anda rasa paling cocok untuk menampilkan karya ({user_answers_dict.get('Fase 5', ['TikTok atau Spotify']).pop()}).")

    roadmap_parts.append("C. Peningkatan Branding & Portofolio:")
    roadmap_parts.append("- Kembangkan 'kalimat pembuka' bio Anda menjadi pernyataan identitas yang kuat di media sosial/portofolio ({user_answers_dict.get('Fase 5', ['puitis atau to the point']).pop()}).")
    roadmap_parts.append("- Buat konten visual digital yang selaras dengan 'gaya visual, nuansa, warna, atau lokasi' yang Anda impikan ({user_answers_dict.get('Fase 5', ['gaya visual Anda']).pop()}).")
    roadmap_parts.append("- Dokumentasikan setiap penampilan atau karya baru, fokus pada 'hal yang bikin Anda beda' ({user_answers_dict.get('Fase 3', ['gaya atau pendekatan unik Anda']).pop()}).")

    return "\n\n".join(narrative_parts) + "\n\n" + "\n".join(roadmap_parts)


@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    messages = data.get('messages', [])
    uji_data = data.get('ujiData', {}) # data from uji.json

    ai_response = get_qa_response(messages, uji_data)

    return jsonify({'response': ai_response})

@app.route('/summarize', methods=['POST'])
def summarize_ai():
    data = request.get_json()
    all_answers = data.get('userAnswers', {})
    user_name = data.get('userName', 'Mahasiswa')
    framework_content = data.get('framework', {})

    ai_summary = generate_narrative_and_roadmap(all_answers, framework_content, user_name)

    return jsonify({'response': ai_summary})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

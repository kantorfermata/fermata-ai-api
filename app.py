from flask import Flask, request, jsonify
import os
from flask_cors import CORS # Import CORS

app = Flask(__name__)
CORS(app) # Mengaktifkan CORS untuk semua route, penting jika ada masalah lintas domain

# --- Placeholder untuk Logika Model AI Kustom Anda ---
# Di SINI Anda akan mengimplementasikan atau memuat model AI Anda yang sebenarnya.

def get_qa_response(messages_history, uji_data_json):
    """
    Logika placeholder untuk menjawab pertanyaan di mode Uji.
    Ini membaca data dari uji.json dan memberikan respons dasar.
    """
    latest_user_message = messages_history[-1]['content'].lower() if messages_history else ""

    if "fermata" in latest_user_message and ("apa" in latest_user_message or "tentang" in latest_user_message):
        return uji_data_json.get('about_fermata_brief', {}).get('description', 'Fermata adalah alat refleksi interaktif berbasis AI.').strip()
    elif "pengembang" in latest_user_message or "dikembangkan" in latest_user_message or "siapa" in latest_user_message:
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
    """
    Logika placeholder untuk menghasilkan narasi dan peta aksi.
    Ini menggabungkan jawaban pengguna dan fragmen dari framework.
    """
    # Gabungkan jawaban user ke dalam string untuk narasi
    all_answers_flat = {}
    for phase, answers_list in user_answers_dict.items():
        all_answers_flat[phase] = ", ".join(answers_list) if answers_list else "belum ada jawaban"

    narrative_parts = []
    narrative_parts.append(f"### Identitas Musikal {user_name}")
    narrative_parts.append(f"Berdasarkan refleksi Anda, {user_name}, perjalanan musikal Anda terbentuk dari pengalaman mendalam di bidang {all_answers_flat.get('Fase 1', 'musik')}. Anda memiliki kecenderungan kuat terhadap {all_answers_flat.get('Fase 3', 'eksplorasi bunyi atau performa')}, membedakan Anda dari yang lain.")
    narrative_parts.append(f"Pengaruh artistik dari {all_answers_flat.get('Fase 2', 'berbagai musisi dan karya')} telah membentuk selera dan gaya Anda, menciptakan keunikan dalam ekspresi musikal Anda.")
    narrative_parts.append(f"Dalam memahami posisi Anda di industri, Anda membayangkan audiens yang {all_answers_flat.get('Fase 5', 'spesifik dan terlibat')}, serta strategi branding yang menekankan pada {all_answers_flat.get('Fase 5', 'kejujuran ekspresi')}.")
    narrative_parts.append(f"Secara keseluruhan, identitas musikal Anda, seperti yang dideskripsikan oleh framework kuratorial Fermata, adalah perpaduan antara keahlian teknis, nilai filosofis, dan potensi dampak sosial dan ekonomi.")

    roadmap_parts = []
    roadmap_parts.append("\n### Peta Aksi Strategis (3-6 Bulan Ke Depan)")
    roadmap_parts.append("A. Pengembangan Artistik:")
    roadmap_parts.append(f"- Lanjutkan eksplorasi pada area yang membuat Anda 'hidup' (misalnya, {all_answers_flat.get('Fase 1', 'sensasi tampil')}).")
    roadmap_parts.append(f"- Latih lebih lanjut aspek yang membedakan Anda dari idola (termasuk {all_answers_flat.get('Fase 2', 'sisi yang tidak Anda tiru')}).")
    roadmap_parts.append(f"- Eksplorasi format atau konteks tampil yang paling 'Anda' banget (misalnya, {all_answers_flat.get('Fase 3', 'panggung akustik atau outdoor')}).")

    roadmap_parts.append("\nB. Strategi Jaringan & Audiens:")
    roadmap_parts.append(f"- Identifikasi dan jangkau komunitas yang sesuai dengan pendengar ideal Anda (misalnya, {all_answers_flat.get('Fase 4', 'penikmat lirik atau komunitas kampus')}).")
    roadmap_parts.append(f"- Cari peluang kolaborasi dengan musisi yang dapat melengkapi 'dua genre/karakter' gabungan gaya Anda (seperti yang Anda sebutkan di {all_answers_flat.get('Fase 4', 'gaya komposisi Anda')}).")
    roadmap_parts.append(f"- Aktif berinteraksi di platform digital yang Anda rasa paling cocok untuk menampilkan karya (misalnya, {all_answers_flat.get('Fase 5', 'TikTok atau Spotify')}).")

    roadmap_parts.append("\nC. Peningkatan Branding & Portofolio:")
    roadmap_parts.append(f"- Kembangkan 'kalimat pembuka' bio Anda menjadi pernyataan identitas yang kuat di media sosial/portofolio ({all_answers_flat.get('Fase 5', 'puitis atau to the point')}).")
    roadmap_parts.append(f"- Buat konten visual digital yang selaras dengan 'gaya visual, nuansa, warna, atau lokasi' yang Anda impikan ({all_answers_flat.get('Fase 5', 'gaya visual Anda')}).")
    roadmap_parts.append(f"- Dokumentasikan setiap penampilan atau karya baru, fokus pada 'hal yang bikin Anda beda' ({all_answers_flat.get('Fase 3', 'gaya atau pendekatan unik Anda')}).")

    return "\n\n".join(narrative_parts) + "\n\n" + "\n".join(roadmap_parts)


@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    messages = data.get('messages', [])
    uji_data = data.get('ujiData', {}) 

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

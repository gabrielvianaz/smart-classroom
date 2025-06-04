import os
import secrets

from flask import Flask, request, jsonify
from flask_cors.extension import CORS

from assistant import Assistant
from constants import MODEL_NAME, CPU, TEMP_FOLDER

service = Flask("assistant")
service.json.ensure_ascii = False
CORS(service)
assistant = Assistant(model_name=MODEL_NAME, device=CPU)


@service.post("/receive_command")
def receive_command():
    if "audio" not in request.files:
        return jsonify({"erro": "nenhum foi enviado"}), 400

    audio = request.files["audio"]
    temp_file_path = os.path.join(TEMP_FOLDER, f"{secrets.token_hex(32).lower()}.wav")
    audio.save(temp_file_path)

    try:
        command_action, command_object = assistant.receive_command(temp_file_path)
        return jsonify({"action": command_action, "object": command_object}), 200
    except Exception:
        return jsonify({"error": "Invalid command"}), 400
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


if __name__ == "__main__":
    if assistant.initialized:
        service.run(host="0.0.0.0", debug=True)

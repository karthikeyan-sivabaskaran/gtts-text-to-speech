from flask import request, send_file
from gtts import gTTS
import uuid
from datetime import datetime
import os
from flask import g
from flasgger.utils import swag_from
import glob
from text_to_audio.app import create_app
from text_to_audio.config import DevelopmentConfig, ProductionConfig
import pathlib

app = create_app(
    config_object=DevelopmentConfig)

swagger_config_dir = str(pathlib.Path(__file__).resolve().parent.parent)

@app.before_request
def before_request_func():
    audio_files = glob.glob('*.mp3')
    for mp3_file in audio_files:
        audio_sts = mp3_file[36:-4]
        print(audio_sts)
        audio_ts = datetime.strptime(audio_sts, '%Y%m%d_%H%M%S%f')
        current_ts = datetime.utcnow()
        diff_ts = current_ts - audio_ts
        duration_in_s = diff_ts.total_seconds()
        minutes = divmod(duration_in_s, 60)[0]
        print(type(minutes))
        if minutes > 30:
            os.remove(mp3_file)
            print('{0} file removed'.format(mp3_file))

    uniq_id = str(uuid.uuid4())
    current_time = datetime.utcnow().strftime('%Y%m%d_%H%M%S%f')[:-3]
    mp3_file_name = uniq_id + current_time + '.mp3'
    print(mp3_file_name)
    g.filename = mp3_file_name

    print("before_request is running!")


@app.route('/hello_world', methods=['GET', 'POST'])
def say_hello():
    '''
    this is test route for flask app
    '''
    return "Hello World!"


@app.route('/text_to_audio')
@swag_from(os.path.join(swagger_config_dir, 'swagger_configs', 'swagger_config1.yml'))
def text_to_audio():
    mytext = request.args.get("input_text")
    language = 'en'
    obj = gTTS(text=mytext, lang=language, slow=False)
    # os.chdir('text_to_audio')
    # obj.save(g.filename)
    obj.save(os.path.join(os.getcwd(), 'text_to_audio', g.filename))


    return send_file(g.filename, attachment_filename='text_to_audio.mp3', as_attachment=True)

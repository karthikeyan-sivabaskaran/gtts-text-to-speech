
from text_to_audio.routes import app

if __name__  == '__main__':
    app.debug = True
    app.run(host=app.config['SERVER_ADDRESS'], port=app.config['SERVER_PORT'])
    app.run(host="0.0.0.0", port=5777)
from flask import Flask, send_from_directory, request, abort

app = Flask(__name__)

sync_list = ['butts','cats','burrito']

def get_sync_list():
    sync_list_items = [{'index': index, 'text': item} for index, item in enumerate(sync_list)]
    return sync_list_items

@app.route('/')
def root():
    return send_from_directory('../client/.svelte-kit/output/prerendered', 'fallback.html')

@app.route('/<path:path>')
def assets(path):
    return send_from_directory('../client/.svelte-kit/output/client', path)

@app.route('/notes', methods=['GET'])
def get_sticky_notes():
    sticky_notes = get_sync_list()
    return {'sticky_notes': sticky_notes}

@app.route('/notes', methods=['POST'])
def create_sticky_note():
    data = request.get_json(force=True)
    if data is not None:
        text = data['text']

        sync_list.append(text)
        sync_list_item = sync_list[-1]

        return {'sticky_note': {'index': len(sync_list)-1, 'text': text}}
    return abort(404)

@app.route('/notes/<index>', methods=['DELETE'])
def delete_sticky_note(index):
    index = int(index)
    sync_list.pop(index)
    return {'deleted': index}


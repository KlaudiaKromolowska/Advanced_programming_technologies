from flask import jsonify
from flask import request

from app import app
from app import db
from models import Note
from models import NoteType


@app.route('/add_note_type', methods=['POST'])
def add_note_type():
    note_name = request.json.get('name')
    note_type = NoteType(name=note_name)
    db.session.add(note_type)
    db.session.commit()
    return jsonify({"success": f'New note type added: {note_name}'})


@app.route('/get_note_types', methods=['GET'])
def get_note_types():
    note_types = NoteType.query.all()
    json_note_types = []
    for nt in note_types:
        json_note_types.append(nt.to_json())
    return jsonify(json_note_types)


@app.route('/remove_note_type/<int:note_type_id>', methods=['DELETE'])
def remove_note_type(note_type_id):
    nt_to_delete = NoteType.query.get(note_type_id)
    name = nt_to_delete.name
    db.session.delete(nt_to_delete)
    db.session.commit()
    return jsonify(
        {'success': f'Note type deleted: {name}'}
    )


@app.route('/add_note', methods=['POST'])
def add_note():
    id = request.json.get('id')
    title = request.json.get('title')
    content = request.json.get('content')
    note_type = request.json.get('note_type_id')
    important = request.json.get('important')
    is_task = request.json.get('is_task')
    note = Note(
        id=id,
        title=title,
        content=content,
        note_type=note_type,
        important=important,
        is_task=is_task,
    )
    db.session.add(note)
    db.session.commit()
    return jsonify({'success': f'New note added: {title}'})


@app.route('/get_note/<int:note_id>', methods=['GET'])
def get_note(note_id):
    nt = Note.query.get(note_id)
    return jsonify(nt.to_json())


@app.route('/list', methods=['GET'])
def list():
    sort_by = request.args.get('sort_by')
    filter_by = request.args.get('filter_by')
    filter_value = request.args.get('filter_value')
    if filter_by == 'title':
        note = Note.query.filter_by(title=filter_value).order_by(sort_by).all()
    elif filter_by == 'content':
        note = Note.query.filter_by(content=filter_value).order_by(sort_by).all()
    elif filter_by == 'note_type':
        note = Note.query.filter_by(note_type=filter_value).order_by(sort_by).all()
    elif filter_by == 'important':
        note = Note.query.filter_by(important=filter_value).order_by(sort_by).all()
    elif filter_by == 'is_task':
        note = Note.query.filter_by(is_task=filter_value).order_by(sort_by).all()
    else:
        note = Note.query.order_by(sort_by).all()

    note_list = []
    for n in note:
        note_list.append(n.to_json())
    return jsonify(note_list)


@app.route('/edit_note/<int:note_id>', methods=['PUT'])
def edit_note(note_id):
    nt_for_editing = Note.query.get_or_404(note_id)
    id = note_id
    title = request.json.get('title')
    content = request.json.get('content')
    note_type = request.json.get('note_type')
    important = request.json.get('important')
    is_task = request.json.get('is_task')
    print(nt_for_editing)
    nt_for_editing.id = id
    nt_for_editing.title = title
    nt_for_editing.content = content
    nt_for_editing.note_type = note_type
    nt_for_editing.important = important
    nt_for_editing.is_task = is_task
    db.session.commit()
    return jsonify(
        {'success': f'Note modified for: {title}'}
    )


@app.route('/remove_note/<int:note_id>', methods=['DELETE'])
def remove_note(note_id):
    nt_to_delete = Note.query.get(note_id)
    db.session.delete(nt_to_delete)
    db.session.commit()
    return jsonify(
        {'success': f'Note deleted: {nt_to_delete.title}'}
    )

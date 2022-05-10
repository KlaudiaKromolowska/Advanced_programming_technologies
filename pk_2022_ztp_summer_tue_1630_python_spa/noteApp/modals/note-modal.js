export class FormModalView {

    constructor() {
        this.app = document.getElementById('root');
    }

    setDataSubmitCallback(callback){
        this.submitCallback  = callback;
    }

    openForm(types, data) {
        this.modal = this._render(types, data);
        const myModal = new bootstrap.Modal(this.modal)
        myModal.toggle();

        this.modal.addEventListener('hidden.bs.modal', (event) => {
            this.modal.remove();
            this.modal = null;
        })
        this._listenForSubmit();
    }

    closeForm(){
        if(this.modal){
            bootstrap.Modal.getInstance(this.modal).hide();
        }
    }

    _render(types, data) {
        const note = data ? data : {};
        const modal = document.createElement('div');
        modal.classList.add('modal', 'fade');
        modal.id = 'modalForm';
        const select = this._makeSelectWithTypes(types, note)

        modal.innerHTML = `<div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">${note.id ? 'Edit note' : 'Create note'}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="container">
                        <form id="note-form">
                        ${note.id ? `<input type="hidden" name="id" value="${note.id}"> `: ''}
                            <div class="mb-3">
                                <label for="name" class="form-label">Title</label>
                                <input type="text" value="${note.title || ''}" class="form-control" id="title" name="title">
                            </div>
                            <div class="mb-3">
                                <label for="author" class="form-label">Content</label>
                                <input type="text" value="${note.content || ''}" class="form-control" id="content" name="content">
                            </div>
                             <div class="mb-3">
                                <label for="type" class="form-label">Type</label>
                                ${select.outerHTML}
                            </div>
                            <div class="mb-3">
                                <input class="form-check-input" ${note.important ? 'checked' : ''} type="checkbox" value="true" id="important" name="important">
                                <label class="form-check-label" for="flexCheckDefault">
                                   Important
                                </label>
                            </div>
                            <div class="mb-3">
                                <input class="form-check-input" ${note.is_task ? 'checked' : ''} type="checkbox" value="true" id="is_task" name="is_task">
                                <label class="form-check-label" for="flexCheckDefault">
                                   Is task
                                </label>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="submit-button">Save changes</button>
                </div>
            </div>
        </div>`;

        this.app.appendChild(modal)
        return modal;
    }

    _makeSelectWithTypes(types, note) {
        const select = document.createElement("select")
        select.classList.add('form-select');
        select.id = 'type';
        select.name = 'note_type_id'

        const options = types.map(type => `<option ${type.id == note.note_type ? 'selected' : '' } value="${type.id}">${type.name}</option>`)

        select.innerHTML = `
              <option value="">Chose type</option>
              ${options.join('\n')}
        `

        return select;
    }

    _listenForSubmit() {
        this.modal.querySelector('#submit-button').addEventListener('click', () => {

            const noteData = {};

            const formData = new FormData(document.getElementById('note-form'))
            for (const [name, value] of formData.entries()) {
                noteData[name] = value;
            }
            this._onSubmit(noteData)
        })
    }

    _onSubmit(noteData){
        this.submitCallback(noteData);
    }
}
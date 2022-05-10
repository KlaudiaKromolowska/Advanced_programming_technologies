export class TypeFormModalView {

    constructor() {
        this.app = document.getElementById('root');
    }

    setDataSubmitCallback(callback){
        this.submitCallback  = callback;
    }

    openForm() {
        this.modal = this._render();
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

    _render() {
        const modal = document.createElement('div');
        modal.classList.add('modal', 'fade');
        modal.id = 'modalForm';

        modal.innerHTML = `<div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Create type</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="container">
                        <form id="type-form">
                            <div class="mb-3">
                                <label for="name" class="form-label">Name</label>
                                <input type="text" value="" class="form-control" id="name" name="name">
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

    _listenForSubmit() {
        this.modal.querySelector('#submit-button').addEventListener('click', () => {

            const typeData = {};

            const formData = new FormData(document.getElementById('type-form'))
            for (const [name, value] of formData.entries()) {
                typeData[name] = value;
            }
            this._onSubmit(typeData)
        })
    }

    _onSubmit(noteData){
        this.submitCallback(noteData);
    }
}
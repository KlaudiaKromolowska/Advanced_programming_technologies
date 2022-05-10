import {NoteModel} from "./model/note.js";
import {NoteListView} from "./views/note-list.js";
import {FormModalView} from "../modals/note-modal.js";
import {TypeModel} from "../type/model/type.js";
import {ToastController} from "../toast/controller.js";

export class NoteController{
    constructor() {
        this.noteModel = new NoteModel();
        this.typeModel = new TypeModel();
        this.toastController = new ToastController();
        this.filters = {};

        this.notesListView = new NoteListView(document.getElementById('note-container'))
        this.notesListView.bindEditClick(this.handleNoteEditClicked)
        this.notesListView.bindDeleteClick(this.handleNoteDeleteClicked)
        this.notesListView.bindFilterChange(this.handleFiltersChange)

        this.refreshNotesList();
    }

    refreshNotesList = async () => {
        this.notesListView.placeSpinner();
        try {
            const notes = await this.noteModel.getAllNotes(this.filters);
            this.notesListView.displayList(notes, this.filters);
        } catch (e){
            this.toastController.showToast(e.toString(),'error');
        } finally {
            this.notesListView.removeSpinner();
        }
    }

    handleCreateNoteClicked = async () => {
        const formModalView = this._createModal();
        const types = await this.typeModel.getAllTypes();
        formModalView.openForm(types);
    }

    handleNoteEditClicked = async (id) => {
        const formModalView = this._createModal();
        const note = await this.noteModel.getNoteById(id)
        const types = await this.typeModel.getAllTypes();
        formModalView.openForm(types, note);
    }

    handleNoteDeleteClicked = async (id) => {
        this.notesListView.placeSpinner();
        try {
            await this.noteModel.deleteNote(id);
            await this.refreshNotesList();
        } catch (e){
            this.toastController.showToast(e.toString(), 'error')
        } finally {
            this.notesListView.removeSpinner();
        }
    }

    handleFiltersChange = (filters) => {
        this.filters = filters;
        this.refreshNotesList();
    }

    _createModal() {
        const formModalView = new FormModalView();
        formModalView.setDataSubmitCallback(async (data) => {
            try {
                await this.noteModel.saveNote(data);
                this.toastController.showToast('Note successfully created', 'success');
                formModalView.closeForm();
                this.refreshNotesList();
            } catch (e) {
                this.toastController.showError(e)
            }
        });

        return formModalView;
    }
}
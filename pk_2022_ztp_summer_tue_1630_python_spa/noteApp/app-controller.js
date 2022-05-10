import {TypeController} from "./type/controller.js";
import {NoteController} from "./note/controller.js";

export class AppController {
    constructor(view) {
        this.view = view

        const typeController = new TypeController();
        const noteController = new NoteController();

        this.view.bindCreateNoteButtonClicked(noteController.handleCreateNoteClicked);
        this.view.bindCreateTypeButtonClicked(typeController.handleCreateTypeClicked);
    }
}
export class NoteModel {
    constructor() {

    }

    getAllNotes(filterObject) {
        const filterParameters = {};
        for (const key in filterObject) {
            if (filterObject[key]) {
                filterParameters[key] = filterObject[key];
            }
        }

        return axios.get('/list', {
            params: filterParameters
        }).then((response) => {
            return response.data;
        });
    }

    getNoteById(id) {
        return axios.get(`/get_note/${id}`).then((response) => {
            if (response.data.errors) {
                throw new Error(response.data.errors.join(`<br>`));
            }

            return response.data;
        });
    }

    saveNote(note) {
        const booleans = {
            is_task: !!note.is_task,
            important: !!note.important,
        }

        const model = { ...note, ...booleans};

        if(!model.id) {

            return axios.post(`/add_note`, model).then((response) => {
                if (response.data.errors) {
                    throw new Error(response.data.errors.join(`<br>`));
                }
            });
        } else {
            model.note_type = model.note_type_id;
            delete model.note_type_id;

            return axios.put(`/edit_note/${note.id}`, model).then((response) => {
                if (response.data.errors) {
                    throw new Error(response.data.errors.join(`<br>`));
                }
            });
        }
    }

    deleteNote(noteId) {
        return axios.delete(`/remove_note/${noteId}`).then((response) => {
            console.log(response.data);
        });
    }
}
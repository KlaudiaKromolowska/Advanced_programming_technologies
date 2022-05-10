export class TypeModel {
    constructor() {

    }

    getAllTypes() {
        return axios.get('/get_note_types').then((response) => {
            if (response.data.errors) {
                throw new Error(response.data.errors.join(`<br>`));
            }

            return response.data;
        });

        // return new Promise((res) => {
        //     setTimeout(() => {
        //         res([
        //             {id: 1, name: 'First type'},
        //             {id: 2, name: "Second type"},
        //             ...this.mem || []]);
        //     }, 1000)
        // })
    }

    saveType(note) {
        const model = {...note};

        return axios.post(`/add_note_type`, model).then((response) => {
            if (response.data.errors) {
                throw new Error(response.data.errors.join(`<br>`));
            }
        });
    }

    deleteType(typeId) {
        return axios.delete(`/remove_note_type/${typeId}`).then((response) => {
            if (response.data.errors) {
                throw new Error(response.data.errors.join(`<br>`));
            }
        });
    }
}
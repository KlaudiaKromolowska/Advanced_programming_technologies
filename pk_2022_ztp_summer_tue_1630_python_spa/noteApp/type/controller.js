import {TypeModel} from "./model/type.js";
import {TypeListView} from "./views/type-list.js";
import {TypeFormModalView} from "../modals/type-modal.js";
import {ToastController} from "../toast/controller.js";

export class TypeController {
    constructor() {
        this.typeModel = new TypeModel();
        this.toastController = new ToastController();

        this.typesListView = new TypeListView(document.getElementById('type-container'))
        this.typesListView.bindDeleteClick(this.handleTypeDeleteClicked)

        this.refreshTypesList();
    }


    refreshTypesList = async () => {
        this.typesListView.placeSpinner();
        const types = await this.typeModel.getAllTypes()
        this.typesListView.displayList(types);
        this.typesListView.removeSpinner();
    }

    handleCreateTypeClicked = async () => {
        const formModalView = this._createModal();
        formModalView.openForm();
    }

    handleTypeDeleteClicked = async (id) => {
        this.typesListView.placeSpinner();
        try {
            await this.typeModel.deleteType(id);
            await this.refreshTypesList();
        } catch (e) {
            this.toastController.showToast(e.toString(), 'error');
        } finally {
            this.typesListView.removeSpinner();
        }
    }

    _createModal() {
        const formModalView = new TypeFormModalView();
        formModalView.setDataSubmitCallback(async (data) => {
            try {
                console.log(data);
                await this.typeModel.saveType(data);
                formModalView.closeForm();
                this.refreshTypesList();
            } catch (e) {
                this.toastController.showToast(e.toString(), 'error');
            }
        });

        return formModalView;
    }
}
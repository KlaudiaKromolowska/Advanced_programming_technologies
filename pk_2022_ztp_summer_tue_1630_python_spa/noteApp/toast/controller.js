import {ToastView} from "./toast-view.js";

export class ToastController {
    constructor() {
        this.toastView = new ToastView()
    }

    showToast(text, type) {
        this.toastView.createToast(text, type);
    }

    showError(e) {
        this.toastView.createToast(e.toString(), 'error');
    }
}
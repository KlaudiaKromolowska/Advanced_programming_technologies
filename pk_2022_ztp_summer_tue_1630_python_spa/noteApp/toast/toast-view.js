export class ToastView{
    createToast(text, type){
        const color = type === 'error' ? 'bg-danger' : type === 'success' ? 'bg-success' : 'bg-primary';

        const toastContainer = document.getElementById('toast-container')

        const toast = document.createElement('div');
        toast.classList.add('toast', 'align-items-center', 'text-white', 'border-0', color)

        toast.innerHTML = `
              <div class="d-flex">
                <div class="toast-body">
                  ${text}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>
        `;
        toastContainer.append(toast);

        const bootstrapToast = new bootstrap.Toast(toast)

        toast.addEventListener('hidden.bs.toast', function () {
            toast.remove();
        })

        bootstrapToast.show()
    }
}
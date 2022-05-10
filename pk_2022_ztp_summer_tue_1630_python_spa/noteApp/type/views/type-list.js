export class TypeListView {

    constructor(container) {
        this.container = container;
    }

    displayList(types) {
        this._render(types || [])
        this._initListeners()
    }

    placeSpinner() {
        const wrapper = document.createElement('div');
        wrapper.classList.add('spinner-wrapper')

        const spinner = document.createElement('div');
        spinner.classList.add('spinner-border', 'm-5');
        spinner.innerHTML = `<span class="visually-hidden">Loading...</span>`;

        wrapper.append(spinner)
        this.container.prepend(wrapper);

        this.spinner = wrapper;
    }

    removeSpinner() {
        if (this.spinner) {
            this.spinner.remove();
        }
    }

    bindDeleteClick(callback) {
        this.deleteClickCallback = callback;
    }

    _render(data) {
        this.container.innerHTML = '';

        const table = document.createElement('table');
        table.classList.add('table');

        const thead = document.createElement('thead');
        thead.innerHTML = `
          <th scope="col">Id</th>
          <th scope="col">Name</th>
          <th scope="col"></th>
        `;
        table.append(thead);

        const tbody = document.createElement('tbody');

        for (const type of data) {
            const tr = document.createElement('tr');
            tr.innerHTML = `
             <td> ${type.id} </td>
             <td> ${type.name} </td> 
             <td>
                <button class="btn btn-outline-danger btn-sm delete-button" data-id="${type.id}">Delete</button>
             </td>
                `;

            tbody.append(tr);
        }

        table.append(tbody);

        this.container.append(table);
    }

    _initListeners() {
        this.container.querySelector('table').addEventListener('click', (event) => {
            if (Array.from(event.target.classList).includes('delete-button')) {
                this.deleteClickCallback(event.target.dataset.id);
            }
        })
    }
}
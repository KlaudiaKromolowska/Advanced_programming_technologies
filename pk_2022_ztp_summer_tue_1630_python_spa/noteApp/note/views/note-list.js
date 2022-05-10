export class NoteListView {

    constructor(container) {
        this.container = container;
    }

    displayList(notes, filters) {
        this._render(notes || [], filters)
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

    bindEditClick(callback) {
        this.editClickCallback = callback;
    }

    bindDeleteClick(callback) {
        this.deleteClickCallback = callback;
    }

    bindFilterChange(callback) {
        this.filterChangeCallback = callback;
    }

    _render(data, filters) {
        this.container.innerHTML = '';

        const filterPanel = this._renderFilter(filters);
        this.container.append(filterPanel);

        const table = document.createElement('table');
        table.classList.add('table', 'table-striped');

        const thead = document.createElement('thead');
        thead.innerHTML = `
          <th scope="col">Id</th>
          <th scope="col">Title</th>
          <th scope="col">Content</th>
          <th scope="col">Type</th>
          <th scope="col">Important</th>
          <th scope="col">Is task</th>
          <th scope="col"></th>
        `;
        table.append(thead);

        const tbody = document.createElement('tbody');

        for (const note of data) {
            const tr = document.createElement('tr');
            tr.innerHTML = `
             <td> ${note.id} </td>
             <td> ${note.title} </td> 
             <td> ${note.content}</td>
             <td> ${note.note_type}</td>
             <td> ${note.important ? 'Yes' : 'No'}</td>
             <td> ${note.is_task ? 'Yes' : 'No'} </td>
             <td>
                <button class="btn btn-outline-primary btn-sm edit-button" data-id="${note.id}">Edit</button>
                <button class="btn btn-outline-danger btn-sm delete-button" data-id="${note.id}">Delete</button>
             </td>
                `;

            tbody.append(tr);
        }

        table.append(tbody);

        this.container.append(table);
    }

    _renderFilter(filters) {
        const container = document.createElement('div');

        container.innerHTML = `
            <div class="filter-header">
                <div class="row">
                  <div class="col-md-4">
                        <label for="sort_by" class="form-label">Sort by</label>
                        <select class="form-select" id="sort_by">
                          <option value=""></option>
                          <option ${filters.sort_by === 'title' ? 'selected' : ''} value="title">Title</option>
                          <option ${filters.sort_by === 'content' ? 'selected' : ''} value="content">Content</option>
                          <option ${filters.sort_by === 'note_type' ? 'selected' : ''} value="note_type">Type</option>
                          <option ${filters.sort_by === 'important' ? 'selected' : ''} value="important">Important</option>
                          <option ${filters.sort_by === 'is_task' ? 'selected' : ''} value="is_task">Is task</option>
                        </select>
                     </div>
                    <div class="col-md-4">
                        <label for="filter_by" class="form-label">Filter by</label>
                        <select class="form-select" id="filter_by">
                          <option value=""></option>
                          <option ${filters.filter_by === 'title' ? 'selected' : ''} value="title">Title</option>
                          <option ${filters.filter_by === 'content' ? 'selected' : ''} value="content">Content</option>
                          <option ${filters.filter_by === 'note_type' ? 'selected' : ''} value="note_type">Type</option>
                          <option ${filters.filter_by === 'important' ? 'selected' : ''} value="important">Important</option>
                          <option ${filters.filter_by === 'is_task' ? 'selected' : ''} value="is_task">Is task</option>
                        </select>
                    </div>
                    <div class="col-md-4">
                        <label for="filter_value" class="form-label">Value</label>
                        <input type="text" id="filter_value" value="${filters.filter_value ? filters.filter_value : ''}" class="form-control">
                    </div>
                </div>
            </div>
        `;

        return container;
    }

    _initListeners() {
        this.container.querySelector('table').addEventListener('click', (event) => {
            if (Array.from(event.target.classList).includes('edit-button')) {
                this.editClickCallback(event.target.dataset.id);
            }
        })

        this.container.querySelector('table').addEventListener('click', (event) => {
            if (Array.from(event.target.classList).includes('delete-button')) {
                this.deleteClickCallback(event.target.dataset.id);
            }
        });

        document.getElementsByClassName('filter-header')[0].addEventListener('change', () => {
            const filters = {
                filter_by : document.getElementById('filter_by').value,
                sort_by : document.getElementById('sort_by').value,
                filter_value : document.getElementById('filter_value').value,
            }

            this.filterChangeCallback(filters);
        });
    }
}
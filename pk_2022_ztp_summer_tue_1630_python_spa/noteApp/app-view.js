export class AppView {
    constructor() {
        this.app = this.getElement('#root');
        this._render();
        this._listenNav();
    }

    _render() {
        const navPanel = document.createElement('div');
        navPanel.innerHTML = `
          <div class="toast-container position-absolute top-0 end-0 p-3" style="z-index: 9000" id="toast-container"></div>
              
          <nav class="navbar navbar-expand-lg navbar-light bg-light" >
              <div class="container-fluid">
                <h2 class="app-title">NotesApp</h2>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                  <ul class="navbar-nav">
                    <li class="nav-item">
                      <a class="nav-link active" data-container="note-tab" aria-current="page" href="#">Notes</a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" data-container="type-tab" href="#">Types</a>
                    </li>
                  </ul>
                </div>
              </div>
          </nav>
            
            <div class="container page-content">
                <div class="tab-content">
                  <div class="tab-pane active" id="note-tab" role="tabpanel" aria-labelledby="note-tab">
                        <button type="button" class="btn btn-primary float-end" id="create-note-button"> Create Note</button>
                        <div id="note-container" style="clear: both"></div>
                  </div>
                  <div class="tab-pane" id="type-tab" role="tabpanel" aria-labelledby="type-tab">
                        <button type="button" class="btn btn-primary float-end" id="create-type-button">Create Type</button>
                        <div id="type-container" style="clear: both"></div>
                  </div>
                </div>
            </div>`;
        this.createNoteButton = navPanel.querySelector('#create-note-button');
        this.createTypeButton = navPanel.querySelector('#create-type-button');

        this.app.append(navPanel);
    }

    getElement(selector) {
        return document.querySelector(selector)
    }

    bindCreateNoteButtonClicked(handler) {
        this.createNoteButton.addEventListener('click', () => {
            handler();
        });
    }

    bindCreateTypeButtonClicked(handler) {
        this.createTypeButton.addEventListener('click', () => {
            handler();
        });
    }

    _listenNav() {
        document.getElementById('navbarNav').addEventListener('click', (event) => {
            if (Array.from(event.target.classList).includes('nav-link')) {
                const activeLink = document.getElementsByClassName("nav-link active")[0];
                activeLink.classList.remove('active');

                event.target.classList.add('active');

                const containerName = event.target.dataset.container;
                const activeTab = document.getElementsByClassName("tab-pane active")[0];
                activeTab.classList.remove('active');
                document.getElementById(containerName).classList.add('active');

            }
        })
    }
}
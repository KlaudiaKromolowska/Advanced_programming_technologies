(()=>{"use strict";class t{constructor(){}getAllTypes(){return axios.get("/get_note_types").then((t=>{if(t.data.errors)throw new Error(t.data.errors.join("<br>"));return t.data}))}saveType(t){const e={...t};return axios.post("/add_note_type",e).then((t=>{if(t.data.errors)throw new Error(t.data.errors.join("<br>"))}))}deleteType(t){return axios.delete(`/remove_note_type/${t}`).then((t=>{if(t.data.errors)throw new Error(t.data.errors.join("<br>"))}))}}class e{constructor(t){this.container=t}displayList(t){this._render(t||[]),this._initListeners()}placeSpinner(){const t=document.createElement("div");t.classList.add("spinner-wrapper");const e=document.createElement("div");e.classList.add("spinner-border","m-5"),e.innerHTML='<span class="visually-hidden">Loading...</span>',t.append(e),this.container.prepend(t),this.spinner=t}removeSpinner(){this.spinner&&this.spinner.remove()}bindDeleteClick(t){this.deleteClickCallback=t}_render(t){this.container.innerHTML="";const e=document.createElement("table");e.classList.add("table");const n=document.createElement("thead");n.innerHTML='\n          <th scope="col">Id</th>\n          <th scope="col">Name</th>\n          <th scope="col"></th>\n        ',e.append(n);const s=document.createElement("tbody");for(const e of t){const t=document.createElement("tr");t.innerHTML=`\n             <td> ${e.id} </td>\n             <td> ${e.name} </td> \n             <td>\n                <button class="btn btn-outline-danger btn-sm delete-button" data-id="${e.id}">Delete</button>\n             </td>\n                `,s.append(t)}e.append(s),this.container.append(e)}_initListeners(){this.container.querySelector("table").addEventListener("click",(t=>{Array.from(t.target.classList).includes("delete-button")&&this.deleteClickCallback(t.target.dataset.id)}))}}class n{constructor(){this.app=document.getElementById("root")}setDataSubmitCallback(t){this.submitCallback=t}openForm(){this.modal=this._render(),new bootstrap.Modal(this.modal).toggle(),this.modal.addEventListener("hidden.bs.modal",(t=>{this.modal.remove(),this.modal=null})),this._listenForSubmit()}closeForm(){this.modal&&bootstrap.Modal.getInstance(this.modal).hide()}_render(){const t=document.createElement("div");return t.classList.add("modal","fade"),t.id="modalForm",t.innerHTML='<div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <h5 class="modal-title" id="exampleModalLabel">Create type</h5>\n                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>\n                </div>\n                <div class="modal-body">\n                    <div class="container">\n                        <form id="type-form">\n                            <div class="mb-3">\n                                <label for="name" class="form-label">Name</label>\n                                <input type="text" value="" class="form-control" id="name" name="name">\n                            </div>\n                        </form>\n                    </div>\n                </div>\n                <div class="modal-footer">\n                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>\n                    <button type="button" class="btn btn-primary" id="submit-button">Save changes</button>\n                </div>\n            </div>\n        </div>',this.app.appendChild(t),t}_listenForSubmit(){this.modal.querySelector("#submit-button").addEventListener("click",(()=>{const t={},e=new FormData(document.getElementById("type-form"));for(const[n,s]of e.entries())t[n]=s;this._onSubmit(t)}))}_onSubmit(t){this.submitCallback(t)}}class s{createToast(t,e){const n="error"===e?"bg-danger":"success"===e?"bg-success":"bg-primary",s=document.getElementById("toast-container"),a=document.createElement("div");a.classList.add("toast","align-items-center","text-white","border-0",n),a.innerHTML=`\n              <div class="d-flex">\n                <div class="toast-body">\n                  ${t}\n                </div>\n                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>\n              </div>\n        `,s.append(a);const o=new bootstrap.Toast(a);a.addEventListener("hidden.bs.toast",(function(){a.remove()})),o.show()}}class a{constructor(){this.toastView=new s}showToast(t,e){this.toastView.createToast(t,e)}showError(t){this.toastView.createToast(t.toString(),"error")}}class o{constructor(){this.typeModel=new t,this.toastController=new a,this.typesListView=new e(document.getElementById("type-container")),this.typesListView.bindDeleteClick(this.handleTypeDeleteClicked),this.refreshTypesList()}refreshTypesList=async()=>{this.typesListView.placeSpinner();const t=await this.typeModel.getAllTypes();this.typesListView.displayList(t),this.typesListView.removeSpinner()};handleCreateTypeClicked=async()=>{this._createModal().openForm()};handleTypeDeleteClicked=async t=>{this.typesListView.placeSpinner();try{await this.typeModel.deleteType(t),await this.refreshTypesList()}catch(t){this.toastController.showToast(t.toString(),"error")}finally{this.typesListView.removeSpinner()}};_createModal(){const t=new n;return t.setDataSubmitCallback((async e=>{try{console.log(e),await this.typeModel.saveType(e),t.closeForm(),this.refreshTypesList()}catch(t){this.toastController.showToast(t.toString(),"error")}})),t}}class i{constructor(){}getAllNotes(t){const e={};for(const n in t)t[n]&&(e[n]=t[n]);return axios.get("/list",{params:e}).then((t=>t.data))}getNoteById(t){return axios.get(`/get_note/${t}`).then((t=>{if(t.data.errors)throw new Error(t.data.errors.join("<br>"));return t.data}))}saveNote(t){const e={is_task:!!t.is_task,important:!!t.important},n={...t,...e};return n.id?(n.note_type=n.note_type_id,delete n.note_type_id,axios.put(`/edit_note/${t.id}`,n).then((t=>{if(t.data.errors)throw new Error(t.data.errors.join("<br>"))}))):axios.post("/add_note",n).then((t=>{if(t.data.errors)throw new Error(t.data.errors.join("<br>"))}))}deleteNote(t){return axios.delete(`/remove_note/${t}`).then((t=>{console.log(t.data)}))}}class l{constructor(t){this.container=t}displayList(t,e){this._render(t||[],e),this._initListeners()}placeSpinner(){const t=document.createElement("div");t.classList.add("spinner-wrapper");const e=document.createElement("div");e.classList.add("spinner-border","m-5"),e.innerHTML='<span class="visually-hidden">Loading...</span>',t.append(e),this.container.prepend(t),this.spinner=t}removeSpinner(){this.spinner&&this.spinner.remove()}bindEditClick(t){this.editClickCallback=t}bindDeleteClick(t){this.deleteClickCallback=t}bindFilterChange(t){this.filterChangeCallback=t}_render(t,e){this.container.innerHTML="";const n=this._renderFilter(e);this.container.append(n);const s=document.createElement("table");s.classList.add("table","table-striped");const a=document.createElement("thead");a.innerHTML='\n          <th scope="col">Id</th>\n          <th scope="col">Title</th>\n          <th scope="col">Content</th>\n          <th scope="col">Type</th>\n          <th scope="col">Important</th>\n          <th scope="col">Is task</th>\n          <th scope="col"></th>\n        ',s.append(a);const o=document.createElement("tbody");for(const e of t){const t=document.createElement("tr");t.innerHTML=`\n             <td> ${e.id} </td>\n             <td> ${e.title} </td> \n             <td> ${e.content}</td>\n             <td> ${e.note_type}</td>\n             <td> ${e.important?"Yes":"No"}</td>\n             <td> ${e.is_task?"Yes":"No"} </td>\n             <td>\n                <button class="btn btn-outline-primary btn-sm edit-button" data-id="${e.id}">Edit</button>\n                <button class="btn btn-outline-danger btn-sm delete-button" data-id="${e.id}">Delete</button>\n             </td>\n                `,o.append(t)}s.append(o),this.container.append(s)}_renderFilter(t){const e=document.createElement("div");return e.innerHTML=`\n            <div class="filter-header">\n                <div class="row">\n                  <div class="col-md-4">\n                        <label for="sort_by" class="form-label">Sort by</label>\n                        <select class="form-select" id="sort_by">\n                          <option value=""></option>\n                          <option ${"title"===t.sort_by?"selected":""} value="title">Title</option>\n                          <option ${"content"===t.sort_by?"selected":""} value="content">Content</option>\n                          <option ${"note_type"===t.sort_by?"selected":""} value="note_type">Type</option>\n                          <option ${"important"===t.sort_by?"selected":""} value="important">Important</option>\n                          <option ${"is_task"===t.sort_by?"selected":""} value="is_task">Is task</option>\n                        </select>\n                     </div>\n                    <div class="col-md-4">\n                        <label for="filter_by" class="form-label">Filter by</label>\n                        <select class="form-select" id="filter_by">\n                          <option value=""></option>\n                          <option ${"title"===t.filter_by?"selected":""} value="title">Title</option>\n                          <option ${"content"===t.filter_by?"selected":""} value="content">Content</option>\n                          <option ${"note_type"===t.filter_by?"selected":""} value="note_type">Type</option>\n                          <option ${"important"===t.filter_by?"selected":""} value="important">Important</option>\n                          <option ${"is_task"===t.filter_by?"selected":""} value="is_task">Is task</option>\n                        </select>\n                    </div>\n                    <div class="col-md-4">\n                        <label for="filter_value" class="form-label">Value</label>\n                        <input type="text" id="filter_value" value="${t.filter_value?t.filter_value:""}" class="form-control">\n                    </div>\n                </div>\n            </div>\n        `,e}_initListeners(){this.container.querySelector("table").addEventListener("click",(t=>{Array.from(t.target.classList).includes("edit-button")&&this.editClickCallback(t.target.dataset.id)})),this.container.querySelector("table").addEventListener("click",(t=>{Array.from(t.target.classList).includes("delete-button")&&this.deleteClickCallback(t.target.dataset.id)})),document.getElementsByClassName("filter-header")[0].addEventListener("change",(()=>{const t={filter_by:document.getElementById("filter_by").value,sort_by:document.getElementById("sort_by").value,filter_value:document.getElementById("filter_value").value};this.filterChangeCallback(t)}))}}class r{constructor(){this.app=document.getElementById("root")}setDataSubmitCallback(t){this.submitCallback=t}openForm(t,e){this.modal=this._render(t,e),new bootstrap.Modal(this.modal).toggle(),this.modal.addEventListener("hidden.bs.modal",(t=>{this.modal.remove(),this.modal=null})),this._listenForSubmit()}closeForm(){this.modal&&bootstrap.Modal.getInstance(this.modal).hide()}_render(t,e){const n=e||{},s=document.createElement("div");s.classList.add("modal","fade"),s.id="modalForm";const a=this._makeSelectWithTypes(t,n);return s.innerHTML=`<div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <h5 class="modal-title" id="exampleModalLabel">${n.id?"Edit note":"Create note"}</h5>\n                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>\n                </div>\n                <div class="modal-body">\n                    <div class="container">\n                        <form id="note-form">\n                        ${n.id?`<input type="hidden" name="id" value="${n.id}"> `:""}\n                            <div class="mb-3">\n                                <label for="name" class="form-label">Title</label>\n                                <input type="text" value="${n.title||""}" class="form-control" id="title" name="title">\n                            </div>\n                            <div class="mb-3">\n                                <label for="author" class="form-label">Content</label>\n                                <input type="text" value="${n.content||""}" class="form-control" id="content" name="content">\n                            </div>\n                             <div class="mb-3">\n                                <label for="type" class="form-label">Type</label>\n                                ${a.outerHTML}\n                            </div>\n                            <div class="mb-3">\n                                <input class="form-check-input" ${n.important?"checked":""} type="checkbox" value="true" id="important" name="important">\n                                <label class="form-check-label" for="flexCheckDefault">\n                                   Important\n                                </label>\n                            </div>\n                            <div class="mb-3">\n                                <input class="form-check-input" ${n.is_task?"checked":""} type="checkbox" value="true" id="is_task" name="is_task">\n                                <label class="form-check-label" for="flexCheckDefault">\n                                   Is task\n                                </label>\n                            </div>\n                        </form>\n                    </div>\n                </div>\n                <div class="modal-footer">\n                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>\n                    <button type="button" class="btn btn-primary" id="submit-button">Save changes</button>\n                </div>\n            </div>\n        </div>`,this.app.appendChild(s),s}_makeSelectWithTypes(t,e){const n=document.createElement("select");n.classList.add("form-select"),n.id="type",n.name="note_type_id";const s=t.map((t=>`<option ${t.id==e.note_type?"selected":""} value="${t.id}">${t.name}</option>`));return n.innerHTML=`\n              <option value="">Chose type</option>\n              ${s.join("\n")}\n        `,n}_listenForSubmit(){this.modal.querySelector("#submit-button").addEventListener("click",(()=>{const t={},e=new FormData(document.getElementById("note-form"));for(const[n,s]of e.entries())t[n]=s;this._onSubmit(t)}))}_onSubmit(t){this.submitCallback(t)}}class d{constructor(){this.noteModel=new i,this.typeModel=new t,this.toastController=new a,this.filters={},this.notesListView=new l(document.getElementById("note-container")),this.notesListView.bindEditClick(this.handleNoteEditClicked),this.notesListView.bindDeleteClick(this.handleNoteDeleteClicked),this.notesListView.bindFilterChange(this.handleFiltersChange),this.refreshNotesList()}refreshNotesList=async()=>{this.notesListView.placeSpinner();try{const t=await this.noteModel.getAllNotes(this.filters);this.notesListView.displayList(t,this.filters)}catch(t){this.toastController.showToast(t.toString(),"error")}finally{this.notesListView.removeSpinner()}};handleCreateNoteClicked=async()=>{const t=this._createModal(),e=await this.typeModel.getAllTypes();t.openForm(e)};handleNoteEditClicked=async t=>{const e=this._createModal(),n=await this.noteModel.getNoteById(t),s=await this.typeModel.getAllTypes();e.openForm(s,n)};handleNoteDeleteClicked=async t=>{this.notesListView.placeSpinner();try{await this.noteModel.deleteNote(t),await this.refreshNotesList()}catch(t){this.toastController.showToast(t.toString(),"error")}finally{this.notesListView.removeSpinner()}};handleFiltersChange=t=>{this.filters=t,this.refreshNotesList()};_createModal(){const t=new r;return t.setDataSubmitCallback((async e=>{try{await this.noteModel.saveNote(e),this.toastController.showToast("Note successfully created","success"),t.closeForm(),this.refreshNotesList()}catch(t){this.toastController.showError(t)}})),t}}axios.defaults.baseURL="http://localhost:5000",new class{constructor(t){this.view=t;const e=new o,n=new d;this.view.bindCreateNoteButtonClicked(n.handleCreateNoteClicked),this.view.bindCreateTypeButtonClicked(e.handleCreateTypeClicked)}}(new class{constructor(){this.app=this.getElement("#root"),this._render(),this._listenNav()}_render(){const t=document.createElement("div");t.innerHTML='\n          <div class="toast-container position-absolute top-0 end-0 p-3" style="z-index: 9000" id="toast-container"></div>\n              \n          <nav class="navbar navbar-expand-lg navbar-light bg-light" >\n              <div class="container-fluid">\n                <h2 class="app-title">NotesApp</h2>\n                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n                  <span class="navbar-toggler-icon"></span>\n                </button>\n                <div class="collapse navbar-collapse" id="navbarNav">\n                  <ul class="navbar-nav">\n                    <li class="nav-item">\n                      <a class="nav-link active" data-container="note-tab" aria-current="page" href="#">Notes</a>\n                    </li>\n                    <li class="nav-item">\n                      <a class="nav-link" data-container="type-tab" href="#">Types</a>\n                    </li>\n                  </ul>\n                </div>\n              </div>\n          </nav>\n            \n            <div class="container page-content">\n                <div class="tab-content">\n                  <div class="tab-pane active" id="note-tab" role="tabpanel" aria-labelledby="note-tab">\n                        <button type="button" class="btn btn-primary float-end" id="create-note-button"> Create Note</button>\n                        <div id="note-container" style="clear: both"></div>\n                  </div>\n                  <div class="tab-pane" id="type-tab" role="tabpanel" aria-labelledby="type-tab">\n                        <button type="button" class="btn btn-primary float-end" id="create-type-button">Create Type</button>\n                        <div id="type-container" style="clear: both"></div>\n                  </div>\n                </div>\n            </div>',this.createNoteButton=t.querySelector("#create-note-button"),this.createTypeButton=t.querySelector("#create-type-button"),this.app.append(t)}getElement(t){return document.querySelector(t)}bindCreateNoteButtonClicked(t){this.createNoteButton.addEventListener("click",(()=>{t()}))}bindCreateTypeButtonClicked(t){this.createTypeButton.addEventListener("click",(()=>{t()}))}_listenNav(){document.getElementById("navbarNav").addEventListener("click",(t=>{if(Array.from(t.target.classList).includes("nav-link")){document.getElementsByClassName("nav-link active")[0].classList.remove("active"),t.target.classList.add("active");const e=t.target.dataset.container;document.getElementsByClassName("tab-pane active")[0].classList.remove("active"),document.getElementById(e).classList.add("active")}}))}})})();
// ------------ Materialize initialization 
document.addEventListener('DOMContentLoaded', function () {
  // sidenav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // confirm delete modal
  let deleteModal = document.querySelectorAll('.modal');
  M.Modal.init(deleteModal);

  // datepicker
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    showClearBtn: "False",
    i18n: {
      done: "Select"
    }
  });

  // initialization of select
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);

  // initialization of collapsable elements
  let collapsable = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsable);
  
});


// document.addEventListener('DOMContentLoaded', function () {
//   let deleteModal = document.querySelectorAll('.modal');
//   M.Modal.init(deleteModal);
// });
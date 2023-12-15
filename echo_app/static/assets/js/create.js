$(function() {
  function removeNote() {
      $(".remove-note").off('click').on('click', function(event) {
          event.stopPropagation();
          $(this).parents('.single-note-item').remove();
      });
  }

  function favouriteNote() {
      $(".favourite-note").off('click').on('click', function(event) {
          event.stopPropagation();
          $(this).parents('.single-note-item').toggleClass('note-favourite');
      });
  }

  function addLabelGroups() {
      $('.category-selector .badge-group-item').off('click').on('click', function(event) {
          event.preventDefault();
          var getclass = this.className;
          var getSplitclass = getclass.split(' ')[0];
          var parentNoteItem = $(this).parents('.single-note-item');

          if ($(this).hasClass('badge-business')) {
              parentNoteItem.removeClass('note-social note-important').toggleClass(getSplitclass);
          } else if ($(this).hasClass('badge-social')) {
              parentNoteItem.removeClass('note-business note-important').toggleClass(getSplitclass);
          } else if ($(this).hasClass('badge-important')) {
              parentNoteItem.removeClass('note-social note-business').toggleClass(getSplitclass);
          }
      });
  }

  var $btns = $('.note-link').click(function() {
      var $el = $('.' + this.id).fadeIn();
      $('#note-full-container > div').not($el).hide();
      $btns.removeClass('active');
      $(this).addClass('active');
  });

  $('#add-notes').on('click', function(event) {
      $('#addnotesmodal').modal('show');
      $('#btn-n-save').hide();
      $('#btn-n-add').show();
  });

  // Button add
  $("#btn-n-add").on('click', function(event) {
      event.preventDefault();
      var today = new Date();
      var dd = String(today.getDate()).padStart(2, '0');
      var mm = String(today.getMonth() + 1).padStart(2, '0'); // Adding 1 to month as it starts from 0
      var yyyy = today.getFullYear();
      var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
      today = dd + ' ' + monthNames[mm - 1]  + ' ' + yyyy;

      var $_noteTitle = $('#note-has-title').val();
      var $_noteDescription = $('#note-has-description').val();

      var $html = '<div class="col-md-4 single-note-item all-category"><div class="card card-body">' +
          '<span class="side-stick"></span>' +
          '<h5 class="note-title text-truncate w-75 mb-0" data-noteHeading="'+$_noteTitle+'">'+$_noteTitle+'<i class="point fa fa-circle ml-1 font-10"></i></h5>' +
          '<p class="note-date font-12 text-muted">'+today+'</p>' +
          '<div class="note-content">' +
              '<p class="note-inner-content text-muted" data-noteContent="'+$_noteDescription+'">'+$_noteDescription+'</p>' +
          '</div>' +
          '<div class="d-flex align-items-center">' +
              '<span class="mr-1"><i class="fa fa-star favourite-note"></i></span>' +
              '<span class="mr-1"><i class="fa fa-trash remove-note"></i></span>' +
              '<div class="ml-auto">' +
                  '<div class="category-selector btn-group">' +
                      '<a class="nav-link dropdown-toggle category-dropdown label-group p-0" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="true">' +
                          '<div class="category">' +
                              '<div class="category-business"></div>' +
                              '<div class="category-social"></div>' +
                              '<div class="category-important"></div>' +
                              '<span class="more-options text-dark"><i class="icon-options-vertical"></i></span>'+
                          '</div>' +
                      '</a>' +
                      '<div class="dropdown-menu dropdown-menu-right category-menu">' +
                          '<a class="note-business badge-group-item badge-business dropdown-item position-relative category-business text-success" href="javascript:void(0);"><i class="mdi mdi-checkbox-blank-circle-outline mr-1"></i>Business</a>' +
                          '<a class="note-social badge-group-item badge-social dropdown-item position-relative category-social text-info" href="javascript:void(0);"><i class="mdi mdi-checkbox-blank-circle-outline mr-1"></i> Social</a>' +
                          '<a class="note-important badge-group-item badge-important dropdown-item position-relative category-important text-danger" href="javascript:void(0);"><i class="mdi mdi-checkbox-blank-circle-outline mr-1"></i> Important</a>' +
                      '</div>' +
                  '</div>' +
              '</div>' +
          '</div>' +
      '</div></div> ';

      $("#note-full-container").prepend($html);
      $('#addnotesmodal').modal('hide');

      removeNote();
      favouriteNote();
      addLabelGroups();
  });

  $('#addnotesmodal').on('hidden.bs.modal', function (event) {
      event.preventDefault();
      $('#note-has-title').val('');
      $('#note-has-description').val('');
  });

  removeNote();
  favouriteNote();
  addLabelGroups();

  $('#btn-n-add').prop('disabled', true); 
});

$('#note-has-title').keyup(function() {
  var empty = $('#note-has-title').val() === '';
  $('#btn-n-add').prop('disabled', empty);
});

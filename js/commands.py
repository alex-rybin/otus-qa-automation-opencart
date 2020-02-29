ADD_IMAGE_UPLOAD_FIELD = """$('#form-upload').remove();

$('body').prepend('<form enctype="multipart/form-data" id="form-upload";"><input type="file" name="file[]" value="" multiple="multiple" /></form>');

if (typeof timer != 'undefined') {{
  clearInterval(timer);
}}

timer = setInterval(function() {{
  if ($('#form-upload input[name=\\'file[]\\']').val() != '') {{
    clearInterval(timer);

    $.ajax({{
      url: 'index.php?route=common/filemanager/upload&user_token={token}&directory=',
      type: 'post',
      dataType: 'json',
      data: new FormData($('#form-upload')[0]),
      cache: false,
      contentType: false,
      processData: false,
      beforeSend: function() {{
        $('#button-upload i').replaceWith('<i class="fa fa-circle-o-notch fa-spin"></i>');
        $('#button-upload').prop('disabled', true);
      }},
      complete: function() {{
        $('#button-upload i').replaceWith('<i class="fa fa-upload"></i>');
        $('#button-upload').prop('disabled', false);
      }},
      success: function(json) {{
        if (json['error']) {{
          alert(json['error']);
        }}

        if (json['success']) {{
          alert(json['success']);

          $('#button-refresh').trigger('click');
        }}
      }},
      error: function(xhr, ajaxOptions, thrownError) {{
        alert(thrownError + "\\r\\n" + xhr.statusText + "\\r\\n" + xhr.responseText);
      }}
    }});
  }}
}}, 500);
"""

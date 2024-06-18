
function updateUser(id){
    let name = $("#name"+id).val();
	let surname = $("#surname"+id).val();
	let lastname = $("#lastname"+id).val();
	let group = $("#group"+id).val();
	let group_id = $("#group_id"+id).val();

	$.ajax
		({
			type: "POST",
			url: '../update/'+ id ,
			async: true,
			data: jQuery.param({ "name": name, "surname": surname, "lastname": lastname, "group": group, "group_id": group_id }),
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(result) {
				location.reload();
			}
		})
}

function deleteUser(id){

		$.ajax
			({
				type: "Post",
				url: '../delete/' + id,
				async: true,
				success: function(result) {
					location.reload();
				}
			})
}
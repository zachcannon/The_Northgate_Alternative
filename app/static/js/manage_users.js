/// <reference path="jquery-ui-1.10.3.min.js" />

$( document ).ready(function() {
	

	$('#generateMovieList').click(function generateMovieList() {
	
		var postMovieList = function(movies) {
			$('#movieList').empty();
			$.each( movies['movies'], function(index, value) {
				$('#movieList').append('<li>'+value+'</li>');				
			});
		};
		
		$.post('/recommender_results', {
			recommender: document.getElementById("recommenderstouse").value		
		}).done(postMovieList);
	});

});
/// <reference path="jquery-ui-1.10.3.min.js" />

$( document ).ready(function() {
	

	$('#generateMovieList').click(function generateMovieList() {
	
		var postMovieList = function(movies) {
			$('#movieList').empty();
			$('#movieList').append('<li class="nav-header">Search Results</li>');
			$.each( movies['movies'], function(index, value) {
				$('#movieList').append('<li><a href="https://www.google.com/search?q='+value+'" target="_blank"">'+value+'</a></li>');				
			});
		};
		
		$.post('/recommender_results', {
			recommender: document.getElementById("recommenderstouse").value		
		}).done(postMovieList);
	});

});
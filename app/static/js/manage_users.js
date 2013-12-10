/// <reference path="jquery-ui-1.10.3.min.js" />

$( document ).ready(function() {
	

	$('#generateMovieList').click(function generateMovieList() {
	
		var postMovieList = function(movies) {
			$('#movieList').empty();
			$('#movieList').append('<li class="nav-header">Search Results</li>');
			$.each( movies['movies'], function(index, value) {
				$('#movieList').append('<li class="movie-list-item"><a href="https://www.google.com/search?q='+value+'" target="_blank"">'+value+'</a></li>');				
			});
		};
		
		$.post('/recommender_results').done(postMovieList);
	});
	
	$('#js-test-group-one').click(function () {
		$.post('/load_preformed_group', {
			group: '[1000, 1001]'
		});	
	});
	
	$('#js-test-group-two').click(function () {
		$.post('/load_preformed_group', {
			group: '[1006, 1003, 1004]'
		});	
	});
	
	$('#js-test-group-three').click(function () {
		$.post('/load_preformed_group', {
			group: '[86, 652, 1006]'
		});	
	});
	
	$('#js-test-group-four').click(function () {
		$.post('/load_preformed_group', {
			group: '[450, 243]'
		});	
	});

});